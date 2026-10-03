import frappe
from frappe import _
from frappe.rate_limiter import rate_limit

DISPOSABLE_EMAIL_DOMAINS = {
	"mailinator.com", "tempmail.com", "guerrillamail.com", "10minutemail.com",
	"throwawaymail.com", "yopmail.com", "trashmail.com", "fakeinbox.com",
	"getnada.com", "maildrop.cc", "temp-mail.org", "dispostable.com",
	"sharklasers.com", "mailnesia.com", "mintemail.com",
}


@frappe.whitelist(allow_guest=True, methods=["POST"])
@rate_limit(limit=10, seconds=3600, ip_based=True)
@rate_limit(key="email", limit=3, seconds=3600, ip_based=False)
def submit_enquiry(full_name, email, message, phone=None, organization=None, website=None):
	"""Public contact-form endpoint.

	`website` is a honeypot field in the form - hidden from real visitors with CSS,
	so only a bot filling every field blindly would ever populate it.
	"""
	# Honeypot tripped: pretend success so the bot doesn't learn anything.
	if (website or "").strip():
		return {"ok": True}

	full_name = (full_name or "").strip()
	email = (email or "").strip()
	message = (message or "").strip()
	phone = (phone or "").strip()
	organization = (organization or "").strip()

	if not full_name or not email or not message:
		frappe.throw(_("Please fill in your name, email, and message."))

	frappe.utils.validate_email_address(email, throw=True)

	domain = email.rsplit("@", 1)[-1].lower()
	if domain in DISPOSABLE_EMAIL_DOMAINS:
		frappe.throw(_("Please use a permanent email address."))

	# Secondary spam guard: the same email can't create more than one enquiry every 10 minutes.
	recent = frappe.db.count(
		"Lead",
		filters={
			"email_id": email,
			"creation": [">", frappe.utils.add_to_date(None, minutes=-10, as_string=True)],
		},
	)
	if recent:
		frappe.throw(_("We've already received your message — we'll be in touch shortly."))

	settings = frappe.get_single("PAHEK Site Settings")
	if settings.recaptcha_enabled:
		secret_key = settings.get_password("recaptcha_secret_key", raise_exception=False)
		if secret_key:
			_verify_recaptcha(frappe.form_dict.get("recaptcha_token"), secret_key)

	lead = frappe.new_doc("Lead")
	lead.lead_name = full_name
	lead.email_id = email
	if phone:
		lead.mobile_no = phone
	if organization:
		lead.company_name = organization
	lead.insert(ignore_permissions=True)
	lead.add_comment("Comment", text=message)

	_notify(settings, lead, full_name, email, phone, organization, message)

	frappe.db.commit()
	return {"ok": True}


def _verify_recaptcha(token, secret_key):
	if not token:
		frappe.throw(_("Please complete the verification and try again."))

	import requests

	try:
		resp = requests.post(
			"https://www.google.com/recaptcha/api/siteverify",
			data={"secret": secret_key, "response": token},
			timeout=5,
		)
		result = resp.json()
	except Exception:
		frappe.log_error(title="PAHEK reCAPTCHA verify failed", message=frappe.get_traceback())
		return  # fail open on API/network error - deliberate availability-over-strictness default

	if not result.get("success") or result.get("score", 1) < 0.5:
		frappe.throw(_("We couldn't verify your submission. Please try again."))


def _notify(settings, lead, full_name, email, phone, organization, message):
	# Falls back to the same contact address already shown on the site footer/contact page
	# until Charles confirms the Zoho admin@paheksecurity.com inbox is live.
	to = settings.enquiry_notification_email or settings.public_email or "paheksec@yahoo.co.uk"
	try:
		frappe.sendmail(
			recipients=[to],
			subject=f"New website enquiry from {full_name}",
			message=frappe.render_template(
				"<p><b>Name:</b> {{ name }}</p>"
				"<p><b>Email:</b> {{ email }}</p>"
				"{% if phone %}<p><b>Phone:</b> {{ phone }}</p>{% endif %}"
				"{% if organization %}<p><b>Organization:</b> {{ organization }}</p>{% endif %}"
				"<p><b>Message:</b></p><p>{{ message }}</p>"
				'<p><a href="{{ lead_url }}">View this Lead in PAHEK Desk</a></p>',
				{
					"name": full_name,
					"email": email,
					"phone": phone,
					"organization": organization,
					"message": message,
					"lead_url": frappe.utils.get_url(f"/app/lead/{lead.name}"),
				},
			),
			now=True,
		)
	except Exception:
		# The enquiry is already saved as a Lead either way - a missing/broken
		# outgoing Email Account must never cause the submission itself to fail.
		frappe.log_error(title="PAHEK enquiry notification failed", message=frappe.get_traceback())
