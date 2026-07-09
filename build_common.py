
# -*- coding: utf-8 -*-
"""
Shared constants + templates for the CyberQunit static site build.
Imported by build_site.py
"""

SITE = "CyberQunit"
LEGAL = "Qunit Technologies Pvt Ltd"
DOMAIN = "https://qunittech.com"
PHONE_DISPLAY = "+91 78279 61018"
PHONE_TEL = "+917827961018"
WA_NUMBER = "917827961018"
EMAIL = "Help@qunittech.com"
ADDRESS = "B-7, 1st Floor, Sector-2, Noida, Uttar Pradesh 201301, India"

SOCIALS = {
    "facebook": "https://www.facebook.com/profile.php?id=100091997715658",
    "twitter": "https://twitter.com/qunit0001",
    "youtube": "https://www.youtube.com/@Qunit1",
    "instagram": "https://www.instagram.com/_qunit_/",
    "linkedin": "https://www.linkedin.com/company/qunit/",
}

WA_LINK = f"https://wa.me/{WA_NUMBER}?text=Hi%20CyberQunit%2C%20I%27d%20like%20to%20speak%20with%20a%20security%20expert."

NAV = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Services", "services.html"),
    ("Academic Partnership", "academic-partnership.html"),
    ("Blog", "blog.html"),
    ("Contact", "contact.html"),
]

SERVICE_LINKS = [
    ("Vulnerability Assessment & Penetration Testing (VAPT)", "vapt.html"),
    ("GRC & Compliance Audit", "grc-compliance.html"),
    ("vCISO — Virtual CISO Services", "vciso.html"),
    ("AI & LLM Security", "ai-security.html"),
    ("Cloud Security", "cloud-security.html"),
    ("OT, ICS & Hardware Security", "ot-hardware-security.html"),
    ("Red Teaming & DevSecOps", "red-teaming-devsecops.html"),
]

LOGO_SVG = """
<svg viewBox="0 0 240 60" class="h-9 w-auto sm:h-10" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CyberQunit logo">
  <defs>
    <linearGradient id="swoosh" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#22d3ee"/>
    </linearGradient>
  </defs>
  <g transform="translate(2,4)">
    <path d="M26 2 L48 12 V30 C48 44 38 51 26 56 C14 51 4 44 4 30 V12 Z" fill="#0a1330" stroke="#0e2a52" stroke-width="1"/>
    <circle cx="26" cy="24" r="7.5" fill="none" stroke="#22d3ee" stroke-width="3"/>
    <rect x="23.5" y="28" width="5" height="12" rx="2" fill="#22d3ee"/>
    <path d="M0 40 C14 54 40 54 54 38" fill="none" stroke="url(#swoosh)" stroke-width="4" stroke-linecap="round"/>
  </g>
  <text x="62" y="30" font-family="'Sora',Arial,sans-serif" font-weight="700" font-size="24" fill="#e6f6fb">Cyber<tspan fill="#22d3ee">Qunit</tspan></text>
  <text x="62" y="44" font-family="Arial,sans-serif" font-weight="600" font-size="8.5" letter-spacing="1.5" fill="#7fb8c9">YOUR SHIELD. OUR EXPERTISE.</text>
</svg>
"""

def nav_html(active):
    items = []
    for label, href in NAV:
        cls = "nav-link active" if href == active else "nav-link"
        if label == "Services":
            items.append(f"""
            <li class="relative group">
              <a href="{href}" class="{cls}">Services <svg class="inline w-3 h-3 ml-0.5 opacity-70" viewBox="0 0 20 20" fill="currentColor"><path d="M5.5 7.5l4.5 5 4.5-5z"/></svg></a>
              <div class="mega-menu">
                {''.join(f'<a href="{h}" class="mega-item">{t}</a>' for t, h in SERVICE_LINKS)}
              </div>
            </li>""")
        else:
            items.append(f'<li><a href="{href}" class="{cls}">{label}</a></li>')
    return "\n".join(items)


def head(title, description, canonical, keywords="", schema="", og_image="assets/img/og-cover.svg"):
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keywords}">
<link rel="canonical" href="{DOMAIN}/{canonical}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="{SITE} — {LEGAL}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{DOMAIN}/{canonical}">
<meta property="og:image" content="{DOMAIN}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@qunit0001">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{schema}"""


def whatsapp_and_book_widget():
    return f"""
<!-- Floating action cluster -->
<div class="fab-cluster" id="fabCluster">
  <button id="bookDemoBtn" class="fab fab-book" aria-haspopup="dialog" aria-controls="bookDemoModal">
    <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 7V3M16 7V3M4 11h16M5 5h14a1 1 0 011 1v13a1 1 0 01-1 1H5a1 1 0 01-1-1V6a1 1 0 011-1z"/></svg>
    <span>Book a Demo / Training</span>
  </button>
  <a href="{WA_LINK}" target="_blank" rel="noopener" class="fab fab-whatsapp" aria-label="Chat with CyberQunit on WhatsApp">
    <svg class="w-6 h-6" viewBox="0 0 32 32" fill="currentColor"><path d="M16.02 3C9.4 3 4.02 8.38 4.02 15c0 2.3.63 4.46 1.73 6.32L4 29l7.86-1.7A11.94 11.94 0 0016.02 27C22.64 27 28 21.63 28 15S22.64 3 16.02 3zm0 21.7c-2 0-3.87-.55-5.47-1.5l-.39-.23-4.66 1 1.02-4.55-.25-.4A9.66 9.66 0 016.35 15c0-5.34 4.34-9.68 9.67-9.68S25.7 9.66 25.7 15s-4.34 9.7-9.68 9.7zm5.3-7.26c-.29-.15-1.72-.85-1.99-.95-.27-.1-.46-.15-.66.15-.2.29-.76.94-.93 1.14-.17.2-.34.22-.63.07-.29-.15-1.23-.45-2.34-1.44-.87-.77-1.45-1.72-1.62-2.01-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.2-.29.29-.49.1-.2.05-.37-.02-.51-.07-.15-.66-1.59-.9-2.18-.24-.57-.48-.5-.66-.5-.17 0-.37-.02-.56-.02-.2 0-.51.07-.78.37-.27.29-1.02 1-1.02 2.44s1.05 2.83 1.19 3.03c.15.2 2.06 3.14 5 4.4.7.3 1.24.48 1.67.62.7.22 1.34.19 1.84.11.56-.08 1.72-.7 1.97-1.38.24-.68.24-1.26.17-1.38-.07-.12-.26-.2-.55-.34z"/></svg>
  </a>
</div>

<div id="bookDemoModal" class="modal-overlay hidden" role="dialog" aria-modal="true" aria-labelledby="bookDemoTitle">
  <div class="modal-card">
    <button class="modal-close" id="closeBookDemo" aria-label="Close">&times;</button>
    <h3 id="bookDemoTitle">Book a Free Demo, Audit Consultation, or Training Session</h3>
    <p class="modal-sub">Tell us what you need — a security audit scoping call, a product demo, or a lecture/training session for your institution. We reply within one business day.</p>
    <form class="modal-form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
      <div class="form-row">
        <input type="text" name="Name" placeholder="Full name" required>
        <input type="text" name="Organization" placeholder="Company / Institution">
      </div>
      <div class="form-row">
        <input type="email" name="Email" placeholder="Work email" required>
        <input type="tel" name="Phone" placeholder="Phone / WhatsApp">
      </div>
      <select name="Interest" required>
        <option value="">I'm interested in…</option>
        <option>Security Audit / VAPT consultation</option>
        <option>GRC & Compliance Audit (ISO 27001 / PCI DSS / SOC 2)</option>
        <option>AI / LLM Security Assessment</option>
        <option>Cloud Security Review</option>
        <option>OT / ICS / Hardware Security</option>
        <option>Academic Partnership — Faculty/Student Training</option>
        <option>General Product Demo</option>
      </select>
      <textarea name="Message" rows="3" placeholder="A few details about what you need"></textarea>
      <button type="submit" class="btn-primary w-full">Submit Request</button>
      <p class="form-note">Prefer instant chat? <a href="{WA_LINK}" target="_blank" rel="noopener">Message us on WhatsApp →</a></p>
    </form>
  </div>
</div>
"""


def header_html(active):
    return f"""<header class="site-header" id="siteHeader">
  <div class="topbar">
    <div class="wrap topbar-inner">
      <div class="topbar-left">
        <a href="tel:{PHONE_TEL}">📞 {PHONE_DISPLAY}</a>
        <a href="mailto:{EMAIL}">✉ {EMAIL}</a>
      </div>
      <div class="topbar-right">
        <span>Noida, India</span>
        <a href="{SOCIALS['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn">in</a>
        <a href="{SOCIALS['twitter']}" target="_blank" rel="noopener" aria-label="X / Twitter">X</a>
        <a href="{SOCIALS['instagram']}" target="_blank" rel="noopener" aria-label="Instagram">ig</a>
        <a href="{SOCIALS['youtube']}" target="_blank" rel="noopener" aria-label="YouTube">yt</a>
      </div>
    </div>
  </div>
  <nav class="wrap navbar">
    <a href="index.html" class="brand">{LOGO_SVG}</a>
    <button id="menuToggle" class="menu-toggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <ul class="nav-list" id="navList">
      {nav_html(active)}
    </ul>
    <a href="contact.html" class="btn-primary btn-nav">Get Free Consultation</a>
  </nav>
</header>"""


def footer_html():
    return f"""<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      {LOGO_SVG}
      <p>CyberQunit is the cybersecurity brand of {LEGAL} — protecting businesses, institutions and government partners with AI-augmented security audits, red teaming, compliance, and hands-on cyber education.</p>
      <div class="footer-socials">
        <a href="{SOCIALS['facebook']}" target="_blank" rel="noopener" aria-label="Facebook">Facebook</a>
        <a href="{SOCIALS['twitter']}" target="_blank" rel="noopener" aria-label="X / Twitter">X / Twitter</a>
        <a href="{SOCIALS['youtube']}" target="_blank" rel="noopener" aria-label="YouTube">YouTube</a>
        <a href="{SOCIALS['instagram']}" target="_blank" rel="noopener" aria-label="Instagram">Instagram</a>
        <a href="{SOCIALS['linkedin']}" target="_blank" rel="noopener" aria-label="LinkedIn">LinkedIn</a>
      </div>
    </div>
    <div>
      <h4>Security Audit Services</h4>
      <ul>
        {''.join(f'<li><a href="{h}">{t.split("(")[0].strip()}</a></li>' for t, h in SERVICE_LINKS)}
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="about.html">About CyberQunit</a></li>
        <li><a href="academic-partnership.html">Academic Partnership</a></li>
        <li><a href="blog.html">Cyber & AI Security Blog</a></li>
        <li><a href="contact.html">Contact / Get a Quote</a></li>
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
      </ul>
    </div>
    <div>
      <h4>Head Office</h4>
      <p class="footer-address">{ADDRESS}</p>
      <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <a href="{WA_LINK}" target="_blank" rel="noopener" class="btn-outline btn-sm mt-2">Chat on WhatsApp</a>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; <span id="year"></span> {LEGAL}. All rights reserved. CyberQunit is a registered brand of {LEGAL}.</p>
  </div>
</footer>"""


def service_schema(name, description, url):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "{name}",
  "name": "{name}",
  "description": "{description}",
  "provider": {{"@type": "ProfessionalService", "name": "CyberQunit", "alternateName": "{LEGAL}"}},
  "areaServed": "IN",
  "url": "{DOMAIN}/{url}"
}}
</script>"""


def faq_schema(faqs):
    items = ",\n".join([
        f"""{{"@type":"Question","name":{q!r},"acceptedAnswer":{{"@type":"Answer","text":{a!r}}}}}"""
        for q, a in faqs
    ])
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{items}]}}
</script>"""


def breadcrumb(label):
    return f'<div class="breadcrumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / {label}</div>'


def service_hero(eyebrow, h1, lead, pills=None, crumb=None):
    pills_html = ""
    if pills:
        pills_html = '<div class="badge-row">' + "".join(f'<span class="pill">{p}</span>' for p in pills) + "</div>"
    crumb_label = crumb or eyebrow
    return f"""<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    {breadcrumb(crumb_label)}
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {pills_html}
    <div class="hero-actions">
      <a href="contact.html" class="btn-primary btn-lg">Request This Audit</a>
      <a href="{WA_LINK}" target="_blank" rel="noopener" class="btn-outline btn-lg">Chat on WhatsApp</a>
    </div>
  </div>
</section>"""


def offerings_grid(title_eyebrow, heading, items):
    """items: list of (title, description) tuples"""
    cards = "\n".join(
        f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in items
    )
    return f"""<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">{title_eyebrow}</div>
      <h2>{heading}</h2>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""


def process_section(steps):
    """steps: list of (title, description)"""
    html = "\n".join(f'<div class="step"><h3>{t}</h3><p>{d}</p></div>' for t, d in steps)
    return f"""<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Our Process</div>
      <h2>How the engagement runs</h2>
    </div>
    <div class="steps">{html}</div>
  </div>
</section>"""


def faq_section(faqs):
    items = "\n".join(f"""
    <div class="accordion-item">
      <button class="accordion-btn">{q}<svg class="chev" width="16" height="16" viewBox="0 0 20 20" fill="currentColor"><path d="M5.5 7.5l4.5 5 4.5-5z"/></svg></button>
      <div class="accordion-panel"><p>{a}</p></div>
    </div>""" for q, a in faqs)
    return f"""<section>
  <div class="wrap" style="max-width:820px">
    <div class="section-head">
      <div class="eyebrow center">FAQs</div>
      <h2>Common questions</h2>
    </div>
    {items}
  </div>
</section>"""


def related_services_section(current_href):
    items = [x for x in SERVICE_LINKS if x[1] != current_href]
    cards = "\n".join(f'<a href="{h}" class="card" style="display:block"><h3>{t}</h3></a>' for t, h in items[:3])
    return f"""<section class="alt">
  <div class="wrap">
    <div class="section-head"><div class="eyebrow center">Related Services</div><h2>You might also need</h2></div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>"""


def cta_band(heading, sub=""):
    subp = f'<p class="lead center">{sub}</p>' if sub else ""
    return f"""<section>
  <div class="wrap">
    <div class="cta-band">
      <div class="cta-band-inner">
        <h2>{heading}</h2>
        {subp}
        <div class="hero-actions" style="justify-content:center">
          <a href="contact.html" class="btn-primary btn-lg">Get a Free Quote</a>
          <a href="{WA_LINK}" target="_blank" rel="noopener" class="btn-outline btn-lg">Chat on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>"""


def page(title, description, canonical, body, active="", keywords="", schema="", extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{head(title, description, canonical, keywords, schema)}
{extra_head}
</head>
<body>
{header_html(active)}
<main>
{body}
</main>
{footer_html()}
{whatsapp_and_book_widget()}
<script src="assets/js/main.js" defer></script>
</body>
</html>"""
