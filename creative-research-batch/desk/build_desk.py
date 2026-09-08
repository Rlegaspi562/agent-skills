"""Build the Creative Research Desk page from one batch.

The desk is a single HTML file with no external dependencies. It shows the
tracked tags, the full shortlist with reach and relevance scores, which five
are in the batch, a live reach-vs-relevance weighting slider, and the batch
findings. Open it from disk or serve it on localhost.

Usage:
  python desk/build_desk.py --shortlist shortlist.json --findings findings.json
  python desk/build_desk.py --shortlist shortlist.json --findings findings.json --title "Creative Research Desk: Coffee gear" --tags "#coffee,#espresso,#latteart"

Then either double-click desk/index.html, or:
  python -m http.server 8733 --directory desk
and open http://localhost:8733

shortlist.json: a list of videos. Each needs creator, followers, views,
engagementRate, viewFollowerRatio, ageDays, durationSec, subtitles, viral,
relevance, combined, url, caption, whyShortlisted, selected. See
sample/shortlist.json for the shape. Mark the five that shipped selected: true.

findings.json: headline, headline_detail, second, patterns (list of
{title, desc}). See sample/findings.json.
"""
import argparse
import html
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "index.template.html"


def render_findings(f: dict) -> str:
    e = html.escape
    parts = [
        '<div class="finding">',
        '        <span class="tag">Headline finding</span>',
        f'        <p><strong>{e(f["headline"])}</strong> {e(f.get("headline_detail", ""))}</p>',
    ]
    if f.get("second"):
        parts.append(f'        <p>{e(f["second"])}</p>')
    parts.append("      </div>")
    parts.append('      <div class="patterns">')
    for p in f.get("patterns", []):
        parts.append('        <div class="pattern">')
        parts.append(f'          <div class="t">{e(p["title"])}</div>')
        parts.append(f'          <div class="d">{e(p["desc"])}</div>')
        parts.append("        </div>")
    parts.append("      </div>")
    return "\n".join(parts)


def tags_from(shortlist: list[dict], explicit: str | None) -> list[str]:
    if explicit:
        return [t.strip() if t.strip().startswith("#") else "#" + t.strip() for t in explicit.split(",") if t.strip()]
    seen: dict[str, int] = {}
    for v in shortlist:
        for word in v.get("caption", "").split():
            if word.startswith("#") and len(word) > 1:
                seen[word.lower()] = seen.get(word.lower(), 0) + 1
    return [t for t, _ in sorted(seen.items(), key=lambda kv: -kv[1])[:12]]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shortlist", required=True, type=Path)
    ap.add_argument("--findings", required=True, type=Path)
    ap.add_argument("--out", type=Path, default=HERE / "index.html")
    ap.add_argument("--title", default="Creative Research Desk")
    ap.add_argument("--lede", default=(
        "Point it at a niche, and on a schedule it scans tagged posts, scores them for reach "
        "and relevance, and hands back a ranked batch ready for review."
    ))
    ap.add_argument("--tags", help="Comma-separated hashtags to show as tracked. Default: the most common tags in the shortlist captions.")
    args = ap.parse_args()

    shortlist = json.loads(args.shortlist.read_text(encoding="utf-8"))
    findings = json.loads(args.findings.read_text(encoding="utf-8"))
    if not isinstance(shortlist, list) or not shortlist:
        raise SystemExit("shortlist.json must be a non-empty list of videos")
    if sum(1 for v in shortlist if v.get("selected")) == 0:
        raise SystemExit("no video has selected: true; mark the five that shipped")

    page = TEMPLATE.read_text(encoding="utf-8")
    page = page.replace("{{DESK_TITLE}}", html.escape(args.title))
    page = page.replace("{{DESK_LEDE}}", html.escape(args.lede))
    page = page.replace("/*__DATA__*/[]", json.dumps(shortlist, ensure_ascii=False))
    page = page.replace("/*__TAGS__*/[]", json.dumps(tags_from(shortlist, args.tags)))
    page = page.replace("<!--__FINDINGS__-->", render_findings(findings))

    args.out.write_text(page, encoding="utf-8")
    print(f"wrote {args.out}")
    print(f"serve:  python -m http.server 8733 --directory {args.out.parent}")
    print("open:   http://localhost:8733")


if __name__ == "__main__":
    main()
