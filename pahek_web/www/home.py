import frappe


def get_context(context):
	doc = frappe.get_single("PAHEK Homepage Content")
	if not doc.published and not frappe.has_permission("PAHEK Homepage Content", "read"):
		raise frappe.PageDoesNotExistError

	context.no_cache = 1
	context.doc = doc
	context.title = doc.meta_title or "PAHEK Security — Operational Control for Guarding Operations"
	context.metatags = {
		"description": doc.meta_description
		or "PAHEK helps organizations strengthen operational control through structured supervision, measurable accountability, and field-tested control systems.",
	}
	context.full_width = 1
	context.blueprint_pillars = [
		p.strip() for p in (doc.blueprint_pillars_csv or "").split(",") if p.strip()
	]
	context.insights = frappe.get_all(
		"PAHEK Insight",
		filters={"published": 1},
		fields=["title", "route", "excerpt", "cover_image", "article_number"],
		order_by="published_date desc",
		limit_page_length=5,
	)
