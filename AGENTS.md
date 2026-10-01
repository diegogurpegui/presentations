# Slides

A finished talk is one self-contained HTML file. CSS and JavaScript stay inside that file. Do not link a shared stylesheet, script, or font.

To create a presentation:

1. Read `templates/<name>/TEMPLATE.md`. The first template is `charla`.
2. Copy `templates/<name>/template.html` to `presentations/<slug>.html`.
3. Keep `<style>`, `<script>`, and the SVG sprite unchanged.
4. Replace the `<section class="slide">` elements. Delete unused layouts. Set `<title>`.

Photos may live in `presentations/<slug>/assets/`, or be inlined as data URIs when the deck must travel as a single file.

Open the HTML file in a browser. Arrow keys, space, Home, and End move between slides.
