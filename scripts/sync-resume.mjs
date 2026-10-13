// Pull the resume text out of the Google Doc and rewrite src/data/resume.json.
//
//   npm run sync:resume
//
// The doc is the source of truth for the words: headings, dates and bullets are
// overwritten every run. Anything curated by hand - the intro paragraph, the
// `doc` links, the contact block and the `orgHref` links - is carried across,
// the last of those by matching on the organisation name, so editing the doc
// never silently drops them.
//
// The doc must be shared as "anyone with the link can view"; the export
// endpoint is what this reads, and it needs no credentials.
import { writeFile, readFile } from 'node:fs/promises';

const DOC_ID = '1NlbS4MfB6MhJdZc_8JuYB9X6gKKkf7bl5sWoolPKX9o';
const EXPORT = `https://docs.google.com/document/d/${DOC_ID}/export?format=txt`;
const TARGET = new URL('../src/data/resume.json', import.meta.url);

// "Embedded Security Engineer - ETAS - Waterloo, ON        May 2026 - Sep 2026"
// The date tail is what anchors the split; everything before it is the title.
const DATE_TAIL =
  /\s{2,}((?:[A-Z][a-z]{2}\s+\d{4})\s*[-–—]\s*(?:Present|[A-Z][a-z]{2}\s+\d{4}))\s*$/;

const SECTIONS = {
  'Work Experience': 'experience',
  'Personal Projects': 'projects',
  Education: 'education',
  Skills: 'skills',
};

const clean = (s) =>
  s
    .replace(/–|—/g, '-')
    .replace(/\s+/g, ' ')
    .replace(/([A-Za-z0-9])\(/g, '$1 (')
    .trim();

// Split on commas that are not inside brackets, so "Arm(STM32, nRF, Ti)" stays
// one item instead of three.
function splitList(s) {
  const out = [];
  let depth = 0;
  let buf = '';
  for (const ch of s) {
    if (ch === '(') depth++;
    else if (ch === ')') depth = Math.max(0, depth - 1);
    if (ch === ',' && depth === 0) {
      out.push(buf);
      buf = '';
    } else buf += ch;
  }
  out.push(buf);
  return out.map(clean).filter(Boolean);
}

function parse(text) {
  const lines = text
    .replace(/^﻿/, '')
    .split('\n')
    .map((l) => l.replace(/\r$/, ''));

  const out = { experience: [], projects: [], education: [], skills: [] };
  let bucket = null;
  let current = null;

  for (const raw of lines) {
    const line = raw.replace(/\t/g, ' ').trimEnd();
    if (!line.trim() || /^_+$/.test(line.trim())) continue;

    const heading = SECTIONS[line.trim()];
    if (heading) {
      bucket = heading;
      current = null;
      continue;
    }
    if (!bucket) continue;

    // The portfolio pages repeat the name/email header; that ends the resume.
    if (/^Yuchen Lin$/.test(line.trim())) {
      bucket = null;
      continue;
    }

    if (bucket === 'skills') {
      const m = line.match(/^([A-Za-z ]+):\s*(.+)$/);
      if (m) {
        out.skills.push({
          group: clean(m[1]),
          items: splitList(m[2]),
        });
      }
      continue;
    }

    if (line.trimStart().startsWith('* ')) {
      current?.notes.push(clean(line.trimStart().slice(2)));
      continue;
    }

    const m = line.match(DATE_TAIL);
    if (!m) continue;

    const parts = line.slice(0, m.index).split(/\s+[-–—]\s+/).map(clean).filter(Boolean);
    // Education reads "University - Degree"; everything else "Role - Org".
    const [role, org] =
      bucket === 'education' ? [parts[1] ?? '', parts[0] ?? ''] : [parts[0] ?? '', parts[1] ?? ''];

    current = {
      role,
      org,
      orgHref: '',
      location: parts[2] ?? '',
      // "Sep 2025 - Sep 2025" is one month, not a range.
      period: clean(m[1]).replace(/^(.+?) - \1$/, '$1'),
      notes: [],
    };
    out[bucket].push(current);
  }
  return out;
}

const res = await fetch(EXPORT, { redirect: 'follow' });
if (!res.ok) {
  console.error(`Could not read the doc: HTTP ${res.status}.`);
  console.error('Check that it is still shared as "anyone with the link can view".');
  process.exit(1);
}
const parsed = parse(await res.text());

const empty = Object.entries(parsed).filter(([, v]) => v.length === 0);
if (empty.length) {
  console.error(`Parsed nothing for: ${empty.map(([k]) => k).join(', ')}.`);
  console.error('The doc headings probably moved. resume.json was left alone.');
  process.exit(1);
}

// Carry the hand-curated bits across.
const prev = JSON.parse(await readFile(TARGET, 'utf8'));
const links = new Map(
  [...prev.experience, ...prev.projects, ...prev.education]
    .filter((r) => r.orgHref)
    .map((r) => [r.org, r.orgHref]),
);
const places = new Map(
  [...prev.experience, ...prev.projects, ...prev.education]
    .filter((r) => r.location)
    .map((r) => [r.org, r.location]),
);
for (const key of ['experience', 'projects', 'education']) {
  for (const row of parsed[key]) {
    row.orgHref = links.get(row.org) ?? '';
    row.location ||= places.get(row.org) ?? '';
  }
}

const next = {
  _source: prev._source,
  intro: prev.intro,
  doc: prev.doc,
  contact: prev.contact,
  ...parsed,
};

await writeFile(TARGET, `${JSON.stringify(next, null, 2)}\n`);

const n = (k) => `${parsed[k].length} ${k}`;
console.log(`Wrote src/data/resume.json - ${['experience', 'projects', 'education', 'skills'].map(n).join(', ')}.`);
const missing = [...parsed.experience, ...parsed.projects].filter((r) => !r.orgHref);
if (missing.length) {
  console.log(`No link yet for: ${missing.map((r) => r.org).join(', ')}. Add orgHref by hand.`);
}
