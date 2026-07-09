# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_common import page, breadcrumb, cta_band, DOMAIN

OUT = os.path.dirname(__file__)

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

POSTS = [
    dict(
        slug="blog-owasp-top-10-llm-applications.html",
        tag="AI Security",
        title="OWASP Top 10 for LLM Applications: A Practical Guide for Security Teams",
        date="July 2, 2026",
        read="7 min read",
        excerpt="If you've shipped an LLM-powered feature this year, you've inherited a new class of vulnerabilities. Here's how to think about them without the hype.",
        og="A practical walkthrough of the OWASP Top 10 for LLM Applications risk categories — prompt injection, insecure output handling, training data risks and more — and how to test for them.",
    ),
    dict(
        slug="blog-iso-27001-2022-compliance-checklist.html",
        tag="Compliance",
        title="ISO/IEC 27001:2022 Compliance Checklist for Growing Indian Businesses",
        date="June 18, 2026",
        read="6 min read",
        excerpt="ISO 27001's 2022 revision restructured Annex A into four themes. Here's what actually changes for a company starting certification today.",
        og="A practical ISO/IEC 27001:2022 readiness checklist covering the four Annex A control themes, gap assessment, and what auditors look for.",
    ),
    dict(
        slug="blog-ot-ics-security-2026.html",
        tag="OT Security",
        title="Why OT &amp; ICS Security Can't Be an Afterthought in 2026",
        date="May 27, 2026",
        read="5 min read",
        excerpt="IT and OT are converging faster than most security programs are adapting. Here's what changes when a control system, not a laptop, is the target.",
        og="Why operational technology and industrial control system security requires different methodology than IT security, and how IEC 62443 fits in.",
    ),
]

# --------------------------------------------------------- BLOG LISTING ----
cards = ""
for p in POSTS:
    cards += f"""
    <a href="{p['slug']}" class="card blog-card" style="display:block;padding:0">
      <div style="height:180px;background:linear-gradient(135deg,var(--navy-800),var(--navy-700));display:flex;align-items:center;justify-content:center">
        <span class="pill">{p['tag']}</span>
      </div>
      <div class="blog-body">
        <div class="blog-meta"><span>{p['date']}</span><span>&middot;</span><span>{p['read']}</span></div>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <span class="card-link">Read article →</span>
      </div>
    </a>"""

blog_body = f"""
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    {breadcrumb("Blog")}
    <div class="eyebrow">CyberQunit Blog</div>
    <h1>Cyber Security &amp; AI Security, Explained Without the Hype</h1>
    <p class="lead">Practical write-ups from our audit and research team — VAPT findings patterns, compliance guidance, and how AI is changing both attack and defense.</p>
  </div>
</section>
<section>
  <div class="wrap grid grid-3">{cards}</div>
</section>
""" + cta_band("Want a specific topic covered?", "Tell us what your team is struggling with and we'll consider it for a future post.")

write("blog.html", page(
    title="Cyber Security &amp; AI Security Blog | CyberQunit",
    description="Practical cyber security and AI security articles from CyberQunit: VAPT insights, compliance guidance (ISO 27001, PCI DSS), AI/LLM security, and OT security.",
    canonical="blog.html",
    body=blog_body,
    active="blog.html",
    keywords="cyber security blog, AI security blog, ISO 27001 guide, OWASP LLM Top 10, OT security blog, VAPT insights",
))

# ------------------------------------------------------------ POST PAGES ----

def post_shell(p, content_html):
    body = f"""
<section class="hero" style="padding-bottom:10px">
  <div class="wrap post-body">
    {breadcrumb(p['tag'])}
    <span class="tag-chip">{p['tag']}</span>
    <h1>{p['title']}</h1>
    <div class="blog-meta"><span>By CyberQunit Research Team</span><span>&middot;</span><span>{p['date']}</span><span>&middot;</span><span>{p['read']}</span></div>
  </div>
</section>
<section class="post-body">
  <div class="wrap">
    {content_html}
  </div>
</section>
""" + cta_band("Want us to assess this risk in your own environment?", "Book a free scoping call with our team.")
    schema = f"""<script type="application/ld+json">
{{
  "@context":"https://schema.org",
  "@type":"Article",
  "headline":"{p['title'].replace('&amp;','&')}",
  "description":"{p['og']}",
  "author":{{"@type":"Organization","name":"CyberQunit"}},
  "publisher":{{"@type":"Organization","name":"CyberQunit"}},
  "datePublished":"{p['date']}",
  "mainEntityOfPage":"{DOMAIN}/{p['slug']}"
}}
</script>"""
    return page(
        title=p['title'] + " | CyberQunit Blog",
        description=p['og'],
        canonical=p['slug'],
        body=body,
        active="blog.html",
        keywords=p['tag'],
        schema=schema,
    )

# Post 1: OWASP LLM Top 10
p1 = POSTS[0]
p1_content = """
<p>Large language model features shipped fast in the last two years — chat assistants, retrieval-augmented search, autonomous agents wired into internal tools. Most of that surface area was never threat-modeled the way a traditional web application would be before launch. The OWASP Top 10 for LLM Applications project exists to close that gap, giving security teams a shared vocabulary for a genuinely new risk category.</p>

<h2>Why traditional AppSec testing isn't enough</h2>
<p>A standard web application penetration test still matters for an LLM-powered product — the API layer, authentication, and infrastructure around the model are conventional attack surface. But the model itself introduces failure modes that don't map cleanly onto OWASP's classic Top 10 for web applications. An LLM doesn't have a SQL injection vulnerability in the traditional sense, but it can be manipulated through natural language in ways that produce equivalent business impact.</p>

<h2>Risk categories worth testing for</h2>
<ul>
  <li><strong>Prompt injection.</strong> Both direct (a user typing adversarial instructions) and indirect (malicious instructions hidden in a document, webpage, or email the model later processes) can override intended behaviour.</li>
  <li><strong>Insecure output handling.</strong> Treating model output as trusted content — rendering it directly into a browser, shell, or downstream system — can open XSS, SSRF, or command-injection-style paths.</li>
  <li><strong>Training data and retrieval risks.</strong> Poisoned training or fine-tuning data, and unauthorised retrieval from a RAG pipeline, can leak sensitive information or corrupt model behaviour.</li>
  <li><strong>Excessive agency.</strong> Agents wired to take real-world actions (send emails, hit APIs, execute code) without tight scoping can be manipulated into taking unintended actions.</li>
  <li><strong>Sensitive information disclosure.</strong> Models can be coaxed into revealing system prompts, other users' data, or details about internal architecture.</li>
  <li><strong>Supply chain risk.</strong> Third-party models, plugins, and datasets each add a dependency your security review needs to cover.</li>
</ul>

<h2>What a practical AI security test actually covers</h2>
<p>In our engagements, we test the full path: the system prompt and guardrails, how untrusted input reaches the model, how model output is consumed downstream, and what the model can access or execute. We combine adversarial prompting techniques with conventional application security testing of the surrounding infrastructure — because in almost every real incident we've reviewed, the weakness was in how the application handled the model, not the model provider's training process.</p>

<h2>Where to start</h2>
<p>If you've shipped an LLM feature without a dedicated security review, start with a scoped assessment of your highest-risk integration — usually anything with tool-calling, database access, or exposure to untrusted input (customer messages, uploaded documents, scraped web content). Architecture-level threat modeling before you build the next feature is significantly cheaper than a retrofit.</p>
"""

# Post 2: ISO 27001:2022
p2 = POSTS[1]
p2_content = """
<p>The 2022 revision of ISO/IEC 27001 restructured Annex A from 14 clauses down to four themes — Organizational, People, Physical, and Technological — and consolidated the control count to 93, with 11 new controls addressing areas like threat intelligence, cloud security, and data masking. If your last certification cycle was under the 2013 version, this isn't a cosmetic update; it changes how you organise your Statement of Applicability and your evidence trail.</p>

<h2>Where to start a gap assessment</h2>
<ul>
  <li><strong>Map your existing controls to the four themes.</strong> Organizational controls (policies, roles, supplier relationships), People controls (screening, training, remote working), Physical controls (secure areas, equipment), and Technological controls (access control, cryptography, secure development, monitoring).</li>
  <li><strong>Review the new controls specifically.</strong> Threat intelligence, cloud security posture, ICT readiness for business continuity, physical security monitoring, configuration management, information deletion, data masking, data leakage prevention, monitoring activities, web filtering, and secure coding are the additions most organisations haven't documented yet.</li>
  <li><strong>Re-validate your risk assessment methodology.</strong> Your risk treatment plan needs to reference the updated control set, not the 2013 structure.</li>
</ul>

<h2>What auditors actually check</h2>
<p>Certification bodies aren't grading your policy documents on prose quality — they're checking whether your documented controls match what's actually happening operationally, and whether you can produce evidence on request. The most common finding in first-time audits isn't a missing control; it's a control that exists on paper but has no evidence trail (access review logs, training completion records, incident tickets) behind it.</p>

<h2>A realistic timeline</h2>
<p>For an organisation with reasonable security hygiene already in place, gap assessment through to certification audit typically takes 8–16 weeks: a few weeks for gap assessment and Statement of Applicability, several weeks of control implementation and evidence collection running in parallel with day-to-day operations, then internal audit before the external certification audit. Organisations starting from close to zero should budget closer to 4–6 months.</p>

<h2>ISO 27001 alone isn't a security program</h2>
<p>Certification demonstrates a functioning information security management system — it doesn't replace penetration testing, red teaming, or a security leadership function. Many of the strongest security programs we work with run ISO 27001 compliance, VAPT, and a vCISO engagement in parallel, because each answers a different question: "are our controls documented and operating," "can our systems actually be broken into," and "who owns the decisions in between."</p>
"""

# Post 3: OT/ICS
p3 = POSTS[2]
p3_content = """
<p>Operational technology used to be air-gapped by design. Increasingly, it isn't — remote monitoring, predictive maintenance, and IT/OT integration projects have connected control systems that were never built with network-facing security in mind. The security model that protects a laptop fleet doesn't transfer cleanly to a system controlling physical machinery.</p>

<h2>Why OT security needs different methodology</h2>
<ul>
  <li><strong>Availability outranks confidentiality.</strong> In IT security, data confidentiality is often the top priority. In OT, uptime and physical safety usually come first — a control system going offline can halt production or, in critical infrastructure, create a safety incident.</li>
  <li><strong>Patching isn't simple.</strong> Many industrial systems run on legacy operating systems or proprietary firmware that can't be patched without vendor involvement, extended downtime, or recertification.</li>
  <li><strong>Live testing carries real risk.</strong> Active penetration testing techniques that are routine on IT networks can crash fragile industrial equipment. OT assessments need passive reconnaissance, controlled test-bed environments, and tightly scoped active testing windows.</li>
</ul>

<h2>What a structured OT risk assessment covers</h2>
<p>The IEC 62443 series is the most widely adopted standard for industrial automation and control systems security, and gives a useful structure: asset inventory and criticality ranking, network segmentation review (verifying IT/OT boundaries are enforced, not just diagrammed), vulnerability assessment appropriate to the environment, and a security level target versus achieved-capability gap analysis.</p>

<h2>IoT and hardware extend the same problem</h2>
<p>The same underlying issue — connected systems designed before security was a design requirement — extends to IoT devices and embedded hardware. Firmware with hardcoded credentials, unauthenticated debug interfaces, and unencrypted communication protocols are still common findings in 2026, not historical curiosities.</p>

<h2>Where organisations should start</h2>
<p>If OT and connected hardware have never had a dedicated security review, start with an asset inventory and network segmentation review before commissioning active testing. Understanding what's actually connected to what is, in our experience, the step most organisations skip — and the one that surfaces the most immediately actionable risk.</p>
"""

write(p1['slug'], post_shell(p1, p1_content))
write(p2['slug'], post_shell(p2, p2_content))
write(p3['slug'], post_shell(p3, p3_content))

print("DONE blog")
