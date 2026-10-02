import frappe


def get_context(context):
	doc = frappe.get_single("PAHEK Risk Assessment Content")
	if not doc.published and not frappe.has_permission("PAHEK Risk Assessment Content", "read"):
		raise frappe.PageDoesNotExistError

	context.no_cache = 1
	context.doc = doc
	context.title = doc.meta_title or "Security Risk Assessment — PAHEK Security"
	context.metatags = {"description": doc.meta_description or doc.hero_subheading}
	context.full_width = 1
	context.input_tags = [
		t.strip() for t in (doc.diagnosis_input_tags_csv or "").split(",") if t.strip()
	]
