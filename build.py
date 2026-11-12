import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

H = '<!DOCTYPE html>\n<html lang="de">\n<head>\n'
H += '<meta charset="UTF-8"/>\n<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n'
H += '<title>Reputivo | Dein KI-Assistent für Google-Bewertungen</title>\n'
H += '<meta name="description" content="Reputivo erkennt neue Google-Bewertungen, erstellt professionelle Antwortvorschläge und sendet sie dir direkt auf WhatsApp – zur Prüfung und Freigabe. Für lokale Unternehmen, Restaurants und Dienstleister."/>\n'
H += '<meta name="robots" content="index,follow"/>\n<link rel="canonical" href="https://reputivo.de/"/>\n'
H += '<meta property="og:title" content="Reputivo | Dein KI-Assistent für Google-Bewertungen"/>\n'
H += '<meta property="og:description" content="Reputivo erkennt neue Google-Bewertungen, erstellt professionelle Antwortvorschläge und sendet sie dir direkt auf WhatsApp."/>\n'
H += '<meta property="og:type" content="website"/>\n'
H += '<style>\n'
:root{--bg:#f5f7fb;--panel:rgba(255,255,255,0.72);--stroke:rgba(15,23,42,0.08);--text:#101828;--muted:#5f6c7b;--muted-light:#8896a6;--primary:#0f172a;--primary-soft:#1d4ed8;--accent:#5b7cff;--glow:rgba(91,124,255,0.22);--success:#dff6e8;--success-text:#0c5d3c;--error:#fee2e2;--error-text:#991b1b;--shadow-sm:0 1px 3px rgba(15,23,42,0.06);--shadow:0 22px 60px rgba(15,23,42,0.12);--shadow-lg:0 34px 80px rgba(15,23,42,0.16);--radius:20px;--radius-lg:28px;--radius-xl:36px;--transition:0.25s cubic-bezier(0.4,0,0.2,1)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{font-family:"SF Pro Display","SF Pro Text","Segoe UI",system-ui,-apple-system,Arial,sans-serif;background:radial-gradient(circle at 10% 0%,rgba(91,124,255,0.10),transparent 34%),radial-gradient(circle at 90% 100%,rgba(15,23,42,0.07),transparent 28%),var(--bg);color:var(--text);line-height:1.62;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}button{cursor:pointer;font:inherit;border:none;background:none}ul{list-style:none}
.container{width:min(1160px,calc(100% - 40px));margin:0 auto}
h1{font-size:clamp(2.6rem,5.2vw,4.8rem);line-height:1.02;letter-spacing:-0.065em;font-weight:800}
h2{font-size:clamp(1.9rem,3.2vw,2.8rem);line-height:1.08;letter-spacing:-0.055em;font-weight:700}
h3{font-size:clamp(1.15rem,1.6vw,1.4rem);line-height:1.2;letter-spacing:-0.035em;font-weight:700}
.topbar{position:sticky;top:0;z-index:100;backdrop-filter:blur(20px) saturate(180%);-webkit-backdrop-filter:blur(20px) saturate(180%);background:rgba(245,247,251,0.68);border-bottom:1px solid rgba(15,23,42,0.06);transition:box-shadow var(--transition)}.topbar.scrolled{box-shadow:0 4px 24px rgba(15,23,42,0.08)}
.nav{display:flex;align-items:center;justify-content:space-between;min-height:74px;gap:16px}
.brand{display:inline-flex;align-items:center;gap:11px;font-weight:700;letter-spacing:-0.05em;font-size:1.3rem;flex-shrink:0}
.brand-mark{width:30px;height:30px;display:grid;place-items:center;border-radius:10px;background:linear-gradient(135deg,#0f172a,#1d4ed8 50%,#5b7cff);color:white;box-shadow:0 10px 24px rgba(76,104,255,0.4);font-size:0.85rem;font-weight:800}
.nav-links{display:flex;align-items:center;gap:6px;color:var(--muted);font-size:0.93rem;font-weight:500}
.nav-links a{padding:8px 14px;border-radius:10px;transition:all var(--transition)}
.nav-links a:hover,.nav-links a:focus-visible{color:var(--text);background:rgba(15,23,42,0.04)}
.nav-cta{display:inline-flex;align-items:center;gap:6px;padding:10px 20px;border-radius:999px;font-weight:600;font-size:0.9rem;background:linear-gradient(135deg,#0f172a,#1d4ed8);color:white;box-shadow:0 8px 24px rgba(29,78,216,0.25);transition:all var(--transition);white-space:nowrap;flex-shrink:0}
.nav-cta:hover{transform:translateY(-1px);box-shadow:0 14px 32px rgba(29,78,216,0.35)}
.hamburger{display:none;flex-direction:column;gap:5px;padding:10px 8px;border-radius:10px;z-index:110}
.hamburger span{display:block;width:22px;height:2px;background:var(--text);border-radius:2px;transition:all var(--transition)}
.hamburger.active span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
.hamburger.active span:nth-child(2){opacity:0}
.hamburger.active span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;font-weight:600;font-size:0.95rem;padding:14px 26px;transition:all var(--transition);white-space:nowrap}
.btn-primary{background:linear-gradient(135deg,#0f172a,#1d4ed8 50%,#5b7cff);color:white;box-shadow:0 18px 34px rgba(35,74,204,0.28)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 24px 44px rgba(35,74,204,0.38)}
.btn-secondary{background:rgba(255,255,255,0.82);border:1px solid var(--stroke);color:var(--text)}
.btn-secondary:hover{background:white;border-color:rgba(15,23,42,0.15);transform:translateY(-1px)}
.btn-lg{padding:16px 32px;font-size:1rem}
section{padding:96px 0}
.section-label{display:inline-block;font-size:0.72rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:14px}
.section-header{text-align:center;max-width:700px;margin:0 auto 56px}
.section-header h2{margin-bottom:16px}
.section-header p{color:var(--muted);font-size:1.08rem;line-height:1.6;max-width:560px;margin:0 auto}
</style>
</head>
<body>
<p>Build script test - please wait for full build</p>
</body>
</html>"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Done: index.html written with %d chars' % len(html))