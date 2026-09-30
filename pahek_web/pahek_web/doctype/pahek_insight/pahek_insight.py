import frappe
from frappe.website.website_generator import WebsiteGenerator


class PAHEKInsight(WebsiteGenerator):
	website = frappe._dict(
		template="templates/generators/pahek_insight.html",
		condition_field="published",
		page_title_field="title",
	)

	def get_context(self, context):
		context.template = self.website.template
		context.no_cache = 1
		context.title = self.title
		context.article = self
		context.related = frappe.get_all(
			"PAHEK Insight",
			filters={"published": 1, "name": ["!=", self.name]},
			fields=["title", "route", "excerpt", "cover_image", "article_number"],
			order_by="published_date desc",
			limit_page_length=3,
		)
