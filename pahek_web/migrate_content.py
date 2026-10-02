"""One-time content migration: populates the 5 Desk-editable singleton DocTypes
with the exact copy/content that was live in the hand-built Web Page records.

Run after deploying the DocTypes (new image tag + migrate):
    bench --site pahek.ejitech.life execute pahek_web.migrate_content.run

Safe to re-run: every section is fully overwritten (tables cleared and re-appended)
rather than appended to, so re-running just re-syncs content, it never duplicates rows.
"""

import frappe


def run():
	set_home()
	set_about()
	set_our_approach()
	set_risk_assessment()
	set_guarding_operations()
	frappe.db.commit()
	print("PAHEK content migration complete.")


def set_home():
	doc = frappe.get_single("PAHEK Homepage Content")

	doc.hero_headline = "Move Beyond Security Presence to Operational Control"
	doc.hero_subheading = "PAHEK helps organizations strengthen operational control through structured supervision, measurable accountability, and field-tested control systems."
	doc.hero_cta_primary_label = "Book an Operational Assessment"
	doc.hero_cta_secondary_label = "Explore the Blueprint"
	doc.set("hero_stats", [])
	for value, label in [
		("38+", "Years of field operations"),
		("100s", "Operational site assessments"),
		("NSCDC", "Licensed security operations"),
	]:
		doc.append("hero_stats", {"value": value, "label": label})

	doc.stakes_heading_1 = "Most Security Operations Look Structured — Until Tested"
	doc.stakes_body_1 = "Many organizations assume security is functioning because guards are deployed, patrols are conducted, and reports are submitted regularly."
	doc.stakes_heading_2 = "Visible Activity Is Not the Same as Control"
	doc.stakes_body_2 = (
		"<p>But visible activity is not the same as operational control.</p>"
		"<p>Weak supervision, unverifiable patrols, fragmented accountability, and assumption-based oversight often "
		"create hidden operational exposure long before incidents occur.</p>"
	)

	doc.transformation_heading_1 = "Operational Confidence Comes From Measurable Control"
	doc.transformation_body_1 = (
		"<p>Operational confidence is built through systems that can be monitored, verified, and enforced "
		"consistently across the field.</p>"
		"<p>When supervision is structured, accountability is measurable, and operational activity becomes visible "
		"in real time, organizations gain stronger control over security operations and exposure management.</p>"
	)
	doc.transformation_heading_2 = "A Disciplined, Coordinated, Resilient Operation"
	doc.transformation_body_2 = "The result is a more disciplined, coordinated, and resilient operation — one leadership can oversee with greater clarity and confidence."

	doc.services_intro_heading = "How PAHEK Strengthens Operational Control"
	doc.services_intro_body = "Effective security operations require more than manpower presence. They require structured systems that improve supervision, accountability, operational visibility, and field control. PAHEK supports organizations through operational capabilities designed to strengthen accountability, visibility, and operational control across security personnel, processes, and environments."

	doc.set("service_cards_operations", [])
	for icon_key, heading, body in [
		("shape_grid_doc", "Guarding Operations", "Structured deployment, patrol supervision, and site control systems designed to improve operational accountability and field visibility."),
		("shape_shield_check", "Security Risk Assessments", "Operational exposure identification and vulnerability analysis designed to strengthen security decision-making and reduce hidden risk."),
		("shape_clipboard", "Operational Audits", "Evaluation of supervision quality, patrol integrity, reporting systems, and accountability systems."),
	]:
		doc.append("service_cards_operations", {"icon_key": icon_key, "heading": heading, "body": body})

	doc.set("service_cards_structure", [])
	for icon_key, heading, body in [
		("shape_three_lines", "SOP Development", "Procedural frameworks designed to improve operational consistency, enforcement standards, escalation structure, and field coordination."),
		("shape_person", "Security Training", "Supervisor and guard development programs focused on accountability, reporting discipline, operational awareness, and field performance."),
	]:
		doc.append("service_cards_structure", {"icon_key": icon_key, "heading": heading, "body": body})

	doc.set("service_cards_governance", [])
	for icon_key, heading, body in [
		("shape_shield_check_navy", "Operational Consulting", "Strategic advisory support for organizations seeking stronger operational control, system improvement, and governance alignment."),
		("shape_grid_lines", "Security Governance Support", "Oversight frameworks designed to improve field visibility, accountability enforcement, escalation management, and operational consistency."),
	]:
		doc.append("service_cards_governance", {"icon_key": icon_key, "heading": heading, "body": body})

	doc.capability_heading = "Operational Visibility, Accountability & Control"
	doc.set("capability_items", [])
	for icon_key, label in [
		("shape_eye", "Supervision Quality"),
		("shape_chart_path", "Operational Visibility"),
		("shape_check_circle", "Accountability Enforcement"),
		("shape_compass", "Patrol Verification"),
		("shape_bolt", "Response Coordination"),
		("shape_bars_asc", "Leadership Oversight"),
		("shape_squares", "Operational Consistency"),
		("shape_alert_triangle", "Exposure Management"),
	]:
		doc.append("capability_items", {"icon_key": icon_key, "heading": label})

	doc.plan_heading = "A Structured Path to Stronger Operational Control"
	doc.set("plan_steps", [])
	for number, heading, body in [
		("01", "Book an Operational Assessment", "Identify operational exposure, supervision gaps, and control weaknesses across existing security operations."),
		("02", "Receive an Operational Exposure Review", "Gain visibility into operational risks, accountability gaps, and field supervision performance."),
		("03", "Implement Structured Control Systems", "Strengthen accountability, visibility, supervision, and field performance through structured operational systems."),
	]:
		doc.append("plan_steps", {"number": number, "heading": heading, "body": body})

	doc.narrative_bridge_quote = "Operational discipline is taught before it's deployed."

	doc.authority_heading = "Operational Credibility Built Through Real-World Security Operations"
	doc.set("authority_cards", [])
	for group_label, tag_1, icon_key, heading, body in [
		("38+ yrs", "", "", "Nearly Four Decades of Real-World Security Operations", "Field supervision, deployment oversight, operational assessments, and security operations across multiple operational environments."),
		("6+ Sectors", "28", "", "Experience Across Complex Operational Environments", "Construction, Industrial, Warehousing, Commercial, Corporate, and High-Responsibility Operations."),
		("◆", "", "", "Structured Oversight Systems", "Field-tested operational oversight systems focused on supervision, accountability enforcement, escalation management, reporting integrity, and operational visibility."),
		("100s", "", "", "Operational Site Assessments Across Active Environments", "Operational reviews and site assessments designed to identify supervision gaps, operational exposure, accountability weaknesses, and control vulnerabilities."),
		("", "", "shape_doc_lines", "Developers of a Structured Operational Control Framework", "Developed through real-world field operations, supervision oversight, accountability systems, and measurable operational performance."),
		("◆", "", "", "Active Participation in Security Leadership & Governance", "Ongoing involvement in operational governance discussions, professional development, security leadership initiatives, and industry engagement activities."),
	]:
		doc.append("authority_cards", {"group_label": group_label, "tag_1": tag_1, "icon_key": icon_key, "heading": heading, "body": body})

	doc.set("compliance_strip_items", [])
	for heading in [
		"NSCDC LICENSED SECURITY OPERATIONS",
		"COMPLIANCE-ORIENTED OPERATIONAL STANDARDS",
		"STRUCTURED OVERSIGHT SYSTEMS",
		"ACTIVE INDUSTRY ENGAGEMENT",
	]:
		doc.append("compliance_strip_items", {"heading": heading})

	doc.human_authority_heading = "Operational Leadership That Has Walked the Site"
	doc.human_authority_body_1 = "PAHEK's systems are shaped by decades spent directly in the field — inspecting sites, correcting supervision gaps, and enforcing accountability under real operating conditions."
	doc.human_authority_body_2 = "That field-tested perspective, not theory, is what informs every framework PAHEK builds."
	doc.set("human_authority_stats", [])
	for value, label in [("38+", "Years in field operations"), ("100s", "Site assessments led personally")]:
		doc.append("human_authority_stats", {"value": value, "label": label})

	doc.blueprint_heading = "A Field-Tested Framework for Operational Accountability and Control"
	doc.blueprint_body_1 = "The PAHEK Blueprint was developed to address a persistent operational weakness: the gap between visible security activity and measurable operational control."
	doc.blueprint_body_2 = "Built through real-world operational experience, the framework introduces a structured approach to supervision, accountability, escalation management, operational visibility, and field execution across security environments."
	doc.blueprint_body_3 = "The Blueprint emphasizes operational systems that can be monitored, verified, and enforced consistently over time."
	doc.blueprint_image_caption = "The Blueprint, in daily field use"
	doc.blueprint_pillars_csv = "Supervision, Accountability, Escalation Management, Operational Visibility, Field Execution"

	doc.set("doctrine_quotes", [])
	for quote in [
		"Presence is not control.",
		"If it cannot be verified, it cannot be trusted.",
		"Operational visibility reduces exposure.",
		"Structure without accountability creates hidden risk.",
	]:
		doc.append("doctrine_quotes", {"quote_text": quote})

	doc.set("proof_quotes", [])
	for eyebrow, heading, body in [
		("Patrol Accountability", "Unverified Patrol Activity Creates Assumption-Based Operations", "Operational control weakens when patrol activity cannot be monitored, validated, and enforced through measurable accountability systems."),
		("Field Experience", "38+ Years Across Real-World Security Operations", "Operational exposure across construction, industrial, commercial, warehousing, and high-responsibility operational environments."),
		("Industry Participation", "Contributing to Operational Security Discussions and Professional Development", "Engagement across security leadership platforms, operational forums, and professional industry initiatives."),
		("Operational Doctrine", "Developed to Address the Gap Between Security Presence and Operational Control", "The Blueprint framework introduces a structured operational approach to accountability, verification, and measurable field performance."),
		("Operational Analysis", "Visible Security Activity Can Create False Operational Assurance", "Operational confidence weakens when visibility exists without reliable verification, accountability, and enforcement systems."),
		("Operational Governance", "Structure Without Accountability Creates Hidden Operational Risk", "Many security operations maintain reporting structures and patrol activity while lacking measurable enforcement systems."),
		("Assessment Exposure", "Hundreds of Operational Site Assessments Across Active Environments", "Operational reviews conducted across industrial, corporate, commercial, and high-responsibility operational sites."),
		("Operational Supervision", "Accountability Systems Fail When Oversight Structures Become Inconsistent", "Operational control weakens when supervision standards vary across personnel, shifts, and field environments."),
		("Operational Philosophy", "Presence Is Not Control", "Visible security activity alone does not guarantee operational accountability, supervision integrity, or measurable field performance."),
	]:
		doc.append("proof_quotes", {"eyebrow": eyebrow, "quote_text": heading, "attribution": body})

	doc.final_cta_heading = "Strengthen Operational Control Before Exposure Becomes Incident"
	doc.final_cta_body = "PAHEK supports organizations seeking stronger operational visibility, accountability enforcement, and measurable control across security operations and field environments."

	doc.meta_title = "PAHEK Security — Operational Control for Guarding Operations"
	doc.meta_description = "PAHEK helps organizations strengthen operational control through structured supervision, measurable accountability, and field-tested control systems."
	doc.published = 1
	doc.save(ignore_permissions=True)


def set_about():
	doc = frappe.get_single("PAHEK About Content")

	doc.hero_headline = "A Different Way of Seeing Security Operations"
	doc.hero_subheading = "Most reviews of a guarding operation ask whether personnel are present. PAHEK was built on a different habit — noticing the exposure, drift, and blind spots that presence alone never reveals."
	doc.hero_image_caption = "Field observations, structured into a framework, refined over years."

	doc.formation_heading = "Formed in the Field, Not in Theory"
	doc.formation_body = (
		"<p>A patrol route that looked correct on paper, until walking it revealed a gap the paperwork never showed. "
		"A supervision standard that held whenever someone was watching, and only showed its true state on the one day "
		"no one was. An assumption that worked at nine sites and quietly failed at the tenth, for a reason nobody had "
		"written down until then.</p>"
		"<p>Those weren't isolated incidents. They became the beginning of a different way of seeing security "
		"operations — formed over years of site reviews, risk assessments, and deployment evaluations across "
		"construction, industrial, warehousing, and corporate environments, led by Charles Keku.</p>"
		"<p>Some of these observations held up across every environment that followed. Others were rewritten when "
		"the next site contradicted them. What survived enough places, across enough years, became rigorous enough "
		"to document — eventually forming the basis of the Security Guarding Operations Blueprint.</p>"
	)

	doc.continuity_heading = "Still Being Formed, Not Archived"
	doc.continuity_body = (
		"<p>This way of seeing is not a founding principle preserved from an earlier period. It continues to be "
		"tested today, through ongoing site assessments, direct client coordination, and continued involvement in "
		"the wider security industry.</p>"
		"<p>Every new site still adds to what came before it. The habit of noticing has not stopped forming.</p>"
	)

	doc.built_heading = "What It Built"
	doc.built_intro = "This same habit of noticing is what built the rest of PAHEK's operational system. None of it began as a framework. It began as years of paying attention."
	doc.set("built_cards", [])
	for group_label, heading, body, link_text, link_route in [
		("Guarding Operations", "Accountability, Visibility, Responsiveness", "Why guarding is built around an accountable system — not deployment alone.", "Explore Operational Control", "/guarding-operations"),
		("Security Risk Assessment", "A Diagnosis, Not a List", "Why an assessment produces a ranked understanding of what matters — not just observations.", "Explore the Diagnosis", "/security-risk-assessment"),
		("Our Approach", "One Operating System", "Why every engagement operates inside one system, sharpened by everything learned before it.", "Explore the Operating System", "/our-approach"),
	]:
		doc.append("built_cards", {"group_label": group_label, "heading": heading, "body": body, "link_text": link_text, "link_route": link_route})

	doc.final_cta_heading = "See It Applied to Your Operation"
	doc.final_cta_body = "An assessment is the first place this way of seeing gets applied to your own operation — the same habit of noticing, formed over years of direct field work, not a generic checklist."
	doc.final_cta_secondary_label = "Revisit the Operating System"
	doc.final_cta_secondary_route = "/our-approach"

	doc.meta_title = "About PAHEK Security — Formed in the Field, Not in Theory"
	doc.meta_description = doc.hero_subheading
	doc.published = 1
	doc.save(ignore_permissions=True)


def set_our_approach():
	doc = frappe.get_single("PAHEK Our Approach Content")

	doc.hero_headline = "One Operating System Behind Every PAHEK Engagement"
	doc.hero_subheading = "Guarding, assessment, improvement, and operational fluency are not separate services — they are stages of one continuous operational system, built on constants that never change."
	doc.hero_cta_primary_label = "Request an Operational Assessment"
	doc.hero_cta_secondary_label = "See the Full System"

	doc.os_intro_text = "Every PAHEK engagement operates within one system."
	doc.set("os_constants", [])
	for heading, body in [
		("Doctrine Principles", "What PAHEK believes about security and operational control — present in every engagement."),
		("Ground Truths", "What PAHEK has repeatedly observed through real field experience — sharpened by every engagement."),
	]:
		doc.append("os_constants", {"heading": heading, "body": body})
	doc.os_constants_caption = "Guiding Every Stage of the Operating Cycle"

	doc.set("os_cycle_steps", [])
	for number, heading, body in [
		("STAGE 01", "Operational Diagnosis", "Identifying real exposure and priorities."),
		("STAGE 02", "Operational Control", "Building the accountable system."),
		("STAGE 03", "Operational Improvement", "Correcting drift as conditions evolve."),
		("STAGE 04", "Operational Fluency", "Developing independent capability."),
	]:
		doc.append("os_cycle_steps", {"number": number, "heading": heading, "body": body})
	doc.os_loopback_text = "Each cycle sharpens the next Diagnosis — operational excellence is never static."

	doc.constants_intro_text = "Two Operating Constants stay active throughout every engagement."
	doc.constants_heading = "Operating Constants"
	doc.set("constants_cards", [])
	for group_label, heading, body, link_text, link_route in [
		("Philosophical", "Doctrine Principles", "The premises that govern how PAHEK thinks about security — including the idea that presence is not control. These aren't conclusions reached through fieldwork; they're the starting beliefs that shape how every engagement is approached.", "Explore Doctrine Principles on the Homepage", "/#blueprint"),
		("Empirical", "Ground Truths", "Operational patterns only visible after years of running real guarding operations — earned through experience, not argument. Each engagement adds to this library and sharpens the next.", "Explore Ground Truths on Guarding Operations", "/guarding-operations"),
	]:
		doc.append("constants_cards", {"group_label": group_label, "heading": heading, "body": body, "link_text": link_text, "link_route": link_route})

	doc.cycle_intro_text = "From these constants, one continuous cycle creates value for every client — each stage building directly on the one before it."
	doc.set("cycle_stages", [])
	doc.append("cycle_stages", {
		"number": "01", "heading": "The Operational Diagnosis",
		"body": "<p>A clear, evidence-based picture of where an operation is actually exposed, and what matters most — replacing assumption before any solution is proposed.</p>",
		"link_text": "Explore the Diagnosis on Security Risk Assessment", "link_route": "/security-risk-assessment",
	})
	doc.append("cycle_stages", {
		"number": "02", "heading": "Operational Control",
		"body": "<p>The accountable, verifiable system built in response to the diagnosis — Accountability, Visibility, and Responsiveness working together, not manpower alone.</p>",
		"link_text": "Explore Operational Control on Guarding Operations", "link_route": "/guarding-operations",
	})
	doc.append("cycle_stages", {
		"number": "03", "heading": "Operational Improvement",
		"body": (
			"<p>A control system built well on day one does not stay well-suited to day one thousand. Operations evolve — "
			"personnel change, risks shift, physical conditions change, and even the best-designed system will drift from "
			"its original standard unless something actively keeps adjusting it.</p>"
			"<p>Operational Improvement is PAHEK's ongoing role after a system is built: periodic re-assessment, correcting "
			"drift before it compounds, and adapting supervision, reporting, and escalation structures as real conditions "
			"change. This is not a one-time fix — it is a standing responsibility for as long as the engagement "
			"continues.</p>"
			'<div class="deep-pullquote"><q>Guards rarely drift from standard all at once. It happens one uncorrected '
			'shift at a time.</q><span>Ground Truth — Guarding Operations</span></div>'
			"<p>This is precisely why Operational Improvement exists as a distinct, ongoing stage rather than a box to "
			"check once: the alternative to continuous correction is exactly the quiet, incremental drift this Ground "
			"Truth describes.</p>"
		),
		"link_text": "", "link_route": "",
	})
	doc.append("cycle_stages", {
		"number": "04", "heading": "Operational Fluency",
		"body": (
			"<p>Operational Improvement keeps PAHEK's system sharp. Operational Fluency is different in kind — it is "
			"where a client's own people develop the judgment to recognize exposure, ask the right questions, and "
			"support strong operational decisions independently, rather than relying on a system alone to catch what "
			"it misses.</p>"
			"<p>This is not about making PAHEK unnecessary. It is about building a stronger long-term partnership — the "
			"person responsible for the operation noticing an early warning sign before it becomes a finding, because "
			"they now understand the same operational language PAHEK does.</p>"
			'<div class="deep-tags"><span>Consulting</span><span>Training</span><span>Knowledge Transfer</span>'
			"<span>Operational Reviews</span><span>The Security Guarding Operations Blueprint</span></div>"
			"<p style=\"margin-top:var(--space-5);\">And because operations, people, and risks never stop changing, "
			"what's learned here feeds directly back into a sharper next Diagnosis.</p>"
		),
		"link_text": "", "link_route": "",
	})

	doc.final_cta_heading = "Request an Operational Assessment"
	doc.final_cta_body = "An assessment is the entry point into a continuous operating system — Diagnosis, Control, Improvement, and Operational Fluency, each stage building from what the last one reveals."
	doc.final_cta_secondary_label = "Revisit the Operating System"

	doc.meta_title = "Our Approach — One Operating System Behind Every PAHEK Engagement"
	doc.meta_description = doc.hero_subheading
	doc.published = 1
	doc.save(ignore_permissions=True)


SECTOR_ITEMS = [
	("shape_building_construction", "Construction"),
	("shape_building_industrial", "Industrial"),
	("shape_building_warehouse", "Warehousing"),
	("shape_building_commercial", "Commercial"),
	("shape_building_corporate", "Corporate"),
	("shape_shield_plain", "High-Responsibility Operations"),
]


def set_risk_assessment():
	doc = frappe.get_single("PAHEK Risk Assessment Content")

	doc.hero_headline = "Know Exactly Where Your Operation Is Exposed"
	doc.hero_subheading = "PAHEK conducts structured security risk assessments that replace assumption with a clear, evidence-based diagnosis — where your organization is actually exposed, and what matters most to address first."
	doc.hero_cta_primary_label = "Request a Security Risk Assessment"
	doc.hero_cta_secondary_label = "See How the Diagnosis Works"

	doc.stakes_heading_1 = "Visible Activity Can Still Hide Real Exposure"
	doc.stakes_body_1 = "Operational activity, routine reporting, and day-to-day coordination can create a sense of control — while visibility gaps and accountability inconsistencies continue developing underneath it."
	doc.stakes_heading_2 = "Structured Assessment Replaces Assumption With Diagnosis"
	doc.stakes_body_2 = "PAHEK's structured assessments identify hidden vulnerabilities and exposure conditions across the operation — producing a clear, evidence-based diagnosis of what matters most, not just a description of what was observed."

	doc.diagnosis_heading = "Where the Diagnosis Begins"
	doc.diagnosis_intro = "Operational exposure rarely comes from a single weakness. PAHEK evaluates how physical, supervisory, environmental, and human conditions interact — before converging into one clear diagnosis."
	doc.diagnosis_input_tags_csv = (
		"Physical Security Conditions, Supervision Quality, Personnel Oversight, Access Control, "
		"Operational Movement, Reporting Structures, Escalation Readiness, Operational Zoning, System Integration"
	)
	doc.diagnosis_hub_label = "The Operational Diagnosis"
	doc.diagnosis_hub_sublabel = "One Clear, Evidence-Based Picture"
	doc.set("diagnosis_output_cards", [])
	for icon_key, heading, body in [
		("shape_bars_vert", "Priorities", "Vulnerabilities ranked by what actually matters — not by what's easiest to observe."),
		("shape_check_circle", "Recommendations", "Specific, implementation-focused guidance aligned to real site conditions."),
		("shape_three_lines", "Roadmap", "A clear sequence for what should be addressed first, and what can follow."),
	]:
		doc.append("diagnosis_output_cards", {"icon_key": icon_key, "heading": heading, "body": body})

	doc.documented_heading = "The Diagnosis, Documented"
	doc.documented_body = "The report exists to prove the diagnosis — it is evidence, not the product itself. Findings are structured, prioritized, and written for executive interpretation, not technical complexity."
	doc.proof_caption = "Field findings, reviewed against site reference imagery."

	doc.plan_heading = "A Clear Process for Operational Assessment and Exposure Evaluation"
	doc.set("plan_steps", [])
	for number, heading, body in [
		("01", "Operational Site Review & Exposure Evaluation", "Reviewing operational conditions, visibility concerns, and existing security structures."),
		("02", "Risk Identification, Visibility Assessment & Systems Analysis", "Evaluating operational systems, exposure conditions, and coordination weaknesses."),
		("03", "Structured Findings, Prioritization & Operational Recommendations", "Delivering structured operational intelligence and implementation-focused recommendations."),
	]:
		doc.append("plan_steps", {"number": number, "heading": heading, "body": body})
	doc.plan_cta_label = "See How Findings Are Delivered"

	doc.sectors_heading = "Structured Assessments Across Complex Operational Environments"
	doc.set("sector_items", [])
	for icon_key, label in SECTOR_ITEMS:
		doc.append("sector_items", {"icon_key": icon_key, "heading": label})

	doc.observations_heading = "What Structured Assessment Actually Reveals"
	doc.set("observations", [])
	for idx, quote in enumerate([
		"The risks a client mentions first are rarely the ones that matter most.",
		"A vulnerability nobody has reported yet is not the same as a vulnerability that doesn't exist.",
		"Two sites can look equally well-run and carry completely different levels of real exposure.",
		"Treating every risk as equally urgent is itself a way of prioritizing badly.",
	], start=1):
		doc.append("observations", {"eyebrow": f"Observation {idx:02d} of 04", "quote_text": quote})

	doc.final_cta_heading = "Request an Operational Security Assessment"
	doc.final_cta_body = "PAHEK conducts structured operational assessments designed to convert assumption into a clear, prioritized diagnosis of what's actually exposing your organization."
	doc.final_cta_secondary_label = "Revisit the Operational Diagnosis"

	doc.meta_title = "Security Risk Assessment — PAHEK Security"
	doc.meta_description = doc.hero_subheading
	doc.published = 1
	doc.save(ignore_permissions=True)


def set_guarding_operations():
	doc = frappe.get_single("PAHEK Guarding Operations Content")

	doc.hero_headline = "Move Beyond Reactive Guarding to Structured Operational Control"
	doc.hero_subheading = "Effective guarding operations depend on more than visible guard presence. PAHEK helps organizations strengthen accountability, supervision, and measurable field control through structured oversight systems."
	doc.hero_cta_primary_label = "Request an Operational Assessment"
	doc.hero_cta_secondary_label = "See How the System Works"

	doc.stakes_heading_1 = "Many Guarding Operations Appear Active While Oversight Weakens Behind the Scenes"
	doc.stakes_body_1 = "Guards are deployed. Patrols are conducted. Reports are filed on schedule — and supervision quality, accountability enforcement, and patrol verification can weaken gradually behind that routine, long before an incident reveals it."
	doc.stakes_heading_2 = "Structured Oversight Turns Presence Into Measurable Control"
	doc.stakes_body_2 = "PAHEK helps organizations strengthen guarding operations through structured oversight systems — improving supervision consistency, patrol verification, accountability enforcement, and measurable field control across complex operational environments."

	doc.comparison_heading = "What You're Actually Buying"
	doc.comparison_intro = "Most guarding contracts and a genuinely structured operation can look identical on paper. The difference shows up in what each one actually delivers."
	doc.comparison_old_head = "What Most Guarding Contracts Deliver"
	doc.comparison_new_head = "What Operational Control Actually Requires"
	doc.set("comparison_rows", [])
	for col_a, col_b in [
		("Guards deployed on schedule", "Supervision verified on schedule — not just guards"),
		("Patrol logs completed", "Patrol activity independently confirmed, not self-reported"),
		("Incidents reported after the fact", "Escalation paths defined before deployment begins"),
		("A periodic site visit or audit", "Continuous oversight in the weeks between visits"),
		("Uniformed personnel on site", "An accountable operational system on site"),
	]:
		doc.append("comparison_rows", {"column_a": col_a, "column_b": col_b})
	doc.comparison_cta_label = "Compare Against Your Current Contract"

	doc.control_heading = "The Architecture of Operational Control"
	doc.control_subheading = "Three outcomes, working together, are what operational control actually consists of."
	doc.control_hub_label = "Operational Control"
	doc.set("control_clusters", [])
	for icon_key, heading, body, tag_1, tag_2 in [
		("shape_check_circle", "Accountability", "Clear ownership of standards, with enforcement that doesn't depend on who happens to be watching.", "Layered Oversight", "Accountability Enforcement"),
		("shape_eye_alt", "Visibility", "Activity that's confirmed, not assumed — verified rather than simply logged.", "Patrol Monitoring", "Reporting Integrity"),
		("shape_bolt", "Responsiveness", "Confidence that issues are identified, escalated, and resolved before they become larger problems.", "Escalation Coordination", "Field Oversight"),
	]:
		doc.append("control_clusters", {"icon_key": icon_key, "heading": heading, "body": body, "tag_1": tag_1, "tag_2": tag_2})

	doc.proof_caption = "Operational control, in practice — not asserted, corrected."

	doc.plan_heading = "A Structured Approach to Operational Assessment and Oversight"
	doc.plan_subheading = "PAHEK helps organizations strengthen guarding operations through a simple, structured process."
	doc.set("plan_steps", [])
	for number, heading, body in [
		("01", "Operational Assessment", "PAHEK reviews existing guarding operations, supervision structures, and accountability systems to identify operational gaps, oversight weaknesses, and field visibility concerns."),
		("02", "Operational Planning & Alignment", "Operational findings, supervision requirements, and oversight priorities are reviewed to support deployment planning and structured field coordination."),
		("03", "Deployment & Oversight Coordination", "Guarding operations are coordinated through structured supervision systems, reporting procedures, accountability enforcement, and operational oversight processes designed to support measurable field execution."),
	]:
		doc.append("plan_steps", {"number": number, "heading": heading, "body": body})
	doc.plan_cta_label = "See How Deployment Works"

	doc.sectors_heading = "Operational Experience Across Complex Field Environments"
	doc.set("sector_items", [])
	for icon_key, label in SECTOR_ITEMS:
		doc.append("sector_items", {"icon_key": icon_key, "heading": label})

	doc.observations_heading = "What Running Guarding Operations at Scale Actually Teaches You"
	doc.set("observations", [])
	for idx, quote in enumerate([
		"Policy sets the standard. Supervision decides whether it holds.",
		"Audits capture moments. Supervision reveals patterns.",
		"What a client notices on a site visit and what actually keeps a site secure are rarely the same thing.",
		"Most long-term guarding failures don't begin in year two of a contract. They begin quietly in the first ninety days.",
	], start=1):
		doc.append("observations", {"eyebrow": f"Observation {idx:02d} of 04", "quote_text": quote})

	doc.final_cta_heading = "Find Out What Your Current Guarding Operation Is Actually Delivering"
	doc.final_cta_body = "PAHEK helps organizations move from guard presence to a supervised, accountable operating system — assessed, structured, and built to hold up under real conditions."
	doc.final_cta_secondary_label = "Revisit the Operational Architecture"

	doc.meta_title = "Guarding Operations — PAHEK Security"
	doc.meta_description = doc.hero_subheading
	doc.published = 1
	doc.save(ignore_permissions=True)
