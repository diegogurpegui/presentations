#!/usr/bin/env python3
"""Search and download icons from the Magnific Icons API.

Reads MAGNIFIC_API_KEY from the environment or a repo-root .env file.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.magnific.com"
SHAPES = ("outline", "fill", "lineal-color", "hand-drawn")
COLORS = (
    "gradient",
    "solid-black",
    "multicolor",
    "azure",
    "black",
    "blue",
    "chartreuse",
    "cyan",
    "gray",
    "green",
    "orange",
    "red",
    "rose",
    "spring-green",
    "violet",
    "white",
    "yellow",
)
FREE_SVG = ("all", "free", "premium")
ORDERS = ("relevance", "recent")
FORMATS = ("svg", "png", "gif", "mp4", "aep", "json", "psd", "eps")
PNG_SIZES = (512, 256, 128, 64, 32, 24, 16)
ICON_TYPES = ("standard", "animated", "sticker", "uicon")


def repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "AGENTS.md").is_file():
            return parent
    return here.parents[3]


def load_env(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def api_key() -> str:
    load_env(repo_root() / ".env")
    key = os.environ.get("MAGNIFIC_API_KEY", "").strip()
    if not key:
        print(
            "MAGNIFIC_API_KEY is not set. Copy .env.example to .env and add your key.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return key


def request(path: str, query: list[tuple[str, str]], lang: str, key: str) -> dict:
    url = BASE + path
    if query:
        url += "?" + urllib.parse.urlencode(query)
    req = urllib.request.Request(
        url,
        headers={
            "x-magnific-api-key": key,
            "Accept": "application/json",
            "Accept-Language": lang,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            body = res.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", errors="replace").strip()
        message = detail or err.reason
        try:
            payload = json.loads(detail)
            message = payload.get("message") or message
        except json.JSONDecodeError:
            pass
        print(f"Magnific API {err.code}: {message}", file=sys.stderr)
        raise SystemExit(1) from err
    except urllib.error.URLError as err:
        print(f"Magnific API request failed: {err.reason}", file=sys.stderr)
        raise SystemExit(1) from err
    return json.loads(body) if body else {}


def thumbnail(icon: dict) -> str | None:
    thumbs = icon.get("thumbnails") or []
    if not thumbs:
        return None
    return thumbs[0].get("url")


def compact(icon: dict) -> dict:
    family = icon.get("family") or {}
    style = icon.get("style") or {}
    return {
        "id": icon.get("id"),
        "name": icon.get("name"),
        "slug": icon.get("slug"),
        "family": family.get("name"),
        "style": style.get("name"),
        "free_svg": icon.get("free_svg"),
        "thumbnail": thumbnail(icon),
    }


def emit(payload: dict) -> None:
    json.dump(payload, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


def add_filters(query: list[tuple[str, str]], args: argparse.Namespace) -> None:
    if args.shape:
        query.append(("filters[shape]", args.shape))
    if args.color:
        query.append(("filters[color]", args.color))
    if args.free_svg:
        query.append(("filters[free_svg]", args.free_svg))
    for icon_type in args.icon_type or []:
        query.append(("filters[icon_type][]", icon_type))


def cmd_search(args: argparse.Namespace) -> None:
    query: list[tuple[str, str]] = [
        ("term", args.term),
        ("page", str(args.page)),
        ("per_page", str(args.per_page)),
        ("order", args.order),
        ("thumbnail_size", "128"),
    ]
    if args.family_id:
        query.append(("family-id", str(args.family_id)))
    add_filters(query, args)
    payload = request("/v1/icons", query, args.lang, api_key())
    meta = (payload.get("meta") or {}).get("pagination") or {}
    emit(
        {
            "page": meta.get("current_page", args.page),
            "per_page": meta.get("per_page", args.per_page),
            "total": meta.get("total"),
            "icons": [compact(icon) for icon in payload.get("data") or []],
        }
    )


def cmd_get(args: argparse.Namespace) -> None:
    payload = request(f"/v1/icons/{args.id}", [], args.lang, api_key())
    icon = payload.get("data") if isinstance(payload.get("data"), dict) else payload
    emit(compact(icon))


def cmd_download(args: argparse.Namespace) -> None:
    query = [("format", args.format)]
    if args.format == "png":
        query.append(("png_size", str(args.png_size)))
    payload = request(
        f"/v1/icons/{args.id}/download", query, args.lang, api_key()
    )
    data = payload.get("data") or {}
    url = data.get("url")
    if not url:
        print("Magnific API returned no download URL.", file=sys.stderr)
        raise SystemExit(1)
    dest = Path(args.out)
    if not dest.suffix:
        dest = dest.with_suffix("." + args.format)
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=60) as res:
            dest.write_bytes(res.read())
    except urllib.error.URLError as err:
        print(f"Icon download failed: {err.reason}", file=sys.stderr)
        raise SystemExit(1) from err
    emit(
        {
            "id": args.id,
            "path": str(dest),
            "filename": data.get("filename"),
        }
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Query the Magnific Icons API")
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Search icons by term")
    search.add_argument("term")
    search.add_argument("--page", type=int, default=1)
    search.add_argument("--per-page", type=int, default=8)
    search.add_argument("--order", choices=ORDERS, default="relevance")
    search.add_argument("--shape", choices=SHAPES)
    search.add_argument("--color", choices=COLORS)
    search.add_argument("--free-svg", choices=FREE_SVG, default="free")
    search.add_argument("--family-id", type=int)
    search.add_argument("--icon-type", action="append", choices=ICON_TYPES)
    search.add_argument("--lang", default="en-US")
    search.set_defaults(func=cmd_search)

    get = sub.add_parser("get", help="Fetch one icon by id")
    get.add_argument("id", type=int)
    get.add_argument("--lang", default="en-US")
    get.set_defaults(func=cmd_get)

    download = sub.add_parser("download", help="Download an icon asset")
    download.add_argument("id", type=int)
    download.add_argument("--out", required=True)
    download.add_argument("--format", choices=FORMATS, default="svg")
    download.add_argument("--png-size", type=int, choices=PNG_SIZES, default=512)
    download.add_argument("--lang", default="en-US")
    download.set_defaults(func=cmd_download)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "search" and args.per_page < 1:
        print("--per-page must be greater than 0", file=sys.stderr)
        raise SystemExit(1)
    if getattr(args, "page", 1) < 1:
        print("--page must be greater than 0", file=sys.stderr)
        raise SystemExit(1)
    args.func(args)


if __name__ == "__main__":
    main()
