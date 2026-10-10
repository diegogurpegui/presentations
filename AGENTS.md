# Presentations

`docs/` is the site. It is published as-is under a public URL.

- `docs/index.html` is the presentations page. Newest talks go first.
- Each talk is a folder `docs/index/<slug>/`. Its public URL is `.../index/<slug>`.
- A deck is `index.html` plus `assets/` in that folder. CSS, JavaScript, and fonts stay inside the HTML file. Do not link a shared stylesheet, script, or font.
- Talks that are not in this repo stay as external links on the presentations page.

To create a presentation:

1. Read `templates/<name>/TEMPLATE.md`. The first template is `charla`.
2. Copy `templates/<name>/template.html` to `docs/index/<slug>/index.html`.
3. Keep `<style>`, `<script>`, and the SVG sprite unchanged.
4. Replace the `<section class="slide">` elements. Delete unused layouts. Set `<title>`.
5. Add the talk at the top of `docs/index.html`: event, date (`YYYY-MM-DD`), and a link to `index/<slug>/`.

Images go in `docs/index/<slug>/assets/` and are referenced from the HTML as `assets/<file>`. The folder is the deck: `index.html` and `assets/` travel together. To send one file, inline an image as a data URI and skip `assets/`.

Open a deck's `index.html` in a browser. Arrow keys, space, Home, and End move between slides.
