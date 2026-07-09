# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_common import page, breadcrumb, cta_band, faq_section, faq_schema, WA_LINK

OUT = os.path.dirname(__file__)

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

SEMESTERS = [
    ("1st", 21, [
        ("BTCY 101", "Mathematics for Cyber Security", 4),
        ("BTCY 102", "Secure System Programming &amp; OOPS (C/C++)", 4),
        ("BTCY 103", "Secure Data Structures &amp; Algorithms for Cyber Security", 4),
        ("BTCY 104", "Introduction to IT, Web Technologies &amp; Cyber Security Essentials", 3),
        ("BS SE 101", "Fundamentals of Entrepreneurship", 2),
        ("BS SE 102", "Environment and Sustainability Studies", 2),
        ("BTCY 105", "G-PULSE I", 1),
        ("BTCY 106", "GIG Internship", 1),
    ]),
    ("2nd", 26, [
        ("BTCY 201", "Computer Architecture for Cyber Security", 4),
        ("BTCY 202", "Advanced Operating Systems — Security &amp; Hardening", 3),
        ("BTCY 203", "Python for Security", 4),
        ("BTCY 204", "Hardware Security &amp; Cyber Security Fundamentals", 3),
        ("BS SE 201", "Entrepreneurship and Innovation", 2),
        ("BTCY 205", "G-PULSE II", 1),
        ("BTCY 206", "GIG Internship", 1),
        ("BTCY 207", "Internship I", 8),
    ]),
    ("3rd", 21, [
        ("BTCY 301", "Computer Network Security &amp; Defense", 4),
        ("BTCY 302", "Ethical Hacking &amp; VAPT", 4),
        ("BTCY 303", "Endpoint Security &amp; Threat Hunting", 3),
        ("BTCY 304", "DBMS Security &amp; Forensics", 4),
        ("BS SE 301", "Entrepreneurial Strategic Approach", 2),
        ("BS SE 302", "Indian Knowledge System", 2),
        ("BTCY 305", "G-PULSE III", 1),
        ("BTCY 306", "GIG Internship", 1),
    ]),
    ("4th", 26, [
        ("BTCY 401", "IoT, OT (ICS) &amp; Physical Security Systems", 4),
        ("BTCY 402", "Digital Forensics &amp; Incident Response", 4),
        ("BTCY 403", "Network Security &amp; Traffic Analysis", 3),
        ("BTCY 404", "Cyber Crime Psychology, Investigation &amp; Forensics", 3),
        ("BS SE 401", "Entrepreneurship and Family Business", 2),
        ("BTCY 405", "G-PULSE IV", 1),
        ("BTCY 406", "GIG Internship", 1),
        ("BTCY 407", "Internship II", 8),
    ]),
    ("5th", 22, [
        ("BTCY 501", "Advanced Cryptography &amp; Secure Communication Technologies", 4),
        ("BTCY 502", "OSINT &amp; Digital Investigations", 4),
        ("BTCY 503", "Malware Analysis, Mitigation &amp; Reverse Engineering", 4),
        ("BTCY 504", "Domain Elective I", 3),
        ("BTCY 505", "Open Elective I", 3),
        ("BS SE 501", "Start-Up Operations, Marketing &amp; Growth", 2),
        ("BTCY 506", "G-PULSE V", 1),
        ("BTCY 507", "GIG Internship", 1),
    ]),
    ("6th", 27, [
        ("BTCY 601", "Identity Security &amp; Zero Trust Operations", 4),
        ("BTCY 602", "Offensive Security &amp; Red Teaming", 4),
        ("BTCY 603", "AI &amp; ML for Cyber Defense", 3),
        ("BTCY 604", "Domain Elective II", 3),
        ("BTCY 605", "Open Elective II", 3),
        ("BTCY 606", "G-PULSE VI", 1),
        ("BTCY 607", "GIG Internship", 1),
        ("BTCY 608", "Internship III", 8),
    ]),
    ("7th", 21, [
        ("BTCY 701", "APT Attribution &amp; Counter-Operations", 4),
        ("BTCY 702", "Domain Elective III", 4),
        ("BTCY 703", "Open Elective III", 3),
        ("BTCY 704", "Capstone — Innovative Cyber-Based Project", 8),
        ("BTCY 705", "G-PULSE VII", 1),
        ("BTCY 706", "GIG Internship", 1),
    ]),
    ("8th", 20, [
        ("BTCY 801", "Internship IV (Full-Time)", 20),
    ]),
]

def semester_table(label, total, rows):
    trs = "\n".join(
        f"<tr><td>{code}</td><td>{title}</td><td class='credits'>{c}</td></tr>"
        for code, title, c in rows
    )
    return f"""
    <div class="card" style="margin-bottom:20px">
      <div class="flex justify-between items-center" style="margin-bottom:10px">
        <h3 style="margin:0">Semester {label}</h3>
        <span class="pill">{total} Credits</span>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Code</th><th>Course</th><th>Credits</th></tr></thead>
          <tbody>{trs}</tbody>
        </table>
      </div>
    </div>"""

sem_html = "\n".join(semester_table(l, t, r) for l, t, r in SEMESTERS)

electives_html = """
<div class="grid grid-2">
  <div class="card">
    <h3>Domain Electives</h3>
    <p class="small text-cyan" style="margin-bottom:14px">Choose one per semester (5, 6 &amp; 7)</p>
    <p><strong>Domain Elective I (Sem 5):</strong> Cloud Security &amp; DevSecOps · Network Defense &amp; Security Operations · Systems Programming for Cyber Security · Quantum Security</p>
    <p><strong>Domain Elective II (Sem 6):</strong> Advanced Cyber Defense Operations (SIEM, SOAR &amp; IDPS) · Memory Forensics, API Security &amp; Anti-Forensics · Application Security &amp; Secure Coding · Post-Quantum Security</p>
    <p><strong>Domain Elective III (Sem 7):</strong> Automated Adversary Emulation &amp; Breach Simulation Engineering · Kernel Exploitation &amp; Rootkit Engineering · Cloud &amp; Container Security · Blockchain Security</p>
  </div>
  <div class="card">
    <h3>Open Electives</h3>
    <p class="small text-cyan" style="margin-bottom:14px">Choose one per semester (5, 6 &amp; 7)</p>
    <p><strong>Open Elective I (Sem 5):</strong> Cyber Threat Intelligence, Management &amp; Analysis · Cyber Risk Quantification &amp; Business Resilience · Mobile &amp; Wireless Security · Web3 Security</p>
    <p><strong>Open Elective II (Sem 6):</strong> Cyber Warfare Operations &amp; Strategic Defense · Cyber GRC, Law &amp; Compliance · SOC &amp; Detection Engineering · Autonomous Systems Security</p>
    <p><strong>Open Elective III (Sem 7):</strong> Security Compliance &amp; Audit Methodology · Cyber Deception &amp; Threat Intelligence Platform Engineering · Cyber Research Methodology &amp; Innovation · Space Cyber Security</p>
  </div>
</div>"""

certs_html = """
<div class="table-wrap">
  <table>
    <thead><tr><th>Semester</th><th>Aligned Industry Certification</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>CompTIA ITF+</td></tr>
      <tr><td>2</td><td>Security+</td></tr>
      <tr><td>3</td><td>Network+</td></tr>
      <tr><td>4</td><td>CEH (Certified Ethical Hacker)</td></tr>
      <tr><td>5</td><td>eJPT / PNPT</td></tr>
      <tr><td>6</td><td>CHFI / CySA+</td></tr>
      <tr><td>7</td><td>OSCP Awareness</td></tr>
      <tr><td>8</td><td>Cloud Security / CISSP (Associate)</td></tr>
    </tbody>
  </table>
</div>"""

body = """
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    """ + breadcrumb("Academic Partnership") + """
    <div class="eyebrow">Academic Partnership</div>
    <h1>CyberQunit &times; Galgotias University<br>B.Tech Cyber Security Program</h1>
    <p class="lead">CyberQunit is entering an academic partnership with Galgotias University's School of Skill Sciences &amp; Entrepreneurship to co-build and deliver its full B.Tech in Cyber Security — from faculty training and curriculum design to labs, live projects and placement-ready certification pathways.</p>
    <div class="badge-row">
      <span class="pill">184 Total Credits</span>
      <span class="pill">8 Semesters</span>
      <span class="pill">Faculty Development</span>
      <span class="pill">Industry Capstone Projects</span>
      <span class="pill">Certification-Aligned</span>
    </div>
    <div class="hero-actions">
      <a href="contact.html" class="btn-primary btn-lg">Discuss a Partnership With Us</a>
      <a href=\"""" + WA_LINK + """\" target="_blank" rel="noopener" class="btn-outline btn-lg">Chat on WhatsApp</a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="card" style="border-style:dashed;border-color:rgba(34,211,238,.35);text-align:center;padding:50px 30px">
      <div class="eyebrow center">MOU Signing</div>
      <h3 style="margin-bottom:10px">Photo &amp; signing details to be added here</h3>
      <p class="lead center" style="margin:0 auto">This block is reserved for the official CyberQunit &times; Galgotias University MOU signing photograph and date, to be published once the agreement is finalised.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">What CyberQunit Brings to the Partnership</div>
      <h2>Beyond a syllabus — an industry-run cyber security program</h2>
    </div>
    <div class="grid grid-3">
      <div class="card"><h3>Faculty Development Programs</h3><p>Hands-on training for faculty to teach offensive security, GRC and AI security with current, industry-relevant tooling.</p></div>
      <div class="card"><h3>Industry-Aligned Curriculum &amp; Labs</h3><p>Curriculum co-designed with CyberQunit's practitioners, covering VAPT, cryptography, digital forensics, AI/ML for cyber defense and more.</p></div>
      <div class="card"><h3>Guest Lectures &amp; Workshops</h3><p>Regular sessions delivered by working security consultants — not just academic theory.</p></div>
      <div class="card"><h3>GIG Internship &amp; Placement Pipeline</h3><p>Structured internship slots (GIG Internship each semester, plus four extended internships) with CyberQunit and partner organisations.</p></div>
      <div class="card"><h3>Capstone Project Mentorship</h3><p>CyberQunit consultants mentor final-year Capstone — Innovative Cyber-Based Projects through to completion.</p></div>
      <div class="card"><h3>Certification Exam Preparation</h3><p>Semester-aligned certification roadmap (CompTIA, CEH, OSCP awareness and more) built into the program.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Program Structure</div>
      <h2>B.Tech Cyber Security — 184 Credits Across 8 Semesters</h2>
      <p class="lead center">School of Skill Sciences &amp; Entrepreneurship. Full semester-wise curriculum below.</p>
    </div>
    """ + sem_html + """
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Specialisation Tracks</div>
      <h2>Domain &amp; Open Electives</h2>
    </div>
    """ + electives_html + """
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow center">Certification Roadmap</div>
      <h2>Recommended Certifications, Aligned Semester by Semester</h2>
    </div>
    """ + certs_html + """
    <p class="small center" style="margin-top:16px">*Certification alignment is advisory and reviewed periodically as industry-standard credentials evolve.</p>
  </div>
</section>
"""

faqs = [
    ("Is CyberQunit open to partnerships with other universities and colleges?", "Yes. The Galgotias University program is our flagship academic partnership, and we're actively open to similar faculty training, curriculum design, and guest lecture engagements with other institutions."),
    ("Can our institution book a single guest lecture or workshop without a full curriculum partnership?", "Yes — use the 'Book a Demo / Training' option on any page, or the contact form, and select 'Academic Partnership — Faculty/Student Training' to describe what you need."),
    ("Do students get real internship exposure, or only classroom training?", "The program is built around structured internships every semester (GIG Internship) plus four extended internships and a mentored industry capstone project in the final year."),
]

body += faq_section(faqs)
body += cta_band("Represent a university or training institute?", "Let's talk about faculty training, curriculum partnership, or a guest lecture series.")

write("academic-partnership.html", page(
    title="Academic Partnership — CyberQunit x Galgotias University B.Tech Cyber Security | CyberQunit",
    description="CyberQunit is partnering with Galgotias University to deliver its B.Tech Cyber Security program: faculty training, industry-aligned curriculum, labs, internships and a certification roadmap across 184 credits and 8 semesters.",
    canonical="academic-partnership.html",
    body=body,
    active="academic-partnership.html",
    keywords="cyber security academic partnership, Galgotias University cyber security, B.Tech Cyber Security curriculum, university MOU cyber security, faculty development program cyber security",
    schema=faq_schema(faqs),
))

print("DONE academic partnership")
