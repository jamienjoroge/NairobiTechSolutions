# Sahara Nova website: deploy & launch guide

## What's in this folder
- `dist/`: the finished website. Upload this folder.
- `pages.py`: all page copy, prices, email and domain (edit here).
- `build.py`: rebuilds `dist/` after edits: `python3 build.py`
- `assets/`: stylesheet and script; `static/`: favicon + social share image.

## 1. Domain: saharanova.co.ke (registered)
The site is built for `https://saharanova.co.ke` (no www). To change it, edit `url` and `email` at the top of `pages.py` and run `python3 build.py`.

**Connect it in Netlify:** go to Domain management → Add a domain → `saharanova.co.ke`. Then, at your .co.ke registrar's DNS settings, choose ONE of these:
- **A (easiest): use Netlify DNS.** Netlify shows 4 nameservers (dns1–dns4.p0X.nsone.net); paste them into your registrar's "Nameservers" setting. Afterwards, add email MX records inside Netlify.
- **B: keep the registrar's DNS.** Add `A  @  75.2.60.5` and `CNAME  www  <your-site>.netlify.app`.
DNS can take up to 24 h. HTTPS turns on automatically once it resolves.

**Test version first:** run `python3 build.py --staging` and deploy `dist-staging/`. It is noindex-ed everywhere, so you can test safely on the netlify.app address.

## 2. Deploy to Netlify (free, about 10 min)
1. Create an account at netlify.com → **Add new site → Deploy manually**.
2. Drag the `dist` folder onto the page. The site is live on a `*.netlify.app` address.
3. **Domain management → Add a domain** → enter your domain → follow the DNS instructions. HTTPS is issued automatically.
4. **Forms**: Netlify detects the contact form automatically. Under *Site configuration → Notifications → Form submission notifications*, add your email address.
   (For updates later, connect a GitHub repo so every change deploys automatically.)

## 3. Email
Set up `hello@yourdomain` with Google Workspace or Zoho Mail (Zoho has a free tier). Add their MX/SPF/DKIM records at your DNS provider.

## 4. Google Search Console (critical for SEO)
1. search.google.com/search-console → **Add property → Domain** → verify with a DNS TXT record.
2. **Sitemaps** → submit `https://yourdomain/sitemap.xml`.
3. **URL inspection** → request indexing for the homepage and the 4 service pages.
4. Do the same at Bing Webmaster Tools (you can import from Search Console in one click).

## 5. Analytics
Recommended: **Plausible** (privacy-friendly, no cookie banner). Paste its one-line script before `</head>` in `build.py`'s head template and rebuild.
⚠️ The site sends a strict **Content-Security-Policy** (in `netlify.toml`). When you add Plausible, add its domain to both `script-src` and `connect-src`, e.g. `script-src 'self' https://plausible.io ...; connect-src 'self' https://plausible.io`. Without this the analytics script will be blocked.
Set up a goal for the `/thanks/` page. Every form submission lands there, so it counts leads.
Alternative: GA4 (free, but UK/EU visitors then need a cookie consent banner).

## 6. Google Business Profile
business.google.com → create "Sahara Nova", category *Website designer* (secondary: *Software company*, *Internet marketing service*). Set it as a service-area business if you don't want your address public.

## 7. First 30 days of SEO
- [ ] Claim Clutch, GoodFirms, DesignRush and LinkedIn Company Page profiles. Add their URLs to `same_as` in `pages.py`.
- [ ] Publish 1–2 new blog articles per week (topics are in the strategy doc). Copy the article structure in `pages.py`.
- [ ] Replace the About page's general copy with real team names, photos and LinkedIn links (a strong trust signal).
- [ ] Add a case study as soon as you finish a project (with the client's permission).
- [ ] Check Search Console weekly: indexing errors, queries, and click-through rate.

## Production-readiness audit (23 Sep 2026)
Automated checks passed on all 16 pages: HTML validation, axe accessibility (WCAG 2.1 AA) in light and dark themes at desktop and mobile widths, Lighthouse mobile (Performance 99–100, Accessibility 100, Best Practices 100, SEO 100), zero broken links, valid structured data, and a sitemap that matches the indexable pages.
Functional tests passed: the CSP produces no console errors, the self-hosted fonts load, the mobile menu opens and closes with Escape, the form submission redirects to /thanks/, and the navigation works without JavaScript.

### Must do before launch
- [ ] Final domain → update `url` + `email` in `pages.py`, rebuild
- [ ] Working mailbox for the contact email
- [ ] Netlify form notifications turned on, then one real test submission
- [ ] Confirm the prices on the site match `pages.py`, and that you're happy with every commitment on the site: "reply within 1 working day", "quote within 48 h", "KRA-compliant invoices" (needs eTIMS), "white-label SEO", "in-person meetings"
- [ ] Privacy policy: add the registered company name and address once Sahara Nova Ltd is incorporated

### Should do in the first 2 weeks
- [ ] Real team names/photos on About; James as named author on blog posts (E-E-A-T)
- [ ] Case studies / AI agent examples (Work page)
- [ ] Search Console + Bing, sitemap submitted
- [ ] Google Business Profile; add profile URLs to `same_as`

## Canvas effects (assets/fx.js, about 5.5 KB gzipped)
- Hero: night sky, nova flares, drifting dunes and blowing sand (homepage `.hero`).
- Agent flows: animated step diagrams on the Work page (one per case study) and on the AI & automation page. Steps live in `FLOWS` in `pages.py`.
- The KES 5.4M counter counts up when it scrolls into view. The real figure is already in the HTML, so Google sees it.
- Everything pauses when off-screen or when the tab is hidden. Phones run at 30 fps. "Reduce motion" users get a still frame.
- To turn effects off, remove the `fx.js` script line in `build.py` and rebuild. The site still works fully.
