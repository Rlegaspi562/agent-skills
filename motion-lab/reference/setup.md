# Setup from zero

Verbatim from the article. Path 1 needs no install: open Claude, pick Opus 5.5, paste a prompt, iterate in the preview panel with a frame counter and space-bar pause, then download and screen-record (fine for a first post, not frame-exact).

```bash
# macOS: Node, ffmpeg and a headless browser (Claude Code already installed)
brew install node ffmpeg
mkdir motion-lab && cd motion-lab
npm init -y
npm i -D playwright
npx playwright install chromium
claude            # then type /model and pick Opus 5.5
```

```powershell
# Windows 11, PowerShell: the same lab (open a NEW terminal after winget)
winget install OpenJS.NodeJS.LTS
winget install Gyan.FFmpeg
mkdir motion-lab; cd motion-lab
npm init -y
npm i -D playwright
npx playwright install chromium
claude            # then type /model and pick Opus 5.5
```

Windows notes: PowerShell 5.1 has no &&, hence the semicolons. If PowerShell refuses to run npx, type npx.cmd instead.

Effort: medium for everything; raise it only when a from-scratch piece misses twice. /fast in Claude Code for iteration sprints (up to 2.5x faster, higher token price).

## Remotion and HyperFrames

```bash
# Remotion: video as React components
npx create-video@latest          # pick a template, name it my-video
cd my-video
npm i
npx remotion skills add          # Agent Skills for Claude Code
npm run dev                      # Remotion Studio in your browser
npx remotion render MyComp out/video.mp4   # MyComp = your composition id

# HyperFrames: HTML + GSAP in, MP4 out (needs Node 22+ and FFmpeg)
npx hyperframes init my-video
cd my-video
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
npx hyperframes preview
npx hyperframes render
```
