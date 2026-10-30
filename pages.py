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
    "same_as": ["https://www.linkedin.com/company/saharanova/",
                "https://www.facebook.com/profile.php?id=61595593056428"],
    # Shown in the footer on every page, in this order. Add Instagram, X, YouTube etc. here and to same_as.
    "social": [("LinkedIn", "https://www.linkedin.com/company/saharanova/"),
               ("Facebook", "https://www.facebook.com/profile.php?id=61595593056428")],
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
      summary="An AI agent that finds borrowers who are repaying well, offers them a top-up over SMS and WhatsApp, and takes in complete applications for the credit team to decide on.",
      challenge="Good borrowers were eligible for top-ups, but reaching them and collecting the details for each application took staff time, so most of that demand went untapped.",
      steps=["Connects to the lender's credit system to find customers who are repaying well",
             "Sends each one a top-up offer by SMS, with a link to start a WhatsApp conversation with the agent",
             "Asks the qualifying questions on WhatsApp, such as the collateral offered and how the funds will be used",
             "Logs each complete application in the CRM, where a credit analyst reviews it and makes the decision"],
      stack=["Lender's credit system", "SMS", "WhatsApp", "CRM", "Large language model"],
      results=[("KES 5.4M", "in loan top-up applications taken in during the agent's first week live")]),
 dict(id="odoo-order-to-cash-agent", industry="ERP &amp; operations", tag="Odoo",
      title="Email-to-Odoo order agent for an ERP client",
      summary="An AI agent that reads customer orders from a shared inbox, whether typed in the email, attached as a PDF or sent as a spreadsheet, checks stock and prepares the quotation in Odoo for a person to approve.",
      challenge="Orders arrived in a shared inbox in every format: typed into the email body, attached as PDFs or sent as Excel sheets. Staff had to read each one, re-key it into Odoo, check stock and chase restocking by hand.",
      steps=["Watches the shared orders inbox and reads each order, from the email text, a PDF or an Excel attachment",
             "Matches the customer and products to Odoo records, and hands anything it can't match to a person",
             "Checks stock and creates a quotation in Odoo, then notifies the approver on WhatsApp to review and confirm",
             "When stock is short, prepares a purchase request to restock, so Odoo's normal flow can carry the approved order through"],
      stack=["Odoo ERP", "Email", "PDF and Excel", "WhatsApp", "Large language model"],
      results=[]),
 dict(id="hubspot-crm-agent", industry="Sales &amp; CRM", tag="HubSpot",
      title="HubSpot CRM agent that works your pipeline",
      summary="An AI agent connected to HubSpot that finds and qualifies new leads, replies to them instantly across WhatsApp, email, Instagram and Facebook, and keeps the CRM up to date.",
      challenge="Leads took about five days to get a reply, and many inbound enquiries were missed altogether. Follow-up depended on people remembering to chase leads and log activity, so the CRM went out of date.",
      steps=["Sources new prospects from Google Places and qualifies them into HubSpot",
             "Replies to leads instantly and follows up on WhatsApp, email, Instagram and Facebook",
             "Creates reminders and tasks, logs activity and keeps deal stages up to date",
             "Hands the conversation to a person when the lead asks for one, or for custom offers and price negotiation"],
      stack=["HubSpot CRM", "Google Places", "WhatsApp", "Email", "Instagram", "Facebook", "Large language model"],
      results=[("~5 days → instant", "average time for a lead to get a reply")]),
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

FLOWS = {"loan-top-up-agent": [["Credit system", "The agent finds customers who are repaying well."], ["SMS offer", "Each gets a top-up offer by SMS with a link to WhatsApp."], ["WhatsApp agent", "The agent asks the qualifying questions: collateral, use of funds."], ["CRM", "A complete application is logged in the CRM."], ["Credit analyst", "An analyst reviews and decides, as the human in the loop."]], "odoo-order-to-cash-agent": [["Shared inbox", "An order arrives as email text, a PDF or an Excel sheet."], ["AI agent", "The agent reads the order and matches the customer and products to Odoo."], ["Stock check", "Inventory is checked for every line."], ["Quotation", "A quotation is created in Odoo, ready for review."], ["Approver on WhatsApp", "The approver is notified to review and confirm."], ["Restock", "If stock is short, a purchase request is prepared."]], "hubspot-crm-agent": [["Google Places", "The agent sources new prospects."], ["HubSpot", "Leads are qualified into the CRM."], ["Instant outreach", "Replies and follow-ups go out on WhatsApp, email, Instagram and Facebook."], ["CRM kept current", "Tasks, activity and deal stages are updated automatically."], ["Human handoff", "A person takes over on request, or for custom offers and haggling."]], "support-and-lead-intake-agents": [["Customer message", "A customer or prospect starts a conversation."], ["AI agent", "The agent answers from the business's own information."], ["Lead captured", "New enquiries are qualified with a few short questions."], ["Sales team", "Lead details are passed straight to the team."], ["Human handoff", "Complex or sensitive conversations go to a person."]]}

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
             '</div><p class="meta" style="margin-top:28px">These agents were designed and built by our founder, James, in a previous role as an implementation engineer. Client names and identifying details are withheld. Want an agent like these? See our <a href="{{/services/ai-automation/}}">AI &amp; automation services</a> or <a href="{{/contact/}}">tell us about your process</a>.</p></div></section>')

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
<p class="clock-note">Our 08:00–18:00 EAT day overlaps 6–8 hours with the UK and Europe, and the first 1–2 hours of the US East Coast day.</p>
</div>
<svg class="dune" viewBox="0 0 1440 90" preserveAspectRatio="none" aria-hidden="true"><path d="M0 60 C 240 10, 420 10, 640 45 S 1100 95, 1440 30 L1440 90 L0 90 Z" style="fill:var(--bg)"/></svg>
</header>"""

HOME_BODY = """<section class="band" style="padding-top:24px"><div class="wrap">
<div class="sec-head"><p class="label">What we do</p><h2>One accountable team for everything digital</h2>
<p class="lede">Most small businesses juggle a web designer, a freelance developer and an SEO contractor who never talk to each other. We put all four disciplines under one roof, one project manager and one invoice.</p></div>
<div class="grid g4">""" + service_cards() + """</div>
</div></section>

""" + cases_band("Our work", "AI agents we've built for real businesses") + """
<section class="band"><div class="wrap">
<div class="sec-head"><p class="label">Why Sahara Nova</p><h2>Onshore-quality work without the onshore price tag</h2></div>
<div class="grid g4">
<div class="edge"><span class="fig">40–60%</span><h3>Lower cost</h3><p>Offshore rates can run 40–60% below onshore agencies (Qubit Labs, 2026), and Kenyan rates sit well below UK, EU and US agencies. We pass that saving on and keep a senior team on your project.</p></div>
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
<div class="edge"><h3>M-Pesa &amp; mobile money</h3><p>STK Push checkouts, Paybill and Till payments, and reconciliation with your orders.</p></div>
<div class="edge"><h3>WhatsApp-first</h3><p>WhatsApp Business ordering, support bots and automated follow-ups.</p></div>
<div class="edge"><h3>Light, fast sites</h3><p>Pages built to load on budget Android phones and slow connections.</p></div>
<div class="edge"><h3>Local search</h3><p>Google Business Profile and "near me" SEO for Nairobi, Kampala, Dar and Kigali.</p></div>
</div>
</div>
</div></section>
"""

HOME_FAQ = [
 ("What does Sahara Nova do?", "We are a Nairobi-based digital agency. We design and build websites, custom software and mobile apps, run SEO and digital marketing, and automate business workflows with AI for small and mid-sized businesses worldwide."),
 ("Where do you work?", "We serve businesses in Kenya and across East Africa, with in-person meetings in Nairobi, and work remotely with businesses anywhere in the world. We invoice in US dollars and work on a schedule that overlaps with yours."),
 ("How much does a website cost?", "Our Website Launch package starts from $1,500 for up to six pages with on-page SEO. Larger sites and e-commerce get a fixed quote within two working days of a short call. Web apps start with an $800 discovery week, credited to the build. See our <a href=\"{{/pricing/}}\">pricing page</a>."),
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
<tr><td>Software that doesn't exist yet</td><td><a href="{{/services/software-development/}}">MVP build</a></td><td>Automation, Dedicated Developer</td></tr>
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
<p>For most small businesses, the website is the best salesperson they have. Too many sites are slow, hard to update and invisible on Google. We build sites to load in under two seconds, rank for the searches your customers make, and make it obvious what to do next.</p>
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
<li><strong>MVPs and SaaS products:</strong> from idea to a first version live in 6–10 weeks</li>
<li><strong>Internal tools:</strong> dashboards, admin panels, quoting and inventory systems</li>
<li><strong>Customer portals:</strong> bookings, accounts, document sharing, payments</li>
<li><strong>Mobile apps:</strong> cross-platform iOS and Android with React Native or Flutter</li>
<li><strong>Integrations:</strong> connecting your CRM, accounting, payments and data sources through APIs</li>
</ul>
<h3>How we work</h3>
<p>Every project starts with a paid discovery week ($800, credited to the build if you go ahead). We map the users, the core workflows and the smallest version worth shipping. After that we build in one-week sprints, and you get a working demo link every Friday. You can change priorities between sprints without renegotiating the whole contract.</p>
<h3>Recent work</h3>
<p>We've built an <a href="{{/work/#odoo-order-to-cash-agent}}">order-to-cash agent for an Odoo ERP client</a> and a <a href="{{/work/#loan-top-up-agent}}">loan top-up agent for a digital lender</a>. If you're weighing up an offshore team, read <a href="{{/why-kenya/}}">why companies hire developers in Kenya</a>.</p>
<h3>Typical stack</h3>
<p>TypeScript, React and Next.js, Node.js, Python, PostgreSQL, React Native and Flutter, hosted on AWS, Google Cloud, Vercel or your own infrastructure.</p>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">Start here</span><h3>MVP / Web App</h3><div class="price">$8,000 <small>from</small></div>
<ul><li>$800 discovery week (credited) &amp; clickable prototype</li><li>Design + build of core features</li><li>Weekly demos, fixed milestones</li><li>Deployment, docs &amp; handover</li></ul><a class="btn" href="{{/contact/}}">Scope my project</a></div>
<div class="plan"><h3>Dedicated Developer</h3><div class="price">$6,000 <small>/mo per developer, from</small></div><ul><li>Full-time engineer on your hours</li><li>Managed by our tech lead</li><li>Scale up or down monthly</li></ul></div>
</div>
</div></div></section>""",
 [("How much does it cost to build an MVP?", "Most MVPs we scope fall between $8,000 and $30,000, depending on the number of user roles, integrations and platforms. A discovery week gives you a fixed, itemised quote."),
  ("Fixed price or hourly?", "Discovery and well-defined projects are fixed price. Ongoing product work runs on a monthly Dedicated Developer plan, so you can change priorities freely."),
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
<p>SEO takes months to compound. When you need leads sooner, we run Google Ads and Meta campaigns with proper conversion tracking, so you can see which campaigns bring in enquiries.</p>
<div class="callout"><p><strong>Honest timelines:</strong> we plan on long-tail rankings in 3–6 months and competitive terms in 9–18 months. Google itself gives no timeline, and anyone promising page one in a few weeks is guessing.</p></div>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">One-off</span><h3>SEO Foundation</h3><div class="price">$900 <small>from</small></div>
<ul><li>Full technical audit + fixes that need no developer time</li><li>Keyword research &amp; page map</li><li>Google Business Profile &amp; Search Console</li><li>Prioritised 90-day roadmap</li></ul><a class="btn" href="{{/contact/}}">Book an audit</a></div>
<div class="plan"><h3>SEO &amp; Content Retainer</h3><div class="price">$750 <small>/month, from</small></div><ul><li>2 optimised articles a month</li><li>On-page improvements &amp; link building</li><li>Monthly report and strategy call</li></ul></div>
</div>
</div></div></section>""",
 [("How long does SEO take to work?", "We plan on early movement on long-tail keywords within 3–6 months and competitive terms in 9–18 months, but nobody can promise a timeline. Technical fixes can show results sooner if your site had indexing problems."),
  ("Do you guarantee first-page rankings?", "No. Nobody controls Google's rankings. We commit to the work, the process and transparent reporting on rankings, traffic and leads."),
  ("Do you offer white-label SEO for agencies?", "Yes. We deliver audits, content and technical fixes under your brand, with your client reporting templates."),
  ("What's included in a monthly SEO report?", "Organic traffic, keyword rankings, Search Console impressions and clicks, conversions from organic search, work completed and next month's priorities.")])

AI = service_page(
 "services/ai-automation/", "AI & automation",
 "AI Automation Agency for Small Businesses | Sahara Nova",
 "AI agents and workflow automation for small businesses: email orders into Odoo, HubSpot CRM agents, support bots and lead intake. From $1,200.",
 "Service · AI &amp; automation",
 "AI automation for small businesses",
 "Give your team back the hours lost to copy-pasting, chasing and reporting. We automate the repetitive work and add AI where it pays for itself.",
 {"name": "AI and business process automation", "type": "Business process automation", "from": "1200"},
 """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Automate the busywork, not the judgement</h2>
<p>Most small businesses lose hours every week to manual tasks: moving leads from forms into a CRM, building the same weekly report, answering the same customer questions. We find those tasks, measure them and automate the ones with a clear payback. Our guide to <a href="{{/blog/which-processes-to-automate-with-ai/}}">choosing which processes to automate with AI</a> explains how.</p>
<h3>Common automations we build</h3>
<ul>
<li><strong>Lead handling:</strong> form → CRM → instant personalised reply → sales alert</li>
<li><strong>Reporting:</strong> weekly dashboards assembled automatically from ads, CRM and accounting</li>
<li><strong>Customer support:</strong> AI assistants trained on your own documents, with human handoff</li>
<li><strong>Document processing:</strong> invoices, receipts and forms read and filed by AI</li>
<li><strong>Operations:</strong> onboarding checklists, reminders, approvals and data syncs between tools</li>
<li><strong>AI agents:</strong> agents that take actions in your systems, like processing orders in your ERP or working leads in your CRM. See <a href="{{/work/}}">our case studies</a></li>
<li><strong>Lending:</strong> loan top-up offers, application intake and compliant repayment reminders. See <a href="{{/blog/ai-agents-for-lenders-kenya/}}">AI agents for lenders and SACCOs</a></li>
</ul>
<h3>Tools</h3>
<p>We connect AI agents to the systems you already run, including Odoo ERP, HubSpot CRM, email and your website chat. We use Make, Zapier and n8n for fast, maintainable workflows, and write custom code with leading AI model APIs when a no-code tool isn't enough. Every automation ships with documentation and error alerts, so nothing fails silently.</p>
<h3>Responsible AI</h3>
<p>We keep a human in the loop for anything customer-facing, minimise the personal data sent to AI services, and document which models and vendors process your data.</p>
</div>
<div class="grid" style="align-content:start">
<div class="plan feature"><span class="tag">Quick win</span><h3>Automation Sprint</h3><div class="price">$1,200 <small>from</small></div>
<ul><li>Process audit of one team</li><li>1–2 workflows automated</li><li>Error alerts &amp; documentation</li><li>Delivered in about 2 weeks</li></ul><a class="btn" href="{{/contact/}}">Find my quick wins</a></div>
<div class="plan"><h3>AI Assistant</h3><div class="price">$2,500 <small>from</small></div><ul><li>Website or internal assistant</li><li>Trained on your documents</li><li>Human handoff &amp; analytics</li></ul></div>
</div>
</div></div></section>
<section class="band"><div class="wrap"><div class="sec-head"><p class="label">Watch an agent work</p><h2>From an emailed order to an approved quotation</h2>
<p class="lede">This is the order agent we built for an Odoo ERP client. Each step used to be done by hand. Hover over or tap a step to see what the agent does.</p></div>""" + flow_fig("odoo-order-to-cash-agent") + """
<div class="btn-row"><a class="btn ghost" href="{{/work/#odoo-order-to-cash-agent}}">Read the case study</a></div></div></section>""" + cases_band("Our work", "AI agents we've built"),
 [("What can a small business automate?", "Good candidates are frequent, rule-based and digital: lead routing, follow-up emails, invoicing reminders, reporting, data entry between tools and first-line support questions."),
  ("Do I need to change my existing software?", "Usually not. We connect the tools you already use, such as Odoo, HubSpot, Pipedrive, Xero, QuickBooks, Google Workspace, Microsoft 365 or Shopify, through their APIs."),
  ("Can you build AI agents for Odoo or HubSpot?", "Yes. We have built an agent that reads emailed orders, including PDFs and spreadsheets, checks stock and prepares quotations in Odoo for approval, and a HubSpot agent that follows up with leads, sets reminders and keeps the CRM up to date. See our <a href=\"{{/work/}}\">case studies</a>, our guide to <a href=\"{{/blog/automate-email-orders-into-odoo-with-ai/}}\">automating email orders into Odoo</a>, or our comparison of <a href=\"{{/blog/hubspot-breeze-vs-custom-ai-agent/}}\">HubSpot's own agents vs a custom agent</a>."),
  ("Is our data safe with AI tools?", "We choose business-tier AI services that don't train on your data, minimise what's sent, and document every data flow. We sign a data processing agreement on request."),
  ("How do you measure ROI?", "Before building, we estimate hours saved per month. After launch, we track runs and time saved so you can see the payback."),
  ("What does it cost to run an AI agent?", "Running costs are billed at cost: AI model usage, WhatsApp message fees and any automation plan such as Make, Zapier or n8n. Our AI Care Plan, from $250 a month, covers monitoring, fixes and updates.")])

WHY_KENYA_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">Africa's tech hub, in Europe's working day</h2>
<p>Nairobi, nicknamed the "Silicon Savannah", is home to a large and growing community of software engineers, designers and digital marketers. M-Pesa, the mobile money platform that changed payments in Kenya, launched and scaled here, and the city's fintech, e-commerce and startup scene keeps producing experienced tech talent.</p>
<h3>1. Time zone overlap</h3>
<p>Kenya runs on East Africa Time (UTC+3) all year, with no daylight saving. That gives you 6–8 hours of live overlap with the UK and Europe, the same time zone as Saudi Arabia and Qatar (one hour behind the UAE), and 1–2 hours at the start of the US East Coast day. That is more overlap with Europe than South Asia offers.</p>
<h3>2. English-first communication</h3>
<p>English is an official language of Kenya and the language of business, university and government, so briefs, calls and documentation need no translation.</p>
<h3>3. Cost</h3>
<p>Kenyan agency rates generally range from under $25 to $99 an hour, compared with $50–$199 in Western Europe and up to $300 in major US cities. Qubit Labs estimates that offshore prices can be 40–60% lower than onshore rates.</p>
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
</tbody></table><p class="meta" style="padding:0 16px 14px">Source: <a href="https://qubit-labs.com/?p=8417">Qubit Labs, Offshore Software Development Rates by Country</a>, updated April 2026.</p></div>
</div>
</div></div></section>"""

PRICING_BODY = """<section class="band"><div class="wrap">
<div class="sec-head"><p class="label">Projects</p><h2>Fixed-price packages</h2><p class="lede">Every project starts with a free 30-minute call. Packages get a written, fixed quote within two working days of it. MVPs and custom AI agents start with an $800 discovery week, credited to the build, which ends in a fixed, itemised quote. The prices below are starting points. Your quote depends on scope, content and integrations.</p></div>
<div class="grid g4">
<div class="plan feature"><span class="tag">Most popular</span><h3>Website Launch</h3><div class="price">$1,500 <small>from</small></div><ul><li>Up to 6 pages, custom design</li><li>On-page SEO, schema, sitemap</li><li>Analytics &amp; Search Console</li><li>2–3 weeks</li></ul><a class="btn" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>Growth Website</h3><div class="price">$3,500 <small>from</small></div><ul><li>Up to 15 pages + CMS/blog</li><li>Conversion tracking &amp; CRM forms</li><li>Keyword map + 3 articles</li><li>4–6 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>E-commerce</h3><div class="price">$4,500 <small>from</small></div><ul><li>Shopify or WooCommerce</li><li>Up to 50 products loaded</li><li>Payments, shipping, product SEO</li><li>4–8 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>MVP / Web App</h3><div class="price">$8,000 <small>from</small></div><ul><li>$800 discovery week (credited) &amp; prototype</li><li>Core features, weekly demos</li><li>Deployment &amp; documentation</li><li>6–10 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Scope my project</a></div>
<div class="plan"><h3>SEO Foundation</h3><div class="price">$900 <small>from</small></div><ul><li>Technical audit + quick fixes</li><li>Keyword research &amp; page map</li><li>Google Business Profile</li><li>90-day roadmap</li></ul><a class="btn ghost" href="{{/contact/}}">Book an audit</a></div>
<div class="plan"><h3>Automation Sprint</h3><div class="price">$1,200 <small>from</small></div><ul><li>Process audit</li><li>1–2 workflows automated</li><li>Error alerts &amp; docs</li><li>About 2 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Find quick wins</a></div>
<div class="plan"><h3>AI Assistant</h3><div class="price">$2,500 <small>from</small></div><ul><li>Website or internal assistant</li><li>Trained on your documents</li><li>Human handoff &amp; analytics</li><li>3–4 weeks</li></ul><a class="btn ghost" href="{{/contact/}}">Get a quote</a></div>
<div class="plan"><h3>Custom AI Agent</h3><div class="price">$3,500 <small>from</small></div><ul><li>Agents that act in your ERP or CRM</li><li>e.g. order intake, lead follow-up</li><li>Human-in-the-loop controls</li><li><a href="{{/work/}}">See examples</a></li></ul><a class="btn ghost" href="{{/contact/}}">Scope my agent</a></div>
</div>
<p class="meta" style="margin-top:14px">SEO Foundation fixes cover anything that needs no developer time, such as titles, metadata, Search Console and Google Business Profile; larger fixes are quoted separately. Mobile apps, and M-Pesa integration for an existing site, are quoted after discovery.</p>
</div></section>
<section class="band alt"><div class="wrap">
<div class="sec-head"><p class="label">Ongoing</p><h2>Monthly plans</h2></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th>From</th><th>Includes</th></tr></thead><tbody>
<tr><td><strong>SEO &amp; Content Retainer</strong></td><td class="num">$750/mo</td><td>2 articles a month, on-page work, link building, monthly report</td></tr>
<tr><td><strong>Dedicated Developer</strong></td><td class="num">$6,000/mo</td><td>Full-time engineer on your hours, managed by our tech lead</td></tr>
<tr><td><strong>Website Care Plan</strong></td><td class="num">$150/mo</td><td>Hosting, updates, backups, uptime monitoring, 2 hours of changes</td></tr>
<tr><td><strong>AI Care Plan</strong></td><td class="num">$250/mo</td><td>Monitoring, error alerts, fixes, prompt and knowledge updates, monthly review (running costs billed at cost)</td></tr>
<tr><td><strong>Ad Management</strong></td><td class="num">$500/mo</td><td>Google or Meta campaigns, conversion tracking, monthly optimisation (ad spend separate)</td></tr>
</tbody></table></div>
<p class="meta" style="margin-top:14px">Prices in USD, excluding any applicable taxes, paid by bank transfer. Clients in Kenya pay the same prices and can pay in KES by bank transfer at the day's exchange rate. Projects: 50% to start, 50% on launch. Plans: monthly in advance, cancel with 30 days' notice.</p>
</div></section>"""

PRICING_FAQ = [
 ("How much does a website cost for a small business?", "A professional small business website with custom design and on-page SEO typically costs $1,500–$5,000 with us. UK agencies typically charge £3,000–£5,000 for a five-page site, and UK freelancers £1,500–£3,000 (Whito, October 2026). E-commerce and web apps cost more because of payments, integrations and custom features."),
 ("Why are your prices lower than UK or US agencies?", "Our team is based in Nairobi, where operating costs are lower. You get the same process and quality standards, with the saving passed on to you."),
 ("Are there hidden costs?", "No. Your quote lists everything, including third-party costs such as hosting, premium plugins, stock images, ad spend, AI model usage, WhatsApp message fees and automation plans such as Make, Zapier or n8n. You pay those directly or we pass them through at cost."),
 ("Which currencies and payment methods do you accept?", "We invoice in US dollars, paid by bank transfer. Clients in Kenya can also pay the equivalent in Kenyan shillings by bank transfer."),
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
<p>The name comes from two ideas. The <em>Sahara</em> stands for where we come from, a young continent, with a median age of about 19. A <em>nova</em> is a star that suddenly shines brighter, which is what we want every client's business to do online.</p>
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
<div class="edge"><span class="fig">USD · KES</span><p>Invoiced in US dollars, or shillings in Kenya.</p></div>
</div>
</div></div></section>
""" + TEAM_SECTION + """<section class="band" id="how-we-work"><div class="wrap">
<div class="sec-head"><p class="label">How a typical website project runs</p><h2>From first call to launch in about four weeks</h2><p class="lede">Software and AI projects follow the same rhythm: a short discovery, a fixed plan, then weekly demos until launch.</p></div>
<div class="steps">
<div class="step" data-w="Day 1"><h3>Discovery call</h3><p>30 minutes on goals, audience and budget. You get a fixed quote within two working days of the call.</p></div>
<div class="step" data-w="Week 1"><h3>Strategy &amp; design</h3><p>Keyword research, sitemap and page designs, all approved before we write any code.</p></div>
<div class="step" data-w="Weeks 2–3"><h3>Build &amp; content</h3><p>Development with weekly demo links. SEO, analytics and schema are built in from day one.</p></div>
<div class="step" data-w="Week 4"><h3>Launch &amp; grow</h3><p>Go live, submit to Google, then optional monthly SEO and care plans.</p></div>
</div>
</div></section>
<section class="band"><div class="wrap"><div class="grid g3">
<a class="service" href="{{/work/}}"><h3>See our work</h3><p>AI agents we've built for lending, ERP and CRM teams, with real results.</p><span class="more">View case studies →</span></a>
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
<div><b>Payment</b>USD or KES by bank transfer</div>
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
<a class="post-card" href="{{/blog/automate-email-orders-into-odoo-with-ai/}}"><span class="meta">Guide · 30 Oct 2026 · 9 min read</span><h3>How to automate email orders into Odoo with AI</h3><p>Turn order emails, PDFs and spreadsheets into Odoo quotations, with careful matching, human approval and the API changes to plan for.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/hubspot-breeze-vs-custom-ai-agent/}}"><span class="meta">Guide · 28 Oct 2026 · 8 min read</span><h3>HubSpot's AI agents vs a custom AI agent: which do you need?</h3><p>What Breeze agents do and cost today, when they're the right choice, and when a custom agent is worth building.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/which-processes-to-automate-with-ai/}}"><span class="meta">Guide · 27 Oct 2026 · 8 min read</span><h3>Which processes should you automate with AI? A practical audit</h3><p>Map the work, score each candidate, and choose between simple automation, an AI step or an agent, before you spend anything.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/ai-agents-for-lenders-kenya/}}"><span class="meta">Guide · 27 Oct 2026 · 7 min read</span><h3>AI agents for digital lenders and SACCOs in Kenya</h3><p>How a WhatsApp top-up agent took in KES 5.4M in applications in its first week, with a credit analyst still making every decision.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/website-cost-in-kenya/}}"><span class="meta">Guide · 22 Oct 2026 · 7 min read</span><h3>How much does a website cost in Kenya in 2026?</h3><p>What you get at each price level, from KES 15,000 template sites to custom builds, plus the yearly costs after launch.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/mpesa-stk-push-integration-guide/}}"><span class="meta">Guide · 22 Oct 2026 · 9 min read</span><h3>M-Pesa STK Push integration: a step-by-step guide</h3><p>How Daraja STK Push works, what you need before you start, and the mistakes behind most failed integrations.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
<a class="post-card" href="{{/blog/outsourcing-web-development-to-kenya/}}"><span class="meta">Guide · 23 Sep 2026 · 8 min read</span><h3>What it costs to outsource web development to Kenya in 2026, and how to do it well</h3><p>Rates by region, how the EAT time zone overlaps with yours, and a checklist for vetting a Kenyan agency.</p><span class="more" style="color:var(--accent-ink);font-weight:600">Read the guide →</span></a>
</div></div></section>"""

ARTICLE_BODY = """<section class="band"><div class="wrap"><article class="prose">
<p class="meta">Published 23 September 2026 · Updated 28 October 2026 · By <a href="{{/about/#team}}">James Njoroge</a>, founder · 8 min read</p>
<p>If you run a small or mid-sized business in the UK, Europe or the US and are weighing up an offshore team for a new website or app, Kenya, and Nairobi in particular, is worth a close look.</p>
<p>This guide covers what it costs, how the time zones work, where Kenya fits against other outsourcing regions, and how to pick a partner without getting burned.</p>

<h2>Why Kenya?</h2>
<p>Nairobi has built a reputation as the "Silicon Savannah". Mobile money platform M-Pesa launched and scaled here, and the city hosts a busy startup scene, international tech companies and a steady stream of computer science graduates. Three practical factors matter most to a small business buyer:</p>
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
<p class="meta">Source: <a href="https://qubit-labs.com/?p=8417">Qubit Labs, Offshore Software Development Rates by Country</a>, updated April 2026.</p>
<p>Rates vary widely within Kenya too, from large vendors at the low end of that range to premium studios at the top. Compare like with like: ask who will do the work, how senior they are, and whether the price is fixed. For reference, our own published packages start at <a href="{{/pricing/}}">$1,500 for a small business website</a>.</p>

<h2>Time zones: the underrated advantage</h2>
<p>With outsourcing, time zone overlap often matters more than the hourly rate. When your developer is asleep during your whole working day, every question costs 24 hours. Kenya doesn't observe daylight saving, so overlap with Europe stays predictable:</p>
<ul>
<li><strong>UK:</strong> 2 hours behind Nairobi in summer, 3 in winter, giving 6–7 hours of shared working time</li>
<li><strong>Central Europe:</strong> 1–2 hours behind, giving 7–8 hours of overlap</li>
<li><strong>Gulf:</strong> the same time as Nairobi in Saudi Arabia, Qatar, Kuwait and Bahrain, and 1 hour ahead in the UAE and Oman, giving almost a full shared day</li>
<li><strong>US East Coast:</strong> 7–8 hours behind, so your morning is our late afternoon, with 1–2 hours of overlap (2 in US summer, 1 in winter) plus async handoffs</li>
</ul>

<h2>Kenya vs other outsourcing destinations</h2>
<p><strong>Eastern Europe</strong> offers strong engineering and a good EU time zone, at rates between Kenya's and Western Europe's. <strong>South and Southeast Asia</strong> offer low rates but shorter overlap with Europe and almost none with the US East Coast. <strong>Latin America</strong> is the natural nearshore choice for US companies. Kenya sits in a useful spot: good overlap with Europe and the Middle East, English as an official language, and rates similar to or below Eastern Europe's.</p>

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
<p>If you'd like to see how that works in practice, <a href="{{/contact/}}">send us your brief</a> and after a short call we'll send a fixed quote within two working days, or see our <a href="{{/services/web-development/}}">web development</a> and <a href="{{/pricing/}}">pricing</a> pages.</p>
</article></div></section>"""


BYLINE = '<p class="meta">Published {date} · By <a href="{{{{/about/#team}}}}">James Njoroge</a>, founder · {mins} min read</p>'

WEBSITE_COST_KENYA_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="22 October 2026 · Updated 28 October 2026", mins=7) + """
<p>Ask five web designers in Nairobi what a website costs and you'll get five answers between KES 5,000 and KES 1 million. They're not all wrong. They're quoting for very different things. This guide breaks down what each price level gets you in 2026, what you'll pay every year after launch, and how to tell which one your business needs.</p>

<h2>The short answer</h2>
<div class="table-wrap"><table><thead><tr><th>Type of website</th><th>Cost (KES)</th><th>Good for</th></tr></thead><tbody>
<tr><td>Do it yourself (WordPress or a site builder)</td><td class="num">About 2,100 a year (domain and hosting)</td><td>Testing an idea, a simple online presence</td></tr>
<tr><td>5-page site from a freelance web designer</td><td class="num">15,000–80,000</td><td>A brochure site that mainly needs to look credible</td></tr>
<tr><td>Custom business website with SEO</td><td class="num">From about 195,000</td><td>Businesses that want Google enquiries</td></tr>
<tr><td>Online shop with M-Pesa checkout</td><td class="num">From about 585,000</td><td>Selling products online</td></tr>
<tr><td>Web app or customer portal</td><td class="num">From about 1,000,000</td><td>Bookings, accounts, dashboards, SaaS</td></tr>
</tbody></table></div>
<p class="meta">DIY and freelancer ranges, domain and shared hosting prices: <a href="https://hostiko.co.ke/blog/how-much-website-cost-kenya-2026">Hostiko, "How much does a website cost in Kenya"</a>, April 2026. Custom, shop and web app figures are Sahara Nova's published starting prices ($1,500, $4,500 and $8,000), converted at about KES 130 to the dollar (October 2026).</p>

<h2>Why the prices are so far apart</h2>
<p>The gap isn't mostly about design. A KES 30,000 site and a KES 200,000 site can look similar on the day they launch. The difference is in the work you can't see:</p>
<ul>
<li><strong>Research before design.</strong> A cheaper site starts from a template. A custom site starts from what your customers search for and what they need to see before they call you.</li>
<li><strong>Speed on real phones.</strong> Most Kenyan visitors arrive on mobile data and mid-range Android phones. Heavy themes and plugins load slowly on those connections, and visitors give up before the page appears.</li>
<li><strong>SEO foundations.</strong> Page titles, structured data, a sitemap, internal links and Google Business Profile setup decide whether anyone finds the site at all.</li>
<li><strong>Content.</strong> Writing that answers real questions takes time. Many cheap quotes assume you'll supply all the text.</li>
<li><strong>Integrations.</strong> M-Pesa checkout, WhatsApp ordering, a CRM or eTIMS-ready invoicing each add real engineering work.</li>
</ul>

<h2>Costs after launch</h2>
<p>A website keeps costing money after it goes live. Budget for these every year:</p>
<ul>
<li><strong>A .co.ke domain:</strong> around KES 1,200 a year (<a href="https://hostiko.co.ke/blog/how-much-website-cost-kenya-2026">Hostiko, 2026</a>).</li>
<li><strong>Hosting:</strong> basic shared hosting can cost under KES 1,000 a year. A busy shop or web app needs more capable hosting, priced by traffic and resources.</li>
<li><strong>Email:</strong> business email on your domain. Some providers have free plans for very small teams; paid plans charge per mailbox each month.</li>
<li><strong>Maintenance:</strong> updates, backups, security fixes and small changes. Ours is the Website Care Plan from $150 a month (about KES 19,500).</li>
<li><strong>Marketing:</strong> SEO content or ads if you want the site to keep bringing in enquiries.</li>
</ul>
<div class="callout"><p><strong>Make sure you own your domain.</strong> A common and costly problem is a domain registered in a former designer's name or account. When it lapses, the website and email go down. Ask for the domain to be registered to your business, with login details you keep.</p></div>

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
<p>Expect to pay KES 15,000–80,000 for a simple five-page site from a freelancer. Our own custom business sites, built to win enquiries from Google, start at about KES 195,000. Online shops and web apps cost more because of payments and custom features. Whatever you choose, keep your domain in your own name. If you'd like a fixed price for your project, see <a href="{{/pricing/}}">our pricing</a> or <a href="{{/contact/}}">send us a short brief</a>. You can pay in KES by bank transfer. More on how we work with local businesses is on our <a href="{{/east-africa/}}">Kenya and East Africa page</a>.</p>
</article></div></section>"""

MPESA_GUIDE_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="22 October 2026 · Updated 27 October 2026", mins=9) + """
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
<div class="callout"><p><strong>The prompt expires quickly.</strong> The PIN prompt stays on the customer's phone for well under a minute. Developer guides report anywhere from about 30 to 60 seconds, and it varies with the network. Only send an STK Push when the customer has just pressed "Pay" and is holding their phone. Don't fire one from a reminder, a scheduled job or a chat the customer may not be watching, because it will usually time out unseen.</p></div>
<p>If the prompt times out, don't resend it automatically. After 30–45 seconds without a result, show a "Resend M-Pesa prompt" button, confirm the previous attempt has failed before sending another, and use a new reference for each attempt. Offer Paybill or Till details as a fallback.</p>

<h2>Step 3: handle the callback</h2>
<p>When the customer finishes, Safaricom posts a JSON result to your callback URL. Inside <code>Body.stkCallback</code> you'll find the <code>CheckoutRequestID</code>, a <code>ResultCode</code> and, only for successful payments, <code>CallbackMetadata</code> with the amount, the M-Pesa receipt number, the transaction time and the phone number.</p>
<div class="table-wrap"><table><thead><tr><th>ResultCode</th><th>What it means</th><th>What to do</th></tr></thead><tbody>
<tr><td class="num">0</td><td>Paid</td><td>Check the amount, save the receipt number, mark the order paid</td></tr>
<tr><td class="num">1032</td><td>Customer cancelled</td><td>Let them try again</td></tr>
<tr><td class="num">1037</td><td>Timed out: no response from the customer, or phone unreachable</td><td>Offer a customer-triggered retry or the Paybill/Till details</td></tr>
<tr><td class="num">2001</td><td>Wrong PIN</td><td>Let them try again</td></tr>
<tr><td class="num">1</td><td>Insufficient balance</td><td>Tell the customer clearly</td></tr>
</tbody></table></div>
<p class="meta">Result codes: Safaricom Daraja; PaybillKE and Mctaba developer guides, 2026. Branch on <code>ResultCode</code>, not the description text, which can change.</p>
<p>Reply to every callback quickly with an HTTP 200, and do any slow work, such as sending emails, after you respond.</p>

<h2>Step 4: check when no callback arrives</h2>
<p>Callbacks sometimes arrive late or not at all. Don't count on Safaricom resending one you missed: a developer who tested failed deliveries saw no retry within the following 30–40 minutes. Run a background job that uses the STK Push query endpoint (<code>/mpesa/stkpushquery/v1/query</code>) with the <code>CheckoutRequestID</code> to check any order still pending after two to three minutes.</p>
<p>Read query results carefully. A "transaction does not exist" response (<code>500.001.1001</code>) has been seen for payments that did exist, and "still under processing" means the payment is in progress, not failed. Treat both as "unknown, check again later", and only show the customer a failure once a query confirms it. Meanwhile, show a "waiting for payment" screen that polls your own server.</p>

<h2>Mistakes that cause most failed integrations</h2>
<ul>
<li><strong>Trusting the callback blindly.</strong> Anyone who finds your callback URL could post a fake success. Use a long, unguessable callback path, confirm the <code>CheckoutRequestID</code> matches an order you created, check the amount, and use the query endpoint to confirm high-value payments.</li>
<li><strong>Processing or charging twice.</strong> Duplicates happen: double-clicks, your own retries, and occasionally a repeated callback. Store each attempt by <code>CheckoutRequestID</code> with a unique constraint before the callback arrives, ignore callbacks for attempts already marked paid or failed, and block a new STK Push while one is pending for the same order.</li>
<li><strong>Calling Daraja from the browser.</strong> This exposes your Consumer Secret and passkey. Keep every Daraja call on the server.</li>
<li><strong>Using a local or HTTP callback URL.</strong> Safaricom needs to reach a public HTTPS address.</li>
<li><strong>Forgetting go-live differences.</strong> Production uses <code>api.safaricom.co.ke</code>, your own shortcode and a production passkey, not the sandbox values.</li>
<li><strong>No reconciliation.</strong> Match M-Pesa receipt numbers against your Paybill or Till statement regularly, so missed callbacks don't turn into unhappy customers.</li>
</ul>

<h2>Going live</h2>
<p>When everything works in the sandbox, start a Go Live application in the Daraja portal with the same account. You'll need your business registration, KRA PIN, the signatory's ID, an active Paybill or Till, and an authorisation letter if the applicant isn't the owner or a director. Safaricom reviews applications manually. Developer guides report a few business days, sometimes longer. Once approved you receive production credentials: Consumer Key and Secret, shortcode and passkey.</p>
<p>Swap the base URL, the shortcode and the passkey. Keep credentials in environment variables, not in your code. Run a few small real payments and check each one against your M-Pesa statement before you announce it.</p>

<h2>Do it yourself or hire help?</h2>
<p>Sending the prompt is the easy part. The work that protects your money is everything around it: timeouts and customer-triggered retries, callbacks you can trust, duplicate protection, status queries and reconciliation. If those aren't in place, you will eventually ship goods for payments that never arrived, or charge someone twice. If you'd like it done for you, as part of a new website or added to an existing one, see our <a href="{{/east-africa/}}">work for Kenyan and East African businesses</a> or <a href="{{/contact/}}">send us a brief</a>. Planning a full new site? Our guide to <a href="{{/blog/website-cost-in-kenya/}}">what a website costs in Kenya</a> covers budgets.</p>
</article></div></section>"""

ODOO_ORDERS_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="30 October 2026", mins=9) + """
<p>If your customers order by email, someone on your team spends part of every day reading those emails and typing them into Odoo. The orders arrive in every shape: a few lines typed into the message, a PDF purchase order, a spreadsheet with forty rows. Re-keying them is slow, and the mistakes show up later as wrong deliveries and credit notes.</p>
<p>AI is now good at the reading part. This guide covers what Odoo does and doesn't do out of the box, the flow we use for an order agent, and the design decisions that separate a reliable setup from one that quietly creates bad orders. It draws on an <a href="{{/work/#odoo-order-to-cash-agent}}">order agent we built for an Odoo client</a>.</p>

<h2>What Odoo does out of the box, and what it doesn't</h2>
<ul>
<li><strong>Email aliases</strong> can turn an incoming email into a record in Odoo. That gets the email into the system, but it doesn't read the order lines and build a quotation from them.</li>
<li><strong>Odoo 19's AI features</strong> include an "Ask AI" assistant, AI fields, configurable AI agents and AI server actions. Odoo's documentation is clear about the limits: Ask AI can open views and reports but can't create or change data, and an AI server action "does not enforce business rules" or "guarantee the correctness of the operation". The business rules still have to come from you.</li>
<li><strong>Document digitisation (OCR)</strong> is built for supplier bills on the accounting side, not for customer purchase orders.</li>
<li><strong>Third-party apps</strong> on the Odoo Apps store offer AI order extraction. Some will fit simple cases. Evaluate them against the design points below before relying on one.</li>
</ul>
<p>So for most businesses, reading customer orders and turning them into clean quotations needs either a well-chosen app or a custom agent connected to Odoo.</p>

<h2>The flow that works</h2>
<ol>
<li><strong>Watch one shared orders inbox.</strong> Ask customers to send orders to a single address, so the agent has one place to look.</li>
<li><strong>Read the order in whatever format it arrives.</strong> Email text, PDF attachments and Excel sheets each need handling, and scanned PDFs need text recognition first.</li>
<li><strong>Match the customer and every product to Odoo records.</strong> This is the step that decides accuracy. Anything the agent can't match confidently goes to a person, never to a guess.</li>
<li><strong>Check stock</strong> for each line before anything is promised.</li>
<li><strong>Create a quotation, not a confirmed order.</strong> Then notify the approver, who reviews it in Odoo and confirms.</li>
<li><strong>Prepare a restock request when stock is short,</strong> for a person to approve before anything goes to a supplier.</li>
</ol>
<p>Once a person confirms the quotation, Odoo's normal process takes over: delivery, invoicing and payment follow the workflow you already use.</p>

<h2>Design decisions that matter</h2>
<h3>Start with quotations and a human approver</h3>
<p>Confirming a quotation in Odoo commits you to the order and starts the rest of your workflow, such as delivery orders when Inventory is installed. Keep a person approving every quotation until you have weeks of evidence that the agent's quotations need no edits. Track how often the approver changes something. That number tells you whether more autonomy is safe.</p>

<h3>Matching is the hard part</h3>
<p>Customers rarely use your product names. They use their own codes, old descriptions, or "the same as last time". Build the matching around your real data: internal references, any customer-specific codes you keep, and past orders from the same customer. Set a clear rule: if a line can't be matched with confidence, the agent flags it for a person rather than picking the closest product.</p>

<h3>Take prices from Odoo, not from the email</h3>
<p>Use your Odoo pricelists to price the quotation. If the customer's PO states a different price, flag the difference for the approver instead of copying it.</p>

<h3>Catch duplicates</h3>
<p>Customers resend orders, forward them with "please confirm", or send an amended version. Check each new email against recent quotations, for example by the customer's PO number and the email thread, before creating anything.</p>

<h3>Don't fight your replenishment settings</h3>
<p>If you already use Odoo's reordering rules or make-to-order routes, they may create purchase requests on their own. Decide which mechanism owns restocking so you don't get two requests for the same shortfall.</p>

<h3>Notifications: WhatsApp rules apply</h3>
<p>Notifying the approver on WhatsApp works well because people see it quickly. A message your business starts on WhatsApp must use an approved template and go to someone who has opted in, and template messages are charged per message. Keep the message short (customer, order value, a link to the quotation) and leave the details in Odoo.</p>

<h3>Leave an audit trail</h3>
<p>Log on each quotation what the agent did and which email it came from, so anyone can trace an order back to its source.</p>

<h2>Technical prerequisites</h2>
<ul>
<li><strong>API access.</strong> On Odoo Online, the external API is only available on the Custom plan, not on One App Free or Standard. Odoo.sh and on-premise installations can use it.</li>
<li><strong>Use the JSON-2 API.</strong> Odoo's new JSON-2 API is available from Odoo 19 (and Odoo Online 18.4). The older XML-RPC and JSON-RPC endpoints are deprecated, with removal scheduled for Odoo Online 21.1 (winter 2027) and Odoo 22 (autumn 2028). Don't build a new integration on them.</li>
<li><strong>A dedicated integration user</strong> with only the access rights the agent needs, using an API key you rotate, rather than a staff member's login.</li>
<li><strong>Real samples to test with.</strong> Collect a few weeks of actual order emails, including the messy ones, before building. They are your test set.</li>
</ul>

<h2>How to measure it</h2>
<p>Before you switch it on, record the current time per order and how often orders are entered wrongly. Afterwards, track:</p>
<ul>
<li>the share of orders matched completely without help</li>
<li>how often the approver edits a quotation</li>
<li>the time from email to approved quotation</li>
<li>errors that reach the customer</li>
</ul>
<p>Widen what the agent does on its own only when those numbers support it.</p>

<h2>When not to do this</h2>
<ul>
<li>You receive only a handful of email orders a week.</li>
<li>Most customers could use a portal or online shop instead, which gives you structured orders without AI.</li>
<li>Your product data in Odoo is incomplete or duplicated. Clean it first, or the agent will match against bad records.</li>
</ul>

<h2>The bottom line</h2>
<p>An order agent removes the re-keying, but the value comes from the design: one inbox, careful matching, quotations a person approves, prices from Odoo and a clear handoff for anything uncertain. If you'd like help deciding whether your order volume justifies it, see our <a href="{{/services/ai-automation/}}">AI and automation services</a>, read <a href="{{/blog/which-processes-to-automate-with-ai/}}">how to choose which processes to automate</a>, or <a href="{{/contact/}}">send us a few sample orders</a>, with personal details removed.</p>
<p class="meta">Sources: Odoo documentation on AI features and inbound email, as summarised by Carly (July 2026); Apideck, "How to integrate with the Odoo API" (updated 27 October 2026); Xyphen IT, "Odoo 19 and the end of XML-RPC" (May 2026); WhatsApp Business Policy and pricing. Checked 30 October 2026.</p>
</article></div></section>"""

BREEZE_VS_CUSTOM_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="28 October 2026", mins=8) + """
<p>If your business runs on HubSpot, you have two ways to add AI agents: switch on HubSpot's own Breeze agents, or build a custom agent around your process. Agencies that build agents, ourselves included, have an obvious bias here, so we'll say it up front: for many HubSpot customers, the built-in agents are the right place to start.</p>
<p>This guide sets out what HubSpot's agents do today, what they cost, and the specific situations where a custom agent is worth building instead.</p>

<h2>What HubSpot's agents do today</h2>
<p>HubSpot groups its AI under the Breeze name. The two agents most businesses ask about are:</p>
<ul>
<li><strong>Customer agent.</strong> Answers customer questions from your own content, can take actions in your CRM, and hands over to your team with full context. HubSpot lists email, chat, forms, WhatsApp, Facebook Messenger and voice as channels. It requires a Professional or Enterprise edition. HubSpot quotes an average resolution rate of 70% on its <a href="https://www.hubspot.com/products/artificial-intelligence/ai-customer-service-agent">customer agent page</a> and 65% in its <a href="https://www.hubspot.com/agent-hub-roi-calculator">ROI calculator</a>.</li>
<li><strong>Prospecting agent.</strong> Researches leads in your CRM and recommends personalised outreach.</li>
</ul>
<p>HubSpot also offers agents for content, data enrichment and deal progression, plus an Agent Builder for creating your own agents inside HubSpot. Those agents can reach outside HubSpot through a set of supported connectors, including Gmail, Google Calendar, Slack, Notion, Asana, Gong and Xero, and through Zapier. You set each tool to "Always allow", "Ask permission" or "Never allow".</p>

<h2>What they cost</h2>
<p>Agents run on HubSpot Credits, priced at $10 per 1,000 credits ($0.01 each).</p>
<div class="table-wrap"><table><thead><tr><th>Item</th><th>Credits</th><th>Cost</th></tr></thead><tbody>
<tr><td>Customer agent: one resolved text conversation</td><td class="num">50</td><td class="num">$0.50</td></tr>
<tr><td>Customer agent: one minute of voice (beta)</td><td class="num">50</td><td class="num">$0.50</td></tr>
<tr><td>Prospecting agent: outreach recommended for one lead</td><td class="num">100</td><td class="num">$1.00</td></tr>
</tbody></table></div>
<p>The monthly allowance for most Hubs is 500 credits on Starter, 3,000 on Professional and 5,000 on Enterprise.</p>
<p class="meta">Source: HubSpot Product and Services Catalog and HubSpot's customer agent page, checked 28 October 2026. HubSpot changes pricing often, so confirm current rates before you budget.</p>
<p>A resolution counts when the agent handles the conversation and it isn't handed to a person within 72 hours. Run the numbers for your own volume. A Professional allowance of 3,000 credits covers 60 resolved conversations a month, and each additional 1,000 resolutions costs $500 in credits. That is often a good price for support work. It's simply a cost to put in the comparison, not a reason to avoid the agent.</p>

<h2>When HubSpot's own agents are the better choice</h2>
<ul>
<li><strong>The work lives in HubSpot.</strong> Your knowledge base, tickets, contacts and deals are already there, so the agent has the context it needs.</li>
<li><strong>You're already on Professional or Enterprise.</strong> You can test the agents without new contracts or a build project.</li>
<li><strong>The job is standard.</strong> Answering support questions, qualifying inbound leads and recommending outreach are what these agents are designed for.</li>
<li><strong>You want the vendor to maintain it.</strong> HubSpot handles hosting, model updates and the interface. Your job is content quality and settings.</li>
</ul>
<p>If most of those are true, start there. Measure resolution rates and handoffs for a month before deciding you need anything more.</p>

<h2>When a custom agent is worth building</h2>
<ul>
<li><strong>The process runs through systems HubSpot can't reach directly.</strong> An ERP like Odoo, a lender's credit system or your own database usually isn't on the supported connector list. Zapier can sometimes bridge the gap, but it adds another dependency, and each Zapier MCP tool call uses two Zapier tasks.</li>
<li><strong>You need strict control over the steps.</strong> For example: a fixed sequence of qualifying questions, approval before any commitment, or rules about exactly when a person takes over. A custom agent can enforce those in code rather than in prompt instructions.</li>
<li><strong>One agent has to work across the whole business.</strong> When a single conversation needs to check stock in the ERP, create an order, update the CRM and alert a person in Slack, it can be simpler to build one agent with access to each system than to chain several tools.</li>
<li><strong>Your edition or setup doesn't fit.</strong> The customer agent needs Professional or Enterprise. If you're on Starter, or your customer data is split between HubSpot and other tools, compare the cost of upgrading with the cost of building.</li>
</ul>

<h2>The costs of a custom agent, honestly</h2>
<p>A custom agent isn't automatically cheaper. You pay to design and build it, then for AI model usage, hosting, monitoring and maintenance as APIs and models change. Someone also has to own it when it breaks. Ask any provider, including us, to put the build cost, monthly running cost and maintenance terms in writing, and compare those with your HubSpot credit spend at realistic volumes.</p>

<h2>Often the answer is both</h2>
<p>The two aren't mutually exclusive. A common, sensible setup is to use HubSpot's customer agent for support questions inside HubSpot, and a custom agent for a cross-system process that writes its results back into HubSpot through its API. HubSpot stays your single record of customers and deals either way.</p>

<h2>An example from our work</h2>
<p>We built a <a href="{{/work/#hubspot-crm-agent}}">HubSpot CRM agent</a> for a business that was taking about five days to reply to leads and missing many inbound enquiries. The agent sources prospects from Google Places, qualifies them into HubSpot, replies instantly across WhatsApp, email, Instagram and Facebook, and hands over to a person when the lead asks for one or wants a custom offer or a better price. Average reply time went from about five days to instant.</p>
<p>The lesson wasn't about the platform. The result came from designing the process: which leads to pursue, what to say first, and exactly when a person should step in. Whichever route you take, do that design work first. Our guide to <a href="{{/blog/which-processes-to-automate-with-ai/}}">choosing which processes to automate with AI</a> walks through it.</p>

<h2>A quick decision checklist</h2>
<ol>
<li>Is the data the agent needs already in HubSpot? If yes, try HubSpot's agents first.</li>
<li>Does the process need systems that aren't on HubSpot's connector list? If yes, price a custom agent or a hybrid setup.</li>
<li>What will it cost at your real monthly volume, in credits on one side and build plus running costs on the other?</li>
<li>Who maintains it, and how will you know when it gets something wrong?</li>
<li>What are the handoff rules, and are they enforced or just suggested?</li>
</ol>
<p>If you'd like a second opinion on your setup, our <a href="{{/services/ai-automation/}}">AI and automation team</a> can review it and tell you honestly whether HubSpot's own agents will do the job. Or <a href="{{/contact/}}">describe your process</a> and we'll reply within one working day.</p>
<p class="meta">Sources: HubSpot, <a href="https://www.hubspot.com/products/artificial-intelligence/ai-customer-service-agent">AI customer agent product page</a> and <a href="https://www.hubspot.com/agent-hub-roi-calculator">Agent Hub ROI calculator</a>; HubSpot Product and Services Catalog (HubSpot Credits); HubSpot Knowledge Base, "Connect apps to HubSpot's AI agents" (updated 18 September 2026); Zapier MCP documentation. All checked 28 October 2026.</p>
</article></div></section>"""

AI_AUDIT_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="27 October 2026", mins=8) + """
<p>Most AI projects that disappoint don't fail because the AI is weak. They fail because someone picked a tool before they understood the process. Gartner predicts that more than 40% of agentic AI projects will be cancelled by the end of 2027 because of escalating costs, unclear business value or inadequate risk controls.</p>
<p>The fix is unglamorous: audit the work first, then choose the simplest technology that does the job. This is how we approach it before building anything.</p>

<h2>Step 1: map the process as it really runs</h2>
<p>Write down what actually happens, not what the procedure document says. For each process, record:</p>
<ul>
<li><strong>The trigger:</strong> an email arrives, a form is submitted, a payment comes in.</li>
<li><strong>Every step and who does it,</strong> including the copy-pasting between tools that nobody lists.</li>
<li><strong>Volume and time:</strong> how often it happens each week and how long each run takes. Measure it rather than guessing.</li>
<li><strong>Exceptions:</strong> how often a case doesn't fit the normal path, and what people do then.</li>
<li><strong>Systems and data:</strong> where the inputs live, and whether those tools have an API.</li>
</ul>
<p>Sitting with the person who does the work for an hour usually tells you more than a workshop. You'll find the workarounds, the spreadsheet that holds everything together, and the step that only one person knows.</p>

<h2>Step 2: score each candidate</h2>
<p>A good automation candidate scores well on most of these:</p>
<div class="table-wrap"><table><thead><tr><th>Question</th><th>Good sign</th><th>Warning sign</th></tr></thead><tbody>
<tr><td>How often does it happen?</td><td>Daily or many times a week</td><td>A few times a month</td></tr>
<tr><td>Is it digital end to end?</td><td>Inputs arrive by email, form or system</td><td>Paper, phone calls, in-person checks</td></tr>
<tr><td>Can the systems be connected?</td><td>Tools have APIs or built-in integrations</td><td>No API, or only screen access</td></tr>
<tr><td>How stable is the process?</td><td>Same steps every time, agreed by the team</td><td>Changes weekly, or nobody agrees how it works</td></tr>
<tr><td>What does a mistake cost?</td><td>Easy to spot and reverse</td><td>Money, legal or safety consequences</td></tr>
<tr><td>Does speed matter?</td><td>Customers wait on it</td><td>Nobody notices a delay</td></tr>
</tbody></table></div>
<p>Then estimate the payback: hours saved per month, plus anything speed is worth, against the cost to build and run it. If you can't name the benefit in a sentence, don't automate it yet.</p>

<h2>Step 3: pick the simplest tool that works</h2>
<p>"AI automation" covers three different things, and most processes only need the first:</p>
<ul>
<li><strong>Rule-based automation.</strong> If the inputs are structured, such as a form field or a payment status, a workflow tool like Make, Zapier or n8n, or the automation built into your CRM or ERP, is cheaper, faster and fully predictable. No AI needed.</li>
<li><strong>An AI step inside a workflow.</strong> Use AI where a person currently has to read something: free-text emails, PDFs, chat messages. The AI turns them into structured data, and ordinary rules take over from there.</li>
<li><strong>An AI agent.</strong> Use an agent when the work needs a back-and-forth conversation or a choice between several actions, such as qualifying a lead or collecting a complete application. Agents are the most flexible option and need the most guardrails.</li>
</ul>
<p>Gartner's own advice runs along the same lines: use agents where decisions are needed, automation for routine workflows, and assistants for simple retrieval.</p>

<h2>Step 4: design the human in the loop</h2>
<p>Before building, write down three lists:</p>
<ul>
<li><strong>What the AI may do on its own:</strong> reply to a lead, create a draft order, log activity.</li>
<li><strong>What needs approval:</strong> anything involving money, commitments or exceptions.</li>
<li><strong>When it must hand over:</strong> the customer asks for a person, the request is unusual, or the AI isn't confident.</li>
</ul>
<p>Log every action the AI takes, alert someone when a run fails, and review a sample of conversations every week at first. AI models can produce confident, wrong answers, so the design has to assume mistakes will happen and catch them.</p>

<h2>Step 5: measure, pilot one process, then expand</h2>
<p>Record the baseline before you build: time per run, response time, error rate, volume. Automate one process, run it alongside the old way for a short period if the stakes are high, and compare. Expand only when the numbers hold up.</p>

<h2>What this looks like in practice</h2>
<ul>
<li><strong>Emailed orders into Odoo.</strong> Orders arrived as email text, PDFs and spreadsheets that staff re-keyed. Reading those is a genuine AI task, so an <a href="{{/work/#odoo-order-to-cash-agent}}">order agent</a> reads each one, matches the customer and products to Odoo records, checks stock and creates a quotation for a person to approve. Once approved, Odoo's own workflow takes over.</li>
<li><strong>Lead replies in HubSpot.</strong> Leads were waiting about five days for a reply, and many inbound enquiries were missed. Speed matters here: a Harvard Business Review study of 1.25 million leads found that companies contacting leads within an hour were seven times as likely to qualify them as those that waited even an hour longer. Our <a href="{{/work/#hubspot-crm-agent}}">HubSpot CRM agent</a> replies instantly and hands over to a person for custom offers and price negotiation.</li>
<li><strong>Loan top-ups for a lender.</strong> The agent collects complete applications, and a credit analyst makes every decision. The <a href="{{/work/#loan-top-up-agent}}">loan top-up agent</a> took in KES 5.4M in applications in its first week.</li>
</ul>

<h2>When not to automate yet</h2>
<ul>
<li>The process isn't agreed or changes every week. Fix the process first.</li>
<li>It happens rarely, so the build and maintenance cost more than the time saved.</li>
<li>A mistake would be costly or hard to reverse and no one can review the output.</li>
<li>The data lives in tools with no API, so the "automation" would be fragile screen-clicking.</li>
<li>You can't measure the benefit.</li>
</ul>

<h2>The bottom line</h2>
<p>Map the process, score it honestly, use the simplest tool that does the job, and keep a person responsible for anything that matters. That sequence decides whether automation saves money or becomes another abandoned pilot. If you'd like a second opinion on which of your processes are worth automating, our <a href="{{/services/ai-automation/}}">Automation Sprint</a> starts with exactly this audit, or <a href="{{/contact/}}">send us a short description of the process</a>.</p>
<p class="meta">Sources: Gartner, "Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027", 25 June 2025. Oldroyd, McElheran and Elkington, "The Short Life of Online Sales Leads", Harvard Business Review, March 2011.</p>
</article></div></section>"""

LENDER_AGENTS_BODY = """<section class="band"><div class="wrap"><article class="prose">
""" + BYLINE.format(date="27 October 2026 · Updated 28 October 2026", mins=7) + """
<p>Digital lenders, microfinance banks and SACCOs in Kenya already hold one of their most valuable assets: customers with a repayment history. Going back to the good borrowers, offering them more and collecting a complete application takes staff time. An AI agent can do the repetitive parts of that work, provided it's designed around the rules lenders operate under.</p>
<p>This guide explains how a top-up agent works, using one we built for a Kenyan digital lender. In its first week live it took in <strong>KES 5.4M in loan top-up applications</strong>.</p>

<h2>The problem: good borrowers nobody has time to call</h2>
<p>A customer who has repaid on time is a known risk. But offering top-ups usually means a loan officer working through a list, contacting each customer, asking the same qualifying questions and typing the answers into a system. That limits how many eligible customers ever hear about an offer.</p>

<h2>How a top-up agent works</h2>
<ol>
<li><strong>Find eligible customers.</strong> The agent connects to the lender's credit or loan management system and picks out customers who are repaying well, using the lender's own eligibility rules.</li>
<li><strong>Make the offer by SMS.</strong> Customers who have consented to receive offers get a short SMS with a top-up offer, an opt-out, and a link that opens a WhatsApp chat with the agent.</li>
<li><strong>Qualify on WhatsApp.</strong> The agent asks the questions the credit team needs, such as the amount, the collateral offered and how the funds will be used, and follows up if an answer is missing or unclear.</li>
<li><strong>Log a complete application.</strong> Each finished application goes into the CRM in a structured format, ready for review.</li>
<li><strong>A person decides.</strong> A credit analyst reviews every application and makes the lending decision. The agent never approves a loan.</li>
</ol>

<h2>Why SMS first, then WhatsApp</h2>
<p>SMS reaches every phone, including feature phones, without mobile data, so it suits the first offer. WhatsApp suits a conversation: customers answer at their own pace and can come back to the chat later.</p>
<p>The order also matters for WhatsApp's rules and pricing. A business can only start a WhatsApp conversation with an approved message template, sent to someone who has opted in, and marketing templates are charged per message. When the customer taps the link and messages you first, a 24-hour customer service window opens for replies. Since 1 October 2026, only the first 1,000 of those service messages a month on each business number are free; after that, each is charged at <a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing">Meta's published rates</a>. Budget for messaging costs at volume.</p>
<div class="callout"><p><strong>Check WhatsApp's lending rules before you build.</strong> Meta's WhatsApp Business Policy prohibits using WhatsApp to buy, sell or promote payday loans, paycheck advances, peer-to-peer lending and debt collection, "irrespective of" any licence the business holds, and Meta applies it at its own discretion. If your product could fall into those categories, run the conversation on a channel you control instead, such as your app, USSD or a web form, and keep the same agent behind it.</p></div>

<h2>Keep a human in the loop</h2>
<p>For lending, the agent should collect and organise information, not make credit decisions. Keeping an analyst responsible for every approval protects the lender's risk standards, keeps the process explainable to regulators and customers, and means the AI never gives a customer a promise the lender can't keep. The agent should also hand the conversation to a person whenever the customer asks for one.</p>

<h2>Compliance basics</h2>
<ul>
<li><strong>Consent for offers.</strong> A top-up offer is direct marketing. Under the Data Protection Act 2019 (section 37), using personal data for commercial purposes needs consent unless another law authorises it. The Data Protection (General) Regulations 2021 require a simple, free opt-out in marketing messages. In a case reported in April 2026, the ODPC ordered lender Platinum Credit to pay a customer KES 400,000 for promotional SMS and calls sent without his consent (<a href="https://www.businessdailyafrica.com/bd/corporate/companies/lender-to-pay-phone-user-for-unsolicited-loan-calls-texts-5287150">Business Daily</a>).</li>
<li><strong>Data minimisation.</strong> Send the AI only the data it needs and document where it is processed. Don't ask customers to type full card or bank account numbers into WhatsApp, which Meta's policy also prohibits.</li>
<li><strong>Full disclosure of terms.</strong> Licensed digital credit providers must give customers the loan terms, including the cost of credit, before a loan is granted. The agent should use the lender's approved wording and never improvise rates or terms.</li>
<li><strong>Collections conduct.</strong> The CBK Digital Credit Providers Regulations 2022 forbid using a borrower's phone contacts to chase repayments, and forbid threats or shaming. Any reminder agent must stay well inside those lines.</li>
<li><strong>Who regulates you.</strong> Digital credit providers are licensed by the Central Bank of Kenya. SASRA regulates deposit-taking SACCOs and some non-deposit-taking SACCOs, including larger and digital ones. The agent works inside your existing approval and disclosure process and doesn't replace it.</li>
</ul>
<p class="meta">This is a summary, not legal advice. Confirm your obligations with your compliance team or legal adviser. Sources: <a href="https://business.whatsapp.com/policy">WhatsApp Business Messaging Policy</a>; <a href="https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing">WhatsApp Business Platform pricing</a>; Data Protection Act 2019; Data Protection (General) Regulations 2021; CBK Digital Credit Providers Regulations 2022; SASRA.</p>

<h2>Other places an agent helps a lender</h2>
<ul>
<li><strong>New loan applications:</strong> the same structured intake for first-time borrowers, on whichever channel your product is allowed to use.</li>
<li><strong>Repayment reminders:</strong> a polite SMS before the due date with the Paybill and account number. Don't push an M-Pesa prompt with the reminder: an STK Push prompt expires in well under a minute, so it times out unless the customer is holding the phone. Instead, let the customer ask to pay, for example by replying or tapping a link, and send the prompt at that moment. Our <a href="{{/blog/mpesa-stk-push-integration-guide/}}">M-Pesa STK Push guide</a> explains the timing. Keep reminders off WhatsApp, where debt collection is prohibited.</li>
<li><strong>Member questions:</strong> balances, statements and loan status, answered from your own system after the member is verified. This depends on your core system having an API the agent can safely read from.</li>
<li><strong>Lead follow-up:</strong> instant replies to enquiries from your website and social pages. A CRM agent we built cut the reply time to new leads <a href="{{/work/#hubspot-crm-agent}}">from about five days to instant</a>.</li>
</ul>

<h2>What it takes to build one</h2>
<p>The AI conversation is rarely the hard part. The work goes into:</p>
<ul>
<li>connecting your credit system, SMS gateway, the conversation channel and the CRM</li>
<li>agreeing eligibility rules, approved wording and handoff rules with your credit and compliance teams</li>
<li>consent records and opt-outs</li>
<li>testing the conversation against real customer answers</li>
</ul>
<p>Start with one use case, measure applications and approval rates, and expand from there.</p>
<p>Read the full <a href="{{/work/#loan-top-up-agent}}">loan top-up agent case study</a>, see our <a href="{{/services/ai-automation/}}">AI and automation services</a>, or <a href="{{/contact/}}">tell us about your lending process</a>.</p>
</article></div></section>"""

EAST_AFRICA_BODY = """<section class="band"><div class="wrap"><div class="grid g2" style="gap:48px">
<div class="prose">
<h2 style="margin-top:0">A Nairobi team that knows your market</h2>
<p>We're based in Nairobi and serve businesses in Kenya, Uganda, Tanzania and Rwanda, as well as clients abroad. Your customers pay by M-Pesa, message you on WhatsApp and browse on mid-range Android phones, and we build for exactly that. You get the same senior team and process we bring to every client, and you can meet us face to face.</p>
<h3>Websites that work on East African connections</h3>
<p>Many of your visitors are on mobile data, so every kilobyte counts. We build lightweight, mobile-first sites that load quickly on 3G and budget phones, rank well on Google and don't drain your customers' bundles.</p>
<h3>M-Pesa and mobile money integration</h3>
<p>We integrate M-Pesa through the Daraja API: STK Push checkout, C2B Paybill and Till payments, B2C payouts and automatic reconciliation with your orders or accounting system. Our <a href="{{/blog/mpesa-stk-push-integration-guide/}}">M-Pesa STK Push integration guide</a> explains how it works.</p>
<h3>WhatsApp and AI for customer service</h3>
<p>Your customers already use WhatsApp. We set up WhatsApp Business ordering, automated replies and AI assistants that answer common questions in English or Swahili, take orders and hand over to a person when needed.</p>
<h3>AI agents already working in Kenya</h3>
<p>We built an AI agent for a digital lender that took in <strong>KES 5.4M in loan top-up applications in its first week</strong>. Read the <a href="{{/work/#loan-top-up-agent}}">case study</a> and our guide to <a href="{{/blog/ai-agents-for-lenders-kenya/}}">AI agents for lenders and SACCOs</a>, or see our <a href="{{/services/ai-automation/}}">AI and automation services</a>.</p>
<h3>Local SEO in Nairobi and beyond</h3>
<p>We optimise your Google Business Profile, local citations and service-area pages so you show up when customers search for "near me" services in Nairobi, Mombasa, Kisumu, Kampala, Dar es Salaam or Kigali.</p>
<h3>Working with businesses across Nairobi</h3>
<p>We work remotely and meet clients at their offices, from Westlands, Kilimani and Upper Hill to the CBD, Industrial Area and Karen. Wondering about budget? Read <a href="{{/blog/website-cost-in-kenya/}}">how much a website costs in Kenya in 2026</a>, or see our <a href="{{/pricing/}}">published prices</a>.</p>
<h3>Business systems</h3>
<p>We build custom software for how East African businesses run: stock and order systems, SACCO and chama portals, school and clinic management tools, and field-sales apps.</p>
</div>
<div class="grid" style="align-content:start;gap:20px">
<div class="table-wrap"><table><thead><tr><th>Need</th><th>What we build</th></tr></thead><tbody>
<tr><td>Sell online</td><td>E-commerce with M-Pesa STK Push, delivery zones and WhatsApp order alerts</td></tr>
<tr><td>Get found</td><td>Google Business Profile, local SEO, Swahili/English pages</td></tr>
<tr><td>Serve customers faster</td><td>WhatsApp Business bots and AI assistants</td></tr>
<tr><td>Run operations</td><td>Inventory, orders, bookings and invoicing</td></tr>
<tr><td>Grow a startup</td><td>MVPs, mobile apps and mobile money payment flows</td></tr>
</tbody></table></div>
<div class="plan"><h3>Paying us locally</h3><ul><li>Same published prices as all our clients</li><li>Pay in KES by bank transfer, at the day's exchange rate</li><li>Meetings at your office in Nairobi, or by video call</li></ul><div class="btn-row" style="margin-top:8px"><a class="btn" href="{{/contact/}}">Book a meeting</a><a class="btn ghost" href="https://wa.me/""" + SITE["whatsapp"] + """?text=Hi%20Sahara%20Nova%2C%20I%27d%20like%20to%20ask%20about%20a%20project">Chat on WhatsApp</a></div></div>
</div>
</div></div></section>"""

EAST_AFRICA_FAQ = [
 ("Do you build websites for businesses in Nairobi?", "Yes. We're a Nairobi-based agency and build websites, e-commerce stores, software and marketing campaigns for Kenyan businesses, with in-person meetings available."),
 ("Can you integrate M-Pesa into my website or app?", "Yes. We integrate M-Pesa through Safaricom's Daraja API, including STK Push checkout, Paybill and Till payments, B2C payouts and automatic reconciliation. Adding it to an existing site is quoted after a short discovery."),
 ("Do you work with businesses in Uganda, Tanzania and Rwanda?", "Yes. We work with businesses across East Africa remotely, by video call."),
 ("Can I pay in Kenyan shillings?", "Yes. Our prices are published in USD and you can pay the equivalent in KES by bank transfer at the day's exchange rate."),
 ("Can you build a WhatsApp chatbot for my business?", "Yes. We build WhatsApp Business ordering flows, automated replies and AI assistants that answer in English or Swahili and hand over to your team when needed."),
]

WEB["updated"] = SEO["updated"] = "2026-10-28"

PAGES = [
 dict(path="", updated="2026-10-28", title="Digital Agency for Small Businesses | Sahara Nova, Nairobi",
      description="A digital agency for small businesses, based in Nairobi: websites, custom software, SEO and AI automation for clients worldwide. Your hours, fixed prices.",
      h1="The Nairobi digital agency that works your hours", hero=HOME_HERO, body=HOME_BODY, faq=HOME_FAQ,
      faq_title="Questions small businesses ask us"),
 dict(path="services/", updated="2026-10-28", title="Web, Software, SEO & AI for Small Businesses | Sahara Nova",
      description="Web design and development, custom software and apps, SEO and digital marketing, and AI automation for small and mid-sized businesses, from one team in Nairobi.",
      eyebrow="Services", h1="Everything digital, from one team",
      lede="Four disciplines, one project lead, one invoice. Start with the service you need most and add the others when you're ready.",
      crumbs=[("/services/", "Services")], body=SERVICES_BODY),
 WEB, SOFT, SEO, AI,
 dict(path="why-kenya/", updated="2026-10-28", title="Hire Developers in Kenya: Why Teams Choose Nairobi | Sahara Nova",
      description="Why hire developers in Kenya: 6–8 hours of overlap with Europe, English-first teams, 40–60% lower costs and Nairobi's deep tech talent pool.",
      eyebrow="Why Kenya", h1="Why hire a development team in Kenya?",
      lede="Time zone overlap with Europe, English as a working language, and rates well below onshore agencies. Here is what working with developers in Nairobi looks like in practice.",
      crumbs=[("/why-kenya/", "Why Kenya")], body=WHY_KENYA_BODY,
      faq=[("Is it safe to outsource development to Kenya?", "Yes, if you choose your partner carefully. Kenya's legal system is based on English common law, its Data Protection Act 2019 follows GDPR principles, and contracts can assign full IP ownership to you."),
           ("What time zone is Kenya in?", "Kenya uses East Africa Time (EAT), UTC+3, all year round with no daylight saving. That is 2–3 hours ahead of the UK and 1–2 hours ahead of central Europe."),
           ("How much do Kenyan developers cost?", "Agency rates in Kenya typically range from under $25 to $99 per hour, depending on seniority and agency size.")]),
 dict(path="work/", title="AI Agent Case Studies: Odoo, HubSpot & Lending | Sahara Nova",
      description="AI agents we've built: loan top-up intake for a lender, email-to-Odoo order processing, a HubSpot CRM agent, and support and lead intake agents.",
      eyebrow="Our work", h1="AI agents we've built",
      lede="Real agents running inside real businesses: taking in loan applications, processing orders in an ERP, working a CRM pipeline and talking to customers. Built by our founder, James, in a previous role; client names are withheld.",
      crumbs=[("/work/", "Work")], body=WORK_BODY, cases=True),
 dict(path="east-africa/", title="Web Design & Software Company in Nairobi, Kenya | Sahara Nova",
      description="Nairobi web design, software, SEO and AI for businesses in Kenya and East Africa: M-Pesa integration, WhatsApp bots, fast mobile sites and local SEO.",
      eyebrow="Kenya &amp; East Africa", h1="Web design, software and marketing for businesses in Kenya and East Africa",
      lede="A Nairobi team building fast websites, M-Pesa-ready apps, WhatsApp automation and local SEO for businesses in Kenya, Uganda, Tanzania and Rwanda.",
      crumbs=[("/east-africa/", "Kenya & East Africa")], body=EAST_AFRICA_BODY, faq=EAST_AFRICA_FAQ,
      area=["Kenya", "Uganda", "Tanzania", "Rwanda"]),
 dict(path="pricing/", updated="2026-10-28", title="Website & Software Development Pricing | Sahara Nova",
      description="Published prices for small business websites (from $1,500), e-commerce, MVPs, SEO (from $900) and AI agents (from $3,500). Fixed quotes after a free call.",
      eyebrow="Pricing", h1="Transparent pricing, fixed quotes",
      lede="Published starting prices, so you know if we fit your budget before you pick up the phone.",
      crumbs=[("/pricing/", "Pricing")], body=PRICING_BODY, faq=PRICING_FAQ),
 dict(path="about/", updated="2026-10-28", title="About Sahara Nova | Digital Agency in Nairobi, Kenya",
      description="Sahara Nova is a small, senior digital team in Nairobi, Kenya, helping small and mid-sized businesses worldwide with websites, software, SEO and automation.",
      eyebrow="About", h1="A small senior team, built for clients anywhere",
      lede="We're a Nairobi-based digital agency that believes small businesses deserve senior, transparent, fairly priced digital work.",
      crumbs=[("/about/", "About")], body=ABOUT_BODY),
 dict(path="contact/", title="Contact Sahara Nova | Get a Fixed Quote",
      description="Tell us about your website, software, SEO or automation project. We reply within one working day and send a fixed quote within two working days of our call.",
      eyebrow="Contact", h1="Tell us about your project",
      lede="A few details are enough to start. We reply within one working day.",
      crumbs=[("/contact/", "Contact")], body=CONTACT_BODY, no_cta=True),
 dict(path="blog/", title="Web, SEO & AI Guides for Small Businesses | Sahara Nova",
      description="Practical guides on websites, SEO, software and AI automation for small business owners, from the Sahara Nova team in Nairobi.",
      eyebrow="Blog", h1="Guides for small business owners",
      lede="Practical, jargon-free advice on websites, SEO, software and automation.",
      crumbs=[("/blog/", "Blog")], body=BLOG_BODY),
 dict(path="blog/outsourcing-web-development-to-kenya/",
      title="Cost of Outsourcing Web Development to Kenya (2026 Guide)",
      description="What it costs to outsource web development to Kenya in 2026: hourly rates by region, time zone overlap, how Kenya compares and how to vet an agency.",
      eyebrow="Guide", h1="What it costs to outsource web development to Kenya in 2026, and how to do it well",
      lede="Rates, time zone overlap, how Kenya compares with other outsourcing regions, and a vetting checklist.",
      crumbs=[("/blog/", "Blog"), ("/blog/outsourcing-web-development-to-kenya/", "Outsourcing to Kenya")],
      article={"date": "2026-09-23", "modified": "2026-10-28"}, body=ARTICLE_BODY),
 dict(path="blog/automate-email-orders-into-odoo-with-ai/",
      title="How to Automate Email Orders Into Odoo With AI | Sahara Nova",
      description="Turn order emails, PDFs and spreadsheets into Odoo quotations with AI: what Odoo does natively, the flow that works, matching, approvals and API changes.",
      eyebrow="Guide", h1="How to automate email orders into Odoo with AI",
      lede="What Odoo handles on its own, the flow we use for an order agent, and the design decisions that keep bad orders out of your system.",
      crumbs=[("/blog/", "Blog"), ("/blog/automate-email-orders-into-odoo-with-ai/", "Email orders into Odoo")],
      article={"date": "2026-10-30"}, body=ODOO_ORDERS_BODY,
      faq=[("Can Odoo create sales orders from emails automatically?", "An email alias can turn an incoming email into a record, but it won't read the order lines and build a quotation. For that you need a third-party app or a custom AI agent connected to Odoo's API."),
           ("Should an AI agent confirm orders in Odoo on its own?", "Not at first. Have the agent create quotations and a person approve them. Confirming starts your delivery and invoicing workflow, so widen the agent's autonomy only when approvers rarely need to edit its quotations."),
           ("Which Odoo plan do I need to connect an AI agent?", "On Odoo Online, external API access requires the Custom plan; it isn't available on One App Free or Standard. Odoo.sh and on-premise installations can use the API. New integrations should use the JSON-2 API.")]),
 dict(path="blog/hubspot-breeze-vs-custom-ai-agent/",
      title="HubSpot Breeze Agents vs a Custom AI Agent | Sahara Nova",
      description="HubSpot's Breeze agents or a custom AI agent? What each costs in 2026, when HubSpot's own agents are enough, and when a custom agent pays off.",
      eyebrow="Guide", h1="HubSpot's AI agents vs a custom AI agent: which do you need?",
      lede="An honest comparison of what HubSpot's built-in agents do and cost today, and the specific cases where a custom agent is worth building.",
      crumbs=[("/blog/", "Blog"), ("/blog/hubspot-breeze-vs-custom-ai-agent/", "HubSpot vs custom agent")],
      article={"date": "2026-10-28"}, body=BREEZE_VS_CUSTOM_BODY,
      faq=[("How much does HubSpot's customer agent cost?", "It runs on HubSpot Credits: 50 credits ($0.50) per resolved text conversation and 50 credits per minute of voice (beta), on top of a Professional or Enterprise subscription. Each edition includes a monthly credit allowance. Prices checked 28 October 2026."),
           ("Can HubSpot's AI agents connect to other systems?", "Yes, through a list of supported connectors such as Gmail, Slack, Notion, Asana, Gong and Xero, and through Zapier. Systems outside that list, such as many ERPs or in-house databases, usually need Zapier or a custom integration."),
           ("When should I build a custom AI agent instead of using HubSpot's?", "When the process depends on systems HubSpot can't reach directly, needs strictly enforced steps and approvals, or spans several business systems in one conversation. Compare build and running costs with your credit spend at real volumes.")]),
 dict(path="blog/which-processes-to-automate-with-ai/",
      title="Which Processes Should You Automate With AI? | Sahara Nova",
      description="A practical AI automation audit for small businesses: map the process, score candidates, and choose between simple automation, an AI step or an AI agent.",
      eyebrow="Guide", h1="Which processes should you automate with AI? A practical audit",
      lede="Most AI projects that disappoint started with the tool instead of the process. Here's how to choose what to automate, and how, before you spend anything.",
      crumbs=[("/blog/", "Blog"), ("/blog/which-processes-to-automate-with-ai/", "What to automate with AI")],
      article={"date": "2026-10-27"}, body=AI_AUDIT_BODY,
      faq=[("Which business processes are best to automate with AI?", "Frequent, digital processes with stable steps, connectable systems and mistakes that are easy to catch. Use AI specifically where a person currently has to read free text, such as emails, documents or chat messages."),
           ("Do I need AI, or is normal automation enough?", "If the inputs are already structured, such as form fields or payment statuses, a rule-based workflow in Make, Zapier, n8n or your CRM is usually cheaper and more predictable. Add AI only for unstructured inputs or conversations."),
           ("When should a business not automate a process?", "When the process isn't agreed or keeps changing, happens rarely, has costly mistakes no one reviews, runs on tools without an API, or has no measurable benefit.")]),
 dict(path="blog/ai-agents-for-lenders-kenya/",
      title="AI Agents for Digital Lenders & SACCOs in Kenya | Sahara Nova",
      description="How a WhatsApp AI agent took in KES 5.4M in loan top-up applications in a week: the flow, human-in-the-loop credit decisions and compliance basics.",
      eyebrow="Guide", h1="AI agents for digital lenders and SACCOs in Kenya",
      lede="How a top-up agent finds good borrowers, qualifies them on WhatsApp and hands complete applications to your credit team.",
      crumbs=[("/blog/", "Blog"), ("/blog/ai-agents-for-lenders-kenya/", "AI agents for lenders")],
      article={"date": "2026-10-27", "modified": "2026-10-28"}, body=LENDER_AGENTS_BODY,
      faq=[("Can an AI agent approve loans?", "It shouldn't. In the agents we build, the AI finds eligible customers, makes the offer and collects a complete application, and a credit analyst makes every lending decision."),
           ("Can lenders use WhatsApp for loan applications?", "Check first. Meta's WhatsApp Business Policy prohibits promoting payday loans, paycheck advances, peer-to-peer lending and debt collection on WhatsApp, regardless of licences. If your product could fall into those categories, use your app, USSD or a web form for the conversation instead."),
           ("Can a repayment reminder include an M-Pesa prompt?", "It's not practical. An STK Push prompt expires in well under a minute, so a prompt sent with a reminder usually times out unseen. Send the reminder with Paybill details, and trigger the prompt only when the customer asks to pay.")]),
 dict(path="blog/website-cost-in-kenya/",
      title="How Much Does a Website Cost in Kenya? (2026 Prices in KES)",
      description="Website prices in Kenya for 2026: DIY, freelancer template sites, custom business sites, online shops and web apps in KES, plus the yearly costs after launch.",
      eyebrow="Guide", h1="How much does a website cost in Kenya in 2026?",
      lede="What you get at each price level, what you'll pay every year after launch, and how to choose.",
      crumbs=[("/blog/", "Blog"), ("/blog/website-cost-in-kenya/", "Website cost in Kenya")],
      article={"date": "2026-10-22", "modified": "2026-10-28"}, body=WEBSITE_COST_KENYA_BODY,
      faq=[("How much does a basic website cost in Kenya?", "A five-page site from a freelance web designer typically costs KES 15,000–80,000, plus around KES 2,100 a year for a .co.ke domain and basic hosting."),
           ("How much does a custom business website cost in Kenya?", "Prices vary widely between agencies. Sahara Nova's Website Launch package, a custom-designed site with SEO built in, starts at $1,500 (about KES 195,000), payable in KES."),
           ("How much is a .co.ke domain per year?", "Around KES 1,200 a year from most Kenyan registrars. Make sure it is registered in your business's name.")]),
 dict(path="blog/mpesa-stk-push-integration-guide/",
      title="M-Pesa STK Push Integration: A Step-by-Step Guide (2026)",
      description="How to add M-Pesa STK Push checkout to your website with the Daraja API: access tokens, the request, callbacks, result codes, going live and common mistakes.",
      eyebrow="Guide", h1="M-Pesa STK Push integration: a step-by-step guide",
      lede="How Lipa na M-Pesa Online works through the Daraja API, what you need first, and how to avoid the mistakes behind most failed integrations.",
      crumbs=[("/blog/", "Blog"), ("/blog/mpesa-stk-push-integration-guide/", "M-Pesa STK Push guide")],
      article={"date": "2026-10-22", "modified": "2026-10-27"}, body=MPESA_GUIDE_BODY,
      faq=[("What is M-Pesa STK Push?", "STK Push, also called Lipa na M-Pesa Online or M-Pesa Express, sends a payment prompt straight to the customer's phone. They enter their M-Pesa PIN to pay, with no need to type a Paybill or account number."),
           ("Do I need a Paybill or Till number for STK Push?", "You can build and test in the Daraja sandbox without one, but you need a Paybill or Till registered to your business to go live."),
           ("How long does an M-Pesa STK Push prompt last?", "Not long: well under a minute. Developer guides report about 30 to 60 seconds, varying with the network. Only send the prompt when the customer is at checkout and ready to pay, and give them a button to resend it if it times out.")]),
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
