import frappe


def get_context(context):
	doc = frappe.get_single("PAHEK About Content")
	if not doc.published and not frappe.has_permission("PAHEK About Content", "read"):
		raise frappe.PageDoesNotExistError

	context.no_cache = 1
	context.doc = doc
	context.title = doc.meta_title or "About PAHEK Security"
	context.metatags = {"description": doc.meta_description or doc.hero_subheading}
	context.full_width = 1
