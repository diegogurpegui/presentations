# Bitcoin modern

Bitcoin orange `#F7931A`, black `#0A0A0A`, white `#FFFFFF`. Deeper orange `#9A5600` is for links on white. The typeface is the system UI font, so nothing is linked or embedded. CSS and JavaScript stay in the HTML file.

Add `dark` or `light` to each slide. Inner slides keep a short title and give the rest of the slide to the content.

## Create a deck

1. Copy [`template.html`](template.html) to `presentations/<slug>/index.html`.
2. Keep `<style>`, `<script>`, and the SVG sprite unchanged.
3. Replace the `<section class="slide">` elements inside `<main class="deck">`. Delete layouts you do not use.
4. Set `<title>` to the talk name.

Do not link stylesheets, scripts, or font files.

## Images

Put photos in `presentations/<slug>/assets/` and point at them from the HTML:

```html
<img alt="" src="assets/foto.jpg">
```

```
presentations/<slug>/
  index.html
  assets/
    foto.jpg
```

`index.html` and `assets/` travel together. To send one file, inline the image as a data URI and omit `assets/`.

On an image slide, `.shade` and the Bitcoin mark stand in until there is a photo. Full-bleed images crop with `object-fit: cover`. Add `contain` when the picture must stay whole. An `<img>` inside `.body` scales to the content area.

## Presenting

Arrow keys, space, Home, and End move between slides. Click the left edge to go back and anywhere else to go forward. The URL hash is `#1`, `#2`, … Print puts one 16:9 slide on each page.

## Layouts

Every slide is `<section class="slide LAYOUT THEME">`. Theme is `dark` or `light`.

### title

First slide. Dark by default. `light` flips it.

```html
<section class="slide title dark">
  <p class="kicker">Evento · 2026</p>
  <h1>Título de<br>la charla</h1>
  <p class="lede">Una línea que sitúa el tema.</p>
  <div class="watermark" aria-hidden="true">
    <svg class="mark" viewBox="0 0 64 64"><use href="#i-btc"/></svg>
  </div>
  <footer class="foot">
    <p class="who">Nombre Apellido</p>
    <p class="meta">Organización</p>
  </footer>
</section>
```

Omit `.lede`, `.watermark`, or `.meta` when unused.

### section

```html
<section class="slide section dark">
  <p class="kicker">Parte 01</p>
  <h2>Una sección</h2>
</section>
```

### bullets

```html
<section class="slide bullets light">
  <header class="bar">
    <h2>Ideas</h2>
  </header>
  <div class="body">
    <ul>
      <li>Una idea.</li>
    </ul>
  </div>
</section>
```

### columns

`cols-2` is two columns. `cols-3` is three.

```html
<section class="slide columns dark">
  <header class="bar"><h2>Dos columnas</h2></header>
  <div class="body cols-2">
    <div>
      <h3>Izquierda</h3>
      <p>Texto.</p>
    </div>
    <div>
      <h3>Derecha</h3>
      <p>Texto.</p>
    </div>
  </div>
</section>
```

### quote

```html
<section class="slide quote dark">
  <blockquote>
    <p>Una idea clara.</p>
    <footer>Fuente</footer>
  </blockquote>
</section>
```

Omit `footer` when unused.

### table

```html
<section class="slide table light">
  <header class="bar"><h2>Una tabla</h2></header>
  <div class="body">
    <table>
      <thead>
        <tr><th>Fecha</th><th>Origen</th><th>Destino</th><th>Importe</th></tr>
      </thead>
      <tbody>
        <tr><td>…</td><td>Ana</td><td>Luis</td><td>100</td></tr>
      </tbody>
    </table>
  </div>
</section>
```

### links

```html
<section class="slide links dark">
  <header class="bar"><h2>Enlaces</h2></header>
  <div class="body">
    <article class="link">
      <a href="https://ejemplo.com">https://ejemplo.com</a>
      <p>Qué hay del otro lado.</p>
    </article>
  </div>
</section>
```

### canvas

Free stage under the title. Build diagrams from `.row`, `.cols`, `.stack`, `.box`, and `.arrow`.

`.box.solid` is orange with black text. Arrow directions: `.down`, `.left`, `.up`. `.mono` is for hashes.

```html
<section class="slide canvas dark">
  <header class="bar"><h2>Cajas y flechas</h2></header>
  <div class="body">
    <div class="row">
      <div class="box">Mensaje</div>
      <span class="arrow" aria-hidden="true"></span>
      <div class="box solid mono">a1b2…c3</div>
    </div>
  </div>
</section>
```

### image

Full-bleed photo. Drop `.shade` and the mark when the photo is in place.

```html
<section class="slide image dark">
  <img alt="" src="assets/foto.jpg">
</section>
```

Add `contain` on the image for a diagram or screenshot that must not be cropped.

### end

Last slide. Contact row: website, X, Instagram, Nostr, LinkedIn. A long `npub` wraps; add `mono` on that value. `end light` is the white version.

```html
<section class="slide end dark">
  <div class="end-copy">
    <svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><use href="#i-btc"/></svg>
    <h2>Gracias</h2>
    <p>Seguimos en contacto.</p>
  </div>
  <ul class="contacts">
    <li>
      <a href="https://diegogurpegui.com">
        <svg class="icon" aria-hidden="true"><use href="#i-globe"/></svg>
        <span class="label">Web</span>
        <span class="value">diegogurpegui.com</span>
      </a>
    </li>
    <li>
      <a href="https://twitter.com/diegogurpegui">
        <svg class="icon" aria-hidden="true"><use href="#i-x"/></svg>
        <span class="label">X</span>
        <span class="value">@diegogurpegui</span>
      </a>
    </li>
    <li>
      <a href="https://instagram.com/diego.gurpegui">
        <svg class="icon" aria-hidden="true"><use href="#i-instagram"/></svg>
        <span class="label">Instagram</span>
        <span class="value">@diego.gurpegui</span>
      </a>
    </li>
    <li>
      <a href="nostr:npub168nqgewzkamnyh53x0epqrftkv2pdh9gzr6558v4vetzr3w7uxfs63926e">
        <svg class="icon" aria-hidden="true"><use href="#i-nostr"/></svg>
        <span class="label">Nostr</span>
        <span class="value">@diegogurpegui.com</span>
      </a>
    </li>
    <li>
      <a href="https://www.linkedin.com/in/diegogurpegui">
        <svg class="icon" aria-hidden="true"><use href="#i-linkedin"/></svg>
        <span class="label">LinkedIn</span>
        <span class="value">/in/diegogurpegui</span>
      </a>
    </li>
  </ul>
</section>
```

Omit the closing sentence when unused. Drop contact rows you do not need.

## Icons

`#i-btc`, `#i-globe`, `#i-x`, `#i-instagram`, `#i-nostr`, `#i-linkedin`, `#i-arrow`, `#i-key`.

```html
<svg class="icon"><use href="#i-btc"/></svg>
```
