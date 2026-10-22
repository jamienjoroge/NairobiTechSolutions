# -*- coding: utf-8 -*-
"""All page content for the Sahara Nova website. Edit copy here, then run build.py."""

SITE = {
    "name": "Sahara Nova",
    "url": "https://saharanova.co.ke",           # live domain (no trailing slash)
    "email": "james@saharanova.co.ke",           # switch to hello@ once that mailbox exists
    "description": "Sahara Nova is a Nairobi-based digital agency building websites, custom software, SEO and AI automation for small and mid-sized businesses in Kenya, East Africa and worldwide.",
    "phone": "+254 794 122 747",                 # shown on the site; also the WhatsApp Business number
    "whatsapp": "254794122747",                  # wa.me number, digits only
    "ga4_id": "G-3BW6LDSBG4",                                # Google Analytics 4 measurement ID, e.g. "G-ABC123XYZ"; empty = no analytics, no cookie bar
    "gsc_verification": "",                      # Search Console HTML-tag code (only if not verifying by DNS)
    # Official profiles (structured data sameAs). Add the Google Business Profile, Clutch, GoodFirms links as they go live.
    "same_as": ["https://www.linkedin.com/company/saharanova/"],
}

# Founder: shown on About, credited on blog posts, and published as Person structured data.
# Add his personal LinkedIn URL to "same_as" and a photo path to "photo" when ready.
FOUNDER = {
    "name": "James Njoroge",
    "role": "Founder & Lead Engineer",
    "bio": ("James started out as an SAP-certified implementation consultant, rolling out ERP systems for businesses, "
            "then moved into designing and building AI agents for lending, CRM and ERP teams, including the "
            "loan top-up agent that took in KES 5.4M in applications in its first week. He holds a B.Tech in "
            "Communication and Computer Networks from the Technical University of Kenya and leads every Sahara Nova project."),
    "knows": ["AI agents", "Business process automation", "ERP implementation", "SAP", "Odoo", "HubSpot",
              "Web development", "Technical SEO"],
    "same_as": [],
    "photo": "",
}

ICON = {
 "web": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/></svg>',
 "code": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg>',
 "seo": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21M7.5 12l2-2 2 1.5 2.5-3"/></svg>',
 "ai": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M18.5 16l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/></svg>',
}

def service_cards():
    items = [
        ("/services/web-development/", "web", "Web design &amp; development",
         "Fast, search-ready websites and online stores that turn visitors into enquiries.",
         ["Marketing websites &amp; landing pages", "Shopify &amp; WooCommerce stores", "Web apps &amp; customer portals"]),
        ("/services/software-development/", "code", "Custom software &amp; apps",
         "MVPs, internal tools and mobile apps, scoped tightly and shipped in weekly increments.",
         ["MVP &amp; SaaS builds", "Dashboards &amp; internal tools", "iOS &amp; Android apps"]),
        ("/services/digital-marketing-seo/", "seo", "Digital marketing &amp; SEO",
         "Technical SEO, content and paid campaigns that compound into steady inbound leads.",
         ["Technical SEO audits &amp; fixes", "Content &amp; link building", "Google &amp; Meta ads"]),
        ("/services/ai-automation/", "ai", "AI &amp; automation",
         "Automate the repetitive work: lead routing, reporting, support replies, data entry.",
         ["Workflow automation (Make, Zapier, n8n)", "AI assistants &amp; chatbots", "CRM &amp; API integrations"]),
    ]
    out = ""
    for url, ic, t, d, li in items:
        lis = "".join(f"<li>{x}</li>" for x in li)
        out += (f'<a class="service" href="{{{{{url}}}}}"><span class="glyph">{ICON[ic]}</span>'
                f'<h3>{t}</h3><p>{d}</p><ul>{lis}</ul><span class="more">Learn more →</span></a>')
    return out

# ---------------------------------------------------------------------------
# AI agent case studies (client names withheld). Add real figures to "results"
# as (figure, label) pairs, e.g. ("10 min", "average top-up processing time").
# An empty results list hides the Results block for that case.
# ---------------------------------------------------------------------------
CASES = [
 dict(id="loan-top-up-agent", industry="Digital lending", tag="Financial services",
      title="AI agent for loan top-up applications",
      summary="An AI agent that takes in loan top-up applications from existing borrowers, so the lending team gets complete, structured applications instead of chasing details.",
      challenge="Top-up requests from existing borrowers arrived as conversations that staff had to follow up manually, collecting the amount, the reason and the supporting details before anyone could review the application.",
      steps=["Engages the borrower in conversation when they ask for a top-up",
             "Collects the requested amount and the details the lender needs for the application",
             "Checks the application is complete and asks follow-up questions if anything is missing",
             "Submits a structured application to the lending team for review and decision"],
      stack=["AI agent platform", "Large language model", "Lender's application workflow"],
      results=[("KES 5.4M", "in loan top-up applications taken in during the agent's first week live")]),
 dict(id="odoo-order-to-cash-agent", industry="ERP &amp; operations", tag="Odoo",
      title="Order-to-cash AI agent for an Odoo ERP client",
      summary="An AI agent that reads customer orders from email and triggers the full order-to-cash workflow in Odoo, with no manual re-keying.",
      challenge="Customer orders arrived by email in free text. Staff had to read each one, type it into the ERP and then push it through each stage of fulfilment and billing by hand.",
      steps=["Monitors the orders inbox and reads each incoming order email",
             "Extracts the customer, products and quantities, and matches them to records in Odoo",
             "Creates the sales order in Odoo",
             "Triggers the downstream business workflow: confirmation, fulfilment and invoicing through to payment"],
      stack=["Odoo ERP", "Email", "Large language model"],
      results=[]),
 dict(id="hubspot-crm-agent", industry="Sales &amp; CRM", tag="HubSpot",
      title="HubSpot CRM agent that works your pipeline",
      summary="An AI agent connected to HubSpot that carries out day-to-day CRM work: reaching out to leads, setting reminders and keeping records up to date.",
      challenge="Sales follow-up depended on people remembering to log activity, update records and chase leads, so the CRM went out of date and leads went cold.",
      steps=["Connects to HubSpot and works across contacts, companies and deals",
             "Reaches out to leads and follows up on schedule",
             "Creates reminders and follow-up tasks for the team",
             "Logs activity and keeps records and deal stages up to date, using the actions HubSpot makes available"],
      stack=["HubSpot CRM", "Email", "Large language model"],
      results=[]),
 dict(id="support-and-lead-intake-agents", industry="Customer experience", tag="Support &amp; sales",
      title="Customer-facing agents for support and lead intake",
      summary="AI agents that answer customer questions and capture new enquiries around the clock, handing over to a person when needed.",
      challenge="Customer questions and new enquiries arrived at all hours. Slow replies frustrated customers and let prospective clients drift to competitors.",
      steps=["Answers common customer questions from the business's own information",
             "Captures and qualifies new leads with a short conversation",
             "Passes lead details to the sales team",
             "Hands complex or sensitive conversations to a human"],
      stack=["Large language model", "Website chat", "CRM"],
      results=[]),
]

FLOWS = {"loan-top-up-agent": [["Borrower request", "An existing borrower asks for a top-up in conversation."], ["AI agent", "The agent handles the conversation and collects the amount and the details the lender needs."], ["Completeness check", "Anything missing triggers a follow-up question until the application is complete."], ["Structured application", "A clean, structured application is created, ready for review."], ["Lending team", "Officers review and decide, with no details left to chase."]], "odoo-order-to-cash-agent": [["Email order", "A customer emails an order in free text."], ["AI agent", "The agent reads the email and extracts the customer, products and quantities."], ["Odoo sales order", "A sales order is created in Odoo and matched to existing records."], ["Fulfilment", "Fulfilment is triggered through Odoo's business workflow."], ["Invoice", "The invoice is raised as the order moves through the workflow."], ["Payment", "The order is tracked through to cash received."]], "hubspot-crm-agent": [["New lead", "A lead or contact arrives in HubSpot."], ["AI agent", "The agent reviews the record and decides the next action."], ["Outreach", "It reaches out to the lead and follows up on schedule."], ["Reminders & tasks", "It creates reminders and follow-up tasks for the team."], ["CRM updated", "Activity is logged and deal stages are kept current."]], "support-and-lead-intake-agents": [["Customer message", "A customer or prospect starts a conversation."], ["AI agent", "The agent answers from the business's own information."], ["Lead captured", "New enquiries are qualified with a few short questions."], ["Sales team", "Lead details are passed straight to the team."], ["Human handoff", "Complex or sensitive conversations go to a person."]]}

import html as _h, json as _j, re as _re
def flow_fig(cid, title=None):
    st = FLOWS[cid]
    label = "Animated diagram: " + " → ".join(s[0] for s in st)
    data = _h.escape(_j.dumps(st, ensure_ascii=False), quote=True)
    return (f'<figure class="flow-viz" data-steps="{data}" data-agent="1">'
            f'<canvas role="img" aria-label="{_h.escape(label, quote=True)}"></canvas>'
            f'<figcaption class="flow-caption"><b>Step 1 · {st[0][0]}</b> {st[0][1]}</figcaption></figure>')

def fig_html(f):
    m = _re.match(r"KES ([\d.]+)M$", f)
    if m:
        return f'<span class="fig" data-count="{m.group(1)}" data-prefix="KES " data-suffix="M" data-dec="1">{f}</span>'
    return f'<span class="fig">{f}</span>'

def case_full(c):
    steps = "".join(f"<li>{s}</li>" for s in c["steps"])
    stack = "".join(f'<li>{s}</li>' for s in c["stack"])
    res = ""
    if c["results"]:
        res = '<div class="case-results">' + "".join(
            f'<div class="edge">{fig_html(f)}<p>{l}</p></div>' for f, l in c["results"]) + "</div>"
    return (f'<article class="case" id="{c["id"]}"><div class="case-meta"><span class="chip">{c["tag"]}</span>'
            f'<span class="label">{c["industry"]}</span></div>'
            f'<h2>{c["title"]}</h2><p class="lede">{c["summary"]}</p>{res}{flow_fig(c["id"])}'
            f'<div class="case-body"><div><h3>The challenge</h3><p>{c["challenge"]}</p>'
            f'<h3 style="margin-top:22px">Connected to</h3><ul class="chips">{stack}</ul></div>'
            f'<div><h3>What the agent does</h3><ol class="flow">{steps}</ol></div></div></article>')

def case_cards():
    return '<div class="grid g4">' + "".join(
        f'<a class="service" href="{{{{/work/#{c["id"]}}}}}"><span class="chip" style="align-self:flex-start">{c["tag"]}</span>'
        f'<h3>{c["title"]}</h3><p>{c["summary"]}</p>'
        + (f'<p class="card-fig"><b data-count="5.4" data-prefix="KES " data-suffix="M" data-dec="1">{c["results"][0][0]}</b> {c["results"][0][1]}</p>' if c["results"] and c["results"][0][0].startswith("KES ") else (f'<p class="card-fig"><b>{c["results"][0][0]}</b> {c["results"][0][1]}</p>' if c["results"] else ""))
        + '<span class="more">Read the case study →</span></a>'
        for c in CASES) + "</div>"

def cases_band(label, heading, alt=True):
    return (f'<section class="band{" alt" if alt else ""}"><div class="wrap"><div class="sec-head"><p class="label">{label}</p>'
            f'<h2>{heading}</h2></div>' + case_cards() +
            '<div class="btn-row"><a class="btn ghost" href="{{/work/}}">See all our work</a></div></div></section>')

WORK_BODY = ('<section class="band"><div class="wrap"><div class="cases">' + "".join(case_full(c) for c in CASES) +
             '</div><p class="meta" style="margin-top:28px">These agents were designed and built by our founding team for earlier clients. Client names and identifying details are withheld. Want an agent like these? See our <a href="{{/services/ai-automation/}}">AI &amp; automation services</a> or <a href="{{/contact/}}">tell us about your process</a>.</p></div></section>')

HOME_HERO = """<header class="hero">
<svg class="stars" viewBox="0 0 1200 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<g fill="#F4F1EA"><circle cx="820" cy="60" r="1.4"/><circle cx="1010" cy="130" r="1"/><circle cx="930" cy="250" r="1.2"/><circle cx="1120" cy="70" r="1.6"/><circle cx="700" cy="140" r="1"/><circle cx="1080" cy="300" r="1"/><circle cx="760" cy="330" r="1.3"/><circle cx="640" cy="40" r="1"/><circle cx="1160" cy="210" r="1.1"/></g>
</svg>
<div class="wrap">
<p class="label">Digital agency · Nairobi · East Africa &amp; worldwide</p>
<h1 style="margin-top:18px">The Nairobi digital agency that <em>works your hours.</em></h1>
<p class="lede">Sahara Nova designs, builds and grows websites, custom software, SEO and AI automation for small and mid-sized businesses in Kenya, East Africa and around the world. You get senior work and fast turnaround, at a fraction of onshore agency rates.</p>
<div class="btn-row"><a class="btn" href="{{/contact/}}">Get a fixed quote</a><a class="btn ghost" href="{{/services/}}">See what we do</a></div>
<div class="clock" role="group" aria-label="Current local times">
<div class="home"><b data-tz="Africa/Nairobi">--:--</b><span>Nairobi · us</span></div>
<div><b data-tz="Europe/London">--:--</b><span>London</span></div>
<div><b data-tz="Europe/Berlin">--:--</b><span>Berlin</span></div>
<div><b data-tz="Asia/Dubai">--:--</b><span>Dubai</span></div>
<div><b data-tz="America/New_York">--:--</b><span>New York</span></div>
</div>
<p class="clock-note">Our 08:00–18:00 EAT day overlaps 6–8 hours with the UK and Europe, and covers US East Coast mornings.</p>
</div>
<svg class="dune" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60 C 240 10, 420 10, 640 45 S 1100 95, 1440 30 L1440 90 L0 90 Z" style="fill:var(--bg)"/></svg>
</header>"""

HOME_BODY = """<section class="band" style="padding-top:24px"><div class="wrap">
<div class="sec-head"><p class="label">What we do</p><h2>One accountable team for everything digital</h2>
<p class="lede">Most small businesses juggle a web designer, a freelance developer and an SEO contractor who never talk to each other. We put all four disciplines under one roof, one project manager and one invoice.</p></div>
<div class="grid g4">""" + service_cards() + """</div>
</div></section>

""" + cases_band("Our team's work", "AI agents our team has built for real businesses") + """
<section class="band"><div class="wrap">
<div class="sec-head"><p class="label">Why Sahara Nova</p><h2>Onshore-quality work without the onshore price tag</h2></div>
<div class="grid g4">
<div class="edge"><span class="fig">40–60%</span><h3>Lower cost</h3><p>Kenyan agency rates sit well below UK, EU and US agencies. We pass that saving on and keep a senior team on your project.</p></div>
<div class="edge"><span class="fig">UTC+3</span><h3>Your working day</h3><p>East Africa Time overlaps most of the European day. Calls happen live, and feedback gets same-day answers.</p></div>
<div class="edge"><span class="fig">2 days</span><h3>Fast quotes, faster sprints</h3><p>A written proposal within two working days. Weekly demos after that, so you always see progress.</p></div>
<div class="edge"><span class="fig">1 team</span><h3>Four disciplines</h3><p>Design, engineering, SEO and automation in one team, so your website, software and marketing work together.</p></div>
</div>
<div class="btn-row"><a class="btn ghost" href="{{/why-kenya/}}">Why hire a team in Kenya</a><a class="btn ghost" href="{{/about/#how-we-work}}">How we work</a></div>
</div></section>


<section class="band"><div class="wrap">
<div class="grid g2" style="align-items:start;gap:48px">
<div class="sec-head" style="margin:0"><p class="label">Kenya &amp; East Africa</p><h2>Built for East African business, too</h2>
<p class="lede">Our home market has its own needs: M-Pesa checkouts, WhatsApp-first customers, patchy mobile data and Android phones on 3G. We design for all of it, and we can meet you in person in Nairobi.</p>
<div class="btn-row"><a class="btn" href="{{/east-africa/}}">Work with us in East Africa</a></div></div>
<div class="grid g2" style="gap:16px">
<div class="edge"><h3>M-Pesa &amp; mobile money</h3><p>STK Push checkouts, Paybill and Till reconciliation, plus Airtel Money and MTN MoMo.</p></div>
<div class="edge"><h3>WhatsApp-first</h3><p>WhatsApp Business ordering, support bots and automated follow-ups.</p></div>
<div class="edge"><h3>Light, fast sites</h3><p>Pages built to load on budget Android phones and slow connections.</p></div>
<div class="edge"><h3>Local search</h3><p>Google Business Profile and "near me" SEO for Nairobi, Kampala, Dar and Kigali.</p></div>
</div>
</div>
</div></section>
"""

HOME_FAQ = [
 ("What does Sahara Nova do?", "We are a Nairobi-based digital agency. We design and build websites, custom software and mobile apps, run SEO and digital marketing, and automate business workflows with AI for small and mid-sized businesses worldwide."),
 ("Where do you work?", "We work with businesses in Kenya and across East Africa, where we can meet in person, and remotely with businesses anywhere in the world, including the UK, Europe, the Middle East and North America. We invoice in USD, GBP or EUR and work on a schedule that overlaps with yours."),
 ("How much does a website cost?", "Our Website Launch package starts from $1,500 for up to six pages with on-page SEO. Larger sites, e-commerce and web apps are quoted at a fixed price after a short discovery call. See our <a href=\"{{/pricing/}}\">pricing page</a>."),
 ("How do we communicate?", "You get a named project lead, a shared Slack or Teams channel, a weekly video call and a demo link every week. Most of our day overlaps with UK and European business hours."),
 ("Who owns the code and content?", "You do. Full ownership of code, designs and content transfers to you on final payment. We sign NDAs and data processing agreements on request."),
]

SERVICES_BODY = """<section class="band"><div class="wrap">
<div class="sec-head"><p class="label">Our services</p><h2>Four disciplines, one team</h2></div>
<div class="grid g2">""" + service_cards() + """</div>
</div></section>
<section class="band alt"><div class="wrap">
<div class="sec-head"><p class="label">How the services connect</p><h2>Built to work together</h2>
<p class="lede">A new website ships with SEO already in place. A web app includes the automations that feed your CRM. Marketing reports come from data we set up correctly at launch. Hiring one team for all of it means nothing gets lost in the handoffs.</p></div>
<div class="table-wrap"><table><thead><tr><th>If you need…</th><th>Start with</th><th>Often paired with</th></tr></thead><tbody>
<tr><td>More enquiries from Google</td><td><a href="{{/services/digital-marketing-seo/}}">SEO Foundation</a></td><td>Website rebuild, content retainer</td></tr>
<tr><td>A new or better website</td><td><a href="{{/services/web-development/}}">Website Launch</a></td><td>SEO retainer, care plan</td></tr>
<tr><td>Software that doesn't exist yet</td><td><a href="{{/services/software-development/}}">MVP build</a></td><td>Automation, dedicated team</td></tr>
<tr><td>Fewer hours lost to admin</td><td><a href="{{/services/ai-automation/}}">Automation Sprint</a></td><td>CRM integration, AI assistant</td></tr>
</tbody></table></div>
</div></section>"""

def service_page(path, crumb, title, desc, eyebrow, h1, lede, svc, sections, faq):
    return dict(path=path, title=title, description=desc, eyebrow=eyebrow, h1=h1, lede=lede,
                crumbs=[("/services/", "Services"), ("/" + path, crumb)], service=svc,
                body=sections, faq=faq)

def deliverables(items):
    return '<div class="grid g3">' + "".join(
        f'<div class="edge"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + "</div>"

WEB = service_page(
 "services/web-development/", "Web design & development",
 "Web Design & Development for Small Businesses | Sahara Nova",
 "Custom website design and development for small businesses: fast, SEO-ready sites, Shopify and WooCommerce stores and web apps. Fixed prices from $1,500.",
 "Service · Web design &amp; development",
 "Web design and development for small businesses",
 "Fast, search-ready websites and online stores that bring in enquiries, built by a senior team in Nairobi at a fixed price.",
 {"name": "Web design and development", "type": "Website design and development", "from": "1500"},
 """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">A website should bring in customers</h2>
<p>For most small businesses, the website is the best salesperson they have. Too many sites are slow, hard to update and invisible on Google. We build sites that load in under two seconds, rank for the searches your customers make, and make it obvious what to do next.</p>
<p>When you outsource web development to Sahara Nova you get a designer, a developer and an SEO specialist working as one team. Keyword research shapes the sitemap, the sitemap shapes the design, and the site launches ready to rank.</p>
<h3>What we build</h3>
<ul>
<li><strong>Marketing websites</strong> for service businesses, consultancies and B2B companies</li>
<li><strong>E-commerce stores</strong> on Shopify or WooCommerce, with payments, shipping and product SEO</li>
<li><strong>Landing pages</strong> for campaigns, built to convert and tested with analytics</li>
<li><strong>Web apps and portals</strong>: booking systems, client dashboards, membership sites</li>
<li><strong>Redesigns and migrations</strong> that keep your existing Google rankings through proper redirects</li>
</ul>
<h3>Built for your market</h3>
<p>Selling in Kenya or East Africa? We build M-Pesa checkouts and WhatsApp ordering into your site. See <a href="{{/east-africa/}}">web design for East African businesses</a> and our <a href="{{/blog/mpesa-stk-push-integration-guide/}}">M-Pesa STK Push guide</a>. Want your site to answer questions and capture leads around the clock? See the <a href="{{/work/#support-and-lead-intake-agents}}">support and lead-intake agents</a> we've built.</p>
<h3>Technology</h3>
<p>We choose the stack that fits your team, not our favourite. That might be WordPress if you want to edit content yourself, Shopify for commerce, Webflow for marketing teams, or custom Next.js and static builds when speed and flexibility matter most.</p>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">Most popular</span><h3>Website Launch</h3><div class="price">$1,500 <small>from, fixed price</small></div>
<ul><li>Up to 6 pages, custom design</li><li>Mobile-first, Core Web Vitals optimised</li><li>On-page SEO, schema &amp; sitemap</li><li>Analytics &amp; Search Console setup</li><li>Live in 2–3 weeks</li></ul><a class="btn" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>Growth Website</h3><div class="price">$3,500 <small>from</small></div><ul><li>Up to 15 pages + blog/CMS</li><li>Conversion tracking &amp; CRM forms</li><li>Keyword map &amp; 3 launch articles</li></ul></div>
<div class="plan"><h3>E-commerce</h3><div class="price">$4,500 <small>from</small></div><ul><li>Shopify or WooCommerce</li><li>Up to 50 products loaded</li><li>Payments, shipping, product schema</li></ul></div>
</div>
</div></div></section>
<section class="band alt"><div class="wrap"><div class="sec-head"><p class="label">Included in every build</p><h2>The details that make a site rank and convert</h2></div>""" +
 deliverables([("Speed", "Optimised images, minimal scripts and good hosting, aiming for green Core Web Vitals on mobile."),
               ("Search foundations", "Clean URLs, unique titles and meta descriptions, schema markup, XML sitemap and internal linking."),
               ("Accessibility", "Semantic HTML, keyboard navigation and colour contrast checked against WCAG 2.2 AA."),
               ("Measurement", "GA4 or Plausible, Search Console and conversion events on every form and button that matters."),
               ("Security", "HTTPS, security headers, spam-protected forms and automatic backups."),
               ("Handover", "Training video, admin access and full ownership of code and content.")]) +
 "</div></section>",
 [("How long does it take to build a small business website?", "A Website Launch project usually goes live in 2–3 weeks. A Growth Website takes 4–6 weeks and e-commerce 4–8 weeks, depending on content and product count."),
  ("Can you redesign my website without losing Google rankings?", "Yes. We crawl your current site, map every URL to its new equivalent, set up 301 redirects and monitor Search Console after launch to protect your rankings."),
  ("Will I be able to edit the website myself?", "Yes. If you want to edit content yourself we build on a CMS such as WordPress, Webflow or Shopify, and we include a short training video."),
  ("Do you write the content?", "We can. Our SEO team writes page copy based on keyword research, or we can polish content you supply.")])

SOFT = service_page(
 "services/software-development/", "Custom software & apps",
 "Custom Software Development for Small Businesses | Sahara Nova",
 "Custom software, MVP and mobile app development for small businesses. A senior offshore team in Nairobi, weekly sprints, your hours. From $8,000.",
 "Service · Custom software &amp; apps",
 "Custom software development for small businesses",
 "MVPs, internal tools and mobile apps, scoped tightly, built in weekly sprints and handed over with clean, documented code.",
 {"name": "Custom software and app development", "type": "Software development", "from": "8000"},
 """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Software that fits how your business works</h2>
<p>Off-the-shelf tools only take you so far. Eventually you need a customer portal, an internal dashboard, or a product of your own. We help small and mid-sized businesses build that software without a full in-house engineering team.</p>
<h3>What we build</h3>
<ul>
<li><strong>MVPs and SaaS products:</strong> from idea to paying users in 6–10 weeks</li>
<li><strong>Internal tools:</strong> dashboards, admin panels, quoting and inventory systems</li>
<li><strong>Customer portals:</strong> bookings, accounts, document sharing, payments</li>
<li><strong>Mobile apps:</strong> cross-platform iOS and Android with React Native or Flutter</li>
<li><strong>Integrations:</strong> connecting your CRM, accounting, payments and data sources through APIs</li>
</ul>
<h3>How we work</h3>
<p>Every project starts with a paid discovery week. We map the users, the core workflows and the smallest version worth shipping. After that we build in one-week sprints, and you get a working demo link every Friday. You can change priorities between sprints without renegotiating the whole contract.</p>
<h3>Recent work</h3>
<p>We've built an <a href="{{/work/#odoo-order-to-cash-agent}}">order-to-cash agent for an Odoo ERP client</a> and a <a href="{{/work/#loan-top-up-agent}}">loan top-up agent for a digital lender</a>. If you're weighing up an offshore team, read <a href="{{/why-kenya/}}">why companies hire developers in Kenya</a>.</p>
<h3>Typical stack</h3>
<p>TypeScript, React and Next.js, Node.js, Python, PostgreSQL, React Native and Flutter, hosted on AWS, Google Cloud, Vercel or your own infrastructure.</p>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">Start here</span><h3>MVP / Web App</h3><div class="price">$8,000 <small>from</small></div>
<ul><li>1-week discovery &amp; clickable prototype</li><li>Design + build of core features</li><li>Weekly demos, fixed milestones</li><li>Deployment, docs &amp; handover</li></ul><a class="btn" href="{{/contact/}}">Scope my project</a></div>
<div class="plan"><h3>Dedicated Developer</h3><div class="price">$3,200 <small>/mo per developer, from</small></div><ul><li>Full-time engineer on your hours</li><li>Managed by our tech lead</li><li>Scale up or down monthly</li></ul></div>
</div>
</div></div></section>""",
 [("How much does it cost to build an MVP?", "Most MVPs we scope fall between $8,000 and $30,000, depending on the number of user roles, integrations and platforms. A discovery week gives you a fixed, itemised quote."),
  ("Fixed price or hourly?", "Discovery and well-defined projects are fixed price. Ongoing product work runs as a monthly dedicated team, so you can change priorities freely."),
  ("Is outsourcing software development to Kenya safe?", "We sign NDAs and IP assignment clauses, use your repositories or give you access to ours from day one, and follow GDPR-aligned data practices. You own all the code."),
  ("Can you take over an existing codebase?", "Yes. We start with a code audit covering architecture, security and test coverage, then propose a plan to stabilise it and keep building.")])

SEO = service_page(
 "services/digital-marketing-seo/", "Digital marketing & SEO",
 "SEO Services for Small Businesses | Sahara Nova",
 "Affordable SEO services for small businesses: technical SEO audits, keyword strategy, content and link building, plus Google Ads. SEO Foundation from $900.",
 "Service · Digital marketing &amp; SEO",
 "SEO services for small businesses",
 "Technical SEO, content and paid campaigns that compound into a steady flow of inbound leads, reported in plain English every month.",
 {"name": "SEO and digital marketing", "type": "Search engine optimisation", "from": "900"},
 """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Be found by customers who are already searching</h2>
<p>SEO is the marketing channel that keeps paying after you stop spending. We fix the technical problems that hold your site back, target the keywords your buyers search for, and publish content that earns rankings and links.</p>
<h3>Our SEO process</h3>
<ol>
<li><strong>Technical audit:</strong> crawlability, indexing, Core Web Vitals, schema, duplicate content and redirects</li>
<li><strong>Keyword map:</strong> every important page gets one primary search intent and a clear job</li>
<li><strong>On-page optimisation:</strong> titles, headings, internal links and content improvements</li>
<li><strong>Content:</strong> articles built around topic clusters that support your service pages</li>
<li><strong>Authority:</strong> digital PR, directory citations and relevant, earned backlinks</li>
<li><strong>Reporting:</strong> rankings, traffic and, most importantly, leads, every month</li>
</ol>
<h3>SEO built into every website</h3>
<p>Every site we build ships with the technical foundations already in place. See our <a href="{{/services/web-development/}}">web design and development</a> service, or compare packages on the <a href="{{/pricing/}}">pricing page</a>.</p>
<h3>Paid media</h3>
<p>SEO takes months to compound. When you need leads sooner, we run Google Ads and Meta campaigns with proper conversion tracking, so every dollar can be traced to an enquiry.</p>
<div class="callout"><p><strong>Honest timelines:</strong> long-tail rankings typically appear in 3–6 months and competitive terms take 9–18 months. Anyone promising page one in a few weeks is guessing.</p></div>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">One-off</span><h3>SEO Foundation</h3><div class="price">$900 <small>from</small></div>
<ul><li>Full technical audit + fixes</li><li>Keyword research &amp; page map</li><li>Google Business Profile &amp; Search Console</li><li>Prioritised 90-day roadmap</li></ul><a class="btn" href="{{/contact/}}">Book an audit</a></div>
<div class="plan"><h3>SEO &amp; Content Retainer</h3><div class="price">$750 <small>/month, from</small></div><ul><li>2–4 optimised articles a month</li><li>On-page improvements &amp; link building</li><li>Monthly report and strategy call</li></ul></div>
</div>
</div></div></section>""",
 [("How long does SEO take to work?", "Expect early movement on long-tail keywords within 3–6 months and competitive terms in 9–18 months. Technical fixes can show results sooner if your site had indexing problems."),
  ("Do you guarantee first-page rankings?", "No. Nobody controls Google's rankings. We commit to the work, the process and transparent reporting on rankings, traffic and leads."),
  ("Do you offer white-label SEO for agencies?", "Yes. We deliver audits, content and technical fixes under your brand, with your client reporting templates."),
  ("What's included in a monthly SEO report?", "Organic traffic, keyword rankings, Search Console impressions and clicks, conversions from organic search, work completed and next month's priorities.")])

AI = service_page(
 "services/ai-automation/", "AI & automation",
 "AI Automation Agency for Small Businesses | Sahara Nova",
 "AI agents and workflow automation for small businesses: order-to-cash in Odoo, HubSpot CRM agents, support bots and lead intake. From $1,200.",
 "Service · AI &amp; automation",
 "AI automation for small businesses",
 "Give your team back the hours lost to copy-pasting, chasing and reporting. We automate the repetitive work and add AI where it pays for itself.",
 {"name": "AI and business process automation", "type": "Business process automation", "from": "1200"},
 """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Automate the busywork, not the judgement</h2>
<p>Most small businesses lose hours every week to manual tasks: moving leads from forms into a CRM, building the same weekly report, answering the same customer questions. We find those tasks, measure them and automate the ones with a clear payback.</p>
<h3>Common automations we build</h3>
<ul>
<li><strong>Lead handling:</strong> form → CRM → instant personalised reply → sales alert</li>
<li><strong>Reporting:</strong> weekly dashboards assembled automatically from ads, CRM and accounting</li>
<li><strong>Customer support:</strong> AI assistants trained on your own documents, with human handoff</li>
<li><strong>Document processing:</strong> invoices, receipts and forms read and filed by AI</li>
<li><strong>Operations:</strong> onboarding checklists, reminders, approvals and data syncs between tools</li>
<li><strong>AI agents:</strong> agents that take actions in your systems, like processing orders in your ERP or working leads in your CRM. See <a href="{{/work/}}">our case studies</a></li>
</ul>
<h3>Tools</h3>
<p>We connect AI agents to the systems you already run, including Odoo ERP, HubSpot CRM, email and your website chat. We use Make, Zapier and n8n for fast, maintainable workflows, and write custom code with leading AI model APIs when a no-code tool isn't enough. Every automation ships with documentation and error alerts, so nothing fails silently.</p>
<h3>Responsible AI</h3>
<p>We keep a human in the loop for anything customer-facing, minimise the personal data sent to AI services, and document which models and vendors process your data.</p>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">Quick win</span><h3>Automation Sprint</h3><div class="price">$1,200 <small>from</small></div>
<ul><li>Process audit of one team</li><li>1–3 workflows automated</li><li>Error alerts &amp; documentation</li><li>Delivered in about 2 weeks</li></ul><a class="btn" href="{{/contact/}}">Find my quick wins</a></div>
<div class="plan"><h3>AI Assistant</h3><div class="price">$2,500 <small>from</small></div><ul><li>Website or internal assistant</li><li>Trained on your documents</li><li>Human handoff &amp; analytics</li></ul></div>
</div>
</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><p class="label">Watch an agent work</p><h2>From an emailed order to cash in the bank</h2>
<p class="lede">This is the order-to-cash agent we built for an Odoo ERP client. Each step used to be done by hand. Hover over or tap a step to see what the agent does.</p></div>""" + flow_fig("odoo-order-to-cash-agent") + """
<div class="btn-row"><a class="btn ghost" href="{{/work/#odoo-order-to-cash-agent}}">Read the case study</a></div></div></section>""" + cases_band("Our team's work", "AI agents our team has built"),
 [("What can a small business automate?", "Good candidates are frequent, rule-based and digital: lead routing, follow-up emails, invoicing reminders, reporting, data entry between tools and first-line support questions."),
  ("Do I need to change my existing software?", "Usually not. We connect the tools you already use, such as Odoo, HubSpot, Pipedrive, Xero, QuickBooks, Google Workspace, Microsoft 365 or Shopify, through their APIs."),
  ("Can you build AI agents for Odoo or HubSpot?", "Yes. We have built an order-to-cash agent that turns emailed orders into Odoo sales orders and runs the workflow through to invoicing, and a HubSpot agent that follows up with leads, sets reminders and keeps the CRM up to date. See our <a href=\"{{/work/}}\">case studies</a>."),
  ("Is our data safe with AI tools?", "We choose business-tier AI services that don't train on your data, minimise what's sent, and document every data flow. We sign a data processing agreement on request."),
  ("How do you measure ROI?", "Before building, we estimate hours saved per month. After launch, we track runs and time saved so you can see the payback.")])

WHY_KENYA_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Africa's tech hub, in Europe's working day</h2>
<p>Nairobi, nicknamed the "Silicon Savannah", is home to a large and growing community of software engineers, designers and digital marketers. M-Pesa, the mobile money platform that changed payments in Kenya, was built and scaled here, and the city's fintech, e-commerce and startup scene keeps producing experienced tech talent.</p>
<h3>1. Time zone overlap</h3>
<p>Kenya runs on East Africa Time (UTC+3) all year, with no daylight saving. That gives you 6–8 hours of live overlap with the UK and Europe, a same-day working rhythm with the Gulf, and morning calls with the US East Coast. Compared with outsourcing to Asia, questions get answered the same day instead of overnight.</p>
<h3>2. English-first communication</h3>
<p>English is an official language of Kenya and the language of business, university and government, so briefs, calls and documentation need no translation.</p>
<h3>3. Cost</h3>
<p>Kenyan agency rates generally range from under $25 to $99 an hour, compared with $50–$199 in Western Europe and up to $300 in major US cities. Many businesses save 40–60% against onshore agencies while working with senior people.</p>
<h3>4. Legal and commercial familiarity</h3>
<p>Kenya's legal system is based on English common law, and its Data Protection Act 2019 closely follows GDPR principles. Contracts, NDAs and data processing agreements will look familiar to UK and EU businesses.</p>
<h3>What does it cost?</h3>
<p>For project-level prices and a comparison with other outsourcing regions, read our guide to <a href="{{/blog/outsourcing-web-development-to-kenya/}}">the cost of outsourcing web development to Kenya</a>, or see <a href="{{/pricing/}}">our published prices</a>. You can also <a href="{{/about/}}">meet the team behind Sahara Nova</a>.</p>
<h3>How to choose a Kenyan agency</h3>
<ul>
<li>Ask to meet the people who will actually do the work.</li>
<li>Insist on weekly demos and access to the code repository from day one.</li>
<li>Check reviews on independent platforms such as Clutch and GoodFirms.</li>
<li>Agree on communication hours, tools and response times in writing.</li>
<li>Make sure IP assignment and confidentiality are in the contract.</li>
</ul>
</div>
<div class="grid" style="align-content:start;gap:20px">
<div class="table-wrap"><table><thead><tr><th>Your city</th><th>Your 09:00 is</th><th>Overlap*</th></tr></thead><tbody>
<tr><td>London (BST)</td><td class="num">11:00 EAT</td><td class="num">7 h</td></tr>
<tr><td>Berlin / Paris (CEST)</td><td class="num">10:00 EAT</td><td class="num">8 h</td></tr>
<tr><td>Dubai (GST)</td><td class="num">08:00 EAT</td><td class="num">8 h</td></tr>
<tr><td>New York (EDT)</td><td class="num">16:00 EAT</td><td class="num">2 h</td></tr>
<tr><td>Sydney (AEST)</td><td class="num">02:00 EAT</td><td class="num">async</td></tr>
</tbody></table><p class="meta" style="padding:0 16px 14px">*Against a 09:00–17:00 day at your end and our 08:00–18:00 EAT core hours. Summer time shown; in winter, UK and EU overlap drops by one hour.</p></div>
<div class="table-wrap"><table><thead><tr><th>Region</th><th>Typical agency rate</th></tr></thead><tbody>
<tr><td>US (major cities)</td><td class="num">$50–$300/h</td></tr>
<tr><td>Western Europe &amp; UK</td><td class="num">$50–$199/h</td></tr>
<tr><td>Eastern Europe</td><td class="num">$25–$149/h</td></tr>
<tr><td>Kenya</td><td class="num">&lt;$25–$99/h</td></tr>
</tbody></table><p class="meta" style="padding:0 16px 14px">Source: Qubit Labs, Offshore Software Development Rates by Country, 2026.</p></div>
</div>
</div></div></section>"""

PRICING_BODY = """<section class="band"><div class="wrap">
<div class="sec-head"><p class="label">Projects</p><h2>Fixed-price packages</h2><p class="lede">Every project starts with a free 30-minute call and a written, fixed quote. The prices below are starting points. Your quote depends on scope, content and integrations.</p></div>
<div class="grid g4">
<div class="plan feature"><span class="tag">Most popular</span><h3>Website Launch</h3><div class="price">$1,500 <small>from</small></div><ul><li>Up to 6 pages, custom design</li><li>On-page SEO, schema, sitemap</li><li>Analytics &amp; Search Console</li><li>2–3 weeks</li></ul><a class="btn" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>Growth Website</h3><div class="price">$3,500 <small>from</small></div><ul><li>Up to 15 pages + CMS/blog</li><li>Conversion tracking &amp; CRM forms</li><li>Keyword map + 3 articles</li><li>4–6 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>E-commerce</h3><div class="price">$4,500 <small>from</small></div><ul><li>Shopify or WooCommerce</li><li>Up to 50 products loaded</li><li>Payments, shipping, product SEO</li><li>4–8 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>MVP / Web App</h3><div class="price">$8,000 <small>from</small></div><ul><li>Discovery week &amp; prototype</li><li>Core features, weekly demos</li><li>Deployment &amp; documentation</li><li>6–10 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Scope my project</a></div>
<div class="plan"><h3>SEO Foundation</h3><div class="price">$900 <small>from</small></div><ul><li>Technical audit + fixes</li><li>Keyword research &amp; page map</li><li>Google Business Profile</li><li>90-day roadmap</li></ul><a class="btn ghost" href="{{/contact/}}">Book an audit</a></div>
<div class="plan"><h3>Automation Sprint</h3><div class="price">$1,200 <small>from</small></div><ul><li>Process audit</li><li>1–3 workflows automated</li><li>Error alerts &amp; docs</li><li>About 2 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Find quick wins</a></div>
<div class="plan"><h3>AI Assistant</h3><div class="price">$2,500 <small>from</small></div><ul><li>Website or internal assistant</li><li>Trained on your documents</li><li>Human handoff &amp; analytics</li><li>3–4 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>Custom AI Agent</h3><div class="price">Quote <small>after discovery</small></div><ul><li>Agents that act in your ERP or CRM</li><li>e.g. order-to-cash, lead follow-up</li><li>Human-in-the-loop controls</li><li><a href="{{/work/}}">See examples</a></li></ul><a class="btn ghost" href="{{/contact/}}">Scope my agent</a></div>
</div></div></section>
<section class="band alt"><div class="wrap">
<div class="sec-head"><p class="label">Ongoing</p><h2>Monthly plans</h2></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th>From</th><th>Includes</th></tr></thead><tbody>
<tr><td><strong>SEO &amp; Content Retainer</strong></td><td class="num">$750/mo</td><td>2–4 articles, on-page work, link building, monthly report</td></tr>
<tr><td><strong>Dedicated Developer</strong></td><td class="num">$3,200/mo</td><td>Full-time engineer on your hours, managed by our tech lead</td></tr>
<tr><td><strong>Website Care Plan</strong></td><td class="num">$150/mo</td><td>Hosting, updates, backups, uptime monitoring, 2 hours of changes</td></tr>
<tr><td><strong>Ad Management</strong></td><td class="num">$500/mo</td><td>Google or Meta campaigns, conversion tracking, monthly optimisation (ad spend separate)</td></tr>
</tbody></table></div>
<p class="meta" style="margin-top:14px">Prices in USD, excluding any applicable taxes. We also invoice in GBP and EUR. Clients in Kenya and East Africa pay the same prices and can pay in KES by M-Pesa or bank transfer at the day's exchange rate. Projects: 50% to start, 50% on launch. Plans: monthly in advance, cancel with 30 days' notice.</p>
</div></section>"""

PRICING_FAQ = [
 ("How much does a website cost for a small business?", "A professional small business website with custom design and on-page SEO typically costs $1,500–$5,000 with us, compared with $5,000–$20,000+ at many UK and US agencies. E-commerce and web apps cost more because of payments, integrations and custom features."),
 ("Why are your prices lower than UK or US agencies?", "Our team is based in Nairobi, where operating costs are lower. You get the same process and quality standards, with the saving passed on to you."),
 ("Are there hidden costs?", "No. Your quote lists everything, including third-party costs such as hosting, premium plugins, stock images or ad spend. You pay those directly or we pass them through at cost."),
 ("Which currencies and payment methods do you accept?", "We invoice in USD, GBP or EUR and accept bank transfer, Wise and card payments. Clients in Kenya and East Africa can also pay in KES by M-Pesa or bank transfer."),
]

TEAM_SECTION = """<section class="band alt" id="team"><div class="wrap">
<div class="sec-head"><p class="label">The team</p><h2>Who you'll work with</h2>
<p class="lede">We're a small team on purpose. The person on your first call is the person accountable for your project.</p></div>
<div class="grid g2" style="gap:48px;align-items:start">
<div class="plan"><p class="label">""" + FOUNDER["role"] + """</p><h3 style="font-size:1.5rem">""" + FOUNDER["name"] + """</h3>
<p>""" + FOUNDER["bio"] + """</p>
<p class="meta">Based in Nairobi · English and Swahili</p></div>
<div class="prose"><h3 style="margin-top:0">What that means for your project</h3>
<ul>
<li><strong>Business systems first.</strong> An ERP implementation background means we start from how your business actually runs, not from a template.</li>
<li><strong>AI that has shipped.</strong> Our agents run in real lending, ERP and CRM workflows. See <a href="{{/work/}}">our case studies</a>.</li>
<li><strong>One accountable lead.</strong> Specialists join for design, engineering and SEO, and one person owns the result.</li>
</ul>
<p>Follow Sahara Nova on <a href="https://www.linkedin.com/company/saharanova/" rel="noopener">LinkedIn</a>.</p></div>
</div></div></section>
"""

ABOUT_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Why we started Sahara Nova</h2>
<p>Small and mid-sized businesses are stuck between two bad options. Onshore agencies charge more than they can afford. Freelance marketplaces leave them managing a string of individuals who don't talk to each other.</p>
<p>We started Sahara Nova in Nairobi to offer a third option: one small, senior team that covers design, engineering, SEO and automation, works on your hours, and prices fairly.</p>
<p>The name comes from two ideas. The <em>Sahara</em> stands for where we come from, a continent with one of the youngest and fastest-growing tech workforces in the world. A <em>nova</em> is a star that suddenly shines brighter, which is what we want every client's business to do online.</p>
<h3>How we work</h3>
<ul>
<li><strong>Senior people on every project.</strong> The people you meet on the sales call do the work.</li>
<li><strong>Transparent by default.</strong> Published pricing, fixed quotes, weekly demos, and your code in your repository.</li>
<li><strong>Measured outcomes.</strong> We agree success metrics up front, such as leads, speed or hours saved, and report on them.</li>
<li><strong>Long-term thinking.</strong> We build things your team can maintain, and we stay available after launch.</li>
</ul>
</div>
<div class="grid" style="align-content:start;gap:18px">
<div class="edge"><span class="fig">Nairobi</span><p>Headquartered in Kenya's tech capital, serving clients worldwide.</p></div>
<div class="edge"><span class="fig">EAT</span><p>Core hours 08:00–18:00 East Africa Time, Monday to Friday.</p></div>
<div class="edge"><span class="fig">USD · GBP · EUR</span><p>Invoiced in your currency.</p></div>
</div>
</div></div></section>
""" + TEAM_SECTION + """<section class="band" id="how-we-work"><div class="wrap">
<div class="sec-head"><p class="label">How a typical website project runs</p><h2>From first call to launch in about four weeks</h2><p class="lede">Software and AI projects follow the same rhythm: a short discovery, a fixed plan, then weekly demos until launch.</p></div>
<div class="steps">
<div class="step" data-w="Day 1"><h3>Discovery call</h3><p>30 minutes on goals, audience and budget. You get a fixed quote within two working days.</p></div>
<div class="step" data-w="Week 1"><h3>Strategy &amp; design</h3><p>Keyword research, sitemap and page designs, all approved before we write any code.</p></div>
<div class="step" data-w="Weeks 2–3"><h3>Build &amp; content</h3><p>Development with weekly demo links. SEO, analytics and schema are built in from day one.</p></div>
<div class="step" data-w="Week 4"><h3>Launch &amp; grow</h3><p>Go live, submit to Google, then optional monthly SEO and care plans.</p></div>
</div>
</div></section>
<section class="band"><div class="wrap"><div class="grid g3">
<a class="service" href="{{/work/}}"><h3>See our work</h3><p>AI agents our team has built for lending, ERP and CRM teams, with real results.</p><span class="more">View case studies →</span></a>
<a class="service" href="{{/why-kenya/}}"><h3>Why a team in Kenya</h3><p>Time zone overlap, English-first communication and fair rates.</p><span class="more">Why Kenya →</span></a>
<a class="service" href="{{/east-africa/}}"><h3>Based in East Africa?</h3><p>Meet us in Nairobi. We build for M-Pesa, WhatsApp and mobile-first customers.</p><span class="more">Kenya &amp; East Africa →</span></a>
</div></div></section>"""

CONTACT_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px;align-items:start">
<form class="contact" name="contact" method="POST" action="/thanks/" data-netlify="true" netlify-honeypot="company_website" data-email=\"""" + SITE["email"] + """\">
<input type="hidden" name="form-name" value="contact">
<p class="hp"><label for="company_website">Leave this empty</label><input id="company_website" name="company_website" tabindex="-1" autocomplete="off"></p>
<div class="form-row">
<div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
<div class="field"><label for="f-email">Work email</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
</div>
<div class="form-row">
<div class="field"><label for="f-company">Company &amp; website</label><input id="f-company" name="company" autocomplete="organization"></div>
<div class="field"><label for="f-country">Country</label><input id="f-country" name="country" autocomplete="country-name"></div>
</div>
<div class="form-row">
<div class="field"><label for="f-service">What do you need?</label><select id="f-service" name="service">
<option>New website</option><option>E-commerce store</option><option>Custom software / MVP</option><option>Mobile app</option><option>SEO / digital marketing</option><option>AI &amp; automation</option><option>Dedicated developer</option><option>Not sure yet</option></select></div>
<div class="field"><label for="f-budget">Budget (USD)</label><select id="f-budget" name="budget">
<option>Under $2,000</option><option>$2,000–$5,000</option><option>$5,000–$15,000</option><option>$15,000–$50,000</option><option>$50,000+</option><option>Monthly retainer</option></select></div>
</div>
<div class="field"><label for="f-msg">Tell us about the project</label><textarea id="f-msg" name="message" required placeholder="Goals, timeline, links to examples you like…"></textarea></div>
<p class="form-note">We use your details only to reply to your enquiry. See our <a href="{{/privacy/}}">privacy policy</a>.</p>
<div><button class="btn" type="submit">Send my brief</button></div>
<p class="form-msg" role="status" aria-live="polite"></p>
</form>
<div class="contact-list">
<h2>What happens next</h2>
<div><b>Within 1 working day</b>We reply to confirm we've read your brief and book a 30-minute call.</div>
<div><b>Within 2 working days of the call</b>You receive a written proposal with scope, timeline and a fixed price.</div>
<div><b>Email</b><span style="user-select:all">""" + SITE["email"] + """</span></div>
<div><b>WhatsApp</b><a href="https://wa.me/""" + SITE["whatsapp"] + """?text=Hi%20Sahara%20Nova%2C%20I%27d%20like%20to%20ask%20about%20a%20project">""" + SITE["phone"] + """</a> · quickest for a short question</div>
<div><b>Location</b>Nairobi, Kenya · East Africa Time (UTC+3). In-person meetings available in Nairobi.</div>
<div><b>Payment</b>USD, GBP, EUR by bank, Wise or card · KES by M-Pesa or bank transfer</div>
<div><b>Hours</b>Mon–Fri, 08:00–18:00 EAT</div>
</div>
</div></div></section>"""

ANALYTICS_NONE = "this website currently runs no analytics and sets no advertising or tracking cookies."
ANALYTICS_GA = ("only if you click Accept on the cookie bar, we use Google Analytics 4, which sets cookies (_ga, _ga_*) to count visits and see which pages people use: "
                "pages visited, referrer, approximate location (country/city), device and browser. Google does not log or store IP addresses for Analytics 4. "
                "If you decline, no analytics code loads. You can change your choice at any time with the Cookie settings link at the bottom of every page. "
                "We use no advertising cookies.")

PRIVACY_BODY = """<section class="band"><div class="wrap"><div class="prose">
<p><em>Last updated: 15 October 2026</em></p>
<h2>Who we are</h2><p>Sahara Nova ("we", "us") is a digital agency based in Nairobi, Kenya. This policy explains how we handle personal data collected through this website. Contact: """ + SITE["email"] + """.</p>
<h2>What we collect</h2><ul><li><strong>Contact form:</strong> name, email, company, country, budget and project details you choose to send.</li><li><strong>Analytics:</strong> """ + (ANALYTICS_GA if SITE["ga4_id"] else ANALYTICS_NONE) + """</li></ul>
<h2>Why we use it</h2><p>To reply to your enquiry, prepare proposals and improve our website. Our lawful bases are your consent and our legitimate interest in responding to business enquiries.</p>
<h2>Sharing and transfers</h2><p>We use trusted processors to run this website and our business, for example website hosting and form handling (Netlify, Inc., USA), email""" + (", and website analytics (Google LLC, USA, only if you accept analytics cookies)" if SITE["ga4_id"] else "") + """. Some of these providers process data outside Kenya and the EU/UK under appropriate safeguards. We never sell your data.</p>
<h2>Retention</h2><p>Enquiries that don't become projects are deleted after 24 months. Client records are kept as long as required by law.</p>
<h2>Your rights</h2><p>Under Kenya's Data Protection Act 2019 and, where applicable, the EU/UK GDPR, you can request access to, correction of or deletion of your personal data, or object to its processing. Email us and we will respond within 30 days.</p>
</div></div></section>"""

BLOG_BODY = """<section class="band"><div class="wrap"><div class="sec-head"><p class="label">Latest</p><h2>Latest guides</h2></div><div class="grid g2">
<a class="post-card" href="{{/blog/website-cost-in-kenya/}}"><span class="meta">Guide · 22 Oct 2026 · 7 min read</span><h3>How much does a website cost in Kenya in 2026?</h3><p>What you get at each price level, from KES 15,000 template sites to custom builds, plus the yearly costs after launch.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/mpesa-stk-push-integration-guide/}}"><span class="meta">Guide · 22 Oct 2026 · 9 min read</span><h3>M-Pesa STK Push integration: a step-by-step guide</h3><p>How Daraja STK Push works, what you need before you start, and the mistakes behind most failed integrations.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/outsourcing-web-development-to-kenya/}}"><span class="meta">Guide · 23 Sep 2026 · 8 min read</span><h3>What it costs to outsource web development to Kenya in 2026, and how to do it well</h3><p>Rates by region, how the EAT time zone overlaps with yours, and a checklist for vetting a Kenyan agency.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
</div></div></section>"""

ARTICLE_BODY = """<section class="band"><div class="wrap"><article class="prose">
<p class="meta">Published 23 September 2026 · By <a href="{{/about/#team}}">James Njoroge</a>, founder · 8 min read</p>
<p>If you run a small or mid-sized business in the UK, Europe or the US, you have probably noticed that agency quotes for a new website or app have climbed steadily. More businesses are looking further afield, and Kenya, Nairobi in particular, has become one of the most talked-about destinations for outsourcing web and software development.</p>
<p>This guide covers what it costs, how the time zones work, where Kenya fits against other outsourcing regions, and how to pick a partner without getting burned.</p>

<h2>Why Kenya?</h2>
<p>Nairobi has built a reputation as the "Silicon Savannah". Mobile money platform M-Pesa was built and scaled here, and the city hosts a busy startup scene, international tech companies and a steady stream of computer science graduates. Three practical factors matter most to a small business buyer:</p>
<ul>
<li><strong>English as a working language.</strong> English is an official language and the default for business and education.</li>
<li><strong>A Europe-friendly time zone.</strong> East Africa Time is UTC+3 all year round.</li>
<li><strong>Competitive rates</strong> for experienced engineers and designers.</li>
</ul>

<h2>How much does it cost to outsource web development to Kenya?</h2>
<p>Published rate guides put Kenyan development rates between under $25 and $99 an hour, depending on seniority and agency size. For comparison:</p>
<div class="table-wrap"><table><thead><tr><th>Region</th><th>Typical hourly rate (USD)</th></tr></thead><tbody>
<tr><td>North America</td><td class="num">$50–$300</td></tr>
<tr><td>Western Europe &amp; UK</td><td class="num">$50–$199</td></tr>
<tr><td>Latin America</td><td class="num">$25–$199</td></tr>
<tr><td>Eastern Europe</td><td class="num">$25–$149</td></tr>
<tr><td>Kenya</td><td class="num">&lt;$25–$99</td></tr>
</tbody></table></div>
<p class="meta">Source: Qubit Labs, "Offshore Software Development Rates by Country", 2026.</p>
<p>Kenyan agencies listed on Clutch show a wide spread. Some large vendors charge under $25 an hour with $10,000 minimum projects, while premium studios charge $100–$199 an hour. For a small business, the useful middle is a senior team charging roughly $30–$50 an hour with fixed-price packages.</p>
<p>In project terms, a small business website that costs $6,000–$15,000 from a London agency will often cost $1,500–$5,000 from a good Kenyan team.</p>

<h2>Time zones: the underrated advantage</h2>
<p>With outsourcing, time zone overlap often matters more than the hourly rate. When your developer is asleep during your whole working day, every question costs 24 hours. Kenya doesn't observe daylight saving, so overlap with Europe stays predictable:</p>
<ul>
<li><strong>UK:</strong> 2 hours behind Nairobi in summer, 3 in winter, giving 6–7 hours of shared working time</li>
<li><strong>Central Europe:</strong> 1–2 hours behind, giving 7–8 hours of overlap</li>
<li><strong>Gulf:</strong> 1 hour ahead, giving almost a full shared day</li>
<li><strong>US East Coast:</strong> 7–8 hours behind, so your morning is our late afternoon, with about 2 hours of overlap plus async handoffs</li>
</ul>

<h2>Kenya vs other outsourcing destinations</h2>
<p><strong>Eastern Europe</strong> offers strong engineering and a good EU time zone, but its rates have risen close to Western levels. <strong>South and Southeast Asia</strong> offer very low rates but little overlap with Europe or the US. <strong>Latin America</strong> is the natural nearshore choice for US companies. Kenya sits in a useful spot: good overlap with Europe and the Middle East, native-level English, and costs well below Eastern Europe.</p>

<h2>What to watch out for</h2>
<ul>
<li><strong>Bait-and-switch staffing.</strong> A senior person sells the project and juniors deliver it. Ask who exactly will work on yours.</li>
<li><strong>No visibility.</strong> Insist on weekly demos and access to the code repository from day one.</li>
<li><strong>Vague scope.</strong> A fixed price only protects you if the scope is written down in detail.</li>
<li><strong>IP and data.</strong> Your contract should assign all intellectual property to you and include confidentiality and, for EU/UK clients, a data processing agreement. Kenya's Data Protection Act 2019 follows many GDPR principles.</li>
<li><strong>Payment terms.</strong> A 30–50% deposit is normal. 100% upfront is a red flag.</li>
</ul>

<h2>A simple vetting checklist</h2>
<ol>
<li>Review their portfolio and ask for two client references you can speak to.</li>
<li>Check independent reviews on Clutch or GoodFirms.</li>
<li>Run a small paid pilot (1–2 weeks) before committing to a large build.</li>
<li>Agree communication tools, meeting times and response times in writing.</li>
<li>Confirm who owns the code, domains, hosting accounts and design files.</li>
</ol>

<p>For the wider case beyond cost, including the talent pool, legal system and data protection, see <a href="{{/why-kenya/}}">why companies hire developers in Kenya</a>.</p>
<h2>The bottom line</h2>
<p>For small and mid-sized businesses in Europe, the UK and the Middle East, Kenya combines lower cost, English-first communication and real working-hours overlap. The key is choosing a partner that works transparently and that you can hold accountable.</p>
<p>If you'd like to see how that works in practice, <a href="{{/contact/}}">send us your brief</a> and we'll reply with a fixed quote within two working days, or see our <a href="{{/services/web-development/}}">web development</a> and <a href="{{/pricing/}}">pricing</a> pages.</p>
</article></div></section>"""


BYLINE = '<p class="meta">Published {date} · By <a href="{{{{/about/#team}}}}">James Njoroge</a>, founder · {mins} min read</p>'

WEBSITE_COST_KENYA_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="22 October 2026", mins=7) + """
<p>Ask five web designers in Nairobi what a website costs and you'll get five answers between KES 5,000 and KES 1 million. They're not all wrong. They're quoting for very different things. This guide breaks down what each price level gets you in 2026, what you'll pay every year after launch, and how to tell which one your business needs.</p>

<h2>The short answer</h2>
<div class="table-wrap"><table><thead><tr><th>Type of website</th><th>Typical cost (KES)</th><th>Good for</th></tr></thead><tbody>
<tr><td>Do it yourself (WordPress or a site builder)</td><td class="num">About 3,000–5,000 in year one</td><td>Testing an idea, a simple online presence</td></tr>
<tr><td>Template site from a freelancer (about 5 pages)</td><td class="num">15,000–80,000</td><td>A brochure site that mainly needs to look credible</td></tr>
<tr><td>Custom business website with SEO</td><td class="num">From about 195,000</td><td>Businesses that want Google enquiries</td></tr>
<tr><td>Online shop with M-Pesa checkout</td><td class="num">From about 585,000</td><td>Selling products online</td></tr>
<tr><td>Web app or customer portal</td><td class="num">From about 1,000,000</td><td>Bookings, accounts, dashboards, SaaS</td></tr>
</tbody></table></div>
<p class="meta">DIY and freelancer ranges: Hostiko, "How much does a website cost in Kenya", 2026. Custom, shop and web app figures are Sahara Nova's published starting prices ($1,500, $4,500 and $8,000), converted at about KES 130 to the dollar (October 2026).</p>

<h2>Why the prices are so far apart</h2>
<p>The gap isn't mostly about design. A KES 30,000 site and a KES 200,000 site can look similar on the day they launch. The difference is in the work you can't see:</p>
<ul>
<li><strong>Research before design.</strong> A cheaper site starts from a template. A custom site starts from what your customers search for and what they need to see before they call you.</li>
<li><strong>Speed on real phones.</strong> Most Kenyan visitors arrive on mobile data and mid-range Android phones. Heavy themes and plugins can take ten seconds or more to load, and people leave.</li>
<li><strong>SEO foundations.</strong> Page titles, structured data, a sitemap, internal links and Google Business Profile setup decide whether anyone finds the site at all.</li>
<li><strong>Content.</strong> Writing that answers real questions takes time. Many cheap quotes assume you'll supply all the text.</li>
<li><strong>Integrations.</strong> M-Pesa checkout, WhatsApp ordering, a CRM or eTIMS-ready invoicing each add real engineering work.</li>
</ul>

<h2>Costs after launch</h2>
<p>A website keeps costing money after it goes live. Budget for these every year:</p>
<ul>
<li><strong>A .co.ke domain:</strong> around KES 1,200 a year from Kenyan registrars.</li>
<li><strong>Hosting:</strong> shared hosting can cost under KES 1,000 a year. A busy shop or web app needs more, often a few thousand shillings a month.</li>
<li><strong>Email:</strong> business email on your domain, free or a few hundred shillings per mailbox each month depending on the provider.</li>
<li><strong>Maintenance:</strong> updates, backups, security fixes and small changes. Ours is the Website Care Plan from $150 a month (about KES 19,500).</li>
<li><strong>Marketing:</strong> SEO content or ads if you want the site to keep bringing in enquiries.</li>
</ul>
<div class="callout"><p><strong>Make sure you own your domain.</strong> The most common problem we see is a business whose domain was registered in a former designer's name or account. When it lapses, the website and email go down. Ask for the domain to be registered to your business, with login details you keep.</p></div>

<h2>Which one do you need?</h2>
<p><strong>A template or freelancer site is fine</strong> if most customers find you through referrals or social media, and the website is mainly somewhere to check you're legitimate.</p>
<p><strong>A custom site with SEO pays for itself</strong> if your customers search Google before they buy, for example "plumber in Kilimani", "accounting firm Westlands" or "school management system Kenya", and one new client is worth more than the site costs.</p>
<p><strong>An online shop or web app</strong> makes sense when the site needs to take payments, bookings or logins. Budget for proper M-Pesa integration. We explain how it works in our <a href="{{/blog/mpesa-stk-push-integration-guide/}}">M-Pesa STK Push integration guide</a>.</p>

<h2>Questions to ask before you pay a deposit</h2>
<ol>
<li>Will the domain, hosting and code be registered in my name?</li>
<li>Who writes the content, and is it included in the price?</li>
<li>How fast does the site load on a phone over mobile data? Can I see a recent example?</li>
<li>What SEO work is included: page titles, Google Business Profile, Search Console, a sitemap?</li>
<li>What does it cost each year after launch, and what happens if I want to move to another developer?</li>
</ol>

<h2>The bottom line</h2>
<p>Expect to pay KES 15,000–80,000 for a simple template site and about KES 195,000 upwards for a custom business site built to win enquiries from Google. Online shops and web apps cost more because of payments and custom features. Whatever you choose, keep your domain in your own name. If you'd like a fixed price for your project, see <a href="{{/pricing/}}">our pricing</a> or <a href="{{/contact/}}">send us a short brief</a>. You can pay in KES by M-Pesa or bank transfer. More on how we work with local businesses is on our <a href="{{/east-africa/}}">Kenya and East Africa page</a>.</p>
</article></div></section>"""

MPESA_GUIDE_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="22 October 2026", mins=9) + """
<p>STK Push, also called Lipa na M-Pesa Online or M-Pesa Express, is the checkout most Kenyan customers now expect. They enter their phone number on your site, a prompt appears on their phone, they type their M-Pesa PIN, and the payment is done. No copying Paybill numbers, no mistyped account references.</p>
<p>This guide explains how an STK Push integration works through Safaricom's Daraja API, what you need before you start, and the mistakes that cause most failed integrations. It's written for business owners who want to understand the process and for developers doing it for the first time.</p>

<h2>What you need first</h2>
<ul>
<li><strong>A Paybill or Till number</strong> registered to your business. You can build and test without one in the sandbox, but you need one to go live.</li>
<li><strong>A Daraja account</strong> on Safaricom's developer portal, with an app created to get a Consumer Key and Consumer Secret.</li>
<li><strong>A server you control.</strong> The payment request must come from your backend, never from the browser, because it uses your secret credentials.</li>
<li><strong>A public HTTPS callback URL</strong> where Safaricom sends the payment result.</li>
</ul>

<h2>How the flow works</h2>
<ol>
<li>The customer enters their phone number at checkout.</li>
<li>Your server gets an access token from Daraja using your Consumer Key and Secret.</li>
<li>Your server sends the STK Push request: amount, phone number, your shortcode and a callback URL.</li>
<li>Safaricom shows the PIN prompt on the customer's phone.</li>
<li>The customer enters their PIN, cancels, or ignores it.</li>
<li>Safaricom posts the result to your callback URL, and your server marks the order paid or failed.</li>
</ol>

<h2>Step 1: get an access token</h2>
<p>Daraja uses OAuth. Send your Consumer Key and Secret as HTTP Basic authentication to the token endpoint. The token is valid for about an hour, so cache it and reuse it instead of requesting a new one for every payment.</p>
<pre><code>GET https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials
Authorization: Basic base64(CONSUMER_KEY:CONSUMER_SECRET)</code></pre>

<h2>Step 2: send the STK Push request</h2>
<p>The request needs a password, which is your shortcode, your passkey and a timestamp joined together and Base64-encoded. The timestamp uses the format <code>yyyyMMddHHmmss</code>, and you build a new password for every request.</p>
<pre><code>POST https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest
Authorization: Bearer ACCESS_TOKEN

{
  "BusinessShortCode": "174379",
  "Password": "base64(ShortCode + Passkey + Timestamp)",
  "Timestamp": "20261022143000",
  "TransactionType": "CustomerPayBillOnline",
  "Amount": 1500,
  "PartyA": "2547XXXXXXXX",
  "PartyB": "174379",
  "PhoneNumber": "2547XXXXXXXX",
  "CallBackURL": "https://yourdomain.co.ke/api/mpesa/callback/long-random-string",
  "AccountReference": "ORDER1042",
  "TransactionDesc": "Order 1042"
}</code></pre>
<ul>
<li><strong>TransactionType</strong> is <code>CustomerPayBillOnline</code> for a Paybill and <code>CustomerBuyGoodsOnline</code> for a Till.</li>
<li><strong>Amount</strong> is a whole number of shillings. No decimals.</li>
<li><strong>Phone numbers</strong> use the 2547… or 2541… format: no plus sign, no leading zero, no spaces. Normalise whatever the customer types.</li>
<li><strong>AccountReference and TransactionDesc</strong> are short. Keep them to an order number.</li>
</ul>
<p>A successful response includes a <code>CheckoutRequestID</code>. Save it against the order. A response code of 0 here only means Safaricom accepted the request. <strong>It does not mean the customer paid.</strong></p>

<h2>Step 3: handle the callback</h2>
<p>When the customer finishes, Safaricom posts a JSON result to your callback URL. Inside <code>Body.stkCallback</code> you'll find the <code>CheckoutRequestID</code>, a <code>ResultCode</code> and, only for successful payments, <code>CallbackMetadata</code> with the amount, the M-Pesa receipt number, the transaction time and the phone number.</p>
<div class="table-wrap"><table><thead><tr><th>ResultCode</th><th>What it means</th><th>What to do</th></tr></thead><tbody>
<tr><td class="num">0</td><td>Paid</td><td>Check the amount, save the receipt number, mark the order paid</td></tr>
<tr><td class="num">1032</td><td>Customer cancelled</td><td>Let them try again</td></tr>
<tr><td class="num">1037</td><td>Phone unreachable or no response</td><td>Offer a retry or a manual Paybill option</td></tr>
<tr><td class="num">1</td><td>Insufficient balance</td><td>Tell the customer clearly</td></tr>
</tbody></table></div>
<p>Reply to every callback quickly with an HTTP 200, and do any slow work, such as sending emails, after you respond.</p>

<h2>Step 4: check when no callback arrives</h2>
<p>Callbacks sometimes arrive late or not at all. Use the STK Push query endpoint (<code>/mpesa/stkpushquery/v1/query</code>) with the <code>CheckoutRequestID</code> to check the status of any order that's still pending after a minute or two. Show the customer a "waiting for payment" screen that polls your own server rather than leaving them guessing.</p>

<h2>Mistakes that cause most failed integrations</h2>
<ul>
<li><strong>Trusting the callback blindly.</strong> Anyone who finds your callback URL could post a fake success. Use a long, unguessable callback path, confirm the <code>CheckoutRequestID</code> matches an order you created, check the amount, and use the query endpoint to confirm high-value payments.</li>
<li><strong>Processing the same payment twice.</strong> Callbacks can be retried. Make the handler idempotent: if the order is already paid, do nothing.</li>
<li><strong>Calling Daraja from the browser.</strong> This exposes your Consumer Secret and passkey. Keep every Daraja call on the server.</li>
<li><strong>Using a local or HTTP callback URL.</strong> Safaricom needs to reach a public HTTPS address.</li>
<li><strong>Forgetting go-live differences.</strong> Production uses <code>api.safaricom.co.ke</code>, your own shortcode and a production passkey, not the sandbox values.</li>
<li><strong>No reconciliation.</strong> Match M-Pesa receipt numbers against your Paybill or Till statement regularly, so missed callbacks don't turn into unhappy customers.</li>
</ul>

<h2>Going live</h2>
<p>When everything works in the sandbox, request go-live from the Daraja portal for your Paybill or Till. Safaricom verifies the business and the person who administers the shortcode, then issues production credentials and a passkey. Swap the base URL, the shortcode and the passkey, run a few small real payments, and check each one against your M-Pesa statement before you announce it.</p>

<h2>Do it yourself or hire help?</h2>
<p>A developer who has done it before can usually add STK Push to an existing site in a few days. Most of that time goes into the parts that protect your money: callbacks, retries, verification and reconciliation. If you'd like it done for you, as part of a new website or added to an existing one, see our <a href="{{/east-africa/}}">work for Kenyan and East African businesses</a> or <a href="{{/contact/}}">send us a brief</a>. Planning a full new site? Our guide to <a href="{{/blog/website-cost-in-kenya/}}">what a website costs in Kenya</a> covers budgets.</p>
</article></div></section>"""

EAST_AFRICA_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">A Nairobi team that knows your market</h2>
<p>We're based in Nairobi and build for businesses in Kenya, Uganda, Tanzania and Rwanda as well as for clients abroad. Your customers pay by M-Pesa, message you on WhatsApp and browse on mid-range Android phones, and we build for exactly that. You get the same senior team and process we bring to every client, and you can meet us face to face.</p>
<h3>Websites that work on East African connections</h3>
<p>Many of your visitors are on mobile data, so every kilobyte counts. We build lightweight, mobile-first sites that load quickly on 3G and budget phones, rank well on Google and don't drain your customers' bundles.</p>
<h3>M-Pesa and mobile money integration</h3>
<p>We integrate M-Pesa through the Daraja API: STK Push checkout, C2B Paybill and Till payments, B2C payouts and automatic reconciliation with your orders or accounting system. Our <a href="{{/blog/mpesa-stk-push-integration-guide/}}">M-Pesa STK Push integration guide</a> explains how it works. For customers in Uganda, Tanzania and Rwanda we also connect Airtel Money and MTN MoMo through regional payment gateways, along with card payments.</p>
<h3>WhatsApp and AI for customer service</h3>
<p>Your customers already use WhatsApp. We set up WhatsApp Business ordering, automated replies and AI assistants that answer common questions in English or Swahili, take orders and hand over to a person when needed.</p>
<h3>AI agents already working in Kenya</h3>
<p>We built an AI agent for a digital lender that took in <strong>KES 5.4M in loan top-up applications in its first week</strong>. Read the <a href="{{/work/#loan-top-up-agent}}">case study</a>, or see our <a href="{{/services/ai-automation/}}">AI and automation services</a>.</p>
<h3>Local SEO in Nairobi and beyond</h3>
<p>We optimise your Google Business Profile, local citations and service-area pages so you show up when customers search for "near me" services in Nairobi, Mombasa, Kisumu, Kampala, Dar es Salaam or Kigali.</p>
<h3>Working with businesses across Nairobi</h3>
<p>We work remotely and meet clients at their offices, from Westlands, Kilimani and Upper Hill to the CBD, Industrial Area and Karen. Wondering about budget? Read <a href="{{/blog/website-cost-in-kenya/}}">how much a website costs in Kenya in 2026</a>, or see our <a href="{{/pricing/}}">published prices</a>.</p>
<h3>Business systems</h3>
<p>We build custom software for how East African businesses run: stock and order systems, SACCO and chama portals, school and clinic management tools, field-sales apps and invoicing that works with KRA eTIMS.</p>
</div>
<div class="grid" style="align-content:start;gap:20px">
<div class="table-wrap"><table><thead><tr><th>Need</th><th>What we build</th></tr></thead><tbody>
<tr><td>Sell online</td><td>E-commerce with M-Pesa STK Push, delivery zones and WhatsApp order alerts</td></tr>
<tr><td>Get found</td><td>Google Business Profile, local SEO, Swahili/English pages</td></tr>
<tr><td>Serve customers faster</td><td>WhatsApp Business bots and AI assistants</td></tr>
<tr><td>Run operations</td><td>Inventory, orders, bookings, eTIMS-ready invoicing</td></tr>
<tr><td>Grow a startup</td><td>MVPs, mobile apps and mobile money payment flows</td></tr>
</tbody></table></div>
<div class="plan"><h3>Paying us locally</h3><ul><li>Same published prices as all our clients</li><li>Pay in KES by M-Pesa or bank transfer, at the day's exchange rate</li><li>Meetings at your office in Nairobi, or by video call</li></ul><div class="btn-row" style="margin-top:8px"><a class="btn" href="{{/contact/}}">Book a meeting</a><a class="btn ghost" href="https://wa.me/""" + SITE["whatsapp"] + """?text=Hi%20Sahara%20Nova%2C%20I%27d%20like%20to%20ask%20about%20a%20project">Chat on WhatsApp</a></div></div>
</div>
</div></div></section>"""

EAST_AFRICA_FAQ = [
 ("Do you build websites for businesses in Nairobi?", "Yes. We're a Nairobi-based agency and build websites, e-commerce stores, software and marketing campaigns for Kenyan businesses, with in-person meetings available."),
 ("Can you integrate M-Pesa into my website or app?", "Yes. We integrate M-Pesa through Safaricom's Daraja API, including STK Push checkout, Paybill and Till payments, B2C payouts and automatic reconciliation."),
 ("Do you work with businesses in Uganda, Tanzania and Rwanda?", "Yes. We serve clients across East Africa remotely and can travel for workshops. We integrate regional payment options such as Airtel Money and MTN MoMo."),
 ("Can I pay in Kenyan shillings?", "Yes. Our prices are published in USD and you can pay the equivalent in KES by M-Pesa or bank transfer at the day's exchange rate."),
 ("Can you build a WhatsApp chatbot for my business?", "Yes. We build WhatsApp Business ordering flows, automated replies and AI assistants that answer in English or Swahili and hand over to your team when needed."),
]

PAGES = [
 dict(path="", title="Digital Agency for Small Businesses | Sahara Nova, Nairobi",
      description="A digital agency for small businesses, based in Nairobi: websites, custom software, SEO and AI automation for clients worldwide. Your hours, fixed prices.",
      h1="The Nairobi digital agency that works your hours", hero=HOME_HERO, body=HOME_BODY, faq=HOME_FAQ,
      faq_title="Questions small businesses ask us"),
 dict(path="services/", title="Web, Software, SEO & AI for Small Businesses | Sahara Nova",
      description="Web design and development, custom software and apps, SEO and digital marketing, and AI automation for small and mid-sized businesses, from one team in Nairobi.",
      eyebrow="Services", h1="Everything digital, from one team",
      lede="Four disciplines, one project lead, one invoice. Start with the service you need most and add the others when you're ready.",
      crumbs=[("/services/", "Services")], body=SERVICES_BODY),
 WEB, SOFT, SEO, AI,
 dict(path="why-kenya/", title="Hire Developers in Kenya: Why Teams Choose Nairobi | Sahara Nova",
      description="Why hire developers in Kenya: 6–8 hours of overlap with Europe, English-first teams, 40–60% lower costs and Nairobi's deep tech talent pool.",
      eyebrow="Why Kenya", h1="Why hire a development team in Kenya?",
      lede="Time zone overlap with Europe, English as a working language, and rates well below onshore agencies. Here is what working with developers in Nairobi looks like in practice.",
      crumbs=[("/why-kenya/", "Why Kenya")], body=WHY_KENYA_BODY,
      faq=[("Is it safe to outsource development to Kenya?", "Yes, if you choose your partner carefully. Kenya's legal system is based on English common law, its Data Protection Act 2019 follows GDPR principles, and contracts can assign full IP ownership to you."),
           ("What time zone is Kenya in?", "Kenya uses East Africa Time (EAT), UTC+3, all year round with no daylight saving. That is 2–3 hours ahead of the UK and 1–2 hours ahead of central Europe."),
           ("How much do Kenyan developers cost?", "Agency rates in Kenya typically range from under $25 to $99 per hour, depending on seniority and agency size.")]),
 dict(path="work/", title="AI Agent Case Studies: Odoo, HubSpot & Lending | Sahara Nova",
      description="AI agents our team has built: loan top-up intake for a lender, email-to-Odoo order-to-cash, a HubSpot CRM agent, and customer support and lead intake agents.",
      eyebrow="Our work", h1="AI agents our team has built",
      lede="Real agents running inside real businesses: taking in loan applications, processing orders in an ERP, working a CRM pipeline and talking to customers. Built by our founding team; client names are withheld.",
      crumbs=[("/work/", "Work")], body=WORK_BODY, cases=True),
 dict(path="east-africa/", title="Web Design & Software Company in Nairobi, Kenya | Sahara Nova",
      description="Nairobi web design, software, SEO and AI for businesses in Kenya and East Africa: M-Pesa integration, WhatsApp bots, fast mobile sites and local SEO.",
      eyebrow="Kenya &amp; East Africa", h1="Web design, software and marketing for businesses in Kenya and East Africa",
      lede="A Nairobi team building fast websites, M-Pesa-ready apps, WhatsApp automation and local SEO for businesses in Kenya, Uganda, Tanzania and Rwanda.",
      crumbs=[("/east-africa/", "Kenya & East Africa")], body=EAST_AFRICA_BODY, faq=EAST_AFRICA_FAQ,
      area=["Kenya", "Uganda", "Tanzania", "Rwanda"]),
 dict(path="pricing/", title="Website & Software Development Pricing | Sahara Nova",
      description="Transparent pricing for small business websites (from $1,500), e-commerce, MVPs, SEO (from $900) and AI automation. Fixed quotes within two working days.",
      eyebrow="Pricing", h1="Transparent pricing, fixed quotes",
      lede="Published starting prices, so you know if we fit your budget before you pick up the phone.",
      crumbs=[("/pricing/", "Pricing")], body=PRICING_BODY, faq=PRICING_FAQ),
 dict(path="about/", title="About Sahara Nova | Digital Agency in Nairobi, Kenya",
      description="Sahara Nova is a small, senior digital team in Nairobi, Kenya, helping small and mid-sized businesses worldwide with websites, software, SEO and automation.",
      eyebrow="About", h1="A small senior team, built for clients anywhere",
      lede="We're a Nairobi-based digital agency that believes small businesses deserve senior, transparent, fairly priced digital work.",
      crumbs=[("/about/", "About")], body=ABOUT_BODY),
 dict(path="contact/", title="Contact Sahara Nova | Get a Fixed Quote",
      description="Tell us about your website, software, SEO or automation project. We reply within one working day and send a fixed quote within two working days of our call.",
      eyebrow="Contact", h1="Tell us about your project",
      lede="A few details are enough to start. We reply within one working day.",
      crumbs=[("/contact/", "Contact")], body=CONTACT_BODY, no_cta=True),
 dict(path="blog/", title="Web, SEO & Automation Guides for Small Businesses | Sahara Nova",
      description="Practical guides on websites, SEO, software and AI automation for small business owners, from the Sahara Nova team in Nairobi.",
      eyebrow="Blog", h1="Guides for small business owners",
      lede="Practical, jargon-free advice on websites, SEO, software and automation.",
      crumbs=[("/blog/", "Blog")], body=BLOG_BODY),
 dict(path="blog/outsourcing-web-development-to-kenya/",
      title="Cost of Outsourcing Web Development to Kenya (2026 Guide)",
      description="What it costs to outsource web development to Kenya in 2026: hourly rates by region, typical project prices, time zone overlap and a checklist for vetting an agency.",
      eyebrow="Guide", h1="What it costs to outsource web development to Kenya in 2026, and how to do it well",
      lede="Rates, time zone overlap, how Kenya compares with other outsourcing regions, and a vetting checklist.",
      crumbs=[("/blog/", "Blog"), ("/blog/outsourcing-web-development-to-kenya/", "Outsourcing to Kenya")],
      article={"date": "2026-09-23", "modified": "2026-10-22"}, body=ARTICLE_BODY),
 dict(path="blog/website-cost-in-kenya/",
      title="How Much Does a Website Cost in Kenya? (2026 Prices in KES)",
      description="Website prices in Kenya for 2026: DIY, freelancer template sites, custom business sites, online shops and web apps in KES, plus the yearly costs after launch.",
      eyebrow="Guide", h1="How much does a website cost in Kenya in 2026?",
      lede="What you get at each price level, what you'll pay every year after launch, and how to choose.",
      crumbs=[("/blog/", "Blog"), ("/blog/website-cost-in-kenya/", "Website cost in Kenya")],
      article={"date": "2026-10-22"}, body=WEBSITE_COST_KENYA_BODY,
      faq=[("How much does a basic website cost in Kenya?", "A simple five-page template site from a freelancer typically costs KES 15,000–80,000, plus around KES 2,000–3,000 a year for a .co.ke domain and basic hosting."),
           ("How much does a custom business website cost in Kenya?", "A custom-designed business website with SEO built in typically starts from about KES 195,000 with an agency. Sahara Nova's Website Launch package starts at $1,500, payable in KES."),
           ("How much is a .co.ke domain per year?", "Around KES 1,200 a year from most Kenyan registrars. Make sure it is registered in your business's name.")]),
 dict(path="blog/mpesa-stk-push-integration-guide/",
      title="M-Pesa STK Push Integration: A Step-by-Step Guide (2026)",
      description="How to add M-Pesa STK Push checkout to your website with the Daraja API: access tokens, the request, callbacks, result codes, going live and common mistakes.",
      eyebrow="Guide", h1="M-Pesa STK Push integration: a step-by-step guide",
      lede="How Lipa na M-Pesa Online works through the Daraja API, what you need first, and how to avoid the mistakes behind most failed integrations.",
      crumbs=[("/blog/", "Blog"), ("/blog/mpesa-stk-push-integration-guide/", "M-Pesa STK Push guide")],
      article={"date": "2026-10-22"}, body=MPESA_GUIDE_BODY,
      faq=[("What is M-Pesa STK Push?", "STK Push, also called Lipa na M-Pesa Online or M-Pesa Express, sends a payment prompt straight to the customer's phone. They enter their M-Pesa PIN to pay, with no need to type a Paybill or account number."),
           ("Do I need a Paybill or Till number for STK Push?", "You can build and test in the Daraja sandbox without one, but you need a Paybill or Till registered to your business to go live."),
           ("How long does an M-Pesa integration take?", "An experienced developer can usually add STK Push to an existing website in a few days, including callback handling, verification and reconciliation.")]),
 dict(path="privacy/", title="Privacy Policy | Sahara Nova",
      description="How Sahara Nova collects, uses and protects personal data submitted through this website.",
      eyebrow="Legal", h1="Privacy policy", lede="Short, plain English, and no advertising cookies.",
      crumbs=[("/privacy/", "Privacy")], body=PRIVACY_BODY),
 dict(path="thanks/", title="Thank you | Sahara Nova", description="Thanks for your enquiry. Sahara Nova will reply within one working day.",
      eyebrow="Message received", h1="Thanks, your brief is in", noindex=True, no_cta=True,
      lede="We reply within one working day to book a 30-minute call. In the meantime, you might like our guide to outsourcing to Kenya.",
      body='<section class="band"><div class="wrap"><div class="btn-row" style="margin:0"><a class="btn" href="{{/blog/outsourcing-web-development-to-kenya/}}">Read the guide</a><a class="btn ghost" href="{{/}}">Back to the homepage</a></div></div></section>'),
 dict(path="404.html", title="Page not found | Sahara Nova", description="This page could not be found. Browse Sahara Nova's web, software, SEO and automation services.",
      eyebrow="404", h1="This page drifted off into the dunes",
      lede="The page you're looking for doesn't exist or has moved.", noindex=True,
      body='<section class="band"><div class="wrap"><div class="btn-row" style="margin:0"><a class="btn" href="{{/}}">Go to the homepage</a><a class="btn ghost" href="{{/services/}}">Browse services</a></div></div></section>'),
]
