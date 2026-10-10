// motion.js: one tokens file, imported everywhere, no inline numbers
export const EASE = {
  enter: 'cubic-bezier(0.16, 1, 0.3, 1)',    // ease-out-expo
  move:  'cubic-bezier(0.76, 0, 0.24, 1)',   // ease-in-out-quart
  exit:  'cubic-bezier(0.7, 0, 0.84, 0)',    // ease-in-expo
  pop:   'cubic-bezier(0.34, 1.56, 0.64, 1)' // ease-out-back
};
export const MS = { feedback: 150, move: 400, hero: 750, exit: 240 };
export const STAGGER = { letter: 30, word: 90, item: 60 };

// Damping ratio from any library's numbers: 1 = no bounce
export const dampingRatio = (k, d, m = 1) => d / (2 * Math.sqrt(k * m));

// A spring as a pure function of time, from 0 to 1.
// zeta: damping ratio (1 no bounce, 0.7 premium, 0.5 playful). f: speed in Hz.
export function spring(t, zeta = 0.7, f = 2) {
  if (t <= 0) return 0;
  const w = 2 * Math.PI * f;
  if (zeta >= 1) return 1 - Math.exp(-w * t) * (1 + w * t);   // no bounce
  const wd = w * Math.sqrt(1 - zeta * zeta);
  return 1 - Math.exp(-zeta * w * t) *
    (Math.cos(wd * t) + (zeta * w / wd) * Math.sin(wd * t));
}
