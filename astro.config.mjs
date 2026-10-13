// @ts-check
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeMathjaxDelimiters from './src/plugins/rehype-mathjax-delimiters.mjs';
import rehypeFigures from './src/plugins/rehype-figures.mjs';

export default defineConfig({
  site: 'https://billylin609.github.io',
  integrations: [sitemap()],
  vite: { plugins: [tailwindcss()] },
  markdown: {
    // The remark/rehype pipeline rather than Astro 7's native processor, because
    // the math handling below is a pair of rehype plugins. remark-math pulls
    // $…$ and $$…$$ out of the markdown verbatim; the first plugin then hands
    // them to MathJax as \(…\) and \[…\]. See the "Math syntax" section of
    // README.md.
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeMathjaxDelimiters, rehypeFigures],
    }),
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      defaultColor: 'light',
    },
  },
});
