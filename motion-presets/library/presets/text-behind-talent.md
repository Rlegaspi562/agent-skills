# Preset: Text behind talent

**id:** `text-behind-talent`

## When to use
When large kinetic text should feel "in the world" — behind legs, laptop,
chair arm — instead of a flat sticker on top.

## Look
Same type styles as hook/body; composite order is the trick, not a new font.

## Technique
1. Duplicate the talent plate (or use Magic Mask / Polygon + tracking).
2. Draw / generate a matte for the **foreground** (legs, laptop, hands).
3. Stack: V1 full plate → V2 kinetic text → V3 foreground matte of talent
   (or Fusion: Text → Merge behind masked FG).
4. Track the matte if the talent moves.

Difficulty: **medium–hard**. Prefer Magic Mask (Resolve 18.5+) on clean
contrast; fall back to polygon tracker.

## DaVinci Resolve Studio
1. Color or Edit: **Magic Mask** on subject limbs/laptop; track forward/back.
2. In Fusion (or using matte clip on higher track): Merge text **under** the
   masked foreground.
3. Feather matte 1–3 px to avoid cutout fringing.
4. Save as Fusion macro `Rumil/Text Behind Talent`.

## Seen in
- DcY72S4B1EG (text behind legs + laptop)
- DcgcNgDh-dX (same family of depth composite on hook beats)
