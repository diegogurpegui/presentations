# Charla

One self-contained HTML file. Navy `#192B58`, charcoal `#1C212C`, peach circle `#F8E0C8`. Ubuntu for text, Spectral for titles on photos. Fonts are already embedded in `template.html`.

## Create a deck

1. Copy [`template.html`](template.html) to `presentations/<slug>.html`.
2. Keep `<style>`, `<script>`, and the SVG sprite unchanged.
3. Replace the `<section class="slide">` elements inside `<main class="deck">`. Delete layouts you do not use.
4. Set `<title>` to the talk name.

Do not link stylesheets, scripts, or font files. The finished talk must stay one HTML file.

Photos and logos may live in `presentations/<slug>/assets/`, or be inlined as data URIs when the file has to travel alone. The `shade-stone` and `shade-dusk` classes are placeholders for when there is no photo yet.

## Presenting

Arrow keys, space, Home, and End move between slides. Click the left edge to go back and anywhere else to go forward. The URL hash is `#1`, `#2`, … Print puts one 16:9 slide on each page. The `n / N` counter is hidden in print.

## Layouts

Every slide is `<section class="slide LAYOUT">`.

### title

```html
<section class="slide title">
  <h1>Título de la charla</h1>
  <p class="kicker"><span class="badge">Evento</span> 2026</p>
  <div class="watermark" aria-hidden="true">
    <svg class="mark"><use href="#i-btc"/></svg>
  </div>
  <div class="band">
    <img class="logo" alt="Organizador" src="assets/logo.svg">
    <div class="speaker">
      <p class="who">Nombre Apellido</p>
      <ul class="pills">
        <li><a href="https://ejemplo.com">ejemplo.com <svg class="icon"><use href="#i-globe"/></svg></a></li>
      </ul>
    </div>
  </div>
</section>
```

Omit `.kicker`, `.watermark`, or `.logo` when unused. A text stand-in is `<p class="logo-text">Nombre</p>`.

### section

Full-bleed photo, centered Spectral title. Add `overlay` and `<div class="veil"></div>` for a dark wash.

```html
<section class="slide section overlay">
  <img class="bg" alt="" src="assets/foto.jpg">
  <div class="veil"></div>
  <h2>Una sección</h2>
</section>
```

### image

```html
<section class="slide image">
  <img alt="" src="assets/foto.jpg">
</section>
```

### bullets

```html
<section class="slide bullets">
  <header class="bar"><h2>Una lista</h2></header>
  <div class="body">
    <ul>
      <li>Primera idea.</li>
      <li>Segunda idea.</li>
    </ul>
  </div>
</section>
```

### links

```html
<section class="slide links">
  <header class="bar"><h2>Enlaces</h2></header>
  <div class="body">
    <article class="link">
      <a href="https://ejemplo.com">https://ejemplo.com</a>
      <p>Qué hay del otro lado.</p>
    </article>
  </div>
</section>
```

### columns

`cols-2` draws a dashed rule. `cols-3` is three equal columns.

```html
<section class="slide columns">
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

### table

```html
<section class="slide table">
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

### canvas

Free stage under the navy bar. Build diagrams from `.row`, `.cols`, `.stack`, `.box`, `.pill`, and `.arrow`.

Box colors: default blue, `.purple`, `.amber`. `.pill` rounds a box. Arrow directions: `.down`, `.left`, `.up`. `.arrow.purple` changes the color. `.mono` is for hashes.

```html
<section class="slide canvas">
  <header class="bar"><h2>Cajas y flechas</h2></header>
  <div class="body">
    <div class="row">
      <div class="box">Mensaje</div>
      <span class="arrow" aria-hidden="true"></span>
      <div class="box purple">Hash</div>
    </div>
    <div class="row">
      <svg class="icon" aria-hidden="true"><use href="#i-key"/></svg>
      <div class="box amber pill">Nonce</div>
    </div>
  </div>
</section>
```

Icons in the sprite: `#i-arrow`, `#i-key`, `#i-db`, `#i-person`, `#i-gear`, `#i-globe`, `#i-btc`.

```html
<svg class="icon"><use href="#i-db"/></svg>
```

A custom drawing can also be an image inside `.body`.

### thanks

```html
<section class="slide thanks">
  <div class="thanks-left">
    <h2>¡Muchas<br>gracias!</h2>
    <ul class="pills">
      <li><a href="https://ejemplo.com">ejemplo.com <svg class="icon"><use href="#i-globe"/></svg></a></li>
    </ul>
  </div>
  <div class="thanks-right">
    <h3>Título de la charla</h3>
    <div class="watermark" aria-hidden="true">
      <svg class="mark"><use href="#i-btc"/></svg>
    </div>
  </div>
</section>
```

Optional extra pills go in `.thanks-right`, after the title.

## Fonts

Ubuntu is under the [Ubuntu Font Licence 1.0](https://ubuntu.com/legal/font-licence). Spectral is under the [SIL Open Font License 1.1](https://openfontlicense.org). Both notices are in the `<style>` block. Leave them there when you copy the file.
