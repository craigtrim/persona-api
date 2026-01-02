/**
 * ============================================================================
 * META ICONS - Collection Tab Selectors
 * ============================================================================
 * 
 * Five icons representing icon collections:
 * - ARCHETYPES_META: Generic personality archetypes (21 icons)
 * - GREEN_EMBER_META: Green Ember character collection (12 icons)
 * - GREEK_MYTHOLOGY_META: Greek Mythology characters (64 icons)
 * - NORSE_MYTHOLOGY_META: Norse Mythology characters (20 icons)
 * - ROMAN_MYTHOLOGY_META: Roman Mythology characters (47 icons)
 * 
 * Style: Matches main icon library (gradient + drop shadow, 100x100 viewBox)
 * ============================================================================
 */


// ============================================================================
// GENERIC ARCHETYPES - Meta Icon
// ============================================================================
// Represents the personality archetype system
// Visual: Multiple overlapping silhouettes suggesting variety of types
// ============================================================================

const ARCHETYPES_META_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="arch-meta-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a3a"/>
      <stop offset="100%" style="stop-color:#0a1018"/>
    </linearGradient>
    <linearGradient id="arch-meta-fig1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6a9aba"/>
      <stop offset="100%" style="stop-color:#3a6a8a"/>
    </linearGradient>
    <linearGradient id="arch-meta-fig2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9a8aba"/>
      <stop offset="100%" style="stop-color:#6a5a8a"/>
    </linearGradient>
    <linearGradient id="arch-meta-fig3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8abaa0"/>
      <stop offset="100%" style="stop-color:#5a8a70"/>
    </linearGradient>
    <filter id="arch-meta-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#arch-meta-bg)"/>
  
  <!-- Back figure (left) -->
  <g filter="url(#arch-meta-shadow)" opacity="0.6">
    <ellipse cx="28" cy="38" rx="10" ry="11" fill="url(#arch-meta-fig2)"/>
    <path d="M16 78 Q14 52 28 48 Q38 50 42 64 L38 78" fill="url(#arch-meta-fig2)"/>
  </g>
  
  <!-- Back figure (right) -->
  <g filter="url(#arch-meta-shadow)" opacity="0.6">
    <ellipse cx="72" cy="38" rx="10" ry="11" fill="url(#arch-meta-fig3)"/>
    <path d="M60 78 Q58 52 72 48 Q82 50 86 64 L82 78" fill="url(#arch-meta-fig3)"/>
  </g>
  
  <!-- Center figure (prominent) -->
  <g filter="url(#arch-meta-shadow)">
    <ellipse cx="50" cy="32" rx="12" ry="13" fill="url(#arch-meta-fig1)"/>
    <path d="M36 82 Q34 50 50 46 Q66 50 68 66 L64 82" fill="url(#arch-meta-fig1)"/>
  </g>
  
  <!-- Pentagon hint (OCEAN) at bottom -->
  <g opacity="0.4">
    <polygon points="50,68 42,74 44,82 56,82 58,74" fill="none" stroke="#6a8aaa" stroke-width="1.5"/>
  </g>
</svg>
`;


// ============================================================================
// GREEN EMBER - Meta Icon
// ============================================================================
// Represents the Green Ember character collection
// Visual: Glowing green ember with rabbit ear silhouette
// ============================================================================

const GREEN_EMBER_META_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ge-meta-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a1e"/>
      <stop offset="100%" style="stop-color:#0a1410"/>
    </linearGradient>
    <linearGradient id="ge-meta-ember" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" style="stop-color:#ccda7a"/>
      <stop offset="50%" style="stop-color:#8aba5a"/>
      <stop offset="100%" style="stop-color:#4a7a3a"/>
    </linearGradient>
    <linearGradient id="ge-meta-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8aaa8a"/>
      <stop offset="100%" style="stop-color:#4a6a4a"/>
    </linearGradient>
    <filter id="ge-meta-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="ge-meta-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="8" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#ge-meta-bg)"/>
  
  <!-- Ember glow -->
  <ellipse cx="50" cy="50" rx="24" ry="28" fill="#aaba6a" opacity="0.15" filter="url(#ge-meta-glow)"/>
  
  <!-- Green ember gem -->
  <g filter="url(#ge-meta-shadow)">
    <path d="M50 22 L66 42 L58 78 L42 78 L34 42 Z" fill="url(#ge-meta-ember)"/>
    <!-- Facet highlights -->
    <path d="M50 22 L50 50 L34 42 Z" fill="#daea9a" opacity="0.3"/>
    <path d="M50 50 L66 42 L58 78 Z" fill="#3a5a2a" opacity="0.3"/>
  </g>
  
  <!-- Rabbit ear silhouettes flanking the ember -->
  <g opacity="0.5">
    <!-- Left ear -->
    <ellipse cx="24" cy="40" rx="5" ry="16" fill="url(#ge-meta-fur)" transform="rotate(-15 24 40)"/>
    <!-- Right ear -->
    <ellipse cx="76" cy="40" rx="5" ry="16" fill="url(#ge-meta-fur)" transform="rotate(15 76 40)"/>
  </g>
  
  <!-- Inner ember gleam -->
  <ellipse cx="48" cy="40" rx="6" ry="10" fill="#eefa9a" opacity="0.4"/>
</svg>
`;


// ============================================================================
// NORSE MYTHOLOGY - Meta Icon
// ============================================================================
// Represents the Norse Mythology character collection (20 icons)
// Visual: Thor's hammer, Odin's ravens, rune hint
// ============================================================================

const NORSE_MYTHOLOGY_META_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="nm-meta-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a3a"/>
      <stop offset="100%" style="stop-color:#0a1018"/>
    </linearGradient>
    <linearGradient id="nm-meta-hammer" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9a9aa0"/>
      <stop offset="100%" style="stop-color:#5a5a60"/>
    </linearGradient>
    <linearGradient id="nm-meta-raven" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3a3a4a"/>
      <stop offset="100%" style="stop-color:#1a1a2a"/>
    </linearGradient>
    <filter id="nm-meta-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#nm-meta-bg)"/>
  
  <!-- Thor's hammer (Mjolnir) -->
  <g filter="url(#nm-meta-shadow)">
    <rect x="47" y="20" width="6" height="30" fill="#5a4a3a"/>
    <rect x="36" y="44" width="28" height="16" rx="2" fill="url(#nm-meta-hammer)"/>
    <rect x="40" y="48" width="20" height="8" fill="#7a7a80"/>
  </g>
  
  <!-- Odin's ravens silhouettes -->
  <g opacity="0.6">
    <ellipse cx="22" cy="32" rx="10" ry="8" fill="url(#nm-meta-raven)"/>
    <path d="M14 28 L8 24" stroke="url(#nm-meta-raven)" stroke-width="3" stroke-linecap="round"/>
    <ellipse cx="78" cy="32" rx="10" ry="8" fill="url(#nm-meta-raven)"/>
    <path d="M86 28 L92 24" stroke="url(#nm-meta-raven)" stroke-width="3" stroke-linecap="round"/>
  </g>
  
  <!-- Rune hint (Ansuz - Odin's rune) -->
  <g opacity="0.4">
    <path d="M50 68 L44 80 M50 68 L56 80 M46 74 L54 74" stroke="#6a8aaa" stroke-width="2" stroke-linecap="round"/>
  </g>
</svg>
`;


// ============================================================================
// ROMAN MYTHOLOGY - Meta Icon
// ============================================================================
// Represents the Roman Mythology character collection (47 icons)
// Visual: SPQR eagle, laurel wreath, Roman columns
// ============================================================================

const ROMAN_MYTHOLOGY_META_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rm-meta-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a1a3a"/>
      <stop offset="100%" style="stop-color:#0a0810"/>
    </linearGradient>
    <linearGradient id="rm-meta-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#daca6a"/>
      <stop offset="100%" style="stop-color:#9a7a3a"/>
    </linearGradient>
    <linearGradient id="rm-meta-marble" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c0c0c8"/>
      <stop offset="100%" style="stop-color:#808088"/>
    </linearGradient>
    <filter id="rm-meta-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#rm-meta-bg)"/>
  
  <!-- Roman columns (background) -->
  <g opacity="0.3">
    <rect x="14" y="58" width="6" height="32" fill="url(#rm-meta-marble)"/>
    <rect x="12" y="56" width="10" height="4" fill="url(#rm-meta-marble)"/>
    <rect x="80" y="58" width="6" height="32" fill="url(#rm-meta-marble)"/>
    <rect x="78" y="56" width="10" height="4" fill="url(#rm-meta-marble)"/>
  </g>
  
  <!-- Eagle (SPQR symbol) -->
  <g filter="url(#rm-meta-shadow)">
    <path d="M50 18 L44 28 L38 24 L42 34 L34 38 L44 40 L42 50 L50 44 L58 50 L56 40 L66 38 L58 34 L62 24 L56 28 Z" fill="url(#rm-meta-gold)"/>
    <circle cx="50" cy="30" r="4" fill="#2a1a1a"/>
  </g>
  
  <!-- Laurel wreath -->
  <g opacity="0.6">
    <path d="M26 62 Q32 58 38 62 Q32 66 26 62" fill="#7a9a5a"/>
    <path d="M30 68 Q36 64 42 68 Q36 72 30 68" fill="#6a8a4a"/>
    <path d="M62 62 Q68 58 74 62 Q68 66 62 62" fill="#7a9a5a"/>
    <path d="M58 68 Q64 64 70 68 Q64 72 58 68" fill="#6a8a4a"/>
  </g>
  
  <!-- SPQR text hint -->
  <text x="50" y="82" font-size="10" fill="url(#rm-meta-gold)" font-family="serif" text-anchor="middle" opacity="0.5">SPQR</text>
</svg>
`;


// ============================================================================
// GREEK MYTHOLOGY - Meta Icon
// ============================================================================
// Represents the Greek Mythology character collection (64 icons)
// Visual: Lightning bolt (Zeus), trident (Poseidon), Greek column hints
// ============================================================================

const GREEK_MYTHOLOGY_META_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="gm-meta-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a4a"/>
      <stop offset="100%" style="stop-color:#0a1220"/>
    </linearGradient>
    <linearGradient id="gm-meta-bolt" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#faea8a"/>
      <stop offset="100%" style="stop-color:#aa9a2a"/>
    </linearGradient>
    <linearGradient id="gm-meta-trident" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8acaca"/>
      <stop offset="100%" style="stop-color:#4a8a9a"/>
    </linearGradient>
    <filter id="gm-meta-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="gm-meta-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#gm-meta-bg)"/>
  
  <!-- Greek columns (background) -->
  <g opacity="0.3">
    <rect x="12" y="62" width="8" height="28" fill="#4a5a7a"/>
    <rect x="10" y="60" width="12" height="4" fill="#5a6a8a"/>
    <rect x="10" y="88" width="12" height="4" fill="#5a6a8a"/>
    <rect x="80" y="62" width="8" height="28" fill="#4a5a7a"/>
    <rect x="78" y="60" width="12" height="4" fill="#5a6a8a"/>
    <rect x="78" y="88" width="12" height="4" fill="#5a6a8a"/>
  </g>
  
  <!-- Lightning bolt (Zeus) -->
  <g filter="url(#gm-meta-glow)">
    <path d="M38 12 L32 32 L42 30 L26 52 L32 40 L22 42 L38 12" fill="url(#gm-meta-bolt)"/>
  </g>
  
  <!-- Trident (Poseidon) -->
  <g filter="url(#gm-meta-shadow)">
    <rect x="62" y="28" width="3" height="42" rx="1" fill="url(#gm-meta-trident)"/>
    <path d="M55 32 L64 22 L64 34 M64 22 L73 32" stroke="url(#gm-meta-trident)" stroke-width="2.5" fill="none" stroke-linecap="round"/>
    <path d="M64 22 L64 14" stroke="url(#gm-meta-trident)" stroke-width="2.5" stroke-linecap="round"/>
  </g>
  
  <!-- Helmet plume hint (Athena) -->
  <path d="M48 58 Q56 48 54 62 Q60 52 58 68" stroke="#c0a070" stroke-width="2" fill="none" opacity="0.5"/>
  
  <!-- Laurel wreath hint -->
  <g opacity="0.4">
    <path d="M30 72 Q36 68 42 72 Q36 76 30 72" fill="#8aba6a"/>
    <path d="M58 72 Q64 68 70 72 Q64 76 58 72" fill="#8aba6a"/>
  </g>
</svg>
`;


// ============================================================================
// EXPORT
// ============================================================================

const META_ICONS = {
  archetypes: ARCHETYPES_META_SVG,
  greenEmber: GREEN_EMBER_META_SVG,
  greekMythology: GREEK_MYTHOLOGY_META_SVG,
  norseMythology: NORSE_MYTHOLOGY_META_SVG,
  romanMythology: ROMAN_MYTHOLOGY_META_SVG
};

// For ES modules:
// export { META_ICONS, ARCHETYPES_META_SVG, GREEN_EMBER_META_SVG, GREEK_MYTHOLOGY_META_SVG, NORSE_MYTHOLOGY_META_SVG, ROMAN_MYTHOLOGY_META_SVG };
// export default META_ICONS;
