/**
 * ============================================================================
 * ARCHETYPE ICON LIBRARY - SVG Collection
 * ============================================================================
 * 
 * DESIGN SYSTEM OVERVIEW
 * ----------------------
 * Style: "Profile + Prop" with gradient fills and drop shadows
 * Base size: 100x100 viewBox (renders well at 64-100px, acceptable at 40px)
 * Format: Inline SVG, self-contained with embedded defs
 * 
 * VISUAL GRAMMAR
 * --------------
 * Each icon follows a consistent composition:
 *   - Circular background with diagonal gradient (dark)
 *   - Human figure in profile view, looking right
 *   - Archetype-specific prop/tool/context element
 *   - Drop shadow filter for depth
 * 
 * TRAIT ENCODING (subtle, not explicit)
 * -------------------------------------
 *   - Extraversion (E): Posture openness, gesture expansiveness
 *       Low E  = hunched, contained, inward-focused
 *       High E = upright, expansive, outward-reaching
 *   - Agreeableness (A): Color temperature
 *       Low A  = cool blues/teals (#4a7a9a range)
 *       High A = warmer tones (#7a9a8a, #9a8a7a range)
 *   - Conscientiousness (C): Line precision, element organization
 *   - Neuroticism (N): Implied through context/expression
 *   - Openness (O): Prop complexity, creative elements
 * 
 * ARCHETYPE TABLE REFERENCE
 * -------------------------
 * | #  | Archetype      | A | C | E | N | O |
 * |----|----------------|---|---|---|---|---|
 * | 1  | Architect      | L | H | L | L | H |
 * | 2  | Commander      | L | H | H | L | M |
 * | 3  | Mediator       | H | M | L | M | H |
 * | 4  | Performer      | M | L | H | M | H |
 * | 5  | Analyst        | M | H | L | L | L |
 * | 6  | Caregiver      | H | H | M | L | M |
 * | 7  | Adventurer     | L | L | H | L | H |
 * | 8  | Stoic          | M | H | L | L | L |
 * | 9  | Diplomat       | H | H | H | L | M |
 * | 10 | Rebel          | L | L | H | M | H |
 * | 11 | Scholar        | M | H | L | M | H |
 * | 12 | Healer         | H | M | L | H | H |
 * | 13 | Entrepreneur   | L | M | H | L | H |
 * | 14 | Sentinel       | H | H | L | M | L |
 * | 15 | Maverick       | L | L | M | L | H |
 * | 16 | Host           | H | M | H | L | M |
 * | 17 | Critic         | L | H | L | M | M |
 * | 18 | Dreamer        | M | L | L | M | H |
 * | 19 | Warrior        | L | H | H | L | L |
 * | 20 | Sage           | H | M | L | L | H |
 * | 21 | Cipher         | - | - | - | - | - |
 * 
 * USAGE
 * -----
 * Each SVG is self-contained. Copy the entire <svg>...</svg> block.
 * Adjust width/height attributes as needed (viewBox ensures scaling).
 * 
 * For inline HTML: paste directly
 * For React/JSX: convert attributes (stroke-width → strokeWidth, etc.)
 * For img src: save as .svg file or use data URI
 * 
 * ============================================================================
 */


// ============================================================================
// 1. THE ARCHITECT
// ============================================================================
// Traits: A:Low, C:High, E:Low, N:Low, O:High
// Visual: Hunched over blueprint, compass tool, cool tones
// Prop: Drafting compass drawing on blueprint
// ============================================================================

const ARCHITECT_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="architect-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e3a52"/>
      <stop offset="100%" style="stop-color:#0a141e"/>
    </linearGradient>
    <linearGradient id="architect-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7aaacc"/>
      <stop offset="100%" style="stop-color:#4a7a9a"/>
    </linearGradient>
    <linearGradient id="architect-paper" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a4a62"/>
      <stop offset="100%" style="stop-color:#1a3042"/>
    </linearGradient>
    <filter id="architect-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#architect-bg)"/>
  <!-- Blueprint -->
  <rect x="48" y="18" width="34" height="44" rx="3" fill="url(#architect-paper)" filter="url(#architect-shadow)"/>
  <path d="M54 26 H76 M54 34 H72 M54 42 H76 M54 50 H68" stroke="#4a7a9a" stroke-width="1.5" stroke-linecap="round"/>
  <rect x="54" y="54" width="14" height="4" rx="1" fill="#3a6a8a"/>
  <!-- Figure - hunched, focused (Low E) -->
  <g filter="url(#architect-shadow)">
    <ellipse cx="30" cy="36" rx="13" ry="14" fill="url(#architect-skin)"/>
    <ellipse cx="40" cy="36" rx="4" ry="5" fill="url(#architect-skin)"/>
    <path d="M14 82 Q10 52 30 48 Q44 50 48 68 L42 82" fill="url(#architect-skin)"/>
  </g>
  <!-- Arm with compass -->
  <path d="M42 62 Q50 54 54 50" stroke="url(#architect-skin)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="54" cy="50" r="3" fill="#5a9aba"/>
</svg>
`;


// ============================================================================
// 2. THE COMMANDER
// ============================================================================
// Traits: A:Low, C:High, E:High, N:Low, O:Medium
// Visual: Upright posture, pointing forward, directive gesture
// Prop: Pointing arm, command presence, strategic display
// ============================================================================

const COMMANDER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="commander-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a3a"/>
      <stop offset="100%" style="stop-color:#0a1218"/>
    </linearGradient>
    <linearGradient id="commander-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6a9aba"/>
      <stop offset="100%" style="stop-color:#3a6a8a"/>
    </linearGradient>
    <filter id="commander-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#commander-bg)"/>
  <!-- Strategic display/chart -->
  <rect x="52" y="20" width="30" height="24" rx="2" fill="#1a3040" filter="url(#commander-shadow)"/>
  <path d="M58 36 L64 30 L70 34 L76 26" stroke="#4a9aba" stroke-width="2" fill="none" stroke-linecap="round"/>
  <circle cx="76" cy="26" r="2" fill="#6abadc"/>
  <!-- Figure - upright, commanding (High E) -->
  <g filter="url(#commander-shadow)">
    <ellipse cx="28" cy="32" rx="12" ry="13" fill="url(#commander-skin)"/>
    <ellipse cx="37" cy="32" rx="3" ry="4" fill="url(#commander-skin)"/>
    <path d="M16 82 Q14 50 28 46 Q40 48 44 62 L40 82" fill="url(#commander-skin)"/>
  </g>
  <!-- Pointing arm - directive gesture -->
  <path d="M40 54 L58 42" stroke="url(#commander-skin)" stroke-width="6" stroke-linecap="round"/>
  <path d="M58 42 L66 38" stroke="#5a8aaa" stroke-width="3" stroke-linecap="round"/>
  <!-- Shoulder epaulette hint -->
  <rect x="36" y="48" width="8" height="3" rx="1" fill="#4a7a9a"/>
</svg>
`;


// ============================================================================
// 3. THE MEDIATOR
// ============================================================================
// Traits: A:High, C:Medium, E:Low, N:Medium, O:High
// Visual: Gentle posture, warm tones, peaceful symbols
// Prop: Olive branch or balance scales, soft gestures
// ============================================================================

const MEDIATOR_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="mediator-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3a3e"/>
      <stop offset="100%" style="stop-color:#0e1a1e"/>
    </linearGradient>
    <linearGradient id="mediator-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8ab4a4"/>
      <stop offset="100%" style="stop-color:#5a8a7a"/>
    </linearGradient>
    <filter id="mediator-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#mediator-bg)"/>
  <!-- Olive branch -->
  <g filter="url(#mediator-shadow)">
    <path d="M52 24 Q68 32 72 50 Q74 62 70 70" stroke="#3a6a5a" stroke-width="2" fill="none"/>
    <ellipse cx="58" cy="28" rx="4" ry="2" fill="#5a9a7a" transform="rotate(-20 58 28)"/>
    <ellipse cx="64" cy="34" rx="4" ry="2" fill="#5a9a7a" transform="rotate(-10 64 34)"/>
    <ellipse cx="68" cy="42" rx="4" ry="2" fill="#5a9a7a" transform="rotate(5 68 42)"/>
    <ellipse cx="70" cy="52" rx="4" ry="2" fill="#5a9a7a" transform="rotate(20 70 52)"/>
    <ellipse cx="70" cy="62" rx="4" ry="2" fill="#5a9a7a" transform="rotate(30 70 62)"/>
  </g>
  <!-- Figure - gentle, inward (Low E, High A = warm) -->
  <g filter="url(#mediator-shadow)">
    <ellipse cx="28" cy="36" rx="13" ry="14" fill="url(#mediator-skin)"/>
    <ellipse cx="38" cy="36" rx="4" ry="5" fill="url(#mediator-skin)"/>
    <path d="M14 82 Q10 52 28 48 Q42 50 46 66 L40 82" fill="url(#mediator-skin)"/>
  </g>
  <!-- Hands together - peaceful gesture -->
  <path d="M40 60 Q46 56 48 58" stroke="url(#mediator-skin)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="48" cy="58" r="3" fill="#6aaa9a"/>
</svg>
`;


// ============================================================================
// 4. THE PERFORMER
// ============================================================================
// Traits: A:Medium, C:Low, E:High, N:Medium, O:High
// Visual: Dynamic pose, spotlight, theatrical energy
// Prop: Stage spotlight, expressive gesture, microphone
// ============================================================================

const PERFORMER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="performer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2e2a3a"/>
      <stop offset="100%" style="stop-color:#12101a"/>
    </linearGradient>
    <linearGradient id="performer-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ba9acc"/>
      <stop offset="100%" style="stop-color:#8a6a9a"/>
    </linearGradient>
    <linearGradient id="performer-spotlight" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" style="stop-color:#ffeedd" stop-opacity="0.3"/>
      <stop offset="100%" style="stop-color:#ffeedd" stop-opacity="0"/>
    </linearGradient>
    <filter id="performer-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#performer-bg)"/>
  <!-- Spotlight cone -->
  <path d="M70 8 L50 50 L90 50 Z" fill="url(#performer-spotlight)"/>
  <!-- Stage floor line -->
  <path d="M10 78 H90" stroke="#3a3a4a" stroke-width="1"/>
  <!-- Figure - expansive, theatrical (High E) -->
  <g filter="url(#performer-shadow)">
    <ellipse cx="35" cy="32" rx="12" ry="13" fill="url(#performer-skin)"/>
    <ellipse cx="44" cy="32" rx="3" ry="4" fill="url(#performer-skin)"/>
    <path d="M22 76 Q18 48 35 44 Q48 46 52 60 L48 76" fill="url(#performer-skin)"/>
  </g>
  <!-- Raised arm - dramatic gesture -->
  <path d="M46 52 Q58 40 62 28" stroke="url(#performer-skin)" stroke-width="5" stroke-linecap="round"/>
  <!-- Microphone -->
  <ellipse cx="62" cy="24" rx="4" ry="6" fill="#4a4a5a"/>
  <rect x="60" y="28" width="4" height="8" fill="#3a3a4a"/>
</svg>
`;


// ============================================================================
// 5. THE ANALYST
// ============================================================================
// Traits: A:Medium, C:High, E:Low, N:Low, O:Low
// Visual: Focused, methodical, examining data
// Prop: Magnifying glass, data chart, precise elements
// ============================================================================

const ANALYST_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="analyst-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e2a32"/>
      <stop offset="100%" style="stop-color:#0a1014"/>
    </linearGradient>
    <linearGradient id="analyst-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7a9aaa"/>
      <stop offset="100%" style="stop-color:#4a6a7a"/>
    </linearGradient>
    <filter id="analyst-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#analyst-bg)"/>
  <!-- Data chart -->
  <rect x="50" y="22" width="32" height="40" rx="2" fill="#1a2830" filter="url(#analyst-shadow)"/>
  <rect x="56" y="48" width="5" height="10" fill="#3a7a8a"/>
  <rect x="64" y="42" width="5" height="16" fill="#4a8a9a"/>
  <rect x="72" y="36" width="5" height="22" fill="#5a9aaa"/>
  <path d="M54 32 H80" stroke="#2a4a5a" stroke-width="1"/>
  <!-- Figure - focused, contained (Low E, Low O) -->
  <g filter="url(#analyst-shadow)">
    <ellipse cx="26" cy="36" rx="12" ry="13" fill="url(#analyst-skin)"/>
    <ellipse cx="35" cy="36" rx="3" ry="4" fill="url(#analyst-skin)"/>
    <path d="M12 82 Q8 52 26 48 Q38 50 42 66 L38 82" fill="url(#analyst-skin)"/>
  </g>
  <!-- Arm holding magnifying glass -->
  <path d="M36 58 Q44 52 50 48" stroke="url(#analyst-skin)" stroke-width="5" stroke-linecap="round"/>
  <!-- Magnifying glass -->
  <circle cx="54" cy="44" r="8" fill="none" stroke="#6a9aaa" stroke-width="2"/>
  <path d="M60 50 L66 56" stroke="#6a9aaa" stroke-width="3" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 6. THE CAREGIVER
// ============================================================================
// Traits: A:High, C:High, E:Medium, N:Low, O:Medium
// Visual: Warm, supportive posture, nurturing gesture
// Prop: Heart symbol, open hands, protective stance
// ============================================================================

const CAREGIVER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="caregiver-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3632"/>
      <stop offset="100%" style="stop-color:#0e1614"/>
    </linearGradient>
    <linearGradient id="caregiver-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a4b89a"/>
      <stop offset="100%" style="stop-color:#6a8a62"/>
    </linearGradient>
    <filter id="caregiver-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#caregiver-bg)"/>
  <!-- Heart symbol -->
  <g filter="url(#caregiver-shadow)">
    <path d="M65 28 C58 18 48 24 55 38 C48 24 38 18 45 28 C52 38 55 48 55 48 C55 48 58 38 65 28" 
          fill="#c47a7a" transform="translate(8, 6) scale(0.8)"/>
  </g>
  <!-- Smaller protected figure hint -->
  <ellipse cx="68" cy="58" rx="8" ry="9" fill="#5a7a6a" opacity="0.7"/>
  <path d="M60 78 Q58 66 68 64 Q76 66 78 74" fill="#5a7a6a" opacity="0.7"/>
  <!-- Main figure - open, nurturing (High A) -->
  <g filter="url(#caregiver-shadow)">
    <ellipse cx="30" cy="34" rx="13" ry="14" fill="url(#caregiver-skin)"/>
    <ellipse cx="40" cy="34" rx="4" ry="5" fill="url(#caregiver-skin)"/>
    <path d="M16 82 Q12 50 30 46 Q44 48 48 64 L44 82" fill="url(#caregiver-skin)"/>
  </g>
  <!-- Arms - protective, welcoming -->
  <path d="M44 56 Q56 50 60 54" stroke="url(#caregiver-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 7. THE ADVENTURER
// ============================================================================
// Traits: A:Low, C:Low, E:High, N:Low, O:High
// Visual: Dynamic, forward-leaning, explorer energy
// Prop: Compass, map, horizon/mountain vista
// ============================================================================

const ADVENTURER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="adventurer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3a2e"/>
      <stop offset="100%" style="stop-color:#0e1610"/>
    </linearGradient>
    <linearGradient id="adventurer-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8aba9a"/>
      <stop offset="100%" style="stop-color:#4a8a6a"/>
    </linearGradient>
    <filter id="adventurer-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#adventurer-bg)"/>
  <!-- Mountain vista -->
  <path d="M50 70 L65 40 L80 55 L95 30" stroke="#3a5a4a" stroke-width="2" fill="none"/>
  <path d="M58 70 L72 48 L82 58" fill="#2a4a3a" opacity="0.5"/>
  <!-- Map -->
  <rect x="52" y="46" width="28" height="22" rx="2" fill="#d4c4a4" filter="url(#adventurer-shadow)" transform="rotate(-5 66 57)"/>
  <path d="M56 52 Q66 50 74 54 M56 60 Q68 56 76 62" stroke="#8a7a5a" stroke-width="1" fill="none"/>
  <circle cx="68" cy="56" r="2" fill="#c44a4a"/>
  <!-- Figure - forward-leaning, dynamic (High E, High O) -->
  <g filter="url(#adventurer-shadow)">
    <ellipse cx="28" cy="34" rx="12" ry="13" fill="url(#adventurer-skin)"/>
    <ellipse cx="37" cy="34" rx="3" ry="4" fill="url(#adventurer-skin)"/>
    <path d="M14 80 Q12 50 28 46 Q42 48 46 62 L42 80" fill="url(#adventurer-skin)"/>
  </g>
  <!-- Pointing at map -->
  <path d="M40 56 Q50 50 56 52" stroke="url(#adventurer-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 8. THE STOIC
// ============================================================================
// Traits: A:Medium, C:High, E:Low, N:Low, O:Low
// Visual: Calm, centered, minimal elements
// Prop: Pillar/column, meditative stillness
// Note: Same OCEAN profile as Analyst - differentiated by stoic philosophy theme
// ============================================================================

const STOIC_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="stoic-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#22282a"/>
      <stop offset="100%" style="stop-color:#0c1012"/>
    </linearGradient>
    <linearGradient id="stoic-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8a9a9a"/>
      <stop offset="100%" style="stop-color:#5a6a6a"/>
    </linearGradient>
    <linearGradient id="stoic-pillar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#4a5a5a"/>
      <stop offset="50%" style="stop-color:#6a7a7a"/>
      <stop offset="100%" style="stop-color:#4a5a5a"/>
    </linearGradient>
    <filter id="stoic-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#stoic-bg)"/>
  <!-- Classical pillar -->
  <g filter="url(#stoic-shadow)">
    <rect x="60" y="24" width="16" height="52" fill="url(#stoic-pillar)"/>
    <rect x="58" y="20" width="20" height="6" rx="1" fill="#5a6a6a"/>
    <rect x="58" y="74" width="20" height="6" rx="1" fill="#5a6a6a"/>
    <!-- Pillar fluting -->
    <path d="M64 26 V72 M68 26 V72 M72 26 V72" stroke="#3a4a4a" stroke-width="1"/>
  </g>
  <!-- Figure - still, centered (Low E, Low O) -->
  <g filter="url(#stoic-shadow)">
    <ellipse cx="30" cy="36" rx="12" ry="13" fill="url(#stoic-skin)"/>
    <ellipse cx="39" cy="36" rx="3" ry="4" fill="url(#stoic-skin)"/>
    <path d="M16 82 Q14 52 30 48 Q42 50 44 66 L40 82" fill="url(#stoic-skin)"/>
  </g>
  <!-- Hands at rest -->
  <path d="M38 62 Q42 60 44 62" stroke="url(#stoic-skin)" stroke-width="4" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 9. THE DIPLOMAT
// ============================================================================
// Traits: A:High, C:High, E:High, N:Low, O:Medium
// Visual: Poised, connecting gesture, bridge imagery
// Prop: Handshake, bridge symbol, dual connection
// ============================================================================

const DIPLOMAT_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="diplomat-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3238"/>
      <stop offset="100%" style="stop-color:#101418"/>
    </linearGradient>
    <linearGradient id="diplomat-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a0b4b8"/>
      <stop offset="100%" style="stop-color:#608088"/>
    </linearGradient>
    <filter id="diplomat-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#diplomat-bg)"/>
  <!-- Bridge symbol -->
  <path d="M48 60 Q60 45 72 60" stroke="#4a6a7a" stroke-width="3" fill="none" filter="url(#diplomat-shadow)"/>
  <path d="M50 60 V70 M60 52 V70 M70 60 V70" stroke="#4a6a7a" stroke-width="2"/>
  <!-- Second figure (smaller, being connected to) -->
  <g opacity="0.8">
    <ellipse cx="72" cy="34" rx="9" ry="10" fill="#6a8a8a"/>
    <path d="M64 70 Q62 52 72 50 Q80 52 82 62" fill="#6a8a8a"/>
  </g>
  <!-- Main figure - open, reaching (High E, High A) -->
  <g filter="url(#diplomat-shadow)">
    <ellipse cx="28" cy="32" rx="12" ry="13" fill="url(#diplomat-skin)"/>
    <ellipse cx="37" cy="32" rx="3" ry="4" fill="url(#diplomat-skin)"/>
    <path d="M14 78 Q12 48 28 44 Q40 46 44 60 L40 78" fill="url(#diplomat-skin)"/>
  </g>
  <!-- Reaching hand - connection gesture -->
  <path d="M40 52 Q52 46 60 48" stroke="url(#diplomat-skin)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="60" cy="48" r="3" fill="#8aaaaa"/>
</svg>
`;


// ============================================================================
// 10. THE REBEL
// ============================================================================
// Traits: A:Low, C:Low, E:High, N:Medium, O:High
// Visual: Defiant posture, breaking convention
// Prop: Raised fist, broken chain, disruption symbol
// ============================================================================

const REBEL_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rebel-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2e2228"/>
      <stop offset="100%" style="stop-color:#120e10"/>
    </linearGradient>
    <linearGradient id="rebel-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ba8a9a"/>
      <stop offset="100%" style="stop-color:#8a5a6a"/>
    </linearGradient>
    <filter id="rebel-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#rebel-bg)"/>
  <!-- Broken chain -->
  <g filter="url(#rebel-shadow)">
    <ellipse cx="58" cy="56" rx="5" ry="4" fill="none" stroke="#7a6a6a" stroke-width="2"/>
    <ellipse cx="68" cy="54" rx="5" ry="4" fill="none" stroke="#7a6a6a" stroke-width="2"/>
    <ellipse cx="78" cy="58" rx="5" ry="4" fill="none" stroke="#7a6a6a" stroke-width="2"/>
    <!-- Break point -->
    <path d="M72 50 L76 46" stroke="#aa7a7a" stroke-width="2"/>
    <path d="M74 56 L78 52" stroke="#aa7a7a" stroke-width="2"/>
  </g>
  <!-- Figure - defiant, upward energy (High E, Low A) -->
  <g filter="url(#rebel-shadow)">
    <ellipse cx="30" cy="34" rx="12" ry="13" fill="url(#rebel-skin)"/>
    <ellipse cx="39" cy="34" rx="3" ry="4" fill="url(#rebel-skin)"/>
    <path d="M16 80 Q14 50 30 46 Q44 48 48 62 L44 80" fill="url(#rebel-skin)"/>
  </g>
  <!-- Raised fist -->
  <path d="M42 52 Q50 40 52 28" stroke="url(#rebel-skin)" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="52" cy="24" rx="5" ry="6" fill="#9a6a7a"/>
</svg>
`;


// ============================================================================
// 11. THE SCHOLAR
// ============================================================================
// Traits: A:Medium, C:High, E:Low, N:Medium, O:High
// Visual: Absorbed in learning, surrounded by knowledge
// Prop: Open book, stack of books, reading posture
// ============================================================================

const SCHOLAR_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="scholar-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a2832"/>
      <stop offset="100%" style="stop-color:#0e0c12"/>
    </linearGradient>
    <linearGradient id="scholar-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9a9ab4"/>
      <stop offset="100%" style="stop-color:#6a6a84"/>
    </linearGradient>
    <filter id="scholar-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#scholar-bg)"/>
  <!-- Stack of books -->
  <g filter="url(#scholar-shadow)">
    <rect x="56" y="58" width="24" height="5" rx="1" fill="#6a5a4a"/>
    <rect x="54" y="52" width="26" height="5" rx="1" fill="#5a6a5a"/>
    <rect x="58" y="46" width="22" height="5" rx="1" fill="#5a5a6a"/>
  </g>
  <!-- Open book being read -->
  <g filter="url(#scholar-shadow)">
    <path d="M50 26 Q50 22 58 24 L74 28 Q78 30 78 34 L78 44 Q78 48 74 46 L58 42 Q50 40 50 36 Z" fill="#d4d0c4"/>
    <path d="M50 26 Q50 22 42 24 L34 26 Q30 28 32 34 L34 42 Q36 46 42 44 L50 40 Q50 36 50 36 Z" fill="#e4e0d4"/>
    <path d="M50 26 V40" stroke="#8a8678" stroke-width="1"/>
    <path d="M54 30 H70 M54 36 H68" stroke="#aaa898" stroke-width="1"/>
  </g>
  <!-- Figure - absorbed, studious (Low E, High O) -->
  <g filter="url(#scholar-shadow)">
    <ellipse cx="28" cy="38" rx="12" ry="13" fill="url(#scholar-skin)"/>
    <ellipse cx="37" cy="38" rx="3" ry="4" fill="url(#scholar-skin)"/>
    <path d="M14 82 Q12 54 28 50 Q40 52 44 66 L40 82" fill="url(#scholar-skin)"/>
  </g>
  <!-- Hands holding book -->
  <path d="M38 58 Q44 50 48 44" stroke="url(#scholar-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 12. THE HEALER
// ============================================================================
// Traits: A:High, C:Medium, E:Low, N:High, O:High
// Visual: Gentle, empathetic presence, healing symbols
// Prop: Herbs/plant, gentle hands, soft glow
// ============================================================================

const HEALER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="healer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#283032"/>
      <stop offset="100%" style="stop-color:#0c1214"/>
    </linearGradient>
    <linearGradient id="healer-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a8c4b8"/>
      <stop offset="100%" style="stop-color:#688878"/>
    </linearGradient>
    <filter id="healer-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="healer-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#healer-bg)"/>
  <!-- Healing herbs/plant -->
  <g filter="url(#healer-glow)">
    <path d="M62 68 Q64 50 68 40" stroke="#4a7a5a" stroke-width="2" fill="none"/>
    <ellipse cx="68" cy="36" rx="6" ry="4" fill="#6aaa7a" transform="rotate(-30 68 36)"/>
    <ellipse cx="72" cy="44" rx="5" ry="3" fill="#5a9a6a" transform="rotate(20 72 44)"/>
    <ellipse cx="64" cy="48" rx="5" ry="3" fill="#6aaa7a" transform="rotate(-20 64 48)"/>
    <!-- Small flower -->
    <circle cx="68" cy="32" r="3" fill="#c4a4b4"/>
  </g>
  <!-- Mortar bowl -->
  <ellipse cx="66" cy="70" rx="10" ry="5" fill="#5a5a5a" filter="url(#healer-shadow)"/>
  <path d="M56 68 Q56 62 66 62 Q76 62 76 68" fill="#4a4a4a"/>
  <!-- Figure - gentle, nurturing (High A, High N shows sensitivity) -->
  <g filter="url(#healer-shadow)">
    <ellipse cx="28" cy="36" rx="12" ry="13" fill="url(#healer-skin)"/>
    <ellipse cx="37" cy="36" rx="3" ry="4" fill="url(#healer-skin)"/>
    <path d="M14 82 Q12 52 28 48 Q40 50 44 66 L40 82" fill="url(#healer-skin)"/>
  </g>
  <!-- Hands working with herbs -->
  <path d="M40 58 Q50 54 56 58" stroke="url(#healer-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 13. THE ENTREPRENEUR
// ============================================================================
// Traits: A:Low, C:Medium, E:High, N:Low, O:High
// Visual: Forward momentum, opportunity-seeking
// Prop: Lightbulb (ideas), rocket, growth chart
// ============================================================================

const ENTREPRENEUR_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="entrepreneur-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a2e3a"/>
      <stop offset="100%" style="stop-color:#0e1016"/>
    </linearGradient>
    <linearGradient id="entrepreneur-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8ab4c4"/>
      <stop offset="100%" style="stop-color:#4a7a8a"/>
    </linearGradient>
    <linearGradient id="entrepreneur-bulb" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" style="stop-color:#ffeedd"/>
      <stop offset="100%" style="stop-color:#ddaa44"/>
    </linearGradient>
    <filter id="entrepreneur-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="entrepreneur-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#entrepreneur-bg)"/>
  <!-- Lightbulb - idea -->
  <g filter="url(#entrepreneur-glow)">
    <path d="M66 20 Q56 20 56 32 Q56 40 62 44 L62 50 L70 50 L70 44 Q76 40 76 32 Q76 20 66 20" fill="url(#entrepreneur-bulb)"/>
    <rect x="62" y="50" width="8" height="4" fill="#888"/>
    <path d="M60 32 Q66 28 72 32" stroke="#fff" stroke-width="1.5" fill="none" opacity="0.6"/>
  </g>
  <!-- Growth arrow -->
  <path d="M52 70 L60 58 L68 64 L78 48" stroke="#4a9a7a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <path d="M74 48 L78 48 L78 52" stroke="#4a9a7a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- Figure - dynamic, forward-leaning (High E, High O) -->
  <g filter="url(#entrepreneur-shadow)">
    <ellipse cx="28" cy="34" rx="12" ry="13" fill="url(#entrepreneur-skin)"/>
    <ellipse cx="37" cy="34" rx="3" ry="4" fill="url(#entrepreneur-skin)"/>
    <path d="M14 80 Q12 50 28 46 Q42 48 46 62 L42 80" fill="url(#entrepreneur-skin)"/>
  </g>
  <!-- Reaching toward idea -->
  <path d="M40 52 Q50 44 56 40" stroke="url(#entrepreneur-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 14. THE SENTINEL
// ============================================================================
// Traits: A:High, C:High, E:Low, N:Medium, O:Low
// Visual: Watchful, protective stance, vigilant
// Prop: Shield, watchtower, guarding posture
// ============================================================================

const SENTINEL_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sentinel-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#282e2a"/>
      <stop offset="100%" style="stop-color:#0c100e"/>
    </linearGradient>
    <linearGradient id="sentinel-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#94a898"/>
      <stop offset="100%" style="stop-color:#5a6a5e"/>
    </linearGradient>
    <linearGradient id="sentinel-shield" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6a7a6a"/>
      <stop offset="50%" style="stop-color:#8a9a8a"/>
      <stop offset="100%" style="stop-color:#5a6a5a"/>
    </linearGradient>
    <filter id="sentinel-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#sentinel-bg)"/>
  <!-- Shield -->
  <g filter="url(#sentinel-shadow)">
    <path d="M56 28 L56 56 Q56 68 68 72 Q80 68 80 56 L80 28 Q68 32 56 28" fill="url(#sentinel-shield)"/>
    <path d="M68 36 L68 60" stroke="#4a5a4a" stroke-width="2"/>
    <path d="M60 44 L76 44" stroke="#4a5a4a" stroke-width="2"/>
  </g>
  <!-- Figure - upright, vigilant (High C, Low E = reserved but alert) -->
  <g filter="url(#sentinel-shadow)">
    <ellipse cx="28" cy="34" rx="12" ry="13" fill="url(#sentinel-skin)"/>
    <ellipse cx="37" cy="34" rx="3" ry="4" fill="url(#sentinel-skin)"/>
    <path d="M14 82 Q12 50 28 46 Q40 48 44 64 L40 82" fill="url(#sentinel-skin)"/>
  </g>
  <!-- Arm holding shield -->
  <path d="M40 54 Q48 48 54 46" stroke="url(#sentinel-skin)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 15. THE MAVERICK
// ============================================================================
// Traits: A:Low, C:Low, E:Medium, N:Low, O:High
// Visual: Independent, unconventional, unique path
// Prop: Diverging path, star, solo journey
// ============================================================================

const MAVERICK_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="maverick-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a283a"/>
      <stop offset="100%" style="stop-color:#0e0c16"/>
    </linearGradient>
    <linearGradient id="maverick-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a49ac4"/>
      <stop offset="100%" style="stop-color:#6a6094"/>
    </linearGradient>
    <filter id="maverick-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#maverick-bg)"/>
  <!-- Diverging paths -->
  <g opacity="0.6">
    <path d="M50 80 Q50 65 60 55 Q70 45 80 45" stroke="#4a4a6a" stroke-width="2" fill="none"/>
    <path d="M50 80 Q50 65 55 58 Q60 50 60 40" stroke="#4a4a6a" stroke-width="2" fill="none" stroke-dasharray="4,2"/>
    <path d="M50 80 Q50 70 45 65 Q35 55 30 55" stroke="#4a4a6a" stroke-width="2" fill="none" stroke-dasharray="2,2"/>
  </g>
  <!-- Star - guiding light -->
  <g filter="url(#maverick-shadow)">
    <path d="M72 22 L74 28 L80 28 L75 32 L77 38 L72 34 L67 38 L69 32 L64 28 L70 28 Z" fill="#c4aa64"/>
  </g>
  <!-- Figure - independent stance (Medium E, High O) -->
  <g filter="url(#maverick-shadow)">
    <ellipse cx="30" cy="36" rx="12" ry="13" fill="url(#maverick-skin)"/>
    <ellipse cx="39" cy="36" rx="3" ry="4" fill="url(#maverick-skin)"/>
    <path d="M16 82 Q14 52 30 48 Q42 50 46 66 L42 82" fill="url(#maverick-skin)"/>
  </g>
  <!-- Looking up at star -->
  <path d="M40 56 Q48 48 52 42" stroke="url(#maverick-skin)" stroke-width="4" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 16. THE HOST
// ============================================================================
// Traits: A:High, C:Medium, E:High, N:Low, O:Medium
// Visual: Welcoming, gathering others, warm presence
// Prop: Open door, gathering table, welcoming gesture
// ============================================================================

const HOST_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="host-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#32302a"/>
      <stop offset="100%" style="stop-color:#14120e"/>
    </linearGradient>
    <linearGradient id="host-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c4b4a4"/>
      <stop offset="100%" style="stop-color:#8a7a6a"/>
    </linearGradient>
    <filter id="host-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#host-bg)"/>
  <!-- Table/gathering surface -->
  <ellipse cx="66" cy="68" rx="18" ry="6" fill="#5a4a3a" filter="url(#host-shadow)"/>
  <!-- Small gathered figures (simplified) -->
  <g opacity="0.7">
    <ellipse cx="58" cy="54" rx="6" ry="7" fill="#7a6a5a"/>
    <ellipse cx="74" cy="54" rx="6" ry="7" fill="#6a7a6a"/>
    <ellipse cx="66" cy="48" rx="6" ry="7" fill="#7a7a6a"/>
  </g>
  <!-- Warm light glow -->
  <ellipse cx="66" cy="58" rx="12" ry="8" fill="#ffeedd" opacity="0.15"/>
  <!-- Main figure - welcoming, open (High E, High A) -->
  <g filter="url(#host-shadow)">
    <ellipse cx="26" cy="34" rx="12" ry="13" fill="url(#host-skin)"/>
    <ellipse cx="35" cy="34" rx="3" ry="4" fill="url(#host-skin)"/>
    <path d="M12 80 Q10 50 26 46 Q40 48 44 62 L40 80" fill="url(#host-skin)"/>
  </g>
  <!-- Both arms open - welcoming gesture -->
  <path d="M40 54 Q52 48 58 52" stroke="url(#host-skin)" stroke-width="5" stroke-linecap="round"/>
  <path d="M20 56 Q14 52 10 56" stroke="url(#host-skin)" stroke-width="4" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 17. THE CRITIC
// ============================================================================
// Traits: A:Low, C:High, E:Low, N:Medium, O:Medium
// Visual: Scrutinizing, evaluating, precise assessment
// Prop: Red pen, checklist, evaluative gaze
// ============================================================================

const CRITIC_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="critic-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a2630"/>
      <stop offset="100%" style="stop-color:#0e0c12"/>
    </linearGradient>
    <linearGradient id="critic-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9a9aaa"/>
      <stop offset="100%" style="stop-color:#5a5a6a"/>
    </linearGradient>
    <filter id="critic-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#critic-bg)"/>
  <!-- Document/checklist -->
  <rect x="50" y="22" width="30" height="40" rx="2" fill="#e8e4dc" filter="url(#critic-shadow)"/>
  <path d="M56 32 H74 M56 40 H74 M56 48 H74 M56 56 H70" stroke="#c4c0b8" stroke-width="1.5"/>
  <!-- Check marks and X -->
  <path d="M54 32 L56 34 L60 30" stroke="#4a8a4a" stroke-width="1.5" fill="none"/>
  <path d="M54 40 L56 42 L60 38" stroke="#4a8a4a" stroke-width="1.5" fill="none"/>
  <path d="M54 48 L58 52 M58 48 L54 52" stroke="#aa4a4a" stroke-width="1.5"/>
  <!-- Red pen marks -->
  <path d="M64 44 Q68 42 72 46" stroke="#cc4444" stroke-width="1.5" fill="none"/>
  <!-- Figure - scrutinizing posture (Low E, Low A) -->
  <g filter="url(#critic-shadow)">
    <ellipse cx="28" cy="36" rx="12" ry="13" fill="url(#critic-skin)"/>
    <ellipse cx="37" cy="36" rx="3" ry="4" fill="url(#critic-skin)"/>
    <path d="M14 82 Q12 52 28 48 Q40 50 44 66 L40 82" fill="url(#critic-skin)"/>
  </g>
  <!-- Arm with red pen -->
  <path d="M40 58 Q48 50 52 48" stroke="url(#critic-skin)" stroke-width="5" stroke-linecap="round"/>
  <!-- Red pen -->
  <path d="M52 48 L62 42" stroke="#cc4444" stroke-width="3" stroke-linecap="round"/>
  <path d="M62 42 L64 40" stroke="#aa3333" stroke-width="2" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// 18. THE DREAMER
// ============================================================================
// Traits: A:Medium, C:Low, E:Low, N:Medium, O:High
// Visual: Contemplative, gazing upward, imaginative
// Prop: Clouds, stars, thought bubbles
// ============================================================================

const DREAMER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="dreamer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e2840"/>
      <stop offset="100%" style="stop-color:#0a1018"/>
    </linearGradient>
    <linearGradient id="dreamer-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a4a4c8"/>
      <stop offset="100%" style="stop-color:#6a6a94"/>
    </linearGradient>
    <filter id="dreamer-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="dreamer-blur" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#dreamer-bg)"/>
  <!-- Stars -->
  <circle cx="60" cy="20" r="2" fill="#ffffcc"/>
  <circle cx="75" cy="28" r="1.5" fill="#ffffcc"/>
  <circle cx="82" cy="18" r="1" fill="#ffffcc"/>
  <circle cx="70" cy="38" r="1" fill="#ffffcc"/>
  <!-- Dreamy clouds -->
  <g filter="url(#dreamer-blur)" opacity="0.4">
    <ellipse cx="68" cy="50" rx="12" ry="6" fill="#6a6a94"/>
    <ellipse cx="78" cy="48" rx="8" ry="5" fill="#6a6a94"/>
    <ellipse cx="58" cy="52" rx="8" ry="4" fill="#6a6a94"/>
  </g>
  <!-- Thought bubbles trail -->
  <circle cx="46" cy="44" r="3" fill="#5a5a7a" opacity="0.5"/>
  <circle cx="52" cy="36" r="4" fill="#5a5a7a" opacity="0.4"/>
  <circle cx="60" cy="30" r="5" fill="#5a5a7a" opacity="0.3"/>
  <!-- Figure - contemplative, upward gaze (Low E, High O) -->
  <g filter="url(#dreamer-shadow)">
    <ellipse cx="30" cy="40" rx="12" ry="13" fill="url(#dreamer-skin)"/>
    <ellipse cx="38" cy="38" rx="3" ry="4" fill="url(#dreamer-skin)"/>
    <path d="M16 84 Q14 54 30 50 Q42 52 46 68 L42 84" fill="url(#dreamer-skin)"/>
  </g>
  <!-- Chin resting on hand - contemplative pose -->
  <path d="M38 52 Q40 48 42 46" stroke="url(#dreamer-skin)" stroke-width="4" stroke-linecap="round"/>
  <circle cx="42" cy="46" r="3" fill="#8a8ab4"/>
</svg>
`;


// ============================================================================
// 19. THE WARRIOR
// ============================================================================
// Traits: A:Low, C:High, E:High, N:Low, O:Low
// Visual: Aggressive, competitive, directed energy
// Prop: Sword, target, battle-ready stance
// ============================================================================

const WARRIOR_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="warrior-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a2228"/>
      <stop offset="100%" style="stop-color:#100c0e"/>
    </linearGradient>
    <linearGradient id="warrior-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#aa8a8a"/>
      <stop offset="100%" style="stop-color:#6a4a4a"/>
    </linearGradient>
    <linearGradient id="warrior-blade" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c4c4cc"/>
      <stop offset="50%" style="stop-color:#9a9aa4"/>
      <stop offset="100%" style="stop-color:#c4c4cc"/>
    </linearGradient>
    <filter id="warrior-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#warrior-bg)"/>
  <!-- Target -->
  <g filter="url(#warrior-shadow)">
    <circle cx="72" cy="50" r="14" fill="none" stroke="#6a4a4a" stroke-width="2"/>
    <circle cx="72" cy="50" r="9" fill="none" stroke="#8a5a5a" stroke-width="2"/>
    <circle cx="72" cy="50" r="4" fill="#aa6a6a"/>
  </g>
  <!-- Figure - aggressive, forward (High E, Low A) -->
  <g filter="url(#warrior-shadow)">
    <ellipse cx="28" cy="34" rx="12" ry="13" fill="url(#warrior-skin)"/>
    <ellipse cx="37" cy="34" rx="3" ry="4" fill="url(#warrior-skin)"/>
    <path d="M14 80 Q12 50 28 46 Q42 48 48 62 L44 80" fill="url(#warrior-skin)"/>
  </g>
  <!-- Arm thrusting sword -->
  <path d="M42 52 L56 46" stroke="url(#warrior-skin)" stroke-width="6" stroke-linecap="round"/>
  <!-- Sword -->
  <path d="M54 48 L68 42" stroke="url(#warrior-blade)" stroke-width="3" stroke-linecap="round"/>
  <path d="M68 42 L72 50" stroke="url(#warrior-blade)" stroke-width="2" stroke-linecap="round"/>
  <!-- Hilt -->
  <rect x="52" y="46" width="6" height="2" rx="1" fill="#5a4a3a" transform="rotate(-15 55 47)"/>
</svg>
`;


// ============================================================================
// 20. THE SAGE
// ============================================================================
// Traits: A:High, C:Medium, E:Low, N:Low, O:High
// Visual: Wise, calm, illuminating presence
// Prop: Lantern, scroll, contemplative posture
// ============================================================================

const SAGE_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="sage-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3230"/>
      <stop offset="100%" style="stop-color:#0e1412"/>
    </linearGradient>
    <linearGradient id="sage-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a4b8a8"/>
      <stop offset="100%" style="stop-color:#647868"/>
    </linearGradient>
    <linearGradient id="sage-lantern" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" style="stop-color:#ffeedd"/>
      <stop offset="100%" style="stop-color:#cc9944"/>
    </linearGradient>
    <filter id="sage-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="sage-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#sage-bg)"/>
  <!-- Lantern glow -->
  <circle cx="68" cy="42" r="16" fill="#ffeedd" opacity="0.15" filter="url(#sage-glow)"/>
  <!-- Lantern -->
  <g filter="url(#sage-shadow)">
    <rect x="62" y="32" width="12" height="18" rx="2" fill="url(#sage-lantern)"/>
    <rect x="60" y="30" width="16" height="4" rx="1" fill="#6a5a4a"/>
    <rect x="60" y="48" width="16" height="3" rx="1" fill="#6a5a4a"/>
    <path d="M68 28 L68 24" stroke="#5a4a3a" stroke-width="2"/>
    <ellipse cx="68" cy="23" rx="4" ry="2" fill="#5a4a3a"/>
    <!-- Flame -->
    <path d="M68 38 Q66 42 68 46 Q70 42 68 38" fill="#ffeecc"/>
  </g>
  <!-- Scroll -->
  <g filter="url(#sage-shadow)">
    <rect x="54" y="60" width="26" height="14" rx="2" fill="#d4c8b4"/>
    <circle cx="54" cy="67" r="3" fill="#c4b8a4"/>
    <circle cx="80" cy="67" r="3" fill="#c4b8a4"/>
    <path d="M58 64 H76 M58 70 H72" stroke="#a49878" stroke-width="1"/>
  </g>
  <!-- Figure - wise, calm (High A, High O, Low E) -->
  <g filter="url(#sage-shadow)">
    <ellipse cx="28" cy="38" rx="12" ry="13" fill="url(#sage-skin)"/>
    <ellipse cx="37" cy="38" rx="3" ry="4" fill="url(#sage-skin)"/>
    <path d="M14 84 Q12 54 28 50 Q40 52 44 68 L40 84" fill="url(#sage-skin)"/>
  </g>
  <!-- Hand raised toward lantern - illumination gesture -->
  <path d="M40 58 Q50 50 58 46" stroke="url(#sage-skin)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="58" cy="46" r="3" fill="#8aa888"/>
</svg>
`;


// ============================================================================
// 21. THE CIPHER
// ============================================================================
// Traits: Undefined / Uncategorized
// Visual: Overlapping geometric shapes suggesting multiple possibilities
// Prop: Circle, square, triangle - the basic forms, unresolved
// Purpose: Represents profiles that don't map to a defined archetype
// ============================================================================

const CIPHER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cipher-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#252532"/>
      <stop offset="100%" style="stop-color:#0c0c14"/>
    </linearGradient>
    <linearGradient id="cipher-skin" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9a9aaa"/>
      <stop offset="100%" style="stop-color:#6a6a7a"/>
    </linearGradient>
    <filter id="cipher-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#cipher-bg)"/>
  
  <!-- Overlapping geometric shapes - first layer (faint) -->
  <g opacity="0.25">
    <circle cx="62" cy="32" r="12" fill="none" stroke="#7a8aaa" stroke-width="1.5"/>
    <rect x="54" y="44" width="20" height="20" rx="2" fill="none" stroke="#8a7aaa" stroke-width="1.5" transform="rotate(15 64 54)"/>
    <polygon points="70,62 82,78 58,78" fill="none" stroke="#aa7a8a" stroke-width="1.5"/>
  </g>
  
  <!-- Overlapping geometric shapes - second layer (more visible) -->
  <g opacity="0.4">
    <circle cx="66" cy="36" r="10" fill="none" stroke="#7a9aaa" stroke-width="1.5"/>
    <rect x="58" y="48" width="16" height="16" rx="2" fill="none" stroke="#9a7aaa" stroke-width="1.5" transform="rotate(-10 66 56)"/>
    <polygon points="68,58 78,72 58,72" fill="none" stroke="#aa8a9a" stroke-width="1.5"/>
  </g>
  
  <!-- Connecting path suggesting flux/possibility -->
  <path d="M56 34 Q64 40 60 50 Q56 60 64 68" stroke="#6a6a8a" stroke-width="1" fill="none" opacity="0.5" stroke-dasharray="2,2"/>
  
  <!-- Figure - neutral posture, contemplating the shapes -->
  <g filter="url(#cipher-shadow)">
    <ellipse cx="28" cy="36" rx="12" ry="13" fill="url(#cipher-skin)"/>
    <ellipse cx="37" cy="36" rx="3" ry="4" fill="url(#cipher-skin)"/>
    <path d="M14 82 Q12 52 28 48 Q40 50 44 66 L40 82" fill="url(#cipher-skin)"/>
  </g>
  
  <!-- Arm gesture - open, contemplating -->
  <path d="M40 58 Q48 52 54 52" stroke="url(#cipher-skin)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="54" cy="52" r="3" fill="#8a8a9a"/>
</svg>
`;


// ============================================================================
// EXPORT / INDEX
// ============================================================================

const ARCHETYPE_ICONS = {
  architect: ARCHITECT_SVG,
  commander: COMMANDER_SVG,
  mediator: MEDIATOR_SVG,
  performer: PERFORMER_SVG,
  analyst: ANALYST_SVG,
  caregiver: CAREGIVER_SVG,
  adventurer: ADVENTURER_SVG,
  stoic: STOIC_SVG,
  diplomat: DIPLOMAT_SVG,
  rebel: REBEL_SVG,
  scholar: SCHOLAR_SVG,
  healer: HEALER_SVG,
  entrepreneur: ENTREPRENEUR_SVG,
  sentinel: SENTINEL_SVG,
  maverick: MAVERICK_SVG,
  host: HOST_SVG,
  critic: CRITIC_SVG,
  dreamer: DREAMER_SVG,
  warrior: WARRIOR_SVG,
  sage: SAGE_SVG,
  cipher: CIPHER_SVG
};

// For ES modules:
// export { ARCHETYPE_ICONS };
// export default ARCHETYPE_ICONS;

// For CommonJS:
// module.exports = { ARCHETYPE_ICONS };
