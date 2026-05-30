<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Catherine Jenishtha — GitHub Profile</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=DM+Sans:wght@300;400;500;600&family=Fira+Code:wght@400;500&family=Great+Vibes&display=swap" rel="stylesheet"/>
<style>
  :root {
    --rose: #E8A0BF;
    --rose-deep: #C96B9A;
    --rose-light: #F7D6E8;
    --blush: #FAE8F2;
    --petal: #FDF0F8;
    --mauve: #9B6B8A;
    --lavender: #C5A8D4;
    --lavender-deep: #9070B0;
    --gold: #D4A96A;
    --gold-light: #F0D5A5;
    --cream: #FFF8F5;
    --ink: #2C1B2E;
    --ink-soft: #5A3D58;
    --ink-mute: #9A7A98;
    --white: #FFFFFF;
    --glass: rgba(255,255,255,0.55);
    --glass-border: rgba(255,255,255,0.75);
    --shadow-rose: 0 8px 32px rgba(201,107,154,0.18);
    --shadow-deep: 0 20px 60px rgba(44,27,46,0.14);
  }
  * { margin:0; padding:0; box-sizing:border-box; }
  
  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--cream);
    color: var(--ink);
    overflow-x: hidden;
    position: relative;
  }

  /* ── AMBIENT BACKGROUND ── */
  body::before {
    content: '';
    position: fixed; inset: 0; z-index: 0;
    background:
      radial-gradient(ellipse 70% 50% at 10% 20%, rgba(232,160,191,0.22) 0%, transparent 70%),
      radial-gradient(ellipse 60% 60% at 90% 80%, rgba(197,168,212,0.18) 0%, transparent 65%),
      radial-gradient(ellipse 50% 40% at 50% 50%, rgba(212,169,106,0.08) 0%, transparent 60%),
      linear-gradient(160deg, #FFF5FB 0%, #FDF0F8 35%, #F8F2FF 70%, #FFF8F5 100%);
    pointer-events: none;
  }

  /* ── FLOATING PETALS ── */
  .petal-bg {
    position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
  }
  .petal {
    position: absolute;
    border-radius: 50% 0 50% 0;
    opacity: 0;
    animation: floatPetal linear infinite;
  }
  @keyframes floatPetal {
    0%   { opacity: 0; transform: translateY(0) rotate(0deg) scale(0.5); }
    10%  { opacity: 0.5; }
    90%  { opacity: 0.3; }
    100% { opacity: 0; transform: translateY(-110vh) rotate(540deg) scale(1); }
  }

  /* ── LAYOUT ── */
  .container {
    position: relative; z-index: 1;
    max-width: 900px; margin: 0 auto;
    padding: 40px 24px 80px;
  }

  /* ── HERO HEADER ── */
  .hero {
    position: relative;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 28px;
    background: linear-gradient(135deg, #2C1B2E 0%, #3E2448 40%, #5A3060 70%, #3E2448 100%);
    box-shadow: 0 24px 80px rgba(44,27,46,0.38), 0 2px 0 rgba(255,255,255,0.1) inset;
    padding: 52px 48px 44px;
    transform-style: preserve-3d;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
  }
  .hero:hover {
    transform: translateY(-4px) rotateX(1deg);
    box-shadow: 0 36px 100px rgba(44,27,46,0.45), 0 2px 0 rgba(255,255,255,0.1) inset;
  }
  /* shimmer overlay */
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(105deg,
      transparent 30%,
      rgba(255,255,255,0.06) 40%,
      rgba(255,255,255,0.12) 50%,
      rgba(255,255,255,0.04) 60%,
      transparent 70%);
    background-size: 200% 100%;
    animation: heroShimmer 4s ease-in-out infinite;
    pointer-events: none;
  }
  @keyframes heroShimmer {
    0%, 100% { background-position: -100% 0; }
    50%       { background-position: 200% 0; }
  }
  /* decorative circles */
  .hero::after {
    content: '';
    position: absolute;
    width: 340px; height: 340px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(232,160,191,0.15) 0%, transparent 70%);
    top: -80px; right: -80px;
    pointer-events: none;
  }
  .hero-orb {
    position: absolute;
    width: 180px; height: 180px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(197,168,212,0.12) 0%, transparent 70%);
    bottom: -40px; left: 10%;
    pointer-events: none;
  }

  .hero-inner { position: relative; z-index: 1; }
  .hero-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 50px;
    padding: 6px 16px;
    font-size: 12px;
    color: var(--rose-light);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 20px;
    backdrop-filter: blur(8px);
  }
  .hero-badge::before { content: '✦'; color: var(--gold); font-size: 10px; }

  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 5vw, 58px);
    color: #FFFFFF;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 12px;
  }
  .hero h1 em {
    font-style: italic;
    background: linear-gradient(90deg, #E8A0BF, #D4A96A, #C5A8D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .hero-role {
    color: rgba(255,255,255,0.65);
    font-size: 15px;
    font-weight: 400;
    margin-bottom: 28px;
    letter-spacing: 0.02em;
  }
  .hero-role span {
    color: var(--rose);
    font-weight: 500;
  }

  .hero-links { display: flex; flex-wrap: wrap; gap: 10px; }
  .hero-link {
    display: inline-flex; align-items: center; gap: 7px;
    padding: 9px 18px;
    border-radius: 50px;
    font-size: 13px;
    font-weight: 500;
    text-decoration: none;
    transition: all 0.25s ease;
    letter-spacing: 0.01em;
    cursor: pointer;
    border: none;
  }
  .hero-link.primary {
    background: linear-gradient(135deg, var(--rose) 0%, var(--rose-deep) 100%);
    color: #fff;
    box-shadow: 0 4px 20px rgba(201,107,154,0.4);
  }
  .hero-link.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 28px rgba(201,107,154,0.55);
  }
  .hero-link.ghost {
    background: rgba(255,255,255,0.1);
    color: rgba(255,255,255,0.8);
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(8px);
  }
  .hero-link.ghost:hover {
    background: rgba(255,255,255,0.18);
    color: #fff;
    transform: translateY(-2px);
  }
  .hero-link svg { width: 15px; height: 15px; }

  /* ── CODE CARD ── */
  .code-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
    margin-bottom: 28px;
  }
  @media (max-width: 680px) { .code-section { grid-template-columns: 1fr; } }

  .glass-card {
    background: var(--glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    box-shadow: var(--shadow-rose), 0 1px 0 rgba(255,255,255,0.8) inset;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    overflow: hidden;
  }
  .glass-card:hover {
    transform: translateY(-5px) scale(1.01);
    box-shadow: 0 20px 60px rgba(201,107,154,0.22), 0 1px 0 rgba(255,255,255,0.9) inset;
  }

  .code-block {
    padding: 24px;
  }
  .code-topbar {
    display: flex; align-items: center; gap: 7px;
    margin-bottom: 18px;
  }
  .dot { width: 11px; height: 11px; border-radius: 50%; }
  .dot.r { background: #FF6B6B; }
  .dot.y { background: #FFD93D; }
  .dot.g { background: #6BCB77; }
  .code-lang {
    margin-left: auto;
    font-size: 11px; font-family: 'Fira Code', monospace;
    color: var(--rose-deep);
    background: var(--rose-light);
    padding: 3px 10px; border-radius: 20px;
  }
  pre {
    font-family: 'Fira Code', monospace;
    font-size: 12.5px;
    line-height: 1.75;
    color: var(--ink);
    white-space: pre-wrap;
    word-break: break-word;
  }
  .tok-kw   { color: #9070B0; font-weight: 600; }
  .tok-str  { color: #B5503A; }
  .tok-fn   { color: #C96B9A; }
  .tok-var  { color: #2C7BB6; }
  .tok-cm   { color: var(--ink-mute); font-style: italic; }
  .tok-num  { color: #D4A96A; }

  /* ── INFO CARD (right side of code section) ── */
  .info-card {
    padding: 28px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 18px;
  }
  .info-card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--ink);
    margin-bottom: 4px;
  }
  .info-card h2 em { font-style: italic; color: var(--rose-deep); }
  .info-card p {
    font-size: 13.5px;
    color: var(--ink-soft);
    line-height: 1.65;
  }

  .stat-row { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .stat-pill {
    background: linear-gradient(135deg, var(--blush) 0%, rgba(197,168,212,0.15) 100%);
    border: 1px solid rgba(232,160,191,0.35);
    border-radius: 12px;
    padding: 12px 14px;
    text-align: center;
    transition: transform 0.2s;
  }
  .stat-pill:hover { transform: scale(1.04); }
  .stat-pill .val {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    font-weight: 700;
    color: var(--rose-deep);
    display: block;
  }
  .stat-pill .lbl {
    font-size: 11px;
    color: var(--mauve);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    display: block;
    margin-top: 2px;
  }

  /* ── SECTION HEADERS ── */
  .section-head {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 18px;
    margin-top: 32px;
  }
  .section-head h3 {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--ink);
  }
  .section-head h3 em { font-style: italic; color: var(--rose-deep); }
  .section-line {
    flex: 1; height: 1px;
    background: linear-gradient(90deg, rgba(201,107,154,0.3), transparent);
  }
  .section-gem {
    width: 8px; height: 8px;
    background: linear-gradient(135deg, var(--rose), var(--lavender));
    transform: rotate(45deg);
    border-radius: 2px;
    flex-shrink: 0;
  }

  /* ── TECH STACK ── */
  .stack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
    gap: 10px;
    margin-bottom: 10px;
  }
  .tech-pill {
    display: flex; align-items: center; gap: 8px;
    padding: 9px 14px;
    background: var(--glass);
    border: 1px solid rgba(232,160,191,0.3);
    border-radius: 50px;
    font-size: 12.5px;
    font-weight: 500;
    color: var(--ink-soft);
    backdrop-filter: blur(10px);
    transition: all 0.25s ease;
    cursor: default;
    white-space: nowrap;
  }
  .tech-pill:hover {
    background: linear-gradient(135deg, var(--rose-light), rgba(197,168,212,0.25));
    border-color: var(--rose);
    color: var(--ink);
    transform: translateY(-3px);
    box-shadow: 0 8px 24px rgba(201,107,154,0.2);
  }
  .tech-dot {
    width: 7px; height: 7px; border-radius: 50%; flex-shrink: 0;
  }

  /* ── EXPERIENCE CARDS ── */
  .exp-card {
    padding: 26px 28px;
    margin-bottom: 14px;
    position: relative;
  }
  .exp-card::before {
    content: '';
    position: absolute;
    left: 0; top: 20px; bottom: 20px;
    width: 3px;
    background: linear-gradient(180deg, var(--rose), var(--lavender));
    border-radius: 2px;
  }
  .exp-header { display: flex; align-items: flex-start; justify-content: space-between; gap: 12px; margin-bottom: 10px; }
  .exp-title { font-weight: 600; font-size: 15px; color: var(--ink); }
  .exp-company { font-size: 13px; color: var(--rose-deep); font-weight: 500; margin-top: 2px; }
  .exp-badge {
    background: linear-gradient(135deg, var(--rose-light), rgba(197,168,212,0.2));
    border: 1px solid rgba(201,107,154,0.25);
    border-radius: 50px;
    padding: 4px 12px;
    font-size: 11px;
    color: var(--mauve);
    white-space: nowrap;
    flex-shrink: 0;
  }
  .exp-list {
    list-style: none;
    display: flex; flex-direction: column; gap: 7px;
    margin-top: 12px;
  }
  .exp-list li {
    font-size: 13px; color: var(--ink-soft); line-height: 1.5;
    padding-left: 16px; position: relative;
  }
  .exp-list li::before {
    content: '✦';
    position: absolute; left: 0;
    color: var(--rose); font-size: 8px; top: 4px;
  }

  /* ── PROJECTS ── */
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 14px;
  }
  .project-card {
    padding: 22px 20px;
    position: relative;
    overflow: hidden;
    cursor: pointer;
  }
  .project-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--rose), var(--lavender), var(--gold));
    border-radius: 20px 20px 0 0;
    opacity: 0;
    transition: opacity 0.3s;
  }
  .project-card:hover::before { opacity: 1; }
  .project-icon {
    width: 40px; height: 40px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    margin-bottom: 12px;
    background: linear-gradient(135deg, var(--blush), rgba(197,168,212,0.2));
    border: 1px solid rgba(232,160,191,0.3);
  }
  .project-name {
    font-size: 14px; font-weight: 600; color: var(--ink);
    margin-bottom: 6px;
  }
  .project-desc {
    font-size: 12px; color: var(--ink-mute); line-height: 1.5;
    margin-bottom: 12px;
  }
  .project-tags { display: flex; flex-wrap: wrap; gap: 5px; }
  .tag {
    font-size: 10px;
    padding: 3px 8px;
    border-radius: 20px;
    background: var(--blush);
    color: var(--rose-deep);
    border: 1px solid rgba(201,107,154,0.2);
  }

  /* ── ACHIEVEMENTS ── */
  .achieve-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 12px;
  }
  .achieve-card {
    display: flex; align-items: flex-start; gap: 14px;
    padding: 18px 20px;
  }
  .achieve-icon {
    width: 42px; height: 42px; flex-shrink: 0;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    background: linear-gradient(135deg, var(--rose-light) 0%, rgba(197,168,212,0.3) 100%);
    box-shadow: 0 4px 12px rgba(201,107,154,0.15);
  }
  .achieve-text .title {
    font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 3px;
  }
  .achieve-text .sub {
    font-size: 12px; color: var(--ink-mute); line-height: 1.4;
  }

  /* ── LEARNING ── */
  .learning-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
  }
  .learn-card {
    padding: 18px 20px;
    position: relative; overflow: hidden;
  }
  .learn-card::after {
    content: '';
    position: absolute;
    width: 80px; height: 80px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(232,160,191,0.15), transparent);
    bottom: -20px; right: -20px;
    pointer-events: none;
  }
  .learn-em {
    font-size: 22px; margin-bottom: 8px; display: block;
  }
  .learn-title {
    font-size: 13.5px; font-weight: 600; color: var(--ink); margin-bottom: 4px;
  }
  .learn-sub {
    font-size: 11.5px; color: var(--ink-mute); line-height: 1.45;
  }
  .progress-bar {
    height: 3px;
    background: rgba(201,107,154,0.15);
    border-radius: 10px;
    margin-top: 10px;
    overflow: hidden;
  }
  .progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--rose), var(--lavender));
    border-radius: 10px;
    animation: fillProgress 1.5s ease-out forwards;
    width: 0%;
  }
  @keyframes fillProgress {
    from { width: 0%; }
    to   { width: var(--pct); }
  }

  /* ── EDUCATION ── */
  .edu-card {
    padding: 28px;
    display: flex; align-items: center; gap: 20px;
  }
  @media (max-width: 540px) { .edu-card { flex-direction: column; align-items: flex-start; } }
  .edu-icon {
    width: 64px; height: 64px; flex-shrink: 0;
    border-radius: 20px;
    background: linear-gradient(135deg, #2C1B2E, #5A3060);
    display: flex; align-items: center; justify-content: center;
    font-size: 28px;
    box-shadow: 0 8px 24px rgba(44,27,46,0.25);
  }
  .edu-title { font-weight: 600; font-size: 15px; color: var(--ink); margin-bottom: 4px; }
  .edu-inst { font-size: 13px; color: var(--rose-deep); margin-bottom: 6px; }
  .edu-meta { font-size: 12px; color: var(--ink-mute); }
  .edu-score {
    margin-left: auto; text-align: center;
    background: linear-gradient(135deg, var(--blush), rgba(197,168,212,0.2));
    border: 1px solid rgba(201,107,154,0.25);
    border-radius: 16px;
    padding: 14px 22px;
    flex-shrink: 0;
  }
  .edu-score .big {
    font-family: 'Playfair Display', serif;
    font-size: 26px; font-weight: 700;
    color: var(--rose-deep); display: block;
  }
  .edu-score .sml { font-size: 11px; color: var(--mauve); }

  /* ── FOOTER ── */
  .footer {
    margin-top: 48px;
    text-align: center;
    padding: 40px 24px;
    background: linear-gradient(135deg, #2C1B2E 0%, #3E2448 100%);
    border-radius: 24px;
    position: relative; overflow: hidden;
    box-shadow: 0 20px 60px rgba(44,27,46,0.3);
  }
  .footer::before {
    content: '';
    position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 60% 80% at 20% 50%, rgba(232,160,191,0.1), transparent),
      radial-gradient(ellipse 50% 70% at 80% 50%, rgba(197,168,212,0.08), transparent);
    pointer-events: none;
  }
  .footer-inner { position: relative; z-index: 1; }
  .footer-quote {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-style: italic;
    color: rgba(255,255,255,0.85);
    margin-bottom: 6px;
  }
  .footer-sub {
    font-size: 13px; color: rgba(255,255,255,0.4);
    margin-bottom: 28px;
  }
  .footer-links { display: flex; justify-content: center; gap: 12px; flex-wrap: wrap; }
  .f-link {
    display: inline-flex; align-items: center; gap: 7px;
    padding: 9px 20px; border-radius: 50px;
    font-size: 13px; font-weight: 500;
    text-decoration: none;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: rgba(255,255,255,0.75);
    transition: all 0.25s;
  }
  .f-link:hover {
    background: rgba(232,160,191,0.2);
    border-color: var(--rose);
    color: #fff;
    transform: translateY(-2px);
  }

  /* ── SCROLLBAR ── */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(201,107,154,0.35); border-radius: 10px; }

  /* ── ENTRANCE ANIMATION ── */
  .reveal {
    opacity: 0; transform: translateY(20px);
    transition: opacity 0.6s ease, transform 0.6s ease;
  }
  .reveal.visible {
    opacity: 1; transform: translateY(0);
  }
</style>
</head>
<body>

<!-- Floating petal background -->
<div class="petal-bg" id="petalBg"></div>

<div class="container">

  <!-- ── HERO ── -->
  <div class="hero reveal">
    <div class="hero-orb"></div>
    <div class="hero-inner">
      <div class="hero-badge">Junior Software Developer · Chennai, India</div>
      <h1>Catherine<br/><em style="font-family:'Great Vibes', cursive; font-size: clamp(48px, 7vw, 76px); -webkit-text-fill-color: transparent; background: linear-gradient(90deg, #E8A0BF, #D4A96A, #C5A8D4); -webkit-background-clip: text; background-clip: text; letter-spacing: 0.02em;">Jenishtha J</em></h1>
      <p class="hero-role">
        Full-Stack · Flutter · Python · Cloud &nbsp;·&nbsp;
        <span>@ Amorio Technologies</span>
      </p>
      <div class="hero-links">
        <a class="hero-link primary" href="https://linkedin.com/in/catherine-jenishtha" target="_blank">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2"/></svg>
          LinkedIn
        </a>
        <a class="hero-link ghost" href="https://cathyjenish.github.io/Portfolio/" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
          Portfolio
        </a>
        <a class="hero-link ghost" href="https://github.com/cathyjenish" target="_blank">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22"/></svg>
          GitHub
        </a>
        <a class="hero-link ghost" href="mailto:cathyjenish02@gmail.com">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          Email
        </a>
      </div>
    </div>
  </div>

  <!-- ── CODE + STATS ── -->
  <div class="code-section reveal">
    <!-- Code card -->
    <div class="glass-card code-block">
      <div class="code-topbar">
        <div class="dot r"></div>
        <div class="dot y"></div>
        <div class="dot g"></div>
        <div class="code-lang">python</div>
      </div>
      <pre><span class="tok-kw">class</span> <span class="tok-fn">CatherineJenishtha</span>:
  <span class="tok-kw">def</span> <span class="tok-fn">__init__</span>(<span class="tok-var">self</span>):
    <span class="tok-var">self</span>.name = <span class="tok-str">"Catherine Jenishtha J"</span>
    <span class="tok-var">self</span>.location = <span class="tok-str">"Chennai 🇮🇳"</span>
    <span class="tok-var">self</span>.role = <span class="tok-str">"Junior Software Developer"</span>

    <span class="tok-var">self</span>.stack = [
      <span class="tok-str">"Python"</span>, <span class="tok-str">"Django"</span>, <span class="tok-str">"React"</span>,
      <span class="tok-str">"Flutter"</span>, <span class="tok-str">"Node.js"</span>, <span class="tok-str">"Flask"</span>
    ]

    <span class="tok-var">self</span>.superpower = (
      <span class="tok-str">"90% buffering reduction 🚀"</span>
    )

  <span class="tok-kw">def</span> <span class="tok-fn">motto</span>(<span class="tok-var">self</span>):
    <span class="tok-kw">return</span> <span class="tok-str">"Build things that matter. ✨"</span>

<span class="tok-var">me</span> = <span class="tok-fn">CatherineJenishtha</span>()
<span class="tok-fn">print</span>(<span class="tok-var">me</span>.motto())</pre>
    </div>

    <!-- Stats card -->
    <div class="glass-card info-card">
      <div>
        <h2><em>About</em> Me</h2>
        <p style="margin-top:10px;">Full-Stack developer passionate about building beautiful, functional apps. From drone path-planning algorithms to Flutter mobile apps — I love solving real problems with elegant code.</p>
      </div>
      <div class="stat-row">
        <div class="stat-pill">
          <span class="val">90%</span>
          <span class="lbl">Buffering ↓</span>
        </div>
        <div class="stat-pill">
          <span class="val">8.4</span>
          <span class="lbl">CGPA / 10</span>
        </div>
        <div class="stat-pill">
          <span class="val">2+</span>
          <span class="lbl">Yrs Exp</span>
        </div>
        <div class="stat-pill">
          <span class="val">4+</span>
          <span class="lbl">Projects</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ── TECH STACK ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3>Tech <em>Stack</em></h3>
      <div class="section-line"></div>
    </div>

    <p style="font-size:12px;color:var(--ink-mute);margin-bottom:12px;letter-spacing:0.08em;text-transform:uppercase;">Languages</p>
    <div class="stack-grid" style="margin-bottom:18px;">
      <div class="tech-pill"><div class="tech-dot" style="background:#3776AB"></div>Python</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#F7DF1E"></div>JavaScript</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#E34F26"></div>HTML5</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#1572B6"></div>CSS3</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#0175C2"></div>Dart</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#00599C"></div>C</div>
    </div>

    <p style="font-size:12px;color:var(--ink-mute);margin-bottom:12px;letter-spacing:0.08em;text-transform:uppercase;">Frameworks & Libraries</p>
    <div class="stack-grid" style="margin-bottom:18px;">
      <div class="tech-pill"><div class="tech-dot" style="background:#092E20"></div>Django</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#61DAFB"></div>React</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#02569B"></div>Flutter</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#339933"></div>Node.js</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#000000"></div>Flask</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#FF4B4B"></div>Streamlit</div>
    </div>

    <p style="font-size:12px;color:var(--ink-mute);margin-bottom:12px;letter-spacing:0.08em;text-transform:uppercase;">Cloud & Databases</p>
    <div class="stack-grid">
      <div class="tech-pill"><div class="tech-dot" style="background:#0078D4"></div>Azure</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#FF9900"></div>AWS S3</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#FFCA28"></div>Firebase</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#47A248"></div>MongoDB</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#4479A1"></div>MySQL</div>
      <div class="tech-pill"><div class="tech-dot" style="background:#5C3EE8"></div>OpenCV</div>
    </div>
  </div>

  <!-- ── EXPERIENCE ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3>Work <em>Experience</em></h3>
      <div class="section-line"></div>
    </div>

    <div class="glass-card exp-card">
      <div class="exp-header">
        <div>
          <div class="exp-title">Junior Software Developer</div>
          <div class="exp-company">Amorio Technologies Pvt. Ltd.</div>
        </div>
        <div class="exp-badge">Oct 2025 – Present</div>
      </div>
      <ul class="exp-list">
        <li>Built Flutter mobile application with backend connectivity, payment gateway & Firebase push notifications</li>
        <li>Developed full-stack e-commerce admin portal using React + Django with product & supplier modules</li>
        <li>Integrated RESTful APIs for decoupled frontend–backend communication</li>
        <li>Managed end-to-end client communication with timely delivery and rapid change resolution</li>
      </ul>
    </div>

    <div class="glass-card exp-card">
      <div class="exp-header">
        <div>
          <div class="exp-title">Project Assistant (Software Developer)</div>
          <div class="exp-company">Mspace Drone Technology Pvt. Ltd.</div>
        </div>
        <div class="exp-badge">Sep 2023 – Jul 2024</div>
      </div>
      <ul class="exp-list">
        <li>Designed Dijkstra-based shortest path planning for autonomous drone routing around polygon obstacles</li>
        <li>Built Tkinter mesh network video streaming app — achieved <strong style="color:var(--rose-deep)">90% reduction</strong> in buffering</li>
        <li>Contributed to polygon obstacle avoidance algorithm for autonomous systems</li>
      </ul>
    </div>
  </div>

  <!-- ── PROJECTS ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3>Featured <em>Projects</em></h3>
      <div class="section-line"></div>
    </div>
    <div class="projects-grid">
      <div class="glass-card project-card">
        <div class="project-icon">🤖</div>
        <div class="project-name">AI Code Reviewer</div>
        <div class="project-desc">Multi-language AI tool for automated code review — detects bugs, style issues & improvements in real-time</div>
        <div class="project-tags">
          <span class="tag">Python</span>
          <span class="tag">Streamlit</span>
          <span class="tag">LLM</span>
        </div>
      </div>
      <div class="glass-card project-card">
        <div class="project-icon">☁️</div>
        <div class="project-name">Azure Static Hosting</div>
        <div class="project-desc">Static website on Azure Blob Storage with CDN integration and public access configuration</div>
        <div class="project-tags">
          <span class="tag">Azure</span>
          <span class="tag">Blob Storage</span>
          <span class="tag">HTML/CSS</span>
        </div>
      </div>
      <div class="glass-card project-card">
        <div class="project-icon">🚁</div>
        <div class="project-name">Drone Path Planning</div>
        <div class="project-desc">Dijkstra's algorithm navigating around polygonal obstacles — 90% buffering reduction in drone feeds</div>
        <div class="project-tags">
          <span class="tag">Python</span>
          <span class="tag">Dijkstra's</span>
          <span class="tag">CV</span>
        </div>
      </div>
      <div class="glass-card project-card">
        <div class="project-icon">🏥</div>
        <div class="project-name">Hospital System</div>
        <div class="project-desc">Full-stack hospital management with patient records, appointments & doctor management</div>
        <div class="project-tags">
          <span class="tag">Flutter</span>
          <span class="tag">Django</span>
          <span class="tag">SQL</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ── ACHIEVEMENTS ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3><em>Achievements</em> & Certs</h3>
      <div class="section-line"></div>
    </div>
    <div class="achieve-grid">
      <div class="glass-card achieve-card">
        <div class="achieve-icon">💎</div>
        <div class="achieve-text">
          <div class="title">Buffering Reduction</div>
          <div class="sub">Cut drone video buffering by 90% using Dijkstra's algorithm</div>
        </div>
      </div>
      <div class="glass-card achieve-card">
        <div class="achieve-icon">📱</div>
        <div class="achieve-text">
          <div class="title">Mobile App Delivery</div>
          <div class="sub">Shipped Flutter app with payment gateway & Firebase notifications</div>
        </div>
      </div>
      <div class="glass-card achieve-card">
        <div class="achieve-icon">🛒</div>
        <div class="achieve-text">
          <div class="title">Full-Stack Portal</div>
          <div class="sub">Built & deployed React + Django e-commerce admin portal end-to-end</div>
        </div>
      </div>
      <div class="glass-card achieve-card">
        <div class="achieve-icon">🌟</div>
        <div class="achieve-text">
          <div class="title">Best Performer</div>
          <div class="sub">Python Developer Internship @ Elevate Labs, Sep 2025</div>
        </div>
      </div>
      <div class="glass-card achieve-card">
        <div class="achieve-icon">☁️</div>
        <div class="achieve-text">
          <div class="title">Cloud Certified</div>
          <div class="sub">Cloud Computing Fundamentals — AWS, Azure, IBM Cloud · Jul 2025</div>
        </div>
      </div>
      <div class="glass-card achieve-card">
        <div class="achieve-icon">🔗</div>
        <div class="achieve-text">
          <div class="title">MEAN Stack Cert</div>
          <div class="sub">Full Stack using MongoDB, Express, Angular, Node.js · Oct 2022</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ── CURRENTLY LEARNING ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3>Currently <em>Learning</em></h3>
      <div class="section-line"></div>
    </div>
    <div class="learning-grid">
      <div class="glass-card learn-card">
        <span class="learn-em">🧱</span>
        <div class="learn-title">Flutter Advanced</div>
        <div class="learn-sub">Riverpod / BLoC, Custom Animations</div>
        <div class="progress-bar"><div class="progress-fill" style="--pct: 70%"></div></div>
      </div>
      <div class="glass-card learn-card">
        <span class="learn-em">☁️</span>
        <div class="learn-title">Cloud & DevOps</div>
        <div class="learn-sub">AWS EC2 & Lambda, CI/CD, Docker</div>
        <div class="progress-bar"><div class="progress-fill" style="--pct: 55%"></div></div>
      </div>
      <div class="glass-card learn-card">
        <span class="learn-em">🏗️</span>
        <div class="learn-title">System Design</div>
        <div class="learn-sub">Scalable Architectures, Caching, LB</div>
        <div class="progress-bar"><div class="progress-fill" style="--pct: 45%"></div></div>
      </div>
      <div class="glass-card learn-card">
        <span class="learn-em">🤖</span>
        <div class="learn-title">ML & AI</div>
        <div class="learn-sub">LLM Integration, Fine-tuning, LangChain</div>
        <div class="progress-bar"><div class="progress-fill" style="--pct: 60%"></div></div>
      </div>
      <div class="glass-card learn-card">
        <span class="learn-em">🔒</span>
        <div class="learn-title">Backend Security</div>
        <div class="learn-sub">JWT Auth, OAuth2, API Rate Limiting</div>
        <div class="progress-bar"><div class="progress-fill" style="--pct: 50%"></div></div>
      </div>
    </div>
  </div>

  <!-- ── EDUCATION ── -->
  <div class="reveal">
    <div class="section-head">
      <div class="section-gem"></div>
      <h3><em>Education</em></h3>
      <div class="section-line"></div>
    </div>
    <div class="glass-card edu-card">
      <div class="edu-icon">🎓</div>
      <div>
        <div class="edu-title">B.E. Computer Science & Engineering</div>
        <div class="edu-inst">SA Engineering College, Chennai</div>
        <div class="edu-meta">2020 – 2024</div>
      </div>
      <div class="edu-score">
        <span class="big">8.4</span>
        <span class="sml">CGPA / 10</span>
      </div>
    </div>
  </div>

  <!-- ── FOOTER ── -->
  <div class="footer reveal" style="margin-top:40px;">
    <div class="footer-inner">
      <div class="footer-quote">"Build things that matter. Learn something every day."</div>
      <div class="footer-sub">— Catherine Jenishtha J, Chennai 🇮🇳</div>
      <div class="footer-links">
        <a class="f-link" href="https://linkedin.com/in/catherine-jenishtha" target="_blank">LinkedIn</a>
        <a class="f-link" href="https://github.com/cathyjenish" target="_blank">GitHub</a>
        <a class="f-link" href="https://cathyjenish.github.io/Portfolio/" target="_blank">Portfolio</a>
        <a class="f-link" href="mailto:cathyjenish02@gmail.com">Email</a>
      </div>
    </div>
  </div>

</div>

<script>
// ── Floating petals ──
const bg = document.getElementById('petalBg');
const colors = ['#F7D6E8','#E8C6DC','#F0D5A5','#D4C8E8','#FBE0EE','#EDD6F5'];
for (let i = 0; i < 22; i++) {
  const p = document.createElement('div');
  p.className = 'petal';
  const size = 8 + Math.random() * 14;
  p.style.cssText = `
    width:${size}px; height:${size * 0.65}px;
    left:${Math.random()*100}%;
    bottom:-30px;
    background:${colors[Math.floor(Math.random()*colors.length)]};
    animation-duration:${8 + Math.random()*14}s;
    animation-delay:${Math.random()*12}s;
    transform: rotate(${Math.random()*360}deg);
  `;
  bg.appendChild(p);
}

// ── Scroll reveal ──
const observer = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// ── 3D tilt on glass cards ──
document.querySelectorAll('.glass-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width  - 0.5;
    const y = (e.clientY - r.top)  / r.height - 0.5;
    card.style.transform = `translateY(-5px) rotateX(${-y*6}deg) rotateY(${x*6}deg) scale(1.01)`;
  });
  card.addEventListener('mouseleave', () => {
    card.style.transform = '';
  });
});

// ── Hero tilt ──
const hero = document.querySelector('.hero');
hero.addEventListener('mousemove', e => {
  const r = hero.getBoundingClientRect();
  const x = (e.clientX - r.left) / r.width  - 0.5;
  const y = (e.clientY - r.top)  / r.height - 0.5;
  hero.style.transform = `translateY(-4px) rotateX(${-y*3}deg) rotateY(${x*3}deg)`;
});
hero.addEventListener('mouseleave', () => {
  hero.style.transform = '';
});
</script>
</body>
</html>
