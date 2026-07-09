# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_common import page, SERVICE_LINKS, DOMAIN, WA_LINK

OUT = os.path.dirname(__file__)

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

ORG_SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "CyberQunit",
  "alternateName": "Qunit Technologies Pvt Ltd",
  "url": "{DOMAIN}",
  "logo": "{DOMAIN}/assets/img/favicon.svg",
  "image": "{DOMAIN}/assets/img/og-cover.svg",
  "description": "CyberQunit (Qunit Technologies Pvt Ltd) delivers AI-augmented security audits including VAPT, GRC & compliance (ISO 27001, PCI DSS, SOC 2), vCISO, AI/LLM security, cloud security, and OT/ICS/hardware security, plus academic cybersecurity partnerships.",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "B-7, 1st Floor, Sector-2",
    "addressLocality": "Noida",
    "addressRegion": "Uttar Pradesh",
    "postalCode": "201301",
    "addressCountry": "IN"
  }},
  "telephone": "+91-78279-61018",
  "email": "Help@qunittech.com",
  "sameAs": [
    "https://www.linkedin.com/company/qunit/",
    "https://twitter.com/qunit0001",
    "https://www.instagram.com/_qunit_/",
    "https://www.youtube.com/@Qunit1",
    "https://www.facebook.com/profile.php?id=100091997715658"
  ]
}}
</script>"""

# ---------------------------------------------------------------- HOME ----
home_body = """
<section class="hero">
  <div class="hero-grid-bg"></div>
  <div class="wrap hero-inner">
    <div>
      <div class="eyebrow">AI-Augmented Cyber Security Partner</div>
      <h1>Stop breaches before they start.<br>Secure the AI you're building too.</h1>
      <p class="lead">CyberQunit — the cyber security arm of Qunit Technologies Pvt Ltd — runs offensive-grade security audits (VAPT, GRC & Compliance, vCISO) and secures the AI systems modern businesses now depend on, backed by an AI-assisted testing methodology that finds more, faster.</p>
      <div class="badge-row">
        <span class="pill">VAPT · Web, API, Mobile, Cloud</span>
        <span class="pill">ISO 27001 · PCI DSS · SOC 2</span>
        <span class="pill">AI / LLM Security</span>
        <span class="pill">OT &amp; Hardware Security</span>
      </div>
      <div class="hero-actions">
        <a href="contact.html" class="btn-primary btn-lg">Get a Free Security Consultation</a>
        <a href="services.html" class="btn-outline btn-lg">Explore Services</a>
      </div>
      <div class="stat-strip">
        <div><div class="num">10+</div><div class="lbl">Industries served</div></div>
        <div><div class="num">6</div><div class="lbl">Specialised audit practices</div></div>
        <div><div class="num">1</div><div class="lbl">University partnership launching 2026</div></div>
        <div><div class="num">24/7</div><div class="lbl">WhatsApp expert access</div></div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="orbit" style="inset:6%"></div>
      <div class="orbit" style="inset:18%"></div>
      <svg viewBox="0 0 200 200" fill="none">
        <path d="M100 10 L175 42 V100 C175 145 142 172 100 190 C58 172 25 145 25 100 V42 Z" fill="#0a1330" stroke="#22d3ee" stroke-width="2" opacity="0.9"/>
        <circle cx="100" cy="88" r="24" fill="none" stroke="#22d3ee" stroke-width="6"/>
        <rect x="90" y="106" width="20" height="38" rx="7" fill="#22d3ee"/>
        <g stroke="#8b5cf6" stroke-width="1.5" opacity="0.7">
          <circle cx="100" cy="100" r="70"/>
          <circle cx="100" cy="100" r="85" stroke-dasharray="4 6"/>
        </g>
      </svg>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">What We Do</div>
      <h2>Two ways we protect you — audits that hold up under scrutiny, and AI security that keeps pace with your roadmap</h2>
      <p class="lead center">We are deliberately focused: elite security audits for organisations that can't afford a breach, and cyber education for the next generation of defenders.</p>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 20 6v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6l8-4z"/></svg></div>
        <h3>Security Audit &amp; Offensive Security Services</h3>
        <p>VAPT (web, API, mobile, network, cloud), GRC &amp; compliance audits (ISO 27001, PCI DSS, SOC 2), vCISO, AI/LLM security testing, cloud security, OT/ICS &amp; hardware security, red teaming and DevSecOps — one partner for the full stack.</p>
        <a href="services.html" class="card-link">See all audit services →</a>
      </div>
      <div class="card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3l9 4-9 4-9-4 9-4zM3 12l9 4 9-4M3 17l9 4 9-4"/></svg></div>
        <h3>Academic Cyber Security Partnership</h3>
        <p>CyberQunit is partnering with Galgotias University to build and run its B.Tech Cyber Security program — faculty training, industry-aligned curriculum, labs, internships and certification pathways.</p>
        <a href="academic-partnership.html" class="card-link">See the partnership →</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Security Audit Services</div>
      <h2>Six practices. One accountable security partner.</h2>
    </div>
    <div class="grid grid-3">
      <div class="card service-card"><span class="tag tag-hot">Most requested</span>
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 12l2 2 4-4M12 3l8 4v5c0 5-3.4 8.5-8 10-4.6-1.5-8-5-8-10V7l8-4z"/></svg></div>
        <h3>VAPT</h3>
        <p>Web app, API, mobile (iOS/Android), network, cloud and IoT penetration testing mapped to OWASP &amp; CERT-In guidelines.</p>
        <a href="vapt.html" class="card-link">Learn more →</a>
      </div>
      <div class="card service-card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 3H5a2 2 0 00-2 2v4m6-6h10a2 2 0 012 2v4M9 3v18M3 9v10a2 2 0 002 2h4"/></svg></div>
        <h3>GRC &amp; Compliance Audit</h3>
        <p>ISO/IEC 27001:2022, PCI DSS, SOC 2, GDPR, HIPAA, RBI, SEBI &amp; IRDAI frameworks — audit-ready, not just paperwork-ready.</p>
        <a href="grc-compliance.html" class="card-link">Learn more →</a>
      </div>
      <div class="card service-card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3 6 6 1-4.5 4.5L18 20l-6-3-6 3 1.5-6.5L3 9l6-1 3-6z"/></svg></div>
        <h3>vCISO — Virtual CISO</h3>
        <p>On-demand security leadership: strategy, execution oversight, incident readiness and board reporting — without a full-time hire.</p>
        <a href="vciso.html" class="card-link">Learn more →</a>
      </div>
      <div class="card service-card"><span class="tag tag-ai">AI-focused</span>
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg></div>
        <h3>AI &amp; LLM Security</h3>
        <p>AI red teaming, prompt-injection &amp; jailbreak testing, OWASP LLM Top 10 assessments, AI governance aligned to ISO/IEC 42001 &amp; NIST AI RMF.</p>
        <a href="ai-security.html" class="card-link">Learn more →</a>
      </div>
      <div class="card service-card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17.5 19a4.5 4.5 0 000-9 6 6 0 00-11.4-1.5A4 4 0 007 16h10.5z"/></svg></div>
        <h3>Cloud Security</h3>
        <p>AWS, Azure &amp; GCP configuration audits, CSPM, container/Kubernetes security and cloud penetration testing.</p>
        <a href="cloud-security.html" class="card-link">Learn more →</a>
      </div>
      <div class="card service-card">
        <div class="icon-box"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 9h6v6H9z"/><path d="M4 9H2M4 15H2M22 9h-2M22 15h-2M9 4V2M15 4V2M9 22v-2M15 22v-2"/></svg></div>
        <h3>OT, ICS &amp; Hardware Security</h3>
        <p>SCADA/ICS risk assessments, IoT device testing and embedded/firmware hardware security testing for critical infrastructure.</p>
        <a href="ot-hardware-security.html" class="card-link">Learn more →</a>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Why CyberQunit</div>
      <h2>Built by practitioners, not a sales-first agency</h2>
    </div>
    <div class="grid grid-4">
      <div class="card"><h3>AI-augmented testing</h3><p>Our human testers use AI tooling to widen attack-surface coverage and cut noise — without ever replacing manual exploitation.</p></div>
      <div class="card"><h3>Compliance that survives audit</h3><p>Deliverables built to satisfy ISO 27001 auditors, PCI QSAs, and regulators — not just your internal checklist.</p></div>
      <div class="card"><h3>Fixed-scope, fixed-price</h3><p>Clear scoping calls before every engagement. No surprise line items in the final report.</p></div>
      <div class="card"><h3>Retest included</h3><p>One free retest cycle on every VAPT and compliance engagement to confirm remediation actually closed the gap.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Client Feedback</div>
      <h2>What partners say about working with us</h2>
    </div>
    <div class="grid grid-2">
      <div class="testi">
        <p>"Working with Qunit Technologies for our website security was a game-changer. They conducted a comprehensive security audit, pinpointing potential risks and promptly providing solutions to enhance our website's protection."</p>
        <div class="who">Mayank Raj — Co-founder &amp; COO, Codebucket Solutions Pvt Ltd</div>
      </div>
      <div class="testi">
        <p>"Their team conducted a meticulous security audit, addressing potential vulnerabilities with efficiency and precision. Their insights and recommendations have significantly strengthened our cybersecurity posture."</p>
        <div class="who">Sidhant Raj — CEO, Eazy Learning</div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="cta-band">
      <div class="cta-band-inner">
        <h2>Talk to a security expert — free, no obligation</h2>
        <p class="lead center">Tell us what you're building or what's worrying you. We'll scope the right audit, not the biggest one.</p>
        <div class="hero-actions" style="justify-content:center">
          <a href="contact.html" class="btn-primary btn-lg">Request a Consultation</a>
          <a href="__WA_LINK__" target="_blank" rel="noopener" class="btn-outline btn-lg">Chat on WhatsApp</a>
        </div>
      </div>
    </div>
  </div>
</section>
""".replace("__WA_LINK__", WA_LINK)

write("index.html", page(
    title="CyberQunit | AI-Powered VAPT, GRC &amp; Compliance, vCISO, AI Security Company in India",
    description="CyberQunit (Qunit Technologies Pvt Ltd) delivers AI-augmented VAPT, GRC & compliance audits (ISO 27001, PCI DSS, SOC 2), vCISO, AI/LLM security, cloud security and OT/hardware security, plus a B.Tech Cyber Security academic partnership.",
    canonical="index.html",
    body=home_body,
    active="index.html",
    keywords="cyber security company India, VAPT services, penetration testing company, AI security, LLM security testing, ISO 27001 audit, PCI DSS compliance, vCISO, cloud security, OT security, cyber security Noida",
    schema=ORG_SCHEMA,
))

# --------------------------------------------------------------- ABOUT ----
about_body = """
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / About</div>
    <div class="eyebrow">About CyberQunit</div>
    <h1>Security expertise, applied honestly.</h1>
    <p class="lead">CyberQunit is the cybersecurity brand under which Qunit Technologies Pvt Ltd delivers offensive security, compliance, and AI security services — built around one idea: a security report is only useful if it changes what you fix next.</p>
  </div>
</section>

<section class="alt">
  <div class="wrap split">
    <div>
      <div class="eyebrow">Our Story</div>
      <h2>From a WordPress-era portfolio to a purpose-built security practice</h2>
      <p>Qunit Technologies Pvt Ltd was founded in Noida, India to give growing businesses access to the kind of security testing usually reserved for large enterprises. As the practice matured — moving deeper into AI system security, cloud-native environments, and regulatory compliance — we consolidated everything under one focused brand: <strong>CyberQunit</strong>.</p>
      <p>We are GeM (Government e-Marketplace) registered and work with startups, SMEs, and enterprise clients across fintech, e-commerce, healthtech, and EdTech, in addition to launching a dedicated academic partnerships track with universities.</p>
    </div>
    <div class="card">
      <h3>At a glance</h3>
      <ul class="checklist">
        <li><svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor"><path d="M7.5 13.5L4 10l1.4-1.4L7.5 10.7l7.1-7.1L16 5l-8.5 8.5z"/></svg> Headquartered in Noida, Uttar Pradesh, India</li>
        <li><svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor"><path d="M7.5 13.5L4 10l1.4-1.4L7.5 10.7l7.1-7.1L16 5l-8.5 8.5z"/></svg> GeM registered vendor</li>
        <li><svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor"><path d="M7.5 13.5L4 10l1.4-1.4L7.5 10.7l7.1-7.1L16 5l-8.5 8.5z"/></svg> Six specialised security practices under one roof</li>
        <li><svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor"><path d="M7.5 13.5L4 10l1.4-1.4L7.5 10.7l7.1-7.1L16 5l-8.5 8.5z"/></svg> Academic partnership program launching with Galgotias University</li>
        <li><svg width="18" height="18" viewBox="0 0 20 20" fill="currentColor"><path d="M7.5 13.5L4 10l1.4-1.4L7.5 10.7l7.1-7.1L16 5l-8.5 8.5z"/></svg> AI-augmented testing methodology across every engagement</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">How We Work</div>
      <h2>A methodology built around evidence, not templates</h2>
    </div>
    <div class="steps">
      <div class="step"><h3>Scope</h3><p>A short discovery call to understand your stack, risk appetite and compliance targets before we quote anything.</p></div>
      <div class="step"><h3>Test</h3><p>Manual, expert-led testing augmented by AI-assisted reconnaissance — never automated-scan-only reports.</p></div>
      <div class="step"><h3>Report</h3><p>Business-risk-ranked findings with reproducible proof-of-concept and remediation guidance developers can act on.</p></div>
      <div class="step"><h3>Retest</h3><p>One included retest cycle to confirm fixes hold, plus an attestation letter for your auditors or customers.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Our People</div>
      <h2>Certified practitioners, held to one standard: findings that hold up</h2>
      <p class="lead center">Our consultants pursue and hold industry-recognised certifications across offensive security, cloud, and compliance disciplines — including credentials such as OSCP, CEH, CISA, CISM, and ISO 27001 Lead Auditor — and we invest continuously in keeping the bench current as attack techniques (including AI-driven ones) evolve.</p>
    </div>
    <div class="grid grid-4">
      <div class="card center"><h3>Offensive Security</h3><p class="small">OSCP-aligned, CEH, CRTP-style tradecraft</p></div>
      <div class="card center"><h3>GRC &amp; Audit</h3><p class="small">ISO 27001 Lead Auditor, CISA</p></div>
      <div class="card center"><h3>Cloud &amp; DevSecOps</h3><p class="small">AWS/Azure security specialisations</p></div>
      <div class="card center"><h3>Leadership</h3><p class="small">CISM-aligned vCISO practitioners</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-band">
      <div class="cta-band-inner">
        <h2>Want to see how we work before you commit?</h2>
        <p class="lead center">Book a free 30-minute consultation and we'll walk through your current risk posture.</p>
        <a href="contact.html" class="btn-primary btn-lg">Talk to Us</a>
      </div>
    </div>
  </div>
</section>
"""

write("about.html", page(
    title="About CyberQunit — The Security Brand of Qunit Technologies Pvt Ltd",
    description="Learn how CyberQunit (Qunit Technologies Pvt Ltd), a Noida-based, GeM-registered security company, builds AI-augmented VAPT, compliance, and vCISO services for growing businesses.",
    canonical="about.html",
    body=about_body,
    active="about.html",
    keywords="about CyberQunit, Qunit Technologies, cyber security company Noida, GeM registered security vendor",
))

# ------------------------------------------------------------ SERVICES ----
def service_card(title, desc, href, tag=None):
    tagd = ""
    if tag == "hot":
        tagd = '<span class="tag tag-hot">Most requested</span>'
    elif tag == "ai":
        tagd = '<span class="tag tag-ai">AI-focused</span>'
    return f"""<div class="card service-card">{tagd}
        <h3>{title}</h3>
        <p>{desc}</p>
        <a href="{href}" class="card-link">View full service breakdown →</a>
      </div>"""

services_body = """
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    <div class="breadcrumb"><a href="index.html">Home</a> / Services</div>
    <div class="eyebrow">Security Audit Services</div>
    <h1>Every audit you need to prove you're secure — and stay that way</h1>
    <p class="lead">From offensive testing to governance and AI risk, CyberQunit runs six focused security practices so you don't have to coordinate five different vendors.</p>
  </div>
</section>

<section>
  <div class="wrap grid grid-3">
""" + "\n".join([
    service_card("Vulnerability Assessment &amp; Penetration Testing (VAPT)", "Web application, API, mobile, network, cloud, IoT and wireless penetration testing mapped to OWASP Top 10, OWASP API Top 10 and CERT-In empanelment-style methodology.", "vapt.html", "hot"),
    service_card("GRC &amp; Compliance Audit", "ISO/IEC 27001:2022, PCI DSS, SOC 2, GDPR, HIPAA, and India-specific frameworks (RBI, SEBI CSCRF, IRDAI) plus BCP/DRP.", "grc-compliance.html"),
    service_card("vCISO — Virtual CISO Services", "Outsourced security leadership: roadmap, execution oversight, incident readiness, and board-level reporting on demand.", "vciso.html"),
    service_card("AI &amp; LLM Security", "AI red teaming, prompt-injection testing, model risk assessments, and AI governance aligned to OWASP LLM Top 10, ISO/IEC 42001 &amp; NIST AI RMF.", "ai-security.html", "ai"),
    service_card("Cloud Security", "AWS/Azure/GCP configuration review, CSPM, container &amp; Kubernetes security, IaC review and cloud penetration testing.", "cloud-security.html"),
    service_card("OT, ICS &amp; Hardware Security", "SCADA/ICS risk assessments aligned to IEC 62443, IoT device testing, and embedded/firmware hardware security testing.", "ot-hardware-security.html"),
]) + """
    <div class="card service-card">
      <h3>Red Teaming &amp; DevSecOps</h3>
      <p>Full-scope adversary simulation, digital forensics &amp; incident response, malware analysis, phishing simulation and DevSecOps pipeline integration.</p>
      <a href="red-teaming-devsecops.html" class="card-link">View full service breakdown →</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Not Sure Where to Start?</div>
      <h2>Match your situation to the right engagement</h2>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>If your situation is…</th><th>Start with</th></tr></thead>
        <tbody>
          <tr><td>"We're shipping a new web/mobile app and need a pre-launch security check"</td><td>VAPT</td></tr>
          <tr><td>"A customer or regulator is asking for ISO 27001 / PCI DSS / SOC 2"</td><td>GRC &amp; Compliance Audit</td></tr>
          <tr><td>"We don't have security leadership and don't know what to prioritise"</td><td>vCISO</td></tr>
          <tr><td>"We're shipping AI/LLM features and don't know what could go wrong"</td><td>AI &amp; LLM Security</td></tr>
          <tr><td>"We run on AWS/Azure/GCP and want to know our real exposure"</td><td>Cloud Security</td></tr>
          <tr><td>"We run industrial/IoT/embedded systems"</td><td>OT, ICS &amp; Hardware Security</td></tr>
          <tr><td>"We want to test our people and detection, not just our code"</td><td>Red Teaming &amp; DevSecOps</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta-band">
      <div class="cta-band-inner">
        <h2>Not sure which service fits? We'll tell you honestly.</h2>
        <a href="contact.html" class="btn-primary btn-lg">Get a Free Scoping Call</a>
      </div>
    </div>
  </div>
</section>
"""

write("services.html", page(
    title="Cyber Security Audit Services — VAPT, GRC, vCISO, AI Security | CyberQunit",
    description="Explore CyberQunit's security audit services: VAPT, GRC & compliance (ISO 27001, PCI DSS, SOC 2), vCISO, AI/LLM security, cloud security, OT/hardware security, and red teaming.",
    canonical="services.html",
    body=services_body,
    active="services.html",
    keywords="security audit services, VAPT company, compliance audit India, vCISO services, AI security services, cloud security audit, OT security",
))

print("DONE home/about/services")
