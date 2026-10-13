import { getCollection, type CollectionEntry } from 'astro:content';
import { sectionOf } from './sections';

export type Entry = CollectionEntry<'entries'>;

const byNewest = (a: Entry, b: Entry) => b.data.date.valueOf() - a.data.date.valueOf();

/** Every published entry, newest first. Drafts never ship. */
export const allEntries = async () =>
  (await getCollection('entries', ({ data }) => !data.draft)).sort(byNewest);

/** The published entries of one section, newest first. */
export const sectionEntries = async (slug: string) =>
  (await allEntries()).filter((e) => e.id.split('/')[0] === slug);

/**
 * Split a section's entries into sub-groups - the course code for coursework,
 * the trip for travel - so a long list stays readable. The group name is the
 * `group` front-matter field, falling back to the directory it sits in. Pages
 * straight inside the section directory have no group.
 */
export const groupEntries = (items: Entry[]) => {
  const name = (e: Entry) => e.data.group ?? e.id.split('/').slice(1, -1)[0] ?? '';
  const order = [...new Set(items.map(name))];
  return order.map((group) => ({ group, items: items.filter((e) => name(e) === group) }));
};

/** The path an entry is served at. The directory path is the URL. */
export const href = (entry: Entry) => `/${entry.id}/`;

/** The section an entry belongs to, for breadcrumbs and listing labels. */
export const entrySection = (entry: Entry) => sectionOf(entry.id);

export const iso = (d: Date) => d.toISOString().slice(0, 10);

export const fmtShort = (d: Date) =>
  d.toLocaleDateString('en-CA', { month: 'short', day: '2-digit', year: 'numeric', timeZone: 'UTC' });

export const fmtLong = (d: Date) =>
  d.toLocaleDateString('en-CA', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
