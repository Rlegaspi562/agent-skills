# Watch notes — DfcNqN9TPp8

Full visual pass (2026-09-20): frames + video review. Audio SFX inferred from timing (not waveform-verified).

## Global layout
- **Split-screen:** top ~50% cream/off-white board (`#F5F5F0`); bottom ~50% talking head.
- Sharp horizontal hard-matte (no subject rotoscope).
- Hard cuts between full-frame talking-head and split stages.

## Caption system (`black-box-captions`)
- White bold sans on tight black rect (light corner radius).
- Phrase chunks (1–4 words), hard pop / cut — not word-by-word bounce.
- Lower-center / on the split line.

## Diagram motion (`tech-diagram-panel`)
Typical kit: pop scale 0→110→100; trim-path line draws; progress bars fill; hard cuts / short slides between states.

### Timestamped beats (approx)
| Time | Graphic |
|---|---|
| 0:00–0:05 | GitHub blog-style charts + header (“August 17 outage…”) |
| 0:07–0:09 | Requests/s line draws L→R; red PEAK callout |
| 0:09–0:13 | Chart slides; CENTRAL US DATA CENTER icon; POD / Istio sidecar + APP CONTAINER; concurrency bar → red at 100% |
| 0:13–0:16 | HPA; replica boxes duplicate; sidecar load drops |
| 0:16–0:20 | HPA WATCH → APP (40% OK) vs Istio sidecar (100% NOT WATCHED) |
| 0:20–0:28 | Client→service 503; retry arrows multiply |
| 0:28–0:32 | HAProxy nodes 1–4; FLOW LIMIT bars → EXHAUSTED |
| 0:32–0:39 | Architecture tree; GATEWAY AUTH expands to 8 services; red locks; 0/8→8/8 FAILING |
| 0:46–0:52 | CENTRAL US vs N. VIRGINIA paths; RTT bar fills |
| 0:52–1:02 | VS Code + TOKEN SERVICE; request dots escalate |
| 1:02–1:08 | Branching request tree; RPS counter → ~31,397 |
| 1:14–1:17 | Uptime/latency graph dip; return to fuller talking head |

## Inferred SFX (unverified)
UI pops on element appear; light whooshes on line draws; tick for counters; soft error buzz on 503 / exhausted / red locks.
