# Sahara Nova website: notes for AI assistants

- Static site: all content lives in `pages.py`; `build.py` renders it to `dist/`. Netlify builds on push to `main`.
- **Before writing or editing any blog post, guide, case study or service copy, read and follow `CONTENT_GUIDELINES.md`.** Key points:
  - Fact-check every claim and cite sources.
  - Never recommend a flow just because it sounds technically plausible. Check real-world constraints such as STK Push prompt expiry, WhatsApp policy, and CBK/ODPC rules.
  - No invented experience, timelines or statistics.
- Work on a branch and open a PR for James to review. Don't push straight to `main`.
- After changes: run `python3 build.py`, then check for broken internal links, valid JSON-LD, one H1 per page, and title/description lengths.
