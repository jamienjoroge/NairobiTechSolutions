// Netlify event function: runs automatically after every verified (non-spam)
// Netlify Forms submission. For the "contact" form it creates a lead in Odoo CRM
// using Odoo 19's JSON-2 API.
//
// Environment variables (Netlify → Project configuration → Environment variables):
//   ODOO_URL          e.g. https://erp.saharanova.co.ke   (no trailing slash)
//   ODOO_API_KEY      API key of the dedicated "Website Integration" Odoo user
//   ODOO_DB           (optional) database name, needed only if the server hosts several
//   ODOO_SALESPERSON  (optional) Odoo user id to assign new leads to. Leave unset when the
//                     integration user has "Own Documents Only" CRM access: Odoo then only
//                     lets it create unassigned leads.
//
// The submission is always kept in Netlify Forms (and its email notification is
// still sent), so if Odoo is down nothing is lost: the error is logged and the
// lead can be added by hand.

const SOURCE_NAME = "Website Contact Form";

// Contact form "What do you need?" option -> CRM tag name
const SERVICE_TAGS = {
  "New website": ["Web Development"],
  "E-commerce store": ["Web Development"],
  "Custom software / MVP": ["Software Development"],
  "Mobile app": ["Software Development"],
  "SEO / digital marketing": ["SEO & AEO"],
  "AI & automation": ["AI & Automation"],
  "Dedicated developer": ["Software Development", "Monthly Plan"],
};

const EAST_AFRICA = [
  "kenya", "uganda", "tanzania", "rwanda", "burundi", "ethiopia",
  "somalia", "south sudan", "djibouti", "eritrea", "drc", "congo",
];

const clean = (v, max = 5000) => String(v ?? "").trim().slice(0, max);

async function odoo(model, method, body) {
  const base = process.env.ODOO_URL.replace(/\/+$/, "");
  const headers = {
    "Content-Type": "application/json",
    Authorization: `bearer ${process.env.ODOO_API_KEY}`,
  };
  if (process.env.ODOO_DB) headers["X-Odoo-Database"] = process.env.ODOO_DB;
  const res = await fetch(`${base}/json/2/${model}/${method}`, {
    method: "POST",
    headers,
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(8000),
  });
  const text = await res.text();
  if (!res.ok) throw new Error(`Odoo ${model}.${method} HTTP ${res.status}: ${text.slice(0, 500)}`);
  return JSON.parse(text);
}

async function idsByName(model, names) {
  if (!names.length) return [];
  const rows = await odoo(model, "search_read", {
    domain: [["name", "in", names]],
    fields: ["id"],
  });
  return rows.map((r) => r.id);
}

export async function handler(event) {
  try {
    const { payload } = JSON.parse(event.body || "{}");
    if (!payload || payload.form_name !== "contact") {
      return { statusCode: 200, body: "ignored" };
    }
    if (!process.env.ODOO_URL || !process.env.ODOO_API_KEY) {
      console.error("ODOO_URL / ODOO_API_KEY not set; lead not sent to Odoo");
      return { statusCode: 200, body: "not configured" };
    }

    const d = payload.data || {};
    if (clean(d.company_website)) return { statusCode: 200, body: "honeypot" };

    const name = clean(d.name, 200);
    const email = clean(d.email, 200);
    const company = clean(d.company, 200);
    const country = clean(d.country, 100);
    const service = clean(d.service, 100);
    const budget = clean(d.budget, 100);
    const message = clean(d.message);

    const tagNames = [...(SERVICE_TAGS[service] || [])];
    if (country) {
      const c = country.toLowerCase();
      tagNames.push(EAST_AFRICA.some((k) => c.includes(k)) ? "Kenya / East Africa" : "International");
    }

    const [tagIds, sourceIds] = await Promise.all([
      idsByName("crm.tag", tagNames),
      idsByName("utm.source", [SOURCE_NAME]),
    ]);

    const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    const details = [
      ["Service", service],
      ["Budget", budget],
      ["Country", country],
      ["Company", company],
      ["Submitted", payload.created_at],
      ["Page", payload.data?.referrer || payload.site_url],
    ].filter(([, v]) => v);
    const description =
      `<p>${esc(message).replace(/\n/g, "<br>")}</p>` +
      `<ul>${details.map(([k, v]) => `<li><b>${k}:</b> ${esc(String(v))}</li>`).join("")}</ul>`;

    const vals = {
      type: "lead",
      name: `Website enquiry: ${service || "General"} – ${company || name}`.slice(0, 200),
      contact_name: name,
      email_from: email,
      partner_name: company || false,
      description,
      tag_ids: [[6, 0, tagIds]],
    };
    if (sourceIds.length) vals.source_id = sourceIds[0];
    vals.user_id = process.env.ODOO_SALESPERSON ? Number(process.env.ODOO_SALESPERSON) : false;

    const created = await odoo("crm.lead", "create", { vals_list: [vals] });
    console.log("Odoo lead created", created);
    return { statusCode: 200, body: "ok" };
  } catch (err) {
    // Never fail the submission: Netlify Forms already stored it.
    console.error("Failed to create Odoo lead:", err.message);
    return { statusCode: 200, body: "error logged" };
  }
}
