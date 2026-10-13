import { visit } from 'unist-util-visit';

/**
 * Turn a paragraph holding a single captioned image into a real figure:
 *
 *   ![Shortest distance from (0, 0)](method1/fig.png)
 *
 *   <figure><img src="…" alt=""><figcaption>Shortest distance…</figcaption></figure>
 *
 * The alt text therefore shows up as a visible caption, written as ordinary
 * markdown. The alt attribute is emptied because the
 * caption now carries that text, and repeating it makes screen readers read it
 * twice.
 */
export default function rehypeFigures() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (!parent || index === null || node.tagName !== 'p') return;

      const children = node.children.filter(
        (c) => !(c.type === 'text' && c.value.trim() === ''),
      );
      const [img] = children;
      if (children.length !== 1 || img.tagName !== 'img') return;

      const caption = typeof img.properties?.alt === 'string' ? img.properties.alt : '';
      if (!caption) return;

      img.properties.alt = '';
      parent.children[index] = {
        type: 'element',
        tagName: 'figure',
        properties: {},
        children: [
          img,
          {
            type: 'element',
            tagName: 'figcaption',
            properties: {},
            children: [{ type: 'text', value: caption }],
          },
        ],
      };
    });
  };
}
