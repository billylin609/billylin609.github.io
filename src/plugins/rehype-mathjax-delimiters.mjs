import { visit, SKIP } from 'unist-util-visit';

/**
 * Hand remark-math's output to MathJax instead of rendering it at build time.
 *
 * remark-math parses `$…$` and `$$…$$` into math nodes, which mdast-util-math
 * turns into `<code class="language-math math-inline">` and
 * `<pre><code class="language-math math-display">`. KaTeX cannot render this
 * project's math - the pages use `\tag`, `\label` and `\eqref`, which it does
 * not support - so this rewrites those elements into the markup MathJax
 * reads at runtime:
 *
 *   <span class="math inline">\(x\)</span>
 *   <div class="math display">\[x\]</div>
 *
 * The TeX stays a text node, so `<`, `>` and `&` are escaped in the HTML and
 * the browser hands MathJax the original characters back via textContent.
 */
export default function rehypeMathjaxDelimiters() {
  return (tree) => {
    visit(tree, 'element', (node, index, parent) => {
      if (!parent || index === null) return;

      // Display math arrives wrapped in a <pre>: replace the <pre> wholesale.
      if (node.tagName === 'pre' && node.children.length === 1 && isMath(node.children[0], 'math-display')) {
        parent.children[index] = displayMath(node.children[0]);
        return [SKIP];
      }
      if (isMath(node, 'math-display')) {
        parent.children[index] = displayMath(node);
        return [SKIP];
      }
      if (isMath(node, 'math-inline')) {
        parent.children[index] = element('span', ['math', 'inline'], `\\(${toText(node)}\\)`);
        return [SKIP];
      }
    });
  };
}

const displayMath = (code) => element('div', ['math', 'display'], `\\[${toText(code)}\\]`);

const isMath = (node, cls) =>
  node.type === 'element' && node.tagName === 'code' && classList(node).includes(cls);

const classList = (node) => {
  const c = node.properties?.className;
  return Array.isArray(c) ? c : typeof c === 'string' ? c.split(/\s+/) : [];
};

const element = (tagName, className, value) => ({
  type: 'element',
  tagName,
  properties: { className },
  children: [{ type: 'text', value }],
});

const toText = (node) =>
  node.type === 'text' ? node.value : (node.children ?? []).map(toText).join('');
