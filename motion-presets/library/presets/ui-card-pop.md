# Preset: Social UI card pop

**id:** `ui-card-pop`

## When to use
Proof beats — profile card, DM thread, screenshot — without leaving the
talking-head world for long.

## Look
- Rounded rectangle card, drop shadow for depth.
- Scale pop onto frame (similar overshoot to kinetic hook).
- May sit over a slowly scaling still photo plate.

## Motion
- Card: 70% → 105% → 100%.
- Photo underlay (optional): slow push-in 100% → 110% over 2–3s.
- DM/screen-record variant: vertical scroll with motion blur.

## DaVinci Resolve Studio
1. Import PNG/JPEG UI (or recreate with Text+ + rounded rectangle Fusion).
2. Transform keyframes for pop; soft shadow via Fusion DropShadow or
   Resolve Shadow tool.
3. For scroll: animate Y position; add Vector Motion Blur in Fusion if needed.
4. Keep on screen 1.5–3s unless rapid montage.

## Seen in
- DcY72S4B1EG (IG profile card + DM scroll examples)
