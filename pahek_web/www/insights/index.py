import frappe


def get_context(context):
	context.no_cache = 1
	context.title = "Operational Insights"
	context.full_width = 1
	context.articles = frappe.get_all(
		"PAHEK Insight",
		filters={"published": 1},
		fields=["title", "route", "excerpt", "cover_image", "article_number", "published_date"],
		order_by="published_date desc",
		limit_page_length=0,
	)
