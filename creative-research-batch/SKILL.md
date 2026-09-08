---
name: creative-research-batch
description: Runs a recurring short-form creative research batch for one niche. Scrapes TikTok hashtags through Apify, ranks on reach and relevance, has Apify watch the top five videos, writes a formatted strategy brief and a four-tab research workbook into a dated Google Drive folder, and builds a local Creative Research Desk page for review. Use when the user asks to run the creative research, run the batch, find this week's videos, or research what is working on TikTok for their niche.
user-invocable: true
argument-hint: "[niche name, or nothing to use the configured niche]"
---

# Creative Research Batch

Every run produces three things for one niche: a brief someone can make
content from, the spreadsheet behind it, and a desk page that shows the whole
shortlist with the scores. The person reading the brief makes ads or posts
from it. Write for that person.

You run the whole batch yourself through two connectors. Do not ask the user
to install anything, upload anything, or run code, unless a step below says
the platform needs it. When you finish they should have a link and nothing
else to do.

## Niche configuration

Everything below reads from this block. Edit it for your niche and leave the
rest of the skill alone. The values shipped here are a worked example for a
direct-to-consumer skincare brand selling on TikTok Shop.

```
Niche:            DTC skincare on TikTok Shop
Reader:           someone on the brand's creative team who makes ads from the brief
The brand:        refer to the client as "the brand" in every output
Hashtags:         skincare, skincaretiktok, tiktokshop, tiktokshopfinds,
                  tiktokmademebuyit, skincarehaul, retinol, barrierrepair,
                  ugc, tiktokads, ecommerce, glowup
Relevance weights:
  3    tiktok shop, tiktokshop, barrier repair, fragrance free, before and after, ugc ad
  2    retinol, ceramide, niacinamide, spf, dupe, offer stack, tiktok ads, ecommerce
  1    skincare haul, moisturizer, serum, acne, glass skin, unboxing
  0.25 glowup, asmr, grwm
Relevance floor for a Viral slot:  1.0
Watch-word to flag when it misfires: tiktokshop
Drive parent folder:  ask the user for the folder name on first run, then reuse it
Desk port:            8733
```

How to pick weights for a new niche: weight 3 is the handful of terms that
only appear when a video is squarely about what the brand sells. Weight 2 is
the product and category vocabulary. Weight 1 is adjacent. Weight 0.25 is
broad lifestyle tags that pull volume but say little. The watch-word is the
most on-target term that also shows up on unrelated content; keep it at 3 and
flag it when it misfires rather than lowering it.

If the user passes a niche name as the argument and it does not match the
block, ask for hashtags and weights before spending anything.

## Connectors, before spending anything

You need **Apify** (scrapes and watches the videos) and **Google Drive**
(where the files go). Check both are connected before step 1.

If Apify is missing, tell the user how to add it on their platform (the README
in this folder has the steps for Cowork, Claude Code, and other agents), then
stop until they confirm. Do the same for Drive. Never proceed on the
assumption that a connector will appear.

Expect two Apify runs per batch, roughly one dollar total.

## 1. Scrape

Run Apify actor `clockworks/tiktok-scraper`, id `GdWCkxBtKWOsKjdch`:

```json
{
  "hashtags": ["<the twelve hashtags from the niche block>"],
  "resultsPerPage": 15,
  "proxyCountryCode": "US",
  "commentsPerPost": 0,
  "topLevelCommentsPerPost": 0,
  "shouldDownloadVideos": false,
  "shouldDownloadCovers": false
}
```

Expect roughly 200 posts.

## 2. Filter

Deduplicate by video id. Drop anything posted more than 30 days ago by
`createTimeISO`. Drop anything under 1,000 views.

Do not filter by date in the actor input. That filter is disabled upstream and
is silently ignored, which is why the scrape pulls more than it needs.

## 3. Rank on two separate scores

**Viral.** Reach, engagement rate, and reach against the creator's own
following. Engagement rate is likes plus comments plus shares plus saves over
views. Reach against following is views over `authorMeta.fans`. Use the log of
views rather than raw views so a single outlier cannot dominate.

**Relevance.** Sum the weights of every term from the niche block found in the
caption and hashtags.

Raw views are never the only input. A video with 1.2M views on a trend filter
is worth less to the brand than one with 22K views that explains how to read a
claim on a listing.

**The watch-word.** Keep it at weight 3 and flag it when it misfires. When a
video qualifies mainly on that one match and turns out to be off topic once
watched, say so in Why Selected and mention it in the brief. That is a finding
about the hashtag, not a mistake to hide: the brand competes for that word
against content that is not in its market.

## 4. Pick five

**Three Viral.** The highest views among videos scoring at or above the
relevance floor, so unrelated content cannot take a slot. Read for format and
hook.

**Two Targeted.** The highest relevance among what remains, regardless of
views. Read for message and audience language. Their value is evidence.

The two groups barely overlap. In a typical 30 day window only a thin slice is
both genuinely viral and specifically about the brand's category. Say so in
the brief.

Keep the full shortlist you ranked, about 20 videos, with every score. The
desk page shows all of it.

## 5. Watch all five

Run the same actor again on just those five URLs:

```json
{
  "postURLs": ["<the five urls>"],
  "aiVideoDescription": true,
  "aiVideoSummary": true,
  "proxyCountryCode": "US",
  "commentsPerPost": 0,
  "topLevelCommentsPerPost": 0
}
```

This step produces the real findings and it is not optional. Apify watches
each video on its own servers and returns `videoMeta.aiVideoDescription`,
timestamped scene descriptions of what is seen and heard, plus
`videoMeta.aiVideoSummary`.

Read every segment of every video. Silent videos often carry the finding: a
price scroll, a listing walkthrough, a held caption over uncut footage.
Captions and metrics alone would file those as empty rows.

Open `videoMeta.coverUrl` and look at it. That is the opening frame, and the
first second decides whether a TikTok works. If the image cannot be fetched
from your environment, take the opening frame from the first timestamped
segment and say so in the brief.

For exact spoken wording try `videoMeta.subtitleLinks`. If you cannot fetch
them, use the AI description and say which you used, per video, in the
workbook's Words Source column.

## 6. Analyze each video

The hook, quoted from the opening line or opening on-screen card. The
structure, beat by beat with timestamps. The retention tactic underneath it.
What the words prove. What the video shows that the words do not. What the
brand should do about it.

## 7. Create today's folder

Inside the Drive parent folder the user named, create a subfolder named with
today's date as `YYYY-MM-DD`. Reuse it if it already exists. Never create a
second folder for the same day. If the parent cannot be found by id, find it
by name, and create it if it is missing, rather than failing the run.

## 8. Write the brief, as a Google Doc in today's folder

Name it `<Niche> TikTok Creative Strategy Brief`. Sections in this order:

1. Title, subtitle, and a research base paragraph: how many videos, over
   what window, how many were scraped to get them
2. **The headline finding.** The single most useful thing in the batch, with
   the specifics that prove it
3. **What the Transcript and Video Analysis Added.** About five bullets, each
   opening with a bolded claim
4. **Transcript Backed Script Patterns.** Numbered, each ending with a bolded
   **Brand use:** line
5. **Examples From the Reviewed Set.** A table: Example, Performance, What it
   really is, What the brand can borrow
6. **What the Visual Only Videos Still Tell Us**
7. **Recommended Creative Families.** Bolded label, one or two sentences each
8. **5 Example Scripts.** Hook, body, CTA. Original scripts informed by the
   observed mechanics, never copies of the source creators
9. **Points on How You Could Present This**
10. **Supporting data.** One line pointing at the workbook

### Format it properly

Write a formatted Google Doc, not markdown pasted into one. Never leave `##`
or `**` or backslash-escaped characters in the finished document. Hashtags and
usernames are written plainly: `#skincare`, `@creator`.

- **Title.** Heading 1, centred, colour `#1F3864`.
- **Subtitle.** Centred, grey, under the title, not a heading.
- **Research base paragraph.** A single cell table with background `#F4F7FB`
  and a thin border. That is the callout box.
- **Section headings.** Heading 2, colour `#1F3864`.
- **Numbered pattern headings.** Heading 3, colour `#2C5085`.
- **Examples table.** A real table. Header row: `#1F3864` background, white
  bold text. No empty row above the header. Body rows left aligned,
  alternating white and `#F7F9FC`.
- **The five scripts.** Each in its own single cell table with background
  `#F8FAFD` and a thin border, so it reads as a card. Hook, Body and CTA
  labels bold inside the cell.
- **Lists.** Real Doc list formatting.

The reader compares batches side by side, so keep this layout identical
between runs.

**How to get there.** If your Drive connector accepts HTML as text and
converts it, write the brief as HTML with these styles inline and upload it
with content type `text/html`. Drive turns it into a Doc and keeps the
headings, colours, table backgrounds and cards. That path works on every
platform this skill has been run on.

## 9. Write the workbook, as a Google Sheet in today's folder

Name it `<Niche> TikTok Batch Research`. Four tabs.

**Viral** and **Targeted**, one row per video, ranked by views: Rank, Bucket,
Creator, Posted, Caption, Views, Engagement Rate, Followers, View/Follower
Ratio, Duration, TikTok URL, Why Selected.

**Workflow**, two columns, Field and Detail: the date, the window, the
hashtags, how many posts were scraped, how many survived filtering, how each
bucket was chosen, what the ranking did not decide (any editorial holds and
why), and that every video was watched by Apify's video analysis. It must
include a row labelled **"Viral vs Targeted, and why both"** that explains, in
plain language for someone seeing this for the first time: Viral videos are
chosen for performance and read for format; Targeted videos are chosen for
subject matter and read for message and their view counts are expected to be
small; the two rarely overlap, so borrow format from Viral, message from
Targeted, and combine them.

**Video Analysis**, one row per video: Bucket, Rank, Creator, Views,
Engagement Rate, TikTok URL, Words Source, Opening Hook, Script Structure,
Primary Tactic, What the Words Prove, What the Video Shows, What the Video
Proves, Brand Application.

**How to get there.** Build the workbook as an `.xlsx` (the four tabs are
plain rows; any spreadsheet library works). Then:

- If your Drive connector can upload a binary file and convert it, upload the
  `.xlsx` as a Google Sheet. Four tabs land intact.
- If it cannot (some Drive connectors reject binary uploads), run
  `scripts/drive_upload.py` from this folder. One-time OAuth setup is at the
  top of that file. It uploads the `.xlsx` and converts it to a four-tab Sheet.
- If neither is possible in this session, upload a single CSV as text with
  content type `text/csv`: stack the four tabs with a heading row before each
  section and a Bucket column on the video rows. That lands a populated
  one-tab Sheet. Say plainly in the report that it is one tab, and hand the
  user the four-tab `.xlsx` as a file.

Never report that the Sheet landed with four tabs unless it did.

## 10. Build and host the Creative Research Desk

The desk is a single HTML page: tracked tags, batch size, cadence and run day
as live controls, the full shortlist with reach and relevance scores, the five
marked as in this batch, a reach-vs-relevance weighting slider that re-ranks
live, and the batch findings.

1. Write `shortlist.json`: every video from step 4's shortlist with creator,
   followers, views, engagementRate, viewFollowerRatio, ageDays, durationSec,
   subtitles, viral, relevance, combined, url, caption, whyShortlisted, and
   `selected: true` on the five that shipped. `desk/sample/shortlist.json`
   shows the shape.
2. Write `findings.json`: headline, headline_detail, second, and four
   patterns with title and desc, drawn from the brief.
   `desk/sample/findings.json` shows the shape.
3. Run `python desk/build_desk.py --shortlist shortlist.json --findings findings.json --title "Creative Research Desk: <Niche>"`.
   It writes `desk/index.html`.
4. Host it:
   - On a machine where you can run a server (Claude Code, a local agent):
     `python -m http.server 8733 --directory desk`, then give the user
     `http://localhost:8733`.
   - In a sandbox with no reachable localhost (Cowork): upload
     `desk/index.html` into today's Drive folder as a plain file, not
     converted (content type `text/html`, conversion off). It opens in any
     browser from a download and needs no server. Tell the user that.

The desk replays the batch. Pressing "Run this batch now" on the page does not
call any service; it animates the shortlist that is baked into the file.

## 11. Hand back the links

Finish with the link to today's folder, the desk (localhost URL or the file in
the folder), a one line summary of the batch, and what the two Apify runs
cost. If any of the three outputs failed to land, name which and why. Do not
report success unless all three are in place.

## How to write

Be specific or say nothing. "Strong engagement" is worthless. "14.2%
engagement, the highest among the Viral picks" is a finding.

Quote what is on screen. Prices, on-screen text and captions are evidence.
Reproduce them exactly as the video description records them.

Name competitors and listing patterns. If a video shows a rival's price band
or page layout, that is intelligence the brand is paying for. Do not soften it.

Separate observation from inference. If two things look connected, say they
line up. Do not claim one caused the other.

No em dashes anywhere. Use a period, comma, colon or parentheses.

Do not use the word "actually".

Do not use steal or stealing. Prefer borrow, study, use the structure.

Never invent footage or numbers. Everything traces to a field in the Apify
data.
