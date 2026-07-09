# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_common import (page, service_schema, faq_schema, service_hero,
                           offerings_grid, process_section, faq_section,
                           related_services_section, cta_band)

OUT = os.path.dirname(__file__)

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

def build(fname, title, description, keywords, h1, eyebrow, lead, pills,
          offerings_heading, offerings, faqs, extra_sections="", schema_name=None):
    body = service_hero(eyebrow, h1, lead, pills)
    body += offerings_grid("What's Included", offerings_heading, offerings)
    body += extra_sections
    body += process_section([
        ("Scope", "A short call to align on assets, timelines and compliance targets."),
        ("Test", "Manual, expert-led testing augmented by AI-assisted analysis."),
        ("Report", "Business-risk-ranked findings with reproducible proof-of-concept."),
        ("Retest", "One included retest cycle plus an attestation letter."),
    ])
    body += faq_section(faqs)
    body += related_services_section(fname)
    body += cta_band("Ready to scope this engagement?", "Get a fixed-price quote within one business day.")
    schema = service_schema(schema_name or h1, description, fname) + "\n" + faq_schema(faqs)
    write(fname, page(title, description, fname, body, active="services.html", keywords=keywords, schema=schema))


# --------------------------------------------------------------- VAPT ----
build(
    fname="vapt.html",
    title="VAPT Services — Web, API, Mobile, Network & Cloud Penetration Testing | CyberQunit",
    description="CyberQunit's VAPT services cover web application, API, mobile, network, cloud, IoT and wireless penetration testing, mapped to OWASP and CERT-In style methodology, with a free retest included.",
    keywords="VAPT services, penetration testing company India, web application penetration testing, API security testing, mobile app VAPT, network penetration testing, cloud penetration testing, vulnerability assessment",
    eyebrow="VAPT — Vulnerability Assessment & Penetration Testing",
    h1="Web, API, Mobile, Network &amp; Cloud Penetration Testing",
    lead="Find the vulnerabilities real attackers would exploit — before they do. Our VAPT engagements combine automated coverage with deep manual exploitation across every layer of your stack.",
    pills=["Web Application", "API", "Mobile (iOS/Android)", "Network", "Cloud", "IoT", "Thick Client", "Wireless"],
    offerings_heading="Nine VAPT disciplines, one engagement team",
    offerings=[
        ("Web Application VAPT", "OWASP Top 10-aligned testing of business logic, authentication, session management and injection flaws."),
        ("API Security Testing", "REST/GraphQL API testing against the OWASP API Security Top 10 — broken auth, excessive data exposure, rate-limiting gaps."),
        ("Mobile Application VAPT", "iOS &amp; Android static and dynamic analysis: insecure storage, weak crypto, API abuse, and reverse-engineering resistance."),
        ("Network Penetration Testing", "Internal and external network testing to identify misconfigurations, lateral movement paths and exposed services."),
        ("Cloud Penetration Testing", "Exploitation-focused testing of AWS/Azure/GCP workloads beyond configuration review."),
        ("IoT &amp; Thick Client Testing", "Firmware, communication protocol and client-application testing for connected devices and desktop apps."),
        ("Wireless Security Assessment", "Wi-Fi and wireless protocol testing for rogue access points, weak encryption and client-side attacks."),
        ("Source Code Review", "Manual and semi-automated secure code review to catch what black-box testing can miss."),
        ("Threat Modeling", "Architecture-level threat modeling before you build, to design out entire vulnerability classes."),
    ],
    faqs=[
        ("What's the difference between vulnerability assessment and penetration testing?", "A vulnerability assessment identifies and lists potential weaknesses, typically via automated scanning. Penetration testing goes further — our consultants manually attempt to exploit those weaknesses to prove real business impact, exactly as an attacker would."),
        ("How long does a typical VAPT engagement take?", "Most single-application engagements run 5–10 working days for testing, plus reporting. Scope, asset count and retesting timelines are agreed upfront during scoping."),
        ("Will testing disrupt our production environment?", "We agree a testing window and rules of engagement before any testing begins, and default to staging environments where available. Production testing is scheduled and rate-limited to avoid disruption."),
        ("Do you follow OWASP and CERT-In style methodology?", "Yes — our testing methodology is aligned to OWASP Testing Guide, OWASP API Security Top 10, and the structure used in CERT-In style empanelled audits, so your report format is familiar to auditors and customers."),
        ("Do we get a certificate or attestation after remediation?", "Yes, once retesting confirms findings are resolved we issue a signed attestation letter you can share with customers, partners or auditors."),
    ],
)

# ------------------------------------------------------- GRC & COMPLIANCE ----
build(
    fname="grc-compliance.html",
    title="GRC & Compliance Audit — ISO 27001, PCI DSS, SOC 2 | CyberQunit",
    description="CyberQunit runs governance, risk and compliance audits for ISO/IEC 27001:2022, PCI DSS, SOC 2, GDPR, HIPAA, and India-specific frameworks including RBI, SEBI CSCRF and IRDAI.",
    keywords="ISO 27001 audit, PCI DSS compliance, SOC 2 readiness, GDPR compliance, HIPAA compliance, RBI cyber security framework, SEBI CSCRF, IRDAI compliance audit, GRC services India",
    eyebrow="GRC &amp; Compliance Audit",
    h1="ISO 27001, PCI DSS, SOC 2 &amp; Regulatory Compliance, Made Audit-Ready",
    lead="Governance, risk and compliance work only counts if it survives an external audit. We build the policies, controls and evidence trail your assessor actually expects to see.",
    pills=["ISO/IEC 27001:2022", "PCI DSS", "SOC 2", "GDPR", "HIPAA", "RBI", "SEBI CSCRF", "IRDAI", "BCP/DRP"],
    offerings_heading="Frameworks we take you through, end to end",
    offerings=[
        ("ISO/IEC 27001:2022 Readiness", "Gap assessment, ISMS design, Statement of Applicability, and internal audit support ahead of certification."),
        ("PCI DSS Compliance", "Scoping, control implementation and QSA-ready evidence for merchants and payment service providers."),
        ("SOC 2 Readiness (Type I &amp; II)", "Trust Services Criteria mapping and control design ahead of your SOC 2 audit."),
        ("GDPR &amp; Data Privacy", "Data mapping, lawful-basis review and privacy control implementation for organisations handling EU personal data."),
        ("HIPAA Compliance", "Administrative, physical and technical safeguard review for healthcare and healthtech platforms."),
        ("RBI Cyber Security Framework", "Control alignment for NBFCs, fintechs and payment platforms regulated by the RBI."),
        ("SEBI CSCRF Compliance", "Cyber security and cyber resilience framework alignment for SEBI-regulated entities."),
        ("IRDAI Compliance Audit", "Information and cyber security control review for insurance sector entities."),
        ("BCP / DRP Planning", "Business continuity and disaster recovery planning, tested through tabletop exercises."),
    ],
    faqs=[
        ("How long does ISO 27001 certification readiness take?", "Typically 8–16 weeks depending on organisational maturity and scope, covering gap assessment, control implementation, and internal audit before your certification body audit."),
        ("Do you issue the ISO 27001 / PCI DSS certificate yourselves?", "No — certification is issued by accredited certification bodies / QSAs. We prepare you to pass that audit and can support liaison with your chosen certifying body."),
        ("What's the difference between GRC and vCISO services?", "GRC delivers structured governance, documented controls and audit-ready evidence. vCISO provides ongoing security leadership and execution. Many clients run both in parallel — see our vCISO page for the distinction."),
        ("Can one engagement cover multiple frameworks (e.g. ISO 27001 and SOC 2)?", "Yes — many controls overlap. We map a single control set to multiple frameworks where possible to reduce duplicate effort."),
    ],
)

# ------------------------------------------------------------- vCISO ----
vciso_extra = """
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">vCISO or GRC — Which Do You Need?</div>
      <h2>Most teams confuse leadership with compliance</h2>
      <p class="lead center">A vCISO runs and executes your security program. GRC delivers structured governance, risk management and audit-ready compliance. They solve different problems — many organisations need both, run in parallel.</p>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>If you need…</th><th>Start with</th></tr></thead>
        <tbody>
          <tr><td>Someone to run and execute your security program day-to-day</td><td>vCISO</td></tr>
          <tr><td>Structured governance, risk management and audit readiness</td><td>GRC &amp; Compliance Audit</td></tr>
          <tr><td>Both leadership and provable compliance outcomes</td><td>vCISO + GRC, run in parallel</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
"""
build(
    fname="vciso.html",
    title="vCISO — Virtual CISO Services for Growing Businesses | CyberQunit",
    description="CyberQunit's vCISO service gives you on-demand security leadership — strategy, execution oversight, incident readiness and board reporting — without the cost of a full-time CISO hire.",
    keywords="vCISO services, virtual CISO, outsourced CISO India, security leadership as a service, fractional CISO",
    eyebrow="vCISO — Virtual CISO Services",
    h1="On-Demand Security Leadership, Without a Full-Time Hire",
    lead="A vCISO is the right fit when security lacks ownership and direction. Our virtual CISOs bring strategic leadership, align security with business goals, and drive real execution — not just a slide deck.",
    pills=["Security Strategy", "Execution Oversight", "Incident Readiness", "Board Reporting"],
    offerings_heading="What you get with a CyberQunit vCISO",
    offerings=[
        ("Security Strategy &amp; Roadmap", "Business-aligned security planning with clear prioritisation of initiatives and an execution-driven roadmap."),
        ("Security Posture Improvement", "Ongoing measurement and improvement of your security maturity against a defined baseline."),
        ("Execution Oversight", "Accountability for actually closing out security initiatives, not just proposing them."),
        ("Incident Readiness &amp; Response Leadership", "Incident response planning, tabletop exercises, and hands-on leadership if a real incident occurs."),
        ("Security Awareness &amp; Adoption", "Driving organisation-wide security culture, not just annual training compliance."),
        ("Cross-Functional Alignment", "Working with engineering, product and leadership so security decisions don't stall in silos."),
        ("Board &amp; Management Reporting", "Clear, non-technical reporting that helps leadership make informed risk decisions."),
    ],
    extra_sections=vciso_extra,
    faqs=[
        ("When is a vCISO the right fit?", "When there's no dedicated CISO, when security exists but lacks direction and prioritisation, when execution is stalled, or when there's no clear incident response leadership."),
        ("How much time does a vCISO commit per month?", "Engagement models range from a few hours a week to several days a month depending on your organisation's size and risk profile — agreed during scoping."),
        ("Can vCISO and GRC compliance work happen together?", "Yes, and often should. The vCISO owns strategy and execution; the GRC audit produces the documented evidence and control framework that satisfies auditors and customers."),
        ("Is a vCISO engagement a substitute for a full-time CISO forever?", "For many SMEs and mid-market companies, yes, indefinitely. For fast-scaling or highly regulated organisations, a vCISO often bridges the gap until the company is ready to hire a full-time CISO."),
    ],
)

# ------------------------------------------------------------ AI SECURITY ----
build(
    fname="ai-security.html",
    title="AI & LLM Security Testing — AI Red Teaming Services | CyberQunit",
    description="CyberQunit tests the AI you're shipping: LLM/GenAI application security, prompt-injection and jailbreak testing, AI red teaming, and AI governance aligned to OWASP LLM Top 10, ISO/IEC 42001 and NIST AI RMF.",
    keywords="AI security testing, LLM security testing, AI red teaming, prompt injection testing, GenAI security, OWASP LLM Top 10, AI governance, MLSecOps, AI risk assessment",
    eyebrow="AI &amp; LLM Security",
    h1="Security Testing for the AI Systems You're Shipping",
    lead="Every AI feature you ship is a new attack surface. We red-team your models and AI-integrated applications the same way attackers will — and help you govern AI risk before regulators ask you to.",
    pills=["LLM/GenAI Apps", "Prompt Injection", "AI Red Teaming", "RAG &amp; Vector DB", "ISO/IEC 42001", "NIST AI RMF"],
    offerings_heading="Where AI introduces risk, we test it",
    offerings=[
        ("LLM / GenAI Application Security Testing", "End-to-end testing of chatbots, copilots and AI agents built on top of foundation models, covering the OWASP Top 10 for LLM Applications."),
        ("Prompt Injection &amp; Jailbreak Testing", "Direct and indirect prompt injection, jailbreak, and guardrail-bypass testing against your production prompts and system instructions."),
        ("AI Model Red Teaming", "Adversarial testing of model behaviour, output manipulation, data leakage and unsafe content generation."),
        ("RAG Pipeline &amp; Vector Database Security", "Testing retrieval-augmented generation pipelines for data poisoning, unauthorised retrieval, and embedding-based leakage."),
        ("AI Supply Chain &amp; Training Data Risk Review", "Assessment of third-party model, plugin and dataset risk across your AI supply chain."),
        ("AI Governance &amp; Risk Assessment", "Risk assessments and control design aligned to ISO/IEC 42001 (AI management systems) and the NIST AI Risk Management Framework."),
        ("MLSecOps Integration", "Embedding security testing and monitoring into your ML/LLMOps pipeline, not bolted on after deployment."),
    ],
    faqs=[
        ("Is AI security testing different from regular application penetration testing?", "It builds on it. We still test the underlying application, APIs and infrastructure — but add AI-specific attack classes like prompt injection, model extraction, training-data leakage and unsafe output generation that traditional VAPT doesn't cover."),
        ("Do you test third-party LLM integrations (OpenAI, Anthropic, etc.) or only self-hosted models?", "Both. Most of our engagements test how your application integrates with a third-party model provider — the risk usually lives in your prompts, guardrails, and data flow, not the base model itself."),
        ("What frameworks do you align AI security work to?", "OWASP Top 10 for LLM Applications for technical testing, and ISO/IEC 42001 or the NIST AI Risk Management Framework for governance and risk assessment work, depending on your regulatory context."),
        ("We're pre-launch — can you review our AI architecture before we build?", "Yes, architecture-level AI threat modeling before development is one of the highest-leverage engagements we offer — it's far cheaper to design out a risk than to retrofit a fix."),
    ],
)

# ---------------------------------------------------------- CLOUD SECURITY ----
build(
    fname="cloud-security.html",
    title="Cloud Security Audit — AWS, Azure & GCP | CyberQunit",
    description="CyberQunit's cloud security services cover AWS, Azure and GCP configuration audits, CSPM, container and Kubernetes security, IaC review, and cloud penetration testing.",
    keywords="cloud security audit, AWS security assessment, Azure security review, GCP security, CSPM, Kubernetes security, container security, cloud penetration testing, IaC security review",
    eyebrow="Cloud Security",
    h1="Cloud Security Audits for AWS, Azure &amp; Google Cloud",
    lead="Misconfigurations, not zero-days, cause most cloud breaches. We audit your cloud environment the way an attacker would enumerate it — then help you fix what actually matters first.",
    pills=["AWS", "Azure", "GCP", "Kubernetes", "IaC", "CSPM", "IAM"],
    offerings_heading="Full-stack cloud security coverage",
    offerings=[
        ("Cloud Configuration Review (CSPM)", "Systematic review against CIS Benchmarks for AWS, Azure and GCP to catch misconfigurations before attackers do."),
        ("Cloud Penetration Testing", "Exploitation-focused testing of cloud workloads, storage, and identity boundaries — beyond a configuration checklist."),
        ("Identity &amp; Access Management Review", "IAM policy review to eliminate privilege escalation paths and over-permissioned roles."),
        ("Container &amp; Kubernetes Security", "Cluster configuration review, image scanning, and runtime security testing for containerised workloads."),
        ("Infrastructure-as-Code (IaC) Security Review", "Terraform, CloudFormation and similar templates reviewed for insecure defaults before they're deployed."),
        ("DevSecOps Pipeline Security", "Embedding security gates into CI/CD pipelines so misconfigurations are caught before production."),
        ("Cloud Compliance Mapping", "Mapping cloud controls to ISO 27001, PCI DSS, or SOC 2 requirements for cloud-hosted environments."),
    ],
    faqs=[
        ("Do you need access to our cloud console for this audit?", "Yes, for configuration review we typically request read-only IAM access. Penetration testing can be scoped separately with appropriate authorisation and cloud-provider rules of engagement."),
        ("Which cloud providers do you support?", "AWS, Microsoft Azure and Google Cloud Platform, including hybrid and multi-cloud environments."),
        ("Can this satisfy our ISO 27001 or SOC 2 cloud control requirements?", "Yes — findings and remediation evidence from a cloud security audit map directly into the technical controls required by ISO 27001, SOC 2 and PCI DSS."),
    ],
)

# --------------------------------------------------- OT / ICS / HARDWARE ----
build(
    fname="ot-hardware-security.html",
    title="OT, ICS & Hardware Security Testing | CyberQunit",
    description="CyberQunit secures operational technology, industrial control systems and connected hardware — SCADA/ICS risk assessments aligned to IEC 62443, IoT device testing, and embedded/firmware security testing.",
    keywords="OT security, ICS security, SCADA security assessment, IEC 62443, IoT security testing, hardware security testing, embedded systems security, firmware security testing",
    eyebrow="OT, ICS &amp; Hardware Security",
    h1="Securing Operational Technology, Industrial Systems &amp; Connected Hardware",
    lead="OT and hardware environments can't be patched like IT systems — and can't afford downtime for testing either. We assess industrial and embedded environments with methodology built for that reality.",
    pills=["SCADA/ICS", "IEC 62443", "IoT Devices", "Embedded Systems", "Firmware", "Physical Security"],
    offerings_heading="Purpose-built for OT, IoT and hardware environments",
    offerings=[
        ("SCADA / ICS Risk Assessment", "Risk assessment of industrial control environments aligned to the IEC 62443 series of standards."),
        ("OT Network Segmentation Review", "Verifying IT/OT network boundaries are actually enforced, not just diagrammed."),
        ("IoT Device Security Testing", "Testing connected devices across communication protocols, companion apps, and cloud back-ends."),
        ("Embedded &amp; Firmware Security Testing", "Firmware extraction, static analysis and runtime testing of embedded systems for hardcoded credentials and logic flaws."),
        ("Hardware Penetration Testing", "Physical interface testing (JTAG, UART, debug ports) and tamper-resistance assessment for connected hardware."),
        ("Physical Security &amp; Access Control Review", "Assessment of physical access controls protecting critical systems and facilities."),
    ],
    faqs=[
        ("Will testing risk downtime on live industrial systems?", "We use non-disruptive, passive assessment techniques on live OT environments by default, and only conduct active testing in a controlled test-bed or scheduled maintenance window with explicit sign-off."),
        ("Do you follow IEC 62443 for OT/ICS assessments?", "Yes, our ICS risk assessment methodology is structured around the IEC 62443 series, the widely adopted standard for industrial automation and control systems security."),
        ("Can you test a hardware product before it ships?", "Yes — pre-launch hardware and firmware security testing is one of the highest-value engagements, since post-launch hardware fixes are far more expensive."),
    ],
)

# --------------------------------------------- RED TEAMING / DEVSECOPS ----
build(
    fname="red-teaming-devsecops.html",
    title="Red Teaming, DevSecOps & Incident Response | CyberQunit",
    description="CyberQunit runs full-scope red teaming, purple teaming, DevSecOps pipeline integration, digital forensics and incident response, malware analysis, and phishing simulation.",
    keywords="red teaming services, purple team exercise, DevSecOps consulting, digital forensics and incident response, malware analysis, phishing simulation, incident response planning",
    eyebrow="Red Teaming &amp; DevSecOps",
    h1="Test Your People and Detection, Not Just Your Code",
    lead="A clean VAPT report doesn't mean you'd catch a real intrusion. Our red team and DevSecOps practice tests detection, response and your software delivery pipeline end to end.",
    pills=["Red Teaming", "Purple Teaming", "DFIR", "Malware Analysis", "Phishing Simulation", "DevSecOps"],
    offerings_heading="Offense, response, and secure delivery",
    offerings=[
        ("Red Teaming &amp; Adversary Simulation", "Full-scope, goal-oriented simulated attacks testing prevention, detection and response across people, process and technology."),
        ("Purple Teaming", "Collaborative exercises pairing our red team with your defenders to improve detection coverage in real time."),
        ("Digital Forensics &amp; Incident Response", "Rapid investigation, containment and root-cause analysis when an incident occurs."),
        ("Malware Analysis &amp; Reverse Engineering", "Static and dynamic analysis of suspicious binaries to understand behaviour and scope of compromise."),
        ("Phishing Campaign Simulation", "Realistic phishing simulations to measure and improve human-layer resilience, paired with awareness training."),
        ("DevSecOps Pipeline Integration", "Embedding SAST, DAST, SCA and secret-scanning into your CI/CD pipeline so vulnerabilities are caught pre-merge."),
        ("Incident Response Planning", "Playbook development and tabletop exercises so your team knows exactly what to do before an incident happens."),
    ],
    faqs=[
        ("How is red teaming different from a penetration test?", "Penetration testing looks for as many vulnerabilities as possible within a defined scope. Red teaming is goal-oriented and stealthy — simulating a real adversary trying to achieve a specific objective, testing detection and response along the way."),
        ("Do you announce red team exercises in advance?", "Only a small, pre-agreed group (the 'white cell') knows in advance. The rest of your security team is tested exactly as they would be during a real incident."),
        ("Can you help us respond to an active incident right now?", "Yes — contact us directly by phone or WhatsApp for time-sensitive incident response; we prioritise active-incident requests."),
    ],
)

print("DONE service deep pages")
