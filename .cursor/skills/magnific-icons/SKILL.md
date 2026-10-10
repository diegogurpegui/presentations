---
name: magnific-icons
description: Search and download Magnific icons into a slide deck. Use when the user asks for Magnific icons, stock icons, or icons from magnific.com inside a presentation.
---

# Magnific icons

Search and download icons from the [Magnific Icons API](https://docs.magnific.com/api-reference/icons/icons-api). The key lives in `MAGNIFIC_API_KEY` (repo-root `.env`, gitignored). Never print the key, never write it into a file that is committed.

Run from the repo root:

```bash
python3 .cursor/skills/magnific-icons/scripts/icons.py search "wallet" --shape outline --per-page 8
python3 .cursor/skills/magnific-icons/scripts/icons.py get 52912
python3 .cursor/skills/magnific-icons/scripts/icons.py download 52912 --out docs/index/<slug>/assets/wallet.svg
```

If the script exits 2, the key is missing. Finish the deck without Magnific icons and say so. Do not invent icon files.

## Choosing an icon

- Save files in `docs/index/<slug>/assets/` and reference them as `assets/<file>`.
- Default format is SVG. Use `--format png` only when the slide needs a bitmap.
- Search defaults to free SVGs (`--free-svg free`) so download does not hit a premium lock.
- Keep one shape for a deck (`outline` or `fill`). Pass `--lang es-ES` or `en-US` to match the talk.
- Pick from the search JSON (`id`, `name`, `family`, `style`, `thumbnail`). Download that id. Do not hotlink thumbnail URLs in the deck.
