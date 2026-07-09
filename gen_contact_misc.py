# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build_common import page, breadcrumb, WA_LINK, EMAIL, PHONE_DISPLAY, PHONE_TEL, ADDRESS, LEGAL, SITE

OUT = os.path.dirname(__file__)

def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)

# ------------------------------------------------------------- CONTACT ----
contact_body = f"""
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    {breadcrumb("Contact")}
    <div class="eyebrow">Contact CyberQunit</div>
    <h1>Let's scope your security engagement</h1>
    <p class="lead">Tell us about your systems and timeline. We reply within one business day with next steps — never a generic sales deck.</p>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="card">
      <h3>Request a Consultation</h3>
      <form class="contact-form" action="mailto:{EMAIL}" method="post" enctype="text/plain">
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
          <option>VAPT (Web / API / Mobile / Network / Cloud)</option>
          <option>GRC & Compliance Audit (ISO 27001 / PCI DSS / SOC 2)</option>
          <option>vCISO — Virtual CISO Services</option>
          <option>AI / LLM Security Assessment</option>
          <option>Cloud Security Review</option>
          <option>OT, ICS & Hardware Security</option>
          <option>Red Teaming & DevSecOps</option>
          <option>Academic Partnership — Faculty/Student Training</option>
          <option>Something else</option>
        </select>
        <textarea name="Message" rows="4" placeholder="A few details about your systems, timeline, or what's prompting this request"></textarea>
        <button type="submit" class="btn-primary w-full btn-lg">Send Request</button>
        <p class="form-note">This opens your email client addressed to {EMAIL}. Prefer to skip the form? <a href="{WA_LINK}" target="_blank" rel="noopener">Message us on WhatsApp →</a></p>
      </form>
    </div>
    <div>
      <div class="card" style="margin-bottom:20px">
        <h3>Head Office</h3>
        <p>{ADDRESS}</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
        <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
        <a href="{WA_LINK}" target="_blank" rel="noopener" class="btn-outline btn-sm">Chat on WhatsApp</a>
      </div>
      <div class="card">
        <h3>Prefer to book directly?</h3>
        <p>Use the <strong>Book a Demo / Training</strong> button in the bottom-right corner on any page to request a product demo, an audit scoping call, or a lecture/training session for your institution.</p>
      </div>
    </div>
  </div>
</section>
"""

write("contact.html", page(
    title="Contact CyberQunit — Request a Security Consultation",
    description="Contact CyberQunit (Qunit Technologies Pvt Ltd) in Noida, India to scope a VAPT, compliance, vCISO, AI security, or academic partnership engagement.",
    canonical="contact.html",
    body=contact_body,
    active="contact.html",
    keywords="contact CyberQunit, cyber security consultation, Qunit Technologies contact, cyber security company Noida contact",
))

# ------------------------------------------------------------ PRIVACY ----
privacy_body = f"""
<section class="hero" style="padding-bottom:20px">
  <div class="wrap">
    {breadcrumb("Privacy Policy")}
    <div class="eyebrow">Legal</div>
    <h1>Privacy Policy</h1>
    <p class="lead">Last updated: July 2026. This is a starting template — please have it reviewed by qualified legal counsel before publishing, especially if you process EU (GDPR), Indian (DPDP Act), or healthcare (HIPAA) personal data.</p>
  </div>
</section>
<section class="post-body">
  <div class="wrap">
    <h2>Information We Collect</h2>
    <p>{SITE} ("we", "us"), operated by {LEGAL}, collects information you voluntarily provide through our contact and consultation forms, including name, organisation, email address, phone number, and the details of your enquiry. We may also collect standard technical data (IP address, browser type, pages visited) through website analytics.</p>
    <h2>How We Use Information</h2>
    <p>We use the information you provide to respond to enquiries, scope and deliver security engagements, and — with your consent — to send relevant updates about our services. We do not sell personal information to third parties.</p>
    <h2>Data From Security Engagements</h2>
    <p>Any systems, code, credentials, or data shared with us during a security audit engagement is governed by a separate signed confidentiality and engagement agreement, not this website privacy policy.</p>
    <h2>Cookies &amp; Analytics</h2>
    <p>This site may use cookies or similar technologies for basic analytics and to remember your preferences. You can control cookies through your browser settings.</p>
    <h2>Your Rights</h2>
    <p>Depending on your jurisdiction, you may have rights to access, correct, or request deletion of your personal data. Contact us at {EMAIL} to exercise these rights.</p>
    <h2>Contact</h2>
    <p>Questions about this policy can be sent to {EMAIL} or {ADDRESS}.</p>
  </div>
</section>
"""

write("privacy-policy.html", page(
    title="Privacy Policy | CyberQunit",
    description="Privacy policy for CyberQunit, the cybersecurity brand of Qunit Technologies Pvt Ltd.",
    canonical="privacy-policy.html",
    body=privacy_body,
    active="",
    keywords="",
))

# ------------------------------------------------------------- 404 ----
notfound_body = """
<section class="hero center" style="padding:120px 0">
  <div class="wrap">
    <div class="eyebrow center">Error 404</div>
    <h1>This page has been patched out of existence.</h1>
    <p class="lead center">The page you're looking for doesn't exist or has moved. Let's get you back to safety.</p>
    <div class="hero-actions" style="justify-content:center">
      <a href="index.html" class="btn-primary btn-lg">Back to Home</a>
      <a href="services.html" class="btn-outline btn-lg">View Services</a>
    </div>
  </div>
</section>
"""

write("404.html", page(
    title="Page Not Found | CyberQunit",
    description="The page you're looking for doesn't exist or has moved.",
    canonical="404.html",
    body=notfound_body,
    active="",
))

print("DONE contact/privacy/404")
