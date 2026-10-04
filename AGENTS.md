# Slides

A finished talk is a folder. CSS, JavaScript, and fonts stay inside the HTML file. Do not link a shared stylesheet, script, or font.

To create a presentation:

1. Read `templates/<name>/TEMPLATE.md`. The first template is `charla`.
2. Copy `templates/<name>/template.html` to `presentations/<slug>/index.html`.
3. Keep `<style>`, `<script>`, and the SVG sprite unchanged.
4. Replace the `<section class="slide">` elements. Delete unused layouts. Set `<title>`.

Images go in `presentations/<slug>/assets/` and are referenced from the HTML as `assets/<file>`. The folder is the deck: `index.html` and `assets/` travel together. To send one file, inline an image as a data URI and skip `assets/`.

Open `index.html` in a browser. Arrow keys, space, Home, and End move between slides.
