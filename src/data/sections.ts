// The five top-level sections of the site, in nav order.
//
// `slug` is both the URL and the content directory: a page at
// src/content/<slug>/<name>/index.md is served at /<slug>/<name>/ and listed
// on /<slug>. `category` is the matching front-matter value, which the schema
// in content.config.ts enforces.
export const sections = [
  {
    slug: 'resume',
    label: 'Resume & Portfolio',
    short: 'Resume',
    category: 'Resume',
    title: 'Resume &\nportfolio.',
    lede: 'Where I have worked and studied, and the projects worth showing.',
  },
  {
    slug: 'blog',
    label: 'Development Blog',
    short: 'Blog',
    category: 'Develop',
    title: 'Development\nblog.',
    lede: 'Notes on things I have built and the problems that came up while building them.',
  },
  {
    slug: 'travel',
    label: 'Travel + Gallery',
    short: 'Travel',
    category: 'Travel',
    title: 'Travel +\ngallery.',
    lede: 'Places I have been, and the photographs that came back with me.',
  },
  {
    slug: 'coursework',
    label: 'Coursework',
    short: 'Coursework',
    category: 'Course',
    title: 'Work, written out\nin full.',
    lede: 'Assignments kept as web pages rather than PDFs, so the equations stay selectable and the figures stay sharp.',
  },
  {
    slug: 'solutions',
    label: 'Problem Solutions',
    short: 'Solutions',
    category: 'Solutions',
    title: 'Problem\nsolutions.',
    lede: 'Worked solutions, written out so the reasoning is visible rather than just the answer.',
  },
] as const;

export type Section = (typeof sections)[number];
export type SectionSlug = Section['slug'];

/** The section a collection entry belongs to, taken from its first path segment. */
export const sectionOf = (id: string) =>
  sections.find((s) => s.slug === id.split('/')[0]);

export const sectionBySlug = (slug: string) => sections.find((s) => s.slug === slug);
