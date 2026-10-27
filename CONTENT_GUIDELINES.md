# Sahara Nova blog: content rules

Every post, guide, case study and service-page claim follows these rules. They apply whoever writes the draft, whether a person or an AI.

## 1. Write as a practitioner, not a brochure
- Explain how something actually behaves in production, including the limits, failure modes and trade-offs, not just how it is supposed to work.
- **Never recommend a flow because it sounds like it would work.** If we haven't built it, or a credible source doesn't confirm it works in practice, don't present it as advice.
  - Example: an M-Pesa STK Push prompt expires within about a minute. So "send a repayment reminder with an STK prompt" is impractical, because the customer is rarely holding the phone ready to pay. Trigger the prompt only when the customer has just asked to pay.
- Check the platform rules before recommending a channel: Meta/WhatsApp Business policy, Safaricom Daraja terms, CBK, SASRA and ODPC requirements. A design that breaks platform policy is not best practice, however well it works technically.
- Give the honest answer when a tool is the wrong choice. For example, use a simple rule-based automation when AI isn't needed.

## 2. Fact-check every claim
- Every number, rate, price, limit, timeout, regulation or legal duty needs a source, or must be our own measured result. Put a short source line under tables, or link the source inline.
- Use primary sources first: official documentation (Safaricom Daraja, Meta, CBK, ODPC, Kenya Law, SASRA), the original study, then reputable secondary sources. Check the date. Anything about pricing, policy or APIs should be from the last 12 months.
- When sources disagree (for example, STK prompt timeouts reported as 30–60 seconds), give the range and say it varies. Don't pick one number.
- Don't invent experience. No "the most common problem we see…", "clients usually…" or "in our experience it takes N weeks" unless James has confirmed it. Case-study facts come only from what James has confirmed.
- Timelines and costs for our work come from our published pricing or from James. Otherwise, leave them out.

## 3. Legal, financial and compliance topics
- State what the rule says, cite it (Act, section or regulation where possible), and tell readers to confirm with their own legal or compliance adviser. Don't give legal conclusions about a reader's specific business.
- Lending, payments and personal data posts must cover consent and opt-out (Data Protection Act 2019, s.37; Data Protection (General) Regulations 2021), and any channel restrictions.

## 4. Claims about results
- Only publish results we can stand behind (for example, KES 5.4M in the first week, reply time from ~5 days to instant). No projected or "up to" figures.
- No client names. Odoo and HubSpot may be named; keep the AI agent platform generic.

## 5. Before publishing: checklist
- [ ] Every number and rule has a source or is our own confirmed result
- [ ] Each recommended flow has been checked against real-world constraints (timeouts, rate limits, costs, channel policies, regulation)
- [ ] Nothing is advised just because it sounds plausible
- [ ] Failure modes and when not to use the approach are covered
- [ ] No invented experience, timelines or statistics
- [ ] Sources listed are dated within 12 months for fast-moving topics
- [ ] Title ≤ 65 characters, meta description ≤ 160 characters, one H1, internal links to the relevant service page and case study
- [ ] James has reviewed technical and case-study details

## 6. Audience and priorities
- Main market: international small and mid-sized business owners buying **AI automation and AI agents**. Weight new content towards AI automation; Kenya and East Africa posts support local search.
- Plain, British English, no jargon without a one-line explanation, and no hype.
