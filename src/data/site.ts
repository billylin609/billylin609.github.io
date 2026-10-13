// Identity and navigation. Editable text lives in site-settings.json.
import settings from './site-settings.json';
import { sections } from './sections';

const sectionLinks = sections.map((s) => ({ label: s.label, href: `/${s.slug}` }));

export const site = {
  ...settings,
  url: 'https://billylin609.github.io',
  repo: 'https://github.com/billylin609/billylin609.github.io',
  github: 'https://github.com/billylin609',
  // The top bar. Five sections, in the order they are declared in sections.ts.
  nav: sectionLinks,
  menu: [{ label: 'Home', href: '/' }, ...sectionLinks],
  footer: [
    { title: 'Sections', links: sectionLinks.slice(0, 3).map((l) => [l.label, l.href] as const) },
    {
      title: 'More',
      links: [
        ...sectionLinks.slice(3).map((l) => [l.label, l.href] as const),
        ['Home', '/'] as const,
      ],
    },
    {
      title: 'Elsewhere',
      links: [
        ['GitHub', 'https://github.com/billylin609'] as const,
        ['Source of this site', 'https://github.com/billylin609/billylin609.github.io'] as const,
      ],
    },
  ],
} as const;
