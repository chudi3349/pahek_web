import frappe


def get_context(context):
	settings = frappe.get_single("PAHEK Site Settings")

	context.no_cache = 1
	context.title = "Contact PAHEK Security"
	context.metatags = {
		"description": "Get in touch with PAHEK Security to discuss operational challenges or book a security risk assessment.",
	}
	context.full_width = 1
	# Falls back to the same placeholder contact details already shown in the site footer
	# until Charles confirms real ones in PAHEK Site Settings.
	context.phone = settings.phone or "0803 712 5202"
	context.public_email = settings.public_email or "paheksec@yahoo.co.uk"
	context.office_address = settings.office_address or "Office Address — [pending]"
	context.recaptcha_enabled = bool(settings.recaptcha_enabled and settings.recaptcha_site_key)
	context.recaptcha_site_key = settings.recaptcha_site_key
