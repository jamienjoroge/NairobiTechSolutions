#!/usr/bin/env python3
"""Sahara Nova static site builder.

Usage:  python3 build.py            -> builds ./dist (for deployment, clean URLs)
        python3 build.py --preview  -> builds ./preview (relative links, for artifact preview)

Change SITE_URL / EMAIL below and rebuild to switch domain.
"""
import json, os, re, shutil, sys, datetime, html as _html
from pages import PAGES, SITE, FOUNDER

PREVIEW = "--preview" in sys.argv
STAGING = "--staging" in sys.argv   # private test deploy: nothing gets indexed
OUT = os.path.join(os.path.dirname(__file__), "preview" if PREVIEW else ("dist-staging" if STAGING else "dist"))
SRC = os.path.dirname(os.path.abspath(__file__))
TODAY = datetime.date(2026, 10, 22).isoformat()   # site-wide last update; pages can override with "updated"

LOGO = '<svg class="logo-lockup" role="img" aria-label="Sahara Nova" viewBox="0 0 281.7 60"><polygon class="m" points="9,21 18,21 18,51 9,51"/><polygon class="m" points="9,21 21,21 42,51 30,51"/><polygon class="m" points="33,21 42,21 42,51 33,51"/><polygon class="b" points="33,18 42,18 42,9 33,15" /><path class="t" d="M0.7846153846153847 -5.030769230769231H3.9000000000000004Q3.9923076923076923 -4.246153846153846 4.626923076923077 -3.6115384615384616Q5.2615384615384615 -2.976923076923077 6.300000000000001 -2.6192307692307693Q7.338461538461539 -2.2615384615384615 8.630769230769232 -2.2615384615384615Q9.807692307692308 -2.2615384615384615 10.56923076923077 -2.5153846153846153Q11.330769230769231 -2.769230769230769 11.700000000000001 -3.230769230769231Q12.06923076923077 -3.6923076923076925 12.06923076923077 -4.338461538461539Q12.06923076923077 -4.961538461538462 11.607692307692309 -5.296153846153846Q11.146153846153847 -5.630769230769231 10.153846153846155 -5.8500000000000005Q9.161538461538463 -6.06923076923077 7.546153846153847 -6.300000000000001Q6.276923076923078 -6.484615384615385 5.1461538461538465 -6.819230769230769Q4.015384615384615 -7.153846153846154 3.1500000000000004 -7.684615384615386Q2.284615384615385 -8.215384615384616 1.7884615384615388 -8.98846153846154Q1.2923076923076924 -9.761538461538462 1.2923076923076924 -10.823076923076924Q1.2923076923076924 -12.13846153846154 2.0423076923076926 -13.130769230769232Q2.7923076923076926 -14.123076923076924 4.269230769230769 -14.676923076923078Q5.746153846153846 -15.230769230769232 7.892307692307693 -15.230769230769232Q11.123076923076924 -15.230769230769232 12.865384615384617 -13.857692307692307Q14.607692307692309 -12.484615384615385 14.561538461538463 -10.084615384615384H11.561538461538461Q11.46923076923077 -11.446153846153846 10.419230769230769 -12.046153846153846Q9.36923076923077 -12.646153846153847 7.776923076923078 -12.646153846153847Q6.300000000000001 -12.646153846153847 5.342307692307693 -12.207692307692309Q4.384615384615385 -11.76923076923077 4.384615384615385 -10.707692307692309Q4.384615384615385 -10.292307692307693 4.615384615384616 -9.980769230769232Q4.846153846153847 -9.66923076923077 5.4 -9.438461538461539Q5.953846153846154 -9.207692307692309 6.9 -9.0Q7.846153846153847 -8.792307692307693 9.253846153846155 -8.584615384615384Q10.569230769230769 -8.4 11.642307692307693 -8.088461538461539Q12.715384615384616 -7.776923076923078 13.48846153846154 -7.2807692307692315Q14.261538461538462 -6.784615384615385 14.676923076923078 -6.023076923076923Q15.092307692307694 -5.2615384615384615 15.092307692307694 -4.153846153846154Q15.092307692307694 -2.7923076923076926 14.38846153846154 -1.7884615384615388Q13.684615384615386 -0.7846153846153847 12.21923076923077 -0.2307692307692308Q10.753846153846155 0.3230769230769231 8.423076923076923 0.3230769230769231Q6.7615384615384615 0.3230769230769231 5.492307692307692 -0.03461538461538463Q4.223076923076923 -0.39230769230769236 3.3 -0.9923076923076923Q2.376923076923077 -1.5923076923076924 1.8 -2.307692307692308Q1.2230769230769232 -3.0230769230769234 0.9807692307692308 -3.7384615384615385Q0.7384615384615385 -4.453846153846154 0.7846153846153847 -5.030769230769231ZM22.43076923076923 -3.253846153846154V-5.815384615384616H32.30769230769231V-3.253846153846154ZM18.715384615384615 0.0 25.73076923076923 -14.930769230769231H29.053846153846152L36.13846153846154 0.0H32.79230769230769L26.653846153846153 -13.453846153846154H28.130769230769232L22.038461538461537 0.0ZM43.315384615384616 -8.76923076923077H55.15384615384615V-6.207692307692308H43.315384615384616ZM54.646153846153844 -14.930769230769231H57.715384615384615V0.0H54.646153846153844ZM40.61538461538461 -14.930769230769231H43.684615384615384V0.0H40.61538461538461ZM65.9076923076923 -3.253846153846154V-5.815384615384616H75.78461538461538V-3.253846153846154ZM62.192307692307686 0.0 69.2076923076923 -14.930769230769231H72.53076923076922L79.61538461538461 0.0H76.26923076923077L70.13076923076923 -13.453846153846154H71.6076923076923L65.51538461538462 0.0ZM84.0923076923077 0.0V-14.930769230769231H94.22307692307692Q95.95384615384616 -14.930769230769231 97.23461538461538 -14.457692307692309Q98.51538461538462 -13.984615384615385 99.23076923076923 -12.98076923076923Q99.94615384615385 -11.976923076923077 99.94615384615385 -10.407692307692308Q99.94615384615385 -9.346153846153847 99.57692307692308 -8.607692307692307Q99.20769230769231 -7.86923076923077 98.55000000000001 -7.407692307692308Q97.8923076923077 -6.946153846153846 97.03846153846155 -6.703846153846154Q96.18461538461538 -6.461538461538462 95.21538461538462 -6.392307692307693L94.8923076923077 -6.5769230769230775Q96.50769230769231 -6.5538461538461545 97.54615384615386 -6.311538461538462Q98.58461538461539 -6.06923076923077 99.10384615384615 -5.434615384615386Q99.62307692307692 -4.800000000000001 99.62307692307692 -3.553846153846154V0.0H96.55384615384615V-3.3461538461538463Q96.55384615384615 -4.2 96.25384615384615 -4.673076923076923Q95.95384615384616 -5.1461538461538465 95.18076923076924 -5.330769230769231Q94.40769230769232 -5.515384615384615 92.95384615384616 -5.515384615384615H87.16153846153847V0.0ZM87.16153846153847 -7.915384615384616H94.22307692307692Q95.51538461538462 -7.915384615384616 96.19615384615385 -8.53846153846154Q96.87692307692308 -9.161538461538463 96.87692307692308 -10.223076923076924Q96.87692307692308 -11.23846153846154 96.19615384615385 -11.76923076923077Q95.51538461538462 -12.3 94.22307692307692 -12.3H87.16153846153847ZM107.79230769230769 -3.253846153846154V-5.815384615384616H117.66923076923077V-3.253846153846154ZM104.07692307692308 0.0 111.09230769230768 -14.930769230769231H114.41538461538461L121.5 0.0H118.15384615384616L112.01538461538462 -13.453846153846154H113.49230769230769L107.4 0.0ZM148.9846153846154 -3.0461538461538464 148.01538461538462 -2.653846153846154V-14.930769230769231H151.0846153846154V0.0H148.01538461538462L135.94615384615386 -11.792307692307693L136.91538461538462 -12.184615384615386V0.0H133.84615384615387V-14.930769230769231H136.91538461538462ZM165.83076923076925 0.30000000000000004Q162.85384615384618 0.30000000000000004 160.7423076923077 -0.6346153846153847Q158.63076923076923 -1.5692307692307694 157.51153846153846 -3.3Q156.3923076923077 -5.030769230769231 156.3923076923077 -7.453846153846154Q156.3923076923077 -9.9 157.51153846153846 -11.630769230769232Q158.63076923076923 -13.361538461538462 160.7423076923077 -14.296153846153846Q162.85384615384618 -15.230769230769232 165.83076923076925 -15.230769230769232Q168.83076923076925 -15.230769230769232 170.93076923076924 -14.296153846153846Q173.03076923076924 -13.361538461538462 174.15 -11.630769230769232Q175.26923076923077 -9.9 175.26923076923077 -7.453846153846154Q175.26923076923077 -5.030769230769231 174.15 -3.3Q173.03076923076924 -1.5692307692307694 170.93076923076924 -0.6346153846153847Q168.83076923076925 0.30000000000000004 165.83076923076925 0.30000000000000004ZM165.83076923076925 -2.353846153846154Q167.6769230769231 -2.353846153846154 169.07307692307694 -2.907692307692308Q170.4692307692308 -3.4615384615384617 171.26538461538462 -4.592307692307692Q172.06153846153848 -5.723076923076923 172.06153846153848 -7.453846153846154Q172.06153846153848 -9.184615384615386 171.26538461538462 -10.315384615384616Q170.4692307692308 -11.446153846153846 169.07307692307694 -12.011538461538462Q167.6769230769231 -12.576923076923078 165.83076923076925 -12.576923076923078Q164.0076923076923 -12.576923076923078 162.5769230769231 -12.011538461538462Q161.14615384615385 -11.446153846153846 160.33846153846156 -10.315384615384616Q159.53076923076924 -9.184615384615386 159.53076923076924 -7.453846153846154Q159.53076923076924 -5.723076923076923 160.33846153846156 -4.592307692307692Q161.14615384615385 -3.4615384615384617 162.5769230769231 -2.907692307692308Q164.0076923076923 -2.353846153846154 165.83076923076925 -2.353846153846154ZM185.8615384615385 0.0 179.26153846153846 -14.930769230769231H182.65384615384616L188.30769230769232 -1.453846153846154H187.24615384615385L192.87692307692308 -14.930769230769231H196.22307692307695L189.6923076923077 0.0ZM203.1 -3.253846153846154V-5.815384615384616H212.97692307692307V-3.253846153846154ZM199.3846153846154 0.0 206.4 -14.930769230769231H209.72307692307692L216.80769230769232 0.0H213.46153846153845L207.3230769230769 -13.453846153846154H208.8L202.7076923076923 0.0Z" transform="translate(55.5,43.5)"/></svg>'

NAV = [("/services/", "Services"), ("/work/", "Work"), ("/east-africa/", "East Africa"), ("/pricing/", "Pricing"),
       ("/about/", "About"), ("/blog/", "Blog")]


def rel(from_path, to_path):
    """Link from page at from_path (e.g. 'services/web/') to to_path ('/pricing/')."""
    if not PREVIEW:
        return to_path
    anchor = ""
    if "#" in to_path:
        to_path, anchor = to_path.split("#", 1)
        anchor = "#" + anchor
    fp = from_path.strip("/")
    depth = fp.count("/") if fp.endswith(".html") else fp.count("/") + (1 if fp else 0)
    prefix = "../" * depth
    target = to_path.lstrip("/")
    if target == "" or target.endswith("/"):
        target += "index.html"
    return (prefix + target) + anchor


def links(html, page_path):
    return re.sub(r"\{\{(/[^}]*)\}\}", lambda m: rel(page_path, m.group(1)), html)


def crumbs_html(p):
    if not p.get("crumbs"):
        return ""
    parts = ['<a href="{{/}}">Home</a>']
    for url, name in p["crumbs"][:-1]:
        parts.append(f'<a href="{{{{{url}}}}}">{name}</a>')
    parts.append(f'<span aria-current="page">{p["crumbs"][-1][1]}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + " / ".join(parts) + "</nav>"


def schema_for(p):
    url = SITE["url"] + "/" + p["path"]
    graph = []
    org = {
        "@type": ["Organization", "ProfessionalService"], "@id": SITE["url"] + "/#org",
        "name": SITE["name"], "url": SITE["url"] + "/", "logo": SITE["url"] + "/logo.png",
        "image": SITE["url"] + "/og-image.png",
        "email": SITE["email"], "telephone": SITE["phone"].replace(" ", ""), "description": SITE["description"],
        "address": {"@type": "PostalAddress", "addressLocality": "Nairobi", "addressCountry": "KE"},
        "areaServed": [{"@type": "Country", "name": c} for c in ("Kenya", "Uganda", "Tanzania", "Rwanda")] + ["Worldwide"],
        "priceRange": "$$",
        "knowsAbout": ["Web development", "Custom software development", "Search engine optimisation",
                       "Digital marketing", "AI automation", "Business process automation"],
    }
    if SITE.get("same_as"):
        org["sameAs"] = SITE["same_as"]
    org["founder"] = {"@id": SITE["url"] + "/#founder"}
    graph.append(org)
    graph.append({"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/",
                  "name": SITE["name"], "publisher": {"@id": SITE["url"] + "/#org"}, "inLanguage": "en"})
    graph.append({"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"],
                  "description": p["description"], "isPartOf": {"@id": SITE["url"] + "/#website"},
                  "inLanguage": "en", "dateModified": p.get("updated", TODAY)})
    if p.get("article") or p["path"] == "about/":
        person = {"@type": "Person", "@id": SITE["url"] + "/#founder", "name": FOUNDER["name"],
                  "jobTitle": FOUNDER["role"], "worksFor": {"@id": SITE["url"] + "/#org"},
                  "description": FOUNDER["bio"], "knowsAbout": FOUNDER["knows"],
                  "url": SITE["url"] + "/about/#team", "homeLocation": {"@type": "Place", "name": "Nairobi, Kenya"}}
        if FOUNDER.get("same_as"):
            person["sameAs"] = FOUNDER["same_as"]
        if FOUNDER.get("photo"):
            person["image"] = SITE["url"] + FOUNDER["photo"]
        graph.append(person)
    if p.get("crumbs"):
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE["url"] + "/"}]
        for i, (u, n) in enumerate(p["crumbs"], start=2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": SITE["url"] + u})
        graph.append({"@type": "BreadcrumbList", "itemListElement": items})
    if p.get("service"):
        s = p["service"]
        graph.append({"@type": "Service", "name": s["name"], "serviceType": s["type"],
                      "description": p["description"], "provider": {"@id": SITE["url"] + "/#org"},
                      "areaServed": "Worldwide", "url": url,
                      "offers": {"@type": "Offer", "priceCurrency": "USD", "price": s["from"],
                                 "priceSpecification": {"@type": "PriceSpecification", "minPrice": s["from"], "priceCurrency": "USD"}}})
    if p.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p["faq"]]})
    if p.get("cases"):
        from pages import CASES
        graph.append({"@type": "ItemList", "name": "AI agent case studies", "itemListElement": [
            {"@type": "ListItem", "position": i, "url": url + "#" + c["id"],
             "item": {"@type": "CreativeWork", "name": re.sub("&amp;", "&", c["title"]),
                      "description": c["summary"], "about": re.sub("&amp;", "&", c["industry"]),
                      "creator": {"@id": SITE["url"] + "/#org"}}}
            for i, c in enumerate(CASES, start=1)]})
    if p.get("article"):
        a = p["article"]
        graph.append({"@type": "BlogPosting", "headline": p["h1"], "description": p["description"],
                      "datePublished": a["date"], "dateModified": a.get("modified", a["date"]), "mainEntityOfPage": url,
                      "author": {"@id": SITE["url"] + "/#founder"},
                      "publisher": {"@id": SITE["url"] + "/#org"}, "image": SITE["url"] + "/og-image.png"})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, indent=1, ensure_ascii=False)


def faq_html(p):
    if not p.get("faq"):
        return ""
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in p["faq"])
    return (f'<section class="band"><div class="wrap"><div class="sec-head"><p class="label">FAQ</p>'
            f'<h2>{p.get("faq_title","Common questions")}</h2></div><div class="faq">{items}</div></div></section>')


def render(p):
    path = p["path"]
    canonical = SITE["url"] + "/" + path
    cur = ' aria-current="page"'
    nav = "".join(
        '<a href="{{' + u + '}}"' + (cur if ("/" + path).startswith(u) else "") + ">" + n + "</a>"
        for u, n in NAV)
    head_block = p.get("hero") or (
        f'<header class="page-head"><div class="wrap">{crumbs_html(p)}'
        f'<p class="label">{p.get("eyebrow","")}</p><h1 style="margin-top:14px">{p["h1"]}</h1>'
        f'<p class="lede">{p.get("lede","")}</p></div></header>')
    css = rel(path, "/assets/style.css")
    js = rel(path, "/assets/site.js")
    fx = rel(path, "/assets/fx.js")
    fav = rel(path, "/favicon.svg")
    robots = '<meta name="robots" content="noindex">' if (p.get("noindex") or STAGING) else '<meta name="robots" content="index,follow,max-image-preview:large">'

    T = _html.escape(p['title'], quote=True)
    D = _html.escape(p['description'], quote=True)
    head = f"""<title>{T}</title>
<meta name="description" content="{D}">
<link rel="canonical" href="{canonical}">
{robots}
<meta property="og:type" content="{'article' if p.get('article') else 'website'}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:title" content="{T}">
<meta property="og:description" content="{D}">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE['url']}/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2140">
<link rel="icon" href="{rel(path, "/favicon.ico")}" sizes="32x32">
<link rel="icon" href="{fav}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{rel(path, "/apple-touch-icon.png")}">
<link rel="manifest" href="{rel(path, "/site.webmanifest")}">
<link rel="preload" href="{rel(path, "/fonts/instrument-sans-latin-400-normal.woff2")}" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{rel(path, "/fonts/syne-latin-700-normal.woff2")}" as="font" type="font/woff2" crossorigin>
<script>document.documentElement.classList.add('js')</script>
<link rel="stylesheet" href="{css}">
<script type="application/ld+json">
{schema_for(p)}
</script>""" + (f'\n<meta name="google-site-verification" content="{SITE["gsc_verification"]}">' if SITE.get("gsc_verification") else "")

    body = f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
<a class="brand" href="{{{{/}}}}" aria-label="{SITE['name']} home">{LOGO}</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn" href="{{{{/contact/}}}}">Get a quote</a></nav>
</div></header>
<main id="main">
{head_block}
{p['body']}
{faq_html(p)}
{'' if p.get('no_cta') else CTA}
</main>
{FOOTER}
<script src="{js}" defer></script>
<script src="{fx}" defer></script>""" + (f'\n<script src="{rel(path, "/assets/analytics.js")}" data-ga="{SITE["ga4_id"]}" defer></script>' if SITE.get("ga4_id") else "")

    body = links(body, path).replace("__YEAR__", str(datetime.date.today().year))
    body = body.replace("__COOKIE__", ' · <button type="button" class="link-btn" data-cookie-settings>Cookie settings</button>' if SITE.get("ga4_id") else "")
    def _tw(m):
        rest = body[m.end():m.end() + 800]
        ths = re.findall(r"<th>(.*?)</th>", rest)[:2]
        label = "Table: " + " and ".join(re.sub("<[^>]+>", "", t) for t in ths) if ths else "Table"
        return f'<div class="table-wrap" tabindex="0" role="region" aria-label="{label}">'
    body = re.sub(r'<div class="table-wrap">', _tw, body)
    body = re.sub(r'<input (?![^>]*type=)', '<input type="text" ', body)
    if PREVIEW and path == "":
        return head + "\n" + body + "\n"   # artifact host wraps the main page only
    return f'<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n{head}\n</head>\n<body>\n{body}\n</body>\n</html>\n'


CTA = """<section class="band"><div class="wrap"><div class="cta">
<p class="label" style="color:#F2B544">Start a project</p>
<h2>Tell us what you need. You'll have a scoped plan and a fixed quote within two working days.</h2>
<p>No sales scripts. A 30-minute call with the people who will do the work, then a written proposal you can compare with anyone else's.</p>
<div class="btn-row"><a class="btn" href="{{/contact/}}">Get a quote</a><a class="btn ghost" href="{{/pricing/}}">See pricing</a></div>
</div></div></section>"""

FOOTER = """<footer class="site-foot"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{{/}}">""" + LOGO + """</a>
<p style="margin-top:14px;max-width:32ch">Your digital team in Nairobi. Websites, software, marketing and automation for small and mid-sized businesses worldwide.</p></div>
<div><h2>Services</h2><ul>
<li><a href="{{/services/web-development/}}">Web design &amp; development</a></li>
<li><a href="{{/services/software-development/}}">Custom software &amp; apps</a></li>
<li><a href="{{/services/digital-marketing-seo/}}">Digital marketing &amp; SEO</a></li>
<li><a href="{{/services/ai-automation/}}">AI &amp; automation</a></li></ul></div>
<div><h2>Company</h2><ul>
<li><a href="{{/about/}}">About</a></li><li><a href="{{/work/}}">Work</a></li><li><a href="{{/east-africa/}}">Kenya &amp; East Africa</a></li><li><a href="{{/why-kenya/}}">Why outsource to Kenya</a></li>
<li><a href="{{/pricing/}}">Pricing</a></li><li><a href="{{/blog/}}">Blog</a></li>
<li><a href="{{/contact/}}">Contact</a></li></ul></div>
<div><h2>Contact</h2><ul>
<li>""" + SITE["email"] + """</li><li><a href="https://wa.me/""" + SITE["whatsapp"] + """">WhatsApp """ + SITE["phone"] + """</a></li><li>Nairobi, Kenya · EAT (UTC+3)</li><li>M-Pesa accepted</li><li>Mon–Fri, 08:00–18:00 EAT</li></ul></div>
</div>
<div class="foot-base"><span>© __YEAR__ Sahara Nova. All rights reserved.</span><span><a href="{{/privacy/}}">Privacy policy</a>__COOKIE__</span></div>
</div></footer>"""


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(SRC, "assets"), os.path.join(OUT, "assets"))
    if os.path.isdir(os.path.join(SRC, "static", "fonts")):
        shutil.copytree(os.path.join(SRC, "static", "fonts"), os.path.join(OUT, "fonts"))
    for f in ("favicon.svg", "favicon.ico", "og-image.png", "apple-touch-icon.png", "logo.png", "icon-512.png", "site.webmanifest"):
        if os.path.exists(os.path.join(SRC, "static", f)):
            shutil.copy(os.path.join(SRC, "static", f), OUT)
    for p in PAGES:
        if p["path"] == "404.html":
            dest = os.path.join(OUT, "404.html")
        else:
            d = os.path.join(OUT, p["path"])
            os.makedirs(d, exist_ok=True)
            dest = os.path.join(d, "index.html")
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(render(p))
    if not PREVIEW:
        urls = [p for p in PAGES if not p.get("noindex")]
        sm = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for p in urls:
            art = p.get("article") or {}
            lastmod = p.get("updated") or art.get("modified") or art.get("date") or TODAY
            sm.append(f"  <url><loc>{SITE['url']}/{p['path']}</loc><lastmod>{lastmod}</lastmod></url>")
        sm.append("</urlset>")
        open(os.path.join(OUT, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
        open(os.path.join(OUT, "robots.txt"), "w").write(
            "User-agent: *\nDisallow: /\n" if STAGING else f"User-agent: *\nAllow: /\n\nSitemap: {SITE['url']}/sitemap.xml\n")
        open(os.path.join(OUT, "netlify.toml"), "w").write(NETLIFY.replace('    X-Frame-Options = "DENY"', '    X-Frame-Options = "DENY"\n    X-Robots-Tag = "noindex, nofollow"') if STAGING else NETLIFY)
    print("built", len(PAGES), "pages ->", OUT)


NETLIFY = """[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
    X-Frame-Options = "DENY"
    Strict-Transport-Security = "max-age=31536000; includeSubDomains"
    Permissions-Policy = "camera=(), microphone=(), geolocation=(), interest-cohort=()"
    Content-Security-Policy = "default-src 'self'; script-src 'self' 'sha256-Du+OJKJSbdUgz5nrHeWWINvez6XKDDU/tyj/5c2uvwo=' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https://*.google-analytics.com https://*.googletagmanager.com; font-src 'self'; connect-src 'self' https://*.google-analytics.com https://*.analytics.google.com https://*.googletagmanager.com; form-action 'self'; frame-ancestors 'none'; base-uri 'self'; object-src 'none'"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[headers]]
  for = "/fonts/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"
"""

if __name__ == "__main__":
    main()
