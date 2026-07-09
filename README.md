# CyberQunit Website — Handoff Notes

A new, fully static website for **Qunit Technologies Pvt Ltd**, rebranded as **CyberQunit** for all cybersecurity-facing communication (website, social handles, marketing). 18 pages, no CMS, no database, no admin login — built specifically so it can't be hacked the way the old WordPress site was.

## What's in this folder

Open `index.html` directly in a browser to preview the whole site (all links are relative, no server required).

| Page | File |
|---|---|
| Home | `index.html` |
| About | `about.html` |
| Services hub | `services.html` |
| VAPT | `vapt.html` |
| GRC & Compliance Audit | `grc-compliance.html` |
| vCISO | `vciso.html` |
| AI & LLM Security | `ai-security.html` |
| Cloud Security | `cloud-security.html` |
| OT, ICS & Hardware Security | `ot-hardware-security.html` |
| Red Teaming & DevSecOps | `red-teaming-devsecops.html` |
| Academic Partnership (Galgotias University) | `academic-partnership.html` |
| Blog listing + 3 seed posts | `blog.html`, `blog-*.html` |
| Contact | `contact.html` |
| Privacy Policy (template — get legal review) | `privacy-policy.html` |
| 404 | `404.html` |
| SEO | `sitemap.xml`, `robots.txt` |
| Styles / scripts | `assets/css/style.css`, `assets/js/main.js` |
| Build scripts (optional, not needed to run the site) | `build_common.py`, `gen_*.py` |

The `gen_*.py` scripts are how I generated the HTML (shared header/footer/nav/WhatsApp widget from one template, so every page stays consistent). You don't need them to run the site — they're there so a developer can regenerate or extend pages later without hand-editing 18 files. Safe to delete if you just want the site itself.

## Branding decision

- **CyberQunit** — the brand name for all cybersecurity marketing: website, LinkedIn, Instagram, YouTube, X/Twitter.
- **Qunit Technologies Pvt Ltd** — stays as the legal entity name, used in the footer, privacy policy, and contracts.
- This matches naming your team had already started using internally (the old site's logo file was literally named "Final-Cyber-Qunit").
- **Recommendation:** update your social handles/display names to "CyberQunit" (keep the underlying account, just rename) rather than creating new accounts, so you don't lose existing followers/history. Current handles found on the old site: LinkedIn `/company/qunit`, X `@qunit0001`, Instagram `@_qunit_`, YouTube `@Qunit1`, Facebook page.

## Tech stack — and one honest deviation from the plan

You chose **Static HTML/CSS/JS + Tailwind**. I built pure static HTML/CSS/JS as agreed — no CMS, no server, no database, deployable anywhere. For styling, I ended up hand-writing a custom CSS file instead of using Tailwind, for two reasons: this sandbox has no network access to npm to compile Tailwind properly, and the fallback (Tailwind's Play CDN script) is explicitly not recommended for production — it ships an unpurged runtime compiler to every visitor, which hurts page speed and therefore SEO, working against your core goal. A hand-written stylesheet gets you the same "no framework bloat, fast load, fully static" outcome Tailwind was meant to deliver, with better performance. If you later want a component-based rebuild in Next.js/Tailwind proper (e.g. to add a CMS for the blog), this HTML/CSS is a clean reference to hand to a developer.

## What's still needed from you

1. **Your real logo file.** The image you shared in chat didn't come through as a file I could open — I rebuilt a close SVG recreation (shield, keyhole, cyan swoosh, "CyberQunit" wordmark) so the site isn't blank, but it's a stand-in. Send the actual logo file (SVG or high-res PNG) and I'll swap it into the header/footer in `build_common.py` → `LOGO_SVG`, or just replace it directly in each HTML file.
2. **MOU signing photo**, once finalised with Galgotias University — there's a clearly marked placeholder block on `academic-partnership.html` ("MOU Signing — Photo & signing details to be added here").
3. **Real certification list.** Per your instruction, I did *not* claim CERT-In empanelment (confirmed not applicable) and used only safe, generic language about team certifications (OSCP-aligned, CEH, CISA, ISO 27001 Lead Auditor, CISM-aligned) rather than a verified badge wall. If Qunit holds specific verifiable certs/empanelments/badges, send them and I'll replace the generic language with real, linkable badges — this is one of the highest-trust elements a security company's site can have, so it's worth doing properly.
4. **A form backend.** The contact form and "Book a Demo" modal currently submit via `mailto:`, which opens the visitor's email client — works everywhere but isn't reliable on mobile or for visitors without a configured mail client. For production I'd recommend wiring it to Formspree, Netlify Forms, or a simple serverless function so submissions land reliably in your inbox/CRM. I can do this once you tell me your hosting choice.
5. **Domain & hosting decision.** The site currently references `qunittech.com` throughout (meta tags, sitemap). Confirm whether you're keeping that domain or moving to something like `cyberqunit.com`/`cyberqunit.in`, and where you want to host (Netlify, Vercel, and cPanel/shared hosting all work — it's plain static files).

## SEO strategy behind the service pages

Each of the 6 service pages targets a distinct, high-intent keyword cluster instead of one page trying to rank for everything:

- **VAPT** — highest search volume of any offering; broken into Web, API, Mobile, Network, Cloud, IoT, Wireless as sub-topics on one authoritative page.
- **GRC & Compliance** — ISO/IEC 27001:2022, PCI DSS, SOC 2, GDPR, HIPAA, plus India-specific RBI/SEBI/IRDAI frameworks, which most competitors bundle vaguely as "compliance."
- **vCISO** — added per your request after you flagged Kratikal's vCISO page; positioned as distinct from GRC (leadership/execution vs. governance/audit) so both pages can rank independently instead of cannibalising each other.
- **AI & LLM Security** — the "AI in cybersecurity / cybersecurity in AI" theme you asked for, built around real, current frameworks (OWASP Top 10 for LLM Applications, ISO/IEC 42001, NIST AI RMF) rather than generic AI buzzwords, which should age better in search as this space standardises.
- **Cloud Security** and **OT/ICS & Hardware Security** — split apart since they attract different buyers and different search terms.

Every page has a unique title, meta description, keyword-relevant copy, FAQ content with FAQPage schema (eligible for rich results), and Service schema. The homepage and every service page carry Organization/ProfessionalService schema. `sitemap.xml` and `robots.txt` are ready to submit to Google Search Console once the site is live.

## AI theme, sitewide

Beyond the dedicated AI & LLM Security page, "AI-augmented testing" is woven into the homepage hero, About page methodology, and VAPT/Cloud page copy — positioning CyberQunit as AI-aware without overclaiming an AI product you don't have yet (you mentioned a product launch later this year; this site is written so that launch can slot in cleanly later without a rewrite).

## WhatsApp & booking

Every page has a floating WhatsApp button (bottom-right, pulsing, `+91 78279 61018`) and a "Book a Demo / Training" button that opens a modal form covering audit consultations, product demos, and academic training/lecture requests — per your request.

## Next steps I'd suggest

1. Send me the real logo file and any real certification/empanelment list — quick swap once you do.
2. Tell me your hosting/domain decision so I can wire the forms properly instead of `mailto:`.
3. Get `privacy-policy.html` reviewed by a lawyer before publishing (it's a reasonable starting template, not legal advice).
4. Once live, submit `sitemap.xml` to Google Search Console and Bing Webmaster Tools.
