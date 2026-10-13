# Greetings

Hi. My name is Yuchen Lin. This is the construction area for my personal
website. It started with an assignment that required me to publish some work on
a webpage - I had always wanted to host a personal site, so I took the
opportunity and built mine from it. The project was initially created using
Jekyll, and has since been migrated to Astro with the 'Runlog Lite' theme.

## Stack

[Astro 7](https://astro.build) (static output) with the
[Runlog Lite](https://github.com/pasha2do-cyber/runlog-astro-lite) theme
(MIT, see `THEME-LICENSE.md`), Tailwind CSS 4, and MathJax 4 for the math.
Pages are plain markdown in a content collection.

```bash
npm install      # once, to pull the dependencies
npm run dev      # live-reloading dev server on http://localhost:4321
npm run build    # static build into dist/
npm run preview  # serve what was just built
npm run check    # type-check the .astro files

npm run sync:resume   # re-read the resume from the Google Doc
```

Pushing to `main` runs `.github/workflows/publish.yml`, which builds the site
and deploys it to GitHub Pages. The workflow can also be triggered by hand from
the Actions tab. The live site is <https://billylin609.github.io>.

## Layout

```
src/
  content/<section>/<path>/index.md    pages, with figures alongside
  content.config.ts                    front-matter schema
  data/sections.ts                     the five sections and the top bar
  pages/[...id].astro                  every page, served at its directory path
  pages/<section>/index.astro          the five section landing pages
  components/ layouts/ styles/ data/   the theme
  plugins/                             math and figure handling for markdown
```

Two markdown plugins do the custom work, both wired up in `astro.config.mjs`:
`rehype-mathjax-delimiters.mjs` hands the math to MathJax, and
`rehype-figures.mjs` turns images into captioned `<figure>` elements.

`pyproject.toml` pins the Python side (numpy, matplotlib) for `uv`.

## Local setup

The site is an [Astro](https://astro.build) project using the
[Runlog Lite](https://github.com/pasha2do-cyber/runlog-astro-lite) theme. It
needs **Node 22.12 or newer** - Astro 7 refuses to run on older versions.

## Sections

The site is split five ways. `src/data/sections.ts` is the single source of
truth: it drives the top bar, the mobile menu, the footer, the homepage cards
and `llms.txt`, so adding or renaming a section is a one-line edit there.

| Top bar | URL | Content folder | `category` |
| :--- | :--- | :--- | :--- |
| Resume & Portfolio | `/resume` | `src/content/resume/` | `Resume` |
| Development Blog | `/blog` | `src/content/blog/` | `Develop` |
| Travel + Gallery | `/travel` | `src/content/travel/` | `Travel` |
| Coursework | `/coursework` | `src/content/coursework/` | `Course` |
| Problem Solutions | `/solutions` | `src/content/solutions/` | `Solutions` |

Blog, Coursework and Solutions are text listings and share one component,
`SectionIndex.astro`, so they stay identical as the theme changes. Each groups
its entries by the `group` front-matter field, falling back to the folder name.

The other two are built differently, because a list of links is the wrong shape
for them:

- **`/resume`** is a single page that reads top to bottom - intro, work
  experience, personal projects, education, skills - followed by a portfolio
  grid of whatever is in `src/content/resume/`. The resume content itself is
  **not** markdown; it lives in `src/data/resume.json`. See
  [Syncing the resume](#syncing-the-resume) below.
- **`/travel`** opens with a *places been to* strip - every trip on one line,
  newest first - and then a photo grid. Each entry needs a `cover` image in its own
  folder; the grid shows it, and the `[expand]` button opens it full size in a
  lightbox with arrow-key and Escape support. Entries without a `cover` are
  still listed as text underneath, so nothing is hidden.

  The site carries a handful of preview shots; the full albums stay on Google
  Drive, linked per trip through the `album` field. Photographs go in the
  entry's own `figs/` folder - convert HEIC to JPEG first, since the build
  pipeline does not read HEIC, and downscale before committing so the repo does
  not fill up with 4000px originals.

A section with nothing in it renders an empty state telling you which folder to
create, rather than a blank page.

### Syncing the resume

`src/data/resume.json` is generated from a Google Doc, which the page also
links to directly - `doc.view` opens it, and `doc.pdf` hits Google's export
endpoint so the download is always the current version rather than a stale copy
committed to the repo. Both sit at the top of `resume.json`.

To regenerate the text:

```bash
npm run sync:resume
```

The script reads the doc through Google's plain-text export endpoint, so the doc
has to stay shared as **anyone with the link can view**. It needs no
credentials and no API key. The doc ID is at the top of
`scripts/sync-resume.mjs`; change it there if the document moves.

What it overwrites and what it keeps:

| Overwritten from the doc | Kept from the existing file |
| :--- | :--- |
| Work experience, personal projects, education, skills - every heading, date and bullet | `intro`, the `doc` links, the `contact` block, and each `orgHref` link |

Links are matched back on by organisation name, so renaming an employer in the
doc drops its link and the script says so on the way out. If a heading is
renamed and a whole section comes back empty, the script refuses to write and
leaves `resume.json` untouched rather than silently emptying the page.

The portfolio entries under `src/content/resume/` are **not** synced - they are
ordinary markdown pages with their own figures, written once and edited in
place.

## Adding a new page

One directory per piece of work, with its figures inside it. The first folder
under `src/content/` is the section it belongs to:

```
src/content/blog/new_folder/
  index.md        <- the page
  figs/*.png      <- its figures
  script.py       <- the script that produced them
```

1. Create the directory and an `index.md` with this front matter:

   ```yaml
   ---
   title: "<Insert Title>"
   category: "Course/Resume/Develop/Travel/Solutions"
   author: "Yuchen Lin"
   date: 2026-10-13
   summary: "<Insert Summary>"
   ---
   ```

   All five fields are required - the schema in `src/content.config.ts` rejects
   the build otherwise, which is the point: a typo in a field name is an error
   rather than a silently missing byline.

   Pick the `category` that matches the folder the page sits in - the five
   pairs are listed under [Sections](#sections) above. The schema is an enum, so
   a value outside the list fails the build rather than quietly dropping the
   page out of its listing.

   Four optional fields are worth knowing about:

   | Field | Does what |
   | :--- | :--- |
   | `group` | Sub-heading the page is filed under, e.g. `"SYDE 572"`. Pages with no `group` fall back to the folder they sit in. |
   | `cover` | Path to an image in the same folder. The travel gallery needs one; other sections ignore it. |
   | `location` | Shown under the title, next to the date. Meant for travel. |
| `album` | Link to the full photo album - the shared Google Drive folder for that place. Shown on the card and on the page. |
   | `draft` | `true` keeps the page out of every listing and out of the build. |
| `math` | Forces MathJax on or off. Left unset, the page is sniffed for TeX, so you rarely need it. |

   The title, category, author, date and summary are rendered as the page
   header, so don't repeat them as an `#` heading in the body. Start the body
   at `##`.

2. That's it. A folder at `src/content/coursework/syde572/assignment2/` appears
   at `/coursework/syde572/assignment2/`, and in the listings on the homepage
   and `/coursework`, sorted newest first. Nothing to register by hand.

The URL comes from the directory path, so the directory names are the URL. Keep
them lowercase.

## Math syntax

Math is rendered in the browser by MathJax 4. `remark-math` lifts the TeX out
of the markdown verbatim, and `src/plugins/rehype-mathjax-delimiters.mjs` hands
it to MathJax as `\(…\)` and `\[…\]`.

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

### Every piece of TeX must sit inside `$…$` or `$$…$$`

Dollar signs are what mark text as math. Anything outside them is prose, so a
bare LaTeX environment or macro dropped into a paragraph is not picked up -
`\begin{align}` sitting in a paragraph renders as the literal text
`\begin{align}`.

So a multi-line environment is wrapped:

```markdown
$$
\begin{align}
  \frac{dD}{dx} &= 2(x - x_0) + 2\left[(x^2+5) - y_0\right](2x) \\
                &= 2(x - x_0) + 4x(x^2 + 5 - y_0)
\end{align}
$$
```

and so is a cross-reference in running text:

```markdown
Substitute eq. $\eqref{eq:init_point}$ into eq. $\eqref{eq:first_order}$.
```

`aligned`, `bmatrix` and friends work the same way - inside a `$$` block.

### The other trap: never use `$$…$$` inline

`$$` always means display math, so this wrecks the layout:

```markdown
| First | $$0.000$$ |                   <!-- WRONG -->
The point $$(x_0, y_0)$$ is given.      <!-- WRONG -->
```

Use single dollars:

```markdown
| First | $0.000$ |                     <!-- right -->
The point $(x_0, y_0)$ is given.        <!-- right -->
```

### Numbering and referring to equations

Number equations yourself with `\tag`, label them with `\label`, and refer to
them with `\eqref` (parenthesised number) or `\ref` (bare number). MathJax
resolves all three in the browser:

```markdown
$$
D = (x - x_0)^2 + (f(x) - y_0)^2 \tag{1}\label{eq:objective}
$$

From $\eqref{eq:objective}$ we substitute.
```

Because the numbers are manual, they are yours to maintain: insert an equation
in the middle and the ones below it do not renumber themselves.

## Figures

Reference an image relatively and the alt text becomes the visible caption:

```markdown
![Shortest distance from the origin](method1/fig_point_0.000_0.000_init_1.000.png)
```

renders as

```html
<figure><img …><figcaption>Shortest distance from the origin</figcaption></figure>
```

Astro converts the image to WebP at build time, with width, height and
`loading="lazy"` filled in, and gives it a hashed filename. The original stays
in the repo; only the converted copy ships. An image that nothing references is
never built, so dead figures cost nothing but repo size.

Figures are not numbered automatically and there is no cross-reference syntax
for them. If a figure needs a number, put it in the caption text.

## Python environment

Python is the main environment in this repository - it is what produces the
figures. [uv](https://docs.astral.sh/uv/) manages it, and `pyproject.toml` and
`uv.lock` pin the versions, so everyone gets the same ones.

Install uv once, if it is not already there:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then, from the repository root:

```bash
uv sync             # create .venv and install the pinned dependencies
uv run <script>     # run a script inside that environment
```

`uv sync` reads `pyproject.toml`, which needs **Python 3.12 or newer** and
pins numpy and matplotlib. `uv run part1.py` runs a figure script without
activating anything by hand. The `dev` dependency group adds `ipykernel`, for
running the scripts as notebook cells in the editor:

```bash
uv sync --group dev
```

Rerun `uv sync` after pulling, in case the lockfile changed.

## Tables

GitHub-flavoured pipe tables:

```markdown
| Point | $x^*$ | Distance |
| :--- | ---: | ---: |
| $(0,0)$ | $0.0000$ | $5.0000$ |
```

Wide tables scroll sideways rather than stretching the column. There is no
table caption or automatic numbering; a caption goes in a sentence above or
below, or in a `**bold**` line.

## Code listings

A fenced block with a language name is highlighted by Shiki at build time, in a
light and a dark variant that follow the site's theme switcher:

````markdown
```python
def D(x, x0, y0):
    return (x - x0) ** 2 + ((x**2 + 5) - y0) ** 2
```
````

Nothing executes. Code that generates figures lives in the `part*.py` scripts
and is run by hand with `uv run`.

## Quick reference

| Task | Syntax |
| :--- | :--- |
| Inline math | `$x^2$` |
| Display math | `$$` … `$$` on their own lines |
| Multi-line | `align` or `aligned` **inside** a `$$` block |
| Numbered equation | `\tag{1}\label{eq:name}` inside the math |
| Reference it | `$\eqref{eq:name}$` → (1) |
| Figure with caption | `![caption](method1/fig.png)` |
| New page | `src/content/<section>/<name>/index.md` |
| Run a figure script | `uv run part1.py` |
| Dev server | `npm run dev` |
| Never | `$$x$$` inside a line of text, or TeX outside `$…$` |
