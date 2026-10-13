import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';
import { sections } from './data/sections';

const categories = sections.map((s) => s.category) as [string, ...string[]];

// One directory per piece of work: src/content/<section>/<path>/index.md, with
// its figures alongside it so the markdown can reference them relatively. The
// directory path is the URL, and the first segment is the section.
const entries = defineCollection({
  loader: glob({ pattern: '**/index.md', base: './src/content' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      // Enforced rather than free text: the listings group by it, so a typo
      // would quietly split one section into two.
      category: z.enum(categories),
      author: z.string(),
      date: z.coerce.date(),
      summary: z.string(),
      /** Display name for the sub-group a page sits in, e.g. "SYDE 572". */
      group: z.string().optional(),
      /** Lead image, relative to this directory. The gallery needs one. */
      cover: image().optional(),
      /** Where the photographs were taken. Shown on travel entries. */
      location: z.string().optional(),
      /** Link to the full photo album - a shared Google Drive folder. */
      album: z
        .string()
        .refine((s) => /^https?:\/\//.test(s), 'album must be an http(s) link')
        .optional(),
      /** Keep out of the listings and the sitemap while still building it. */
      draft: z.boolean().default(false),
      /** Force MathJax on or off. Left unset, the page is sniffed for TeX. */
      math: z.boolean().optional(),
    }),
});

export const collections = { entries };
