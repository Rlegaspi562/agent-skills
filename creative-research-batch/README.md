# Creative Research Batch

A recurring research run for one niche on TikTok. Point it at your hashtags
and every batch gives you three things:

- **A strategy brief** (Google Doc). The headline finding, what watching the
  videos added, script patterns with a "brand use" line each, an examples
  table, recommended creative families, and five original scripts.
- **A research workbook** (Google Sheet). Four tabs: Viral, Targeted,
  Workflow, Video Analysis. Every number in the brief traces to a row here.
- **A Creative Research Desk** (one HTML page). The full shortlist with reach
  and relevance scores, which five made the batch, and a weighting slider that
  re-ranks live.

It ships configured for direct-to-consumer skincare on TikTok Shop so it runs
on day one. Swapping the niche is one block at the top of `SKILL.md`.

```text
You: /creative-research-batch

Agent: Both connectors are connected. Scraping 12 hashtags now.
       ...
       212 posts, 168 unique, 61 in the last 30 days over 1,000 views.
       Three Viral picks, two Targeted. Watching all five.
       ...
       Folder: <link>   Brief: <link>   Workbook: <link>, four tabs
       Desk: http://localhost:8733
       Apify: two runs, $0.94.
```

## What you need

| Thing | Why | Cost |
|---|---|---|
| An [Apify](https://apify.com) account | It scrapes the hashtags and watches the five videos on its own servers, returning scene-by-scene descriptions | Free tier includes monthly credit. A batch is two runs, about $1 |
| Google Drive | Where the brief and workbook land | Free |
| Python 3.10+ | Builds the desk page and, on some platforms, uploads the workbook | Free |

The video-watching step is what makes this worth running. Metrics and
captions cannot tell you that the top performer is a silent scroll through
prices. The scene descriptions can.

## Install

Clone the repository:

```bash
git clone https://github.com/Rlegaspi562/agent-skills
```

### Claude Code

macOS or Linux:

```bash
mkdir -p ~/.claude/skills && cp -R agent-skills/creative-research-batch ~/.claude/skills/
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills" | Out-Null; Copy-Item -Recurse -Force .\agent-skills\creative-research-batch "$HOME\.claude\skills\"
```

### Cowork

Open Customize in the sidebar, then Skills, then add a skill from a folder and
choose `creative-research-batch`. Or paste the contents of `SKILL.md` as a new
skill body and name it `creative-research-batch`.

### Codex

Same copy commands as Claude Code, replacing `.claude/skills` with
`.codex/skills`.

### Any other agent

The skill is plain Markdown. Paste `SKILL.md` into your system prompt, project
instructions, or custom-instructions box. The agent still needs a way to call
Apify and write to Drive; see the next section.

## Connect Apify and Google Drive

The skill checks both before it spends anything and stops if either is
missing. Here is how to add them.

### Cowork

1. Customize in the sidebar, then Connectors, then the + icon.
2. Search **Apify**. It signs in through your browser. No token to paste.
3. Search **Google Drive** and sign in the same way.

### Claude Code

Google Drive is a built-in connector. Add it under Settings, Connectors, then
sign in.

Apify is an MCP server. Add it with:

```bash
claude mcp add apify --transport http https://mcp.apify.com
```

It opens a browser tab to sign in on first use. If your version asks for a
token instead, create one under Apify Settings, Integrations, API tokens, and
add it as `--header "Authorization: Bearer <token>"` on that command. Keep the
token out of any file you commit.

**Known limit.** The Claude Code Drive connector cannot upload binary files,
which is what a four-tab spreadsheet is. The skill knows this and uses
`scripts/drive_upload.py` instead. That script needs a one-time Google setup,
about ten minutes; the steps are at the top of the file. Without it, the skill
falls back to a one-tab Sheet and hands you the four-tab `.xlsx` as a file.

### Any other agent

Your agent needs two capabilities: call Apify's API (or its MCP server at
`https://mcp.apify.com`) and write files into Google Drive. If it has an
Apify integration and a Drive integration, connect both the way that agent
does it. If it only has HTTP access, it can call Apify's REST API directly
with an API token from Apify Settings, and upload to Drive with
`scripts/drive_upload.py`.

## Run it

```text
/creative-research-batch
```

First run asks which Drive folder the batches should go in. Each run then
creates a dated subfolder, `2026-09-08`, and puts the brief and workbook
there. The desk is served on `http://localhost:8733` when the agent can run a
server, or dropped into the same folder as an HTML file when it cannot (open
it from a download; it needs no server).

To run for a niche other than the configured one:

```text
/creative-research-batch coffee gear
```

The agent asks for hashtags and weights before spending anything.

## Change the niche

Open `SKILL.md`. The block under **Niche configuration** is the only thing
to edit:

- **Hashtags.** About twelve. Mix category tags people browse with
  product-specific ones.
- **Relevance weights.** Weight 3 is the few terms that only appear when a
  video is squarely about what you sell. Weight 2 is product and category
  vocabulary. Weight 1 is adjacent. Weight 0.25 is broad lifestyle tags.
- **Watch-word.** The most on-target term that also shows up on unrelated
  content. It stays at weight 3, and the skill flags it when it misfires,
  because that tells you who you compete with for the tag.

Everything else in the skill reads from that block.

## What lands where

```
<your Drive folder>/
  2026-09-08/
    <Niche> TikTok Creative Strategy Brief     Google Doc
    <Niche> TikTok Batch Research              Google Sheet, four tabs
    index.html                                 the desk, only on platforms without localhost
```

Locally, `desk/index.html` after each run, plus the `shortlist.json` and
`findings.json` it was built from.

## Try the desk before your first run

The folder ships with a sample batch so you can see the page:

```bash
python desk/build_desk.py --shortlist desk/sample/shortlist.json --findings desk/sample/findings.json
python -m http.server 8733 --directory desk
```

Open `http://localhost:8733`. The sample creators and video links are
placeholders and do not resolve; the page is for layout, not data.

## Troubleshooting

**"Apify is not connected."** The skill stops here on purpose. Add the
connector per the section above, then run again.

**The Sheet landed with one tab.** Your platform's Drive connector cannot
upload binary. Set up `scripts/drive_upload.py` once (steps at the top of the
file) and future runs land four tabs. The `.xlsx` the agent handed you has all
four already.

**The brief has `**` or `##` showing as text.** The agent pasted markdown into
a Doc instead of writing HTML with inline styles. Ask it to redo step 8 using
the HTML path described in the skill.

**The scrape returned videos older than 30 days.** Expected. The actor's date
filter is disabled upstream, so the skill filters after the scrape.

**Cost looks higher than $1.** `resultsPerPage` is 15 across 12 hashtags.
Fewer hashtags or a lower page size brings it down, at the cost of a thinner
shortlist.

## Related

This skill finds videos by hashtag scrape. To reverse-engineer specific
URLs you already have, use [`viral-analyze/`](../viral-analyze/).

## Privacy

Nothing in this folder contains credentials. `scripts/drive_upload.py` writes
`client_secret.json` and `token.json` next to itself on first use; both are
listed in `.gitignore`. Do not commit them. The skill never reads anything in
your Drive it did not create.
