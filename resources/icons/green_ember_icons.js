/**
 * ============================================================================
 * GREEN EMBER CHARACTER ICONS - SVG Collection
 * ============================================================================
 * 
 * DESIGN SYSTEM OVERVIEW
 * ----------------------
 * Based on: Archetype Icon Library style
 * Adaptation: Rabbit silhouettes, green-cast palette for Green Ember theme
 * Base size: 100x100 viewBox
 * Personality: Big Five domains (1-5 scale) - see https://botprofile.work/
 * 
 * CHARACTER BIG FIVE PROFILES
 * ---------------------------
 * | Character           | A | C | E | N | O | Key Traits                          |
 * |---------------------|---|---|---|---|---|-------------------------------------|
 * | Heather Longtreader | 4 | 4 | 3 | 3 | 4 | Compassionate healer, curious       |
 * | Picket Longtreader  | 2 | 4 | 2 | 5 | 3 | Fierce, struggles with anger        |
 * | Smalls              | 5 | 4 | 3 | 2 | 4 | Humble servant-leader, wise         |
 * | Helmer              | 2 | 5 | 2 | 2 | 2 | Disciplined, reserved mentor        |
 * | Lord Rake           | 3 | 5 | 4 | 2 | 3 | Strategic, charismatic leader       |
 * | Emma                | 5 | 4 | 3 | 2 | 3 | Nurturing, steady presence          |
 * | Kyle                | 4 | 2 | 4 | 3 | 4 | Eager, impulsive, adventurous       |
 * | Jo Shanks           | 3 | 3 | 2 | 2 | 4 | Independent, unconventional         |
 * | Captain Frye        | 4 | 5 | 3 | 2 | 2 | Dutiful, reliable, traditional      |
 * | Wilfred Longtreader | 4 | 5 | 2 | 3 | 4 | Methodical planner, visionary       |
 * | Morbin Blackhawk    | 1 | 4 | 4 | 2 | 3 | Dominating, cruel raptor lord       |
 * | Redeye Garlackson   | 1 | 3 | 3 | 4 | 2 | Treacherous, paranoid, self-serving |
 * 
 * NOTATION: A=Agreeableness, C=Conscientiousness, E=Extraversion, N=Neuroticism, O=Openness
 * SCALE: 1=Very Low, 2=Low, 3=Medium, 4=High, 5=Very High
 * 
 * COLOR PALETTE
 * -------------
 * Primary greens: #1e3a2e, #2a4a3a, #3a5a4a, #4a7a5a, #5a9a6a, #7aba8a
 * Accent ember:   #8a7a4a, #aa9a5a, #ccba6a (for the "ember" glow)
 * Antagonist:     #3a2a2e, #4a3a3e, #6a4a4e (dark reds/maroons)
 * 
 * RABBIT SILHOUETTE
 * -----------------
 * All characters use rabbit profile with distinctive long ears.
 * Morbin Blackhawk uses raptor/bird silhouette.
 * 
 * ============================================================================
 */


// ============================================================================
// HEATHER LONGTREADER
// ============================================================================
// Big Five: A4 C4 E3 N3 O4
// Compassionate healer-in-training, dedicated, curious, worries but copes
// Prop: Healing herbs/satchel
// ============================================================================

const HEATHER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="heather-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e3a2e"/>
      <stop offset="100%" style="stop-color:#0c1a14"/>
    </linearGradient>
    <linearGradient id="heather-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a8c4a8"/>
      <stop offset="100%" style="stop-color:#687a68"/>
    </linearGradient>
    <filter id="heather-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="heather-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#heather-bg)"/>
  
  <!-- Healing herbs with soft glow -->
  <g filter="url(#heather-glow)">
    <path d="M62 68 Q64 50 68 40" stroke="#3a6a4a" stroke-width="2" fill="none"/>
    <ellipse cx="68" cy="36" rx="6" ry="4" fill="#5a9a6a" transform="rotate(-30 68 36)"/>
    <ellipse cx="72" cy="44" rx="5" ry="3" fill="#4a8a5a" transform="rotate(20 72 44)"/>
    <ellipse cx="64" cy="48" rx="5" ry="3" fill="#5a9a6a" transform="rotate(-20 64 48)"/>
    <!-- Small flower - ember colored -->
    <circle cx="68" cy="32" r="3" fill="#ccba6a"/>
  </g>
  
  <!-- Mortar/healing bowl -->
  <ellipse cx="66" cy="70" rx="10" ry="5" fill="#4a5a4a" filter="url(#heather-shadow)"/>
  <path d="M56 68 Q56 62 66 62 Q76 62 76 68" fill="#3a4a3a"/>
  
  <!-- Rabbit figure -->
  <g filter="url(#heather-shadow)">
    <!-- Ears -->
    <ellipse cx="22" cy="16" rx="4" ry="12" fill="url(#heather-fur)" transform="rotate(-15 22 16)"/>
    <ellipse cx="34" cy="14" rx="4" ry="11" fill="url(#heather-fur)" transform="rotate(10 34 14)"/>
    <!-- Head -->
    <ellipse cx="28" cy="36" rx="12" ry="11" fill="url(#heather-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="38" rx="4" ry="3" fill="url(#heather-fur)"/>
    <!-- Body -->
    <path d="M14 82 Q12 52 28 48 Q40 50 44 66 L40 82" fill="url(#heather-fur)"/>
  </g>
  
  <!-- Arm working with herbs -->
  <path d="M40 58 Q50 54 56 58" stroke="url(#heather-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// PICKET LONGTREADER
// ============================================================================
// Big Five: A2 C4 E2 N5 O3
// Disciplined fighter, struggles with anger/resentment, inward-focused
// Prop: Sword, target/combat stance
// ============================================================================

const PICKET_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="picket-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3a2e"/>
      <stop offset="100%" style="stop-color:#0e1610"/>
    </linearGradient>
    <linearGradient id="picket-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9aba9a"/>
      <stop offset="100%" style="stop-color:#5a7a5a"/>
    </linearGradient>
    <linearGradient id="picket-blade" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#c4c4cc"/>
      <stop offset="50%" style="stop-color:#9a9aa4"/>
      <stop offset="100%" style="stop-color:#c4c4cc"/>
    </linearGradient>
    <filter id="picket-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#picket-bg)"/>
  
  <!-- Target -->
  <g filter="url(#picket-shadow)">
    <circle cx="72" cy="50" r="14" fill="none" stroke="#4a5a4a" stroke-width="2"/>
    <circle cx="72" cy="50" r="9" fill="none" stroke="#5a6a5a" stroke-width="2"/>
    <circle cx="72" cy="50" r="4" fill="#7a8a6a"/>
  </g>
  
  <!-- Rabbit figure - aggressive stance -->
  <g filter="url(#picket-shadow)">
    <!-- Ears - more alert/back -->
    <ellipse cx="20" cy="14" rx="4" ry="12" fill="url(#picket-fur)" transform="rotate(-25 20 14)"/>
    <ellipse cx="32" cy="12" rx="4" ry="11" fill="url(#picket-fur)" transform="rotate(-5 32 12)"/>
    <!-- Head -->
    <ellipse cx="28" cy="34" rx="12" ry="11" fill="url(#picket-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="36" rx="4" ry="3" fill="url(#picket-fur)"/>
    <!-- Body -->
    <path d="M14 80 Q12 50 28 46 Q42 48 48 62 L44 80" fill="url(#picket-fur)"/>
  </g>
  
  <!-- Arm thrusting sword -->
  <path d="M42 52 L56 46" stroke="url(#picket-fur)" stroke-width="6" stroke-linecap="round"/>
  
  <!-- Sword -->
  <path d="M54 48 L68 42" stroke="url(#picket-blade)" stroke-width="3" stroke-linecap="round"/>
  <path d="M68 42 L72 50" stroke="url(#picket-blade)" stroke-width="2" stroke-linecap="round"/>
  <!-- Hilt -->
  <rect x="52" y="46" width="6" height="2" rx="1" fill="#4a5a3a" transform="rotate(-15 55 47)"/>
</svg>
`;


// ============================================================================
// SMALLS (Prince Jupiter)
// ============================================================================
// Big Five: A5 C4 E3 N2 O4
// Servant-hearted, humble, kind, duty-bound, wise big-picture thinker
// Prop: Crown (modest), green ember glow
// ============================================================================

const SMALLS_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="smalls-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3a30"/>
      <stop offset="100%" style="stop-color:#0e1612"/>
    </linearGradient>
    <linearGradient id="smalls-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#a4b8a4"/>
      <stop offset="100%" style="stop-color:#647864"/>
    </linearGradient>
    <linearGradient id="smalls-ember" x1="50%" y1="0%" x2="50%" y2="100%">
      <stop offset="0%" style="stop-color:#aaba6a"/>
      <stop offset="100%" style="stop-color:#6a7a3a"/>
    </linearGradient>
    <filter id="smalls-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
    <filter id="smalls-glow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#smalls-bg)"/>
  
  <!-- Green ember glow -->
  <circle cx="68" cy="45" r="16" fill="#aaba6a" opacity="0.15" filter="url(#smalls-glow)"/>
  
  <!-- Green ember jewel/stone -->
  <g filter="url(#smalls-shadow)">
    <ellipse cx="68" cy="45" rx="10" ry="12" fill="url(#smalls-ember)"/>
    <ellipse cx="66" cy="42" rx="4" ry="5" fill="#ccda8a" opacity="0.5"/>
  </g>
  
  <!-- Simple crown/circlet nearby -->
  <g filter="url(#smalls-shadow)">
    <path d="M56 62 Q60 58 64 62 Q68 58 72 62 Q76 58 80 62" stroke="#aa9a5a" stroke-width="2" fill="none"/>
    <ellipse cx="68" cy="64" rx="12" ry="3" fill="none" stroke="#aa9a5a" stroke-width="2"/>
  </g>
  
  <!-- Rabbit figure - humble posture -->
  <g filter="url(#smalls-shadow)">
    <!-- Ears -->
    <ellipse cx="22" cy="18" rx="4" ry="12" fill="url(#smalls-fur)" transform="rotate(-10 22 18)"/>
    <ellipse cx="34" cy="16" rx="4" ry="11" fill="url(#smalls-fur)" transform="rotate(15 34 16)"/>
    <!-- Head -->
    <ellipse cx="28" cy="38" rx="12" ry="11" fill="url(#smalls-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="40" rx="4" ry="3" fill="url(#smalls-fur)"/>
    <!-- Body -->
    <path d="M14 84 Q12 54 28 50 Q40 52 44 68 L40 84" fill="url(#smalls-fur)"/>
  </g>
  
  <!-- Hand reaching toward ember - contemplative -->
  <path d="M40 60 Q50 52 58 48" stroke="url(#smalls-fur)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="58" cy="48" r="3" fill="#8aa878"/>
</svg>
`;


// ============================================================================
// HELMER
// ============================================================================
// Big Five: A2 C5 E2 N2 O2
// Gruff mentor, extremely disciplined, emotionally reserved, traditional
// Prop: Training sword, pillar/discipline
// ============================================================================

const HELMER_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="helmer-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#22302a"/>
      <stop offset="100%" style="stop-color:#0c1410"/>
    </linearGradient>
    <linearGradient id="helmer-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7a8a7a"/>
      <stop offset="100%" style="stop-color:#4a5a4a"/>
    </linearGradient>
    <linearGradient id="helmer-pillar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#3a4a3a"/>
      <stop offset="50%" style="stop-color:#5a6a5a"/>
      <stop offset="100%" style="stop-color:#3a4a3a"/>
    </linearGradient>
    <filter id="helmer-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#helmer-bg)"/>
  
  <!-- Training post/pillar -->
  <g filter="url(#helmer-shadow)">
    <rect x="62" y="24" width="14" height="52" fill="url(#helmer-pillar)"/>
    <rect x="60" y="20" width="18" height="6" rx="1" fill="#4a5a4a"/>
    <rect x="60" y="74" width="18" height="5" rx="1" fill="#4a5a4a"/>
    <!-- Strike marks -->
    <path d="M64 35 L74 38 M64 48 L74 45 M64 58 L74 62" stroke="#2a3a2a" stroke-width="2"/>
  </g>
  
  <!-- Rabbit figure - stoic stance -->
  <g filter="url(#helmer-shadow)">
    <!-- Ears - alert, upright -->
    <ellipse cx="20" cy="14" rx="4" ry="13" fill="url(#helmer-fur)" transform="rotate(-8 20 14)"/>
    <ellipse cx="32" cy="13" rx="4" ry="12" fill="url(#helmer-fur)" transform="rotate(8 32 13)"/>
    <!-- Scarred/weathered head -->
    <ellipse cx="28" cy="36" rx="12" ry="11" fill="url(#helmer-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="38" rx="4" ry="3" fill="url(#helmer-fur)"/>
    <!-- Eye patch hint -->
    <path d="M32 34 L36 32" stroke="#2a3a2a" stroke-width="2"/>
    <!-- Body -->
    <path d="M14 82 Q12 52 28 48 Q42 50 44 66 L40 82" fill="url(#helmer-fur)"/>
  </g>
  
  <!-- Arms crossed/at rest - controlled -->
  <path d="M38 62 Q42 58 44 60" stroke="url(#helmer-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// LORD RAKE
// ============================================================================
// Big Five: A3 C5 E4 N2 O3
// Tough but fair, strategic organizer, charismatic leader, steady under fire
// Prop: Battle standard, strategic map
// ============================================================================

const RAKE_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="rake-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a22"/>
      <stop offset="100%" style="stop-color:#0a1410"/>
    </linearGradient>
    <linearGradient id="rake-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8aaa8a"/>
      <stop offset="100%" style="stop-color:#4a6a4a"/>
    </linearGradient>
    <filter id="rake-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#rake-bg)"/>
  
  <!-- Strategic display/map -->
  <rect x="52" y="22" width="28" height="22" rx="2" fill="#1a2a20" filter="url(#rake-shadow)"/>
  <path d="M58 36 L64 30 L70 34 L76 28" stroke="#5a9a6a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <circle cx="76" cy="28" r="2" fill="#7aba7a"/>
  
  <!-- Battle standard -->
  <g filter="url(#rake-shadow)">
    <rect x="72" y="46" width="3" height="32" fill="#5a4a3a"/>
    <path d="M75 46 L88 52 L75 58 Z" fill="#4a7a4a"/>
    <!-- Ember symbol on flag -->
    <circle cx="81" cy="52" r="2" fill="#aaba6a"/>
  </g>
  
  <!-- Rabbit figure - commanding posture -->
  <g filter="url(#rake-shadow)">
    <!-- Ears - proud, upright -->
    <ellipse cx="20" cy="12" rx="4" ry="13" fill="url(#rake-fur)" transform="rotate(-5 20 12)"/>
    <ellipse cx="32" cy="11" rx="4" ry="12" fill="url(#rake-fur)" transform="rotate(5 32 11)"/>
    <!-- Head -->
    <ellipse cx="28" cy="32" rx="12" ry="11" fill="url(#rake-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="34" rx="4" ry="3" fill="url(#rake-fur)"/>
    <!-- Body - upright -->
    <path d="M14 80 Q12 48 28 44 Q42 46 46 62 L42 80" fill="url(#rake-fur)"/>
  </g>
  
  <!-- Pointing arm - directive -->
  <path d="M42 54 L58 44" stroke="url(#rake-fur)" stroke-width="6" stroke-linecap="round"/>
  <path d="M58 44 L66 40" stroke="#6a8a6a" stroke-width="3" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// EMMA
// ============================================================================
// Big Five: A5 C4 E3 N2 O3
// Nurturing, warm, reliable, emotionally stable, calming presence
// Prop: Comforting gesture, heart/home symbol
// ============================================================================

const EMMA_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="emma-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3632"/>
      <stop offset="100%" style="stop-color:#0e1614"/>
    </linearGradient>
    <linearGradient id="emma-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#b4c8a4"/>
      <stop offset="100%" style="stop-color:#7a9a6a"/>
    </linearGradient>
    <filter id="emma-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#emma-bg)"/>
  
  <!-- Heart symbol -->
  <g filter="url(#emma-shadow)">
    <path d="M65 30 C58 20 48 26 55 40 C48 26 38 20 45 30 C52 40 55 50 55 50 C55 50 58 40 65 30" 
          fill="#8aaa7a" transform="translate(6, 4) scale(0.75)"/>
  </g>
  
  <!-- Small protected figure hint -->
  <ellipse cx="68" cy="58" rx="7" ry="8" fill="#5a7a5a" opacity="0.7"/>
  <ellipse cx="66" cy="50" rx="3" ry="6" fill="#5a7a5a" opacity="0.7" transform="rotate(-10 66 50)"/>
  <path d="M61 76 Q59 66 68 64 Q75 66 77 72" fill="#5a7a5a" opacity="0.7"/>
  
  <!-- Rabbit figure - open, nurturing -->
  <g filter="url(#emma-shadow)">
    <!-- Ears - gentle angle -->
    <ellipse cx="22" cy="16" rx="4" ry="12" fill="url(#emma-fur)" transform="rotate(-12 22 16)"/>
    <ellipse cx="34" cy="15" rx="4" ry="11" fill="url(#emma-fur)" transform="rotate(12 34 15)"/>
    <!-- Head -->
    <ellipse cx="28" cy="36" rx="12" ry="11" fill="url(#emma-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="38" rx="4" ry="3" fill="url(#emma-fur)"/>
    <!-- Body -->
    <path d="M14 82 Q12 52 28 48 Q42 50 46 66 L42 82" fill="url(#emma-fur)"/>
  </g>
  
  <!-- Arms - protective, welcoming -->
  <path d="M44 58 Q56 52 60 56" stroke="url(#emma-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// KYLE
// ============================================================================
// Big Five: A4 C2 E4 N3 O4
// Friendly, eager, impulsive/reckless, energetic, curious adventurer
// Prop: Map, distant horizon
// ============================================================================

const KYLE_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="kyle-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3a2e"/>
      <stop offset="100%" style="stop-color:#0e1810"/>
    </linearGradient>
    <linearGradient id="kyle-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#9ac49a"/>
      <stop offset="100%" style="stop-color:#5a8a5a"/>
    </linearGradient>
    <filter id="kyle-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#kyle-bg)"/>
  
  <!-- Distant hills/horizon -->
  <path d="M50 70 L65 42 L80 56 L95 32" stroke="#3a5a4a" stroke-width="2" fill="none"/>
  <path d="M58 70 L72 50 L82 60" fill="#2a4a3a" opacity="0.5"/>
  
  <!-- Map -->
  <rect x="52" y="48" width="26" height="20" rx="2" fill="#c4b494" filter="url(#kyle-shadow)" transform="rotate(-5 65 58)"/>
  <path d="M56 54 Q66 52 72 56 M56 62 Q68 58 74 64" stroke="#8a7a5a" stroke-width="1" fill="none"/>
  <circle cx="68" cy="58" r="2" fill="#aa5a4a"/>
  
  <!-- Rabbit figure - eager, forward-leaning -->
  <g filter="url(#kyle-shadow)">
    <!-- Ears - perked forward -->
    <ellipse cx="22" cy="14" rx="4" ry="12" fill="url(#kyle-fur)" transform="rotate(-20 22 14)"/>
    <ellipse cx="33" cy="12" rx="4" ry="11" fill="url(#kyle-fur)" transform="rotate(-5 33 12)"/>
    <!-- Head -->
    <ellipse cx="28" cy="34" rx="11" ry="10" fill="url(#kyle-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="37" cy="36" rx="4" ry="3" fill="url(#kyle-fur)"/>
    <!-- Body - leaning forward -->
    <path d="M14 80 Q12 50 28 46 Q42 48 46 62 L42 80" fill="url(#kyle-fur)"/>
  </g>
  
  <!-- Pointing at map excitedly -->
  <path d="M40 56 Q50 50 56 54" stroke="url(#kyle-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// JO SHANKS
// ============================================================================
// Big Five: A3 C3 E2 N2 O4
// Independent, lone operator, cool under pressure, creative/unorthodox
// Prop: Bow, diverging path/star
// ============================================================================

const JO_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="jo-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a3030"/>
      <stop offset="100%" style="stop-color:#0e1414"/>
    </linearGradient>
    <linearGradient id="jo-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#8aaa8a"/>
      <stop offset="100%" style="stop-color:#4a6a4a"/>
    </linearGradient>
    <filter id="jo-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#jo-bg)"/>
  
  <!-- Diverging paths -->
  <g opacity="0.5">
    <path d="M50 78 Q50 65 60 55 Q70 48 80 48" stroke="#4a5a4a" stroke-width="2" fill="none"/>
    <path d="M50 78 Q50 68 45 62 Q38 54 32 54" stroke="#4a5a4a" stroke-width="2" fill="none" stroke-dasharray="3,2"/>
  </g>
  
  <!-- Star -->
  <g filter="url(#jo-shadow)">
    <path d="M72 24 L74 30 L80 30 L75 34 L77 40 L72 36 L67 40 L69 34 L64 30 L70 30 Z" fill="#aaba6a"/>
  </g>
  
  <!-- Bow -->
  <g filter="url(#jo-shadow)">
    <path d="M58 28 Q68 42 58 58" stroke="#6a5a4a" stroke-width="3" fill="none"/>
    <path d="M58 28 L58 58" stroke="#8a8a6a" stroke-width="1"/>
  </g>
  
  <!-- Rabbit figure - independent stance -->
  <g filter="url(#jo-shadow)">
    <!-- Ears - casual angle -->
    <ellipse cx="22" cy="18" rx="4" ry="12" fill="url(#jo-fur)" transform="rotate(-15 22 18)"/>
    <ellipse cx="33" cy="17" rx="4" ry="11" fill="url(#jo-fur)" transform="rotate(5 33 17)"/>
    <!-- Head -->
    <ellipse cx="28" cy="38" rx="12" ry="11" fill="url(#jo-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="40" rx="4" ry="3" fill="url(#jo-fur)"/>
    <!-- Body -->
    <path d="M14 82 Q12 54 28 50 Q42 52 46 68 L42 82" fill="url(#jo-fur)"/>
  </g>
  
  <!-- Arm gesturing toward own path -->
  <path d="M40 60 Q48 54 54 50" stroke="url(#jo-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// CAPTAIN FRYE
// ============================================================================
// Big Five: A4 C5 E3 N2 O2
// Loyal, dutiful, follows protocol, steady, traditional/by-the-book
// Prop: Ship wheel, shield
// ============================================================================

const FRYE_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="frye-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#283230"/>
      <stop offset="100%" style="stop-color:#0c1412"/>
    </linearGradient>
    <linearGradient id="frye-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#94a894"/>
      <stop offset="100%" style="stop-color:#5a6a5a"/>
    </linearGradient>
    <linearGradient id="frye-wheel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6a5a4a"/>
      <stop offset="100%" style="stop-color:#4a3a2a"/>
    </linearGradient>
    <filter id="frye-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#frye-bg)"/>
  
  <!-- Ship's wheel -->
  <g filter="url(#frye-shadow)">
    <circle cx="68" cy="45" r="16" fill="none" stroke="url(#frye-wheel)" stroke-width="4"/>
    <circle cx="68" cy="45" r="6" fill="url(#frye-wheel)"/>
    <!-- Spokes -->
    <path d="M68 29 L68 37 M68 53 L68 61 M52 45 L60 45 M76 45 L84 45" stroke="url(#frye-wheel)" stroke-width="3"/>
    <path d="M56 33 L62 39 M74 51 L80 57 M56 57 L62 51 M74 39 L80 33" stroke="url(#frye-wheel)" stroke-width="3"/>
    <!-- Handles -->
    <circle cx="68" cy="28" r="3" fill="#5a4a3a"/>
    <circle cx="68" cy="62" r="3" fill="#5a4a3a"/>
    <circle cx="52" cy="45" r="3" fill="#5a4a3a"/>
    <circle cx="84" cy="45" r="3" fill="#5a4a3a"/>
  </g>
  
  <!-- Rabbit figure - steady, vigilant -->
  <g filter="url(#frye-shadow)">
    <!-- Ears - alert -->
    <ellipse cx="20" cy="14" rx="4" ry="13" fill="url(#frye-fur)" transform="rotate(-8 20 14)"/>
    <ellipse cx="32" cy="13" rx="4" ry="12" fill="url(#frye-fur)" transform="rotate(8 32 13)"/>
    <!-- Head -->
    <ellipse cx="28" cy="34" rx="12" ry="11" fill="url(#frye-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="36" rx="4" ry="3" fill="url(#frye-fur)"/>
    <!-- Captain's hat hint -->
    <path d="M18 24 Q28 20 38 24" stroke="#3a4a3a" stroke-width="3" fill="none"/>
    <!-- Body - steady -->
    <path d="M14 82 Q12 52 28 48 Q42 50 44 66 L40 82" fill="url(#frye-fur)"/>
  </g>
  
  <!-- Hands on wheel -->
  <path d="M40 56 Q50 48 54 46" stroke="url(#frye-fur)" stroke-width="5" stroke-linecap="round"/>
</svg>
`;


// ============================================================================
// WILFRED LONGTREADER
// ============================================================================
// Big Five: A4 C5 E2 N3 O4
// Loving father, meticulous planner, works in shadows, long-term visionary
// Prop: Blueprint/plans, compass
// ============================================================================

const WILFRED_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="wilfred-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e3a32"/>
      <stop offset="100%" style="stop-color:#0a1a14"/>
    </linearGradient>
    <linearGradient id="wilfred-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7aba9a"/>
      <stop offset="100%" style="stop-color:#4a7a6a"/>
    </linearGradient>
    <linearGradient id="wilfred-paper" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a4a42"/>
      <stop offset="100%" style="stop-color:#1a3a32"/>
    </linearGradient>
    <filter id="wilfred-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#wilfred-bg)"/>
  
  <!-- Blueprint/plans -->
  <rect x="48" y="20" width="32" height="40" rx="3" fill="url(#wilfred-paper)" filter="url(#wilfred-shadow)"/>
  <path d="M54 28 H74 M54 36 H70 M54 44 H74 M54 52 H66" stroke="#4a7a6a" stroke-width="1.5" stroke-linecap="round"/>
  <rect x="54" y="54" width="12" height="3" rx="1" fill="#3a6a5a"/>
  
  <!-- Compass tool -->
  <g filter="url(#wilfred-shadow)">
    <circle cx="72" cy="68" r="8" fill="none" stroke="#6aba8a" stroke-width="2"/>
    <path d="M72 58 L70 70 L72 66 L74 70 Z" fill="#6aba8a"/>
    <circle cx="72" cy="68" r="2" fill="#6aba8a"/>
  </g>
  
  <!-- Rabbit figure - thoughtful, planning -->
  <g filter="url(#wilfred-shadow)">
    <!-- Ears - mature, slightly back -->
    <ellipse cx="22" cy="18" rx="4" ry="12" fill="url(#wilfred-fur)" transform="rotate(-10 22 18)"/>
    <ellipse cx="34" cy="17" rx="4" ry="11" fill="url(#wilfred-fur)" transform="rotate(8 34 17)"/>
    <!-- Head -->
    <ellipse cx="28" cy="38" rx="12" ry="11" fill="url(#wilfred-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="40" rx="4" ry="3" fill="url(#wilfred-fur)"/>
    <!-- Body -->
    <path d="M14 84 Q12 54 28 50 Q42 52 46 68 L40 84" fill="url(#wilfred-fur)"/>
  </g>
  
  <!-- Arm pointing at plans -->
  <path d="M42 62 Q50 54 54 52" stroke="url(#wilfred-fur)" stroke-width="5" stroke-linecap="round"/>
  <circle cx="54" cy="52" r="3" fill="#5a9a7a"/>
</svg>
`;


// ============================================================================
// MORBIN BLACKHAWK
// ============================================================================
// Big Five: A1 C4 E4 N2 O3
// Cruel, dominating, organized tyranny, commands presence, coldly controlled
// Prop: Crown of thorns, dark wings
// NOTE: Bird silhouette, not rabbit
// ============================================================================

const MORBIN_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="morbin-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a1a1e"/>
      <stop offset="100%" style="stop-color:#100808"/>
    </linearGradient>
    <linearGradient id="morbin-body" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#3a2a2e"/>
      <stop offset="100%" style="stop-color:#1a1214"/>
    </linearGradient>
    <filter id="morbin-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.5"/>
    </filter>
    <filter id="morbin-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#morbin-bg)"/>
  
  <!-- Dark crown -->
  <g filter="url(#morbin-glow)">
    <path d="M54 18 L58 28 L62 16 L66 26 L70 14 L74 26 L78 20" 
          stroke="#4a2a2a" stroke-width="2" fill="none"/>
    <path d="M52 28 L80 28" stroke="#3a2a2a" stroke-width="3"/>
  </g>
  
  <!-- Chains/oppression symbol -->
  <g opacity="0.4">
    <ellipse cx="62" cy="62" rx="5" ry="4" fill="none" stroke="#4a3a3a" stroke-width="2"/>
    <ellipse cx="72" cy="60" rx="5" ry="4" fill="none" stroke="#4a3a3a" stroke-width="2"/>
    <ellipse cx="82" cy="64" rx="5" ry="4" fill="none" stroke="#4a3a3a" stroke-width="2"/>
  </g>
  
  <!-- Raptor figure -->
  <g filter="url(#morbin-shadow)">
    <!-- Wing silhouette behind -->
    <path d="M10 30 Q5 50 15 70 Q20 60 25 65 Q22 50 25 35 Q20 40 10 30" fill="#2a1a1e" opacity="0.8"/>
    
    <!-- Body -->
    <path d="M20 80 Q18 55 30 50 Q42 52 46 68 L42 80" fill="url(#morbin-body)"/>
    
    <!-- Raptor head - hooked beak -->
    <ellipse cx="32" cy="38" rx="10" ry="10" fill="url(#morbin-body)"/>
    <!-- Hooked beak -->
    <path d="M40 36 Q48 38 46 44 Q44 42 40 42 Z" fill="#2a2020"/>
    
    <!-- Fierce eye -->
    <circle cx="34" cy="36" r="3" fill="#6a2a2a"/>
    <circle cx="35" cy="35" r="1" fill="#aa4a4a"/>
    
    <!-- Feather crest -->
    <path d="M24 30 Q22 22 28 26 Q26 20 32 24 Q32 18 38 24" fill="url(#morbin-body)"/>
  </g>
  
  <!-- Talon/claw reaching -->
  <path d="M44 62 L54 56 L58 58 L56 54 L60 52" stroke="#3a2a2a" stroke-width="3" stroke-linecap="round" fill="none"/>
</svg>
`;


// ============================================================================
// REDEYE GARLACKSON
// ============================================================================
// Big Five: A1 C3 E3 N4 O2
// Treacherous, self-serving, charming when needed, paranoid, narrow focus
// Prop: Broken emblem, shadow/mask
// ============================================================================

const REDEYE_SVG = `
<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="redeye-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2a2228"/>
      <stop offset="100%" style="stop-color:#100c10"/>
    </linearGradient>
    <linearGradient id="redeye-fur" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7a6a6a"/>
      <stop offset="100%" style="stop-color:#4a3a3a"/>
    </linearGradient>
    <filter id="redeye-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <circle cx="50" cy="50" r="48" fill="url(#redeye-bg)"/>
  
  <!-- Broken ember emblem -->
  <g filter="url(#redeye-shadow)">
    <ellipse cx="68" cy="40" rx="12" ry="14" fill="#3a4a3a" opacity="0.6"/>
    <!-- Crack through it -->
    <path d="M62 28 L66 38 L60 42 L68 52 L64 48 L70 54" stroke="#1a1a1a" stroke-width="2" fill="none"/>
  </g>
  
  <!-- Shadow/second face hint -->
  <g opacity="0.3">
    <ellipse cx="72" cy="62" rx="10" ry="9" fill="#2a1a1a"/>
    <ellipse cx="74" cy="68" rx="6" ry="4" fill="#2a1a1a"/>
  </g>
  
  <!-- Rabbit figure - shifty posture -->
  <g filter="url(#redeye-shadow)">
    <!-- Ears - one damaged/torn -->
    <ellipse cx="22" cy="18" rx="4" ry="12" fill="url(#redeye-fur)" transform="rotate(-12 22 18)"/>
    <path d="M30 6 Q34 12 33 20 Q36 14 34 8 L30 6" fill="url(#redeye-fur)"/>
    <!-- Head -->
    <ellipse cx="28" cy="38" rx="12" ry="11" fill="url(#redeye-fur)"/>
    <!-- Muzzle -->
    <ellipse cx="38" cy="40" rx="4" ry="3" fill="url(#redeye-fur)"/>
    <!-- Red eye -->
    <circle cx="32" cy="36" r="3" fill="#3a2020"/>
    <circle cx="33" cy="35" r="2" fill="#8a3030"/>
    <!-- Body -->
    <path d="M14 82 Q12 54 28 50 Q42 52 46 68 L40 82" fill="url(#redeye-fur)"/>
  </g>
  
  <!-- Hand concealing/scheming -->
  <path d="M40 60 Q48 56 52 58" stroke="url(#redeye-fur)" stroke-width="5" stroke-linecap="round"/>
  <path d="M52 58 Q58 54 62 56" stroke="#5a4a4a" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
</svg>
`;


// ============================================================================
// EXPORT / INDEX
// ============================================================================

const GREEN_EMBER_ICONS = {
  heather: HEATHER_SVG,
  picket: PICKET_SVG,
  smalls: SMALLS_SVG,
  helmer: HELMER_SVG,
  rake: RAKE_SVG,
  emma: EMMA_SVG,
  kyle: KYLE_SVG,
  jo: JO_SVG,
  frye: FRYE_SVG,
  wilfred: WILFRED_SVG,
  morbin: MORBIN_SVG,
  redeye: REDEYE_SVG
};

// For ES modules:
// export { GREEN_EMBER_ICONS };
// export default GREEN_EMBER_ICONS;

// For CommonJS:
// module.exports = { GREEN_EMBER_ICONS };
