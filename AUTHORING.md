# Authoring pages

How to add a page to this site and how to write math on it. Everything below was
checked against Quarto 1.10.19, the version pinned in
`.github/workflows/publish.yml`.

## Local setup

Install Quarto once from <https://quarto.org/docs/get-started/>, then:

```bash
quarto preview          # live-reloading dev server (replaces `jekyll serve`)
quarto render           # build the whole site into _site/
```

## Adding a new page

1. Create the file, e.g. `SYDE572/assignment2/homework.qmd`.
2. Give it front matter:

   ```yaml
   ---
   title: "Assignment 2"
   subtitle: "SYDE 572 · Assignment 2"
   author: "Yuchen Lin"
   date: 2026-11-03
   ---
   ```

   The title, subtitle, author and date are rendered as the page header, so
   don't repeat them as an `#` heading in the body. Start the body at `##`.

3. Link it from `index.qmd`, pointing at the `.qmd` — Quarto rewrites the
   extension to `.html` for you:

   ```markdown
   - [SYDE 572 — Assignment 2](SYDE572/assignment2/homework.qmd)
   ```

No change to `_quarto.yml` is needed. Its render list globs `SYDE572/**/*.qmd`,
so any new directory under `SYDE572/` is picked up automatically.

Images go in a folder next to the page and are referenced relatively
(`![caption](method1/fig_thing.png)`), the same as before. Quarto copies the
files you actually reference into `_site/`.

## Math syntax

One rule covers almost everything:

| Want | Write | Notes |
| :--- | :--- | :--- |
| Inline math | `$f(x) = x^2 + 5$` | Single dollars, inside a line of text |
| Display math | `$$` on its own line, then the TeX, then `$$` | Centred block on its own |

```markdown
The objective is $D = (x - x_0)^2$, which expands to:

$$
D = (x - x_0)^2 + \left[(x^2 + 5) - y_0\right]^2
$$
```

### The one trap: never use `$$…$$` inline

Jekyll's kramdown accepted `$$x$$` *inside* a line and treated it as inline
math. Quarto (Pandoc) does not — `$$` always means display, so this:

```markdown
| First | $$0.000$$ |        <!-- WRONG -->
The point $$(x_0, y_0)$$ is given.   <!-- WRONG -->
```

turns every table cell and mid-sentence symbol into a centred block and wrecks
the layout. Use single dollars:

```markdown
| First | $0.000$ |          <!-- right -->
The point $(x_0, y_0)$ is given.     <!-- right -->
```

This is the single most common mistake when porting old notes over. All 546
occurrences in `assignment1/homework.qmd` were converted during the migration.

### Multi-line equations

Use `aligned` inside a display block. `&` sets the alignment column and `\\`
ends a line:

```markdown
$$
\begin{aligned}
  \frac{dD}{dx} &= 2(x - x_0) + 2\left[(x^2+5) - y_0\right](2x) \\
                &= 2(x - x_0) + 4x(x^2 + 5 - y_0)
\end{aligned}
$$
```

Matrices work the same way — `bmatrix` nested in a display block:

```markdown
$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
$$
```

## Numbering and referring to equations

**This is the better way, and what you should use in new pages.**

Put a `{#eq-…}` label after the closing `$$`, then refer to it with `@eq-…`:

```markdown
$$
D = (x - x_0)^2 + (f(x) - y_0)^2
$$ {#eq-objective}

$$
\begin{aligned}
  \frac{dD}{dx} &= 2(x - x_0) + 4x(x^2 + 5 - y_0)
\end{aligned}
$$ {#eq-first-order}

Substituting @eq-objective into @eq-first-order gives the stationary point.
```

Quarto numbers the equations in document order and renders the references as
clickable links:

| Form | Renders as |
| :--- | :--- |
| `@eq-objective` | Equation 1 |
| `[@eq-objective]` | Equation 1 |
| `-@eq-objective` | 1 (bare number, no prefix) |

The label **must** start with `eq-`, or Quarto treats it as a plain id and the
reference won't resolve.

Why this beats writing the numbers yourself:

- Numbering is automatic. Insert an equation at the top and everything below
  renumbers; nothing to chase by hand.
- One syntax produces correct output in both HTML and PDF.
- A reference to a label that doesn't exist is reported at render time instead
  of silently printing `(?)`.

### The older `\tag` / `\label` / `\eqref` style

`assignment1/homework.qmd` predates the migration and numbers its equations
manually:

```markdown
$$
D = (x - x_0)^2 \tag{1}\label{eq:objective}
$$

From $\eqref{eq:objective}$ we substitute.
```

This still works — MathJax resolves it in the browser and LaTeX resolves it in
the PDF — so there's no need to go back and rewrite it. Don't start new pages
this way, though: you have to maintain the numbers yourself, and it carries a
PDF trap worth knowing about.

**The trap:** `\tag` inside `align` inside `$$` is illegal in LaTeX
(`amsmath: Erroneous nesting of equation structures`) even though MathJax
tolerates it. The fix, already applied to `assignment1`, is to drop the `$$`
around those blocks and let the environment stand alone:

```markdown
\begin{align}
  a &= b \\
    &= c \tag{2}\label{eq:second}
\end{align}
```

Pandoc re-wraps that for HTML, so the web output is unchanged, and LaTeX gets a
valid environment. If you use `{#eq-…}` labels instead, this never comes up —
use `aligned` in a normal `$$` block and you're fine in both formats.

**Don't mix the two styles in one document.** On its own, each is consistent: a
page using only `\tag{7}` prints `(7)`, and a page using only `{#eq-…}` numbers
from 1 upward. Put both on the same page and the PDF counter drifts — a block
tagged `\tag{2}` printed as `(3)` in testing, because Quarto's labelled
equations had already advanced the counter. `assignment1` is entirely
manual-tag, so it is fine; just don't add `{#eq-…}` labels to it. New pages
should use `{#eq-…}` throughout.

## Figures

### An image you already have

```markdown
![Shortest distance from the origin](method1/fig_point_0.png){#fig-origin}

As @fig-origin shows, the minimum sits on the axis.
```

Labels must start with `fig-`. `@fig-origin` renders as "Figure 1".

### A figure generated when the page renders

Instead of running a script by hand and committing the PNG, let Quarto execute
the code. Use a `{python}` block (note the braces — plain ` ```python ` is a
static listing that is only displayed):

````markdown
```{python}
#| label: fig-parabola
#| fig-cap: "Distance from $(0,0)$ to $f(x) = x^2 + 5$."
#| echo: false

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(x, x**2 + 5, label="$f(x) = x^2 + 5$")
ax.plot(0, 5, "ro", label="closest point")
ax.legend()
plt.show()
```

@fig-parabola was generated at render time.
````

`#| echo: false` hides the source and shows only the figure; drop it to show
both. Captions may contain math.

This needs a few packages in the project venv that aren't there yet:

```bash
uv add --dev pyyaml nbformat nbclient
```

`ipykernel`, `numpy` and `matplotlib` are already present. Do **not** call
`matplotlib.use("Agg")` in a `{python}` block — it suppresses the inline
capture and the figure silently fails to appear.

If you enable this, the CI workflow needs Python set up before `quarto render`,
since the GitHub runner has none of it.

## Tables

Pipe tables, with an optional caption line starting with `:`:

```markdown
| Point | $x^*$ | Distance |
| :--- | ---: | ---: |
| $(0,0)$ | $0.0000$ | $5.0000$ |

: Converged results {#tbl-converged}
```

`@tbl-converged` renders as "Table 1". Labels must start with `tbl-`.

## Code listings

A fence with a bare language name is displayed, not run:

````markdown
```python
def D(x, x0, y0):
    return (x - x0) ** 2 + ((x**2 + 5) - y0) ** 2
```
````

## PDF output

Any page can be rendered to PDF, which is useful for submitting assignments:

```bash
quarto render SYDE572/assignment1/homework.qmd --to pdf
```

The PDF lands in `_site/` alongside the HTML. LaTeX resolves all equation,
figure and table cross-references, and the print styling in `styles.css` is not
involved — this is a real typeset document, not a printed web page.

PDF is deliberately not part of `quarto render`, so site builds stay fast and CI
needs no LaTeX install.

## Quick reference

| Task | Syntax |
| :--- | :--- |
| Inline math | `$x^2$` |
| Display math | `$$` … `$$` on their own lines |
| Multi-line | `aligned` inside a display block |
| Numbered equation | `$$ … $$ {#eq-name}` |
| Reference it | `@eq-name` → Equation 1 |
| Static figure | `![cap](path){#fig-name}` → `@fig-name` |
| Generated figure | ` ```{python} ` + `#| label: fig-name` |
| Table caption | `: Caption {#tbl-name}` → `@tbl-name` |
| Never | `$$x$$` inside a line of text |
