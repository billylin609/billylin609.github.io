import { site } from '../data/site';
import { sections } from '../data/sections';
import { allEntries, href } from '../data/entries';

// llms.txt: a plain-text map of the site for AI assistants and agents.
export async function GET({ site: base }: { site: URL }) {
  const work = await allEntries();
  const u = (p: string) => new URL(p, base).href;

  const body = [
    `# ${site.name}`,
    '',
    `> ${site.description}`,
    '',
    ...sections.flatMap((s) => {
      const items = work.filter((w) => w.id.split('/')[0] === s.slug);
      return [
        `## ${s.label}`,
        '',
        s.lede,
        '',
        ...(items.length === 0
          ? ['Nothing published here yet.']
          : items.map((w) => `- [${w.data.title}](${u(href(w))}): ${w.data.summary}`)),
        '',
      ];
    }),
  ].join('\n');

  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
}
