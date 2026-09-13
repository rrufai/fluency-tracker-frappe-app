import frappe


def after_install():
	create_can_do_statement_doctype()
	create_oral_rubric_score_doctype()
	create_can_do_check_doctype()
	add_certificate_evaluation_custom_fields()


def create_can_do_statement_doctype():
	if frappe.db.exists("DocType", "Can Do Statement"):
		return

	frappe.get_doc(
		{
			"doctype": "DocType",
			"name": "Can Do Statement",
			"module": "Fluency Tracker",
			"custom": 0,
			"autoname": "hash",
			"fields": [
				{
					"fieldname": "course",
					"fieldtype": "Link",
					"options": "LMS Course",
					"label": "Course",
					"reqd": 1,
				},
				{
					"fieldname": "block",
					"fieldtype": "Data",
					"label": "Block",
					"reqd": 1,
				},
				{
					"fieldname": "phase",
					"fieldtype": "Data",
					"label": "Phase",
					"reqd": 1,
				},
				{
					"fieldname": "level",
					"fieldtype": "Select",
					"options": "A1\nA2\nB1\nB2",
					"label": "Level",
					"reqd": 1,
				},
				{
					"fieldname": "order_index",
					"fieldtype": "Int",
					"label": "Order Index",
					"reqd": 1,
				},
				{
					"fieldname": "statement_text",
					"fieldtype": "Small Text",
					"label": "Statement Text",
					"reqd": 1,
				},
			],
			"permissions": [
				{"role": "Instructor", "read": 1, "write": 1, "create": 1},
				{"role": "Moderator", "read": 1, "write": 1, "create": 1},
				{"role": "Batch Evaluator", "read": 1},
				{
					"role": "System Manager",
					"read": 1,
					"write": 1,
					"create": 1,
					"delete": 1,
				},
			],
		}
	).insert(ignore_permissions=True)


def create_oral_rubric_score_doctype():
	if frappe.db.exists("DocType", "Oral Rubric Score"):
		return

	frappe.get_doc(
		{
			"doctype": "DocType",
			"name": "Oral Rubric Score",
			"module": "Fluency Tracker",
			"custom": 0,
			"istable": 1,
			"fields": [
				{
					"fieldname": "criterion",
					"fieldtype": "Data",
					"label": "Criterion",
					"reqd": 1,
				},
				{
					"fieldname": "score",
					"fieldtype": "Int",
					"label": "Score",
					"reqd": 1,
				},
				{
					"fieldname": "notes",
					"fieldtype": "Small Text",
					"label": "Notes",
				},
			],
			"permissions": [
				{
					"role": "System Manager",
					"read": 1,
					"write": 1,
					"create": 1,
					"delete": 1,
				},
			],
		}
	).insert(ignore_permissions=True)


def create_can_do_check_doctype():
	if frappe.db.exists("DocType", "Can Do Check"):
		return

	frappe.get_doc(
		{
			"doctype": "DocType",
			"name": "Can Do Check",
			"module": "Fluency Tracker",
			"custom": 0,
			"autoname": "hash",
			"fields": [
				{
					"fieldname": "student",
					"fieldtype": "Link",
					"options": "User",
					"label": "Student",
					"reqd": 1,
				},
				{
					"fieldname": "can_do_statement",
					"fieldtype": "Link",
					"options": "Can Do Statement",
					"label": "Can Do Statement",
					"reqd": 1,
				},
				{
					"fieldname": "status",
					"fieldtype": "Select",
					"options": "Not Checked\nChecked",
					"label": "Status",
					"reqd": 1,
					"default": "Not Checked",
				},
				{
					"fieldname": "checked_by",
					"fieldtype": "Link",
					"options": "User",
					"label": "Checked By",
				},
				{
					"fieldname": "checked_at",
					"fieldtype": "Datetime",
					"label": "Checked At",
				},
			],
			"permissions": [
				{"role": "Instructor", "read": 1, "write": 1, "create": 1},
				{"role": "Batch Evaluator", "read": 1, "write": 1, "create": 1},
				{"role": "Moderator", "read": 1, "write": 1, "create": 1},
				{
					"role": "System Manager",
					"read": 1,
					"write": 1,
					"create": 1,
					"delete": 1,
				},
				{"role": "All", "read": 1},
			],
		}
	).insert(ignore_permissions=True)


def add_certificate_evaluation_custom_fields():
	from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

	create_custom_fields(
		{
			"LMS Certificate Evaluation": [
				{
					"fieldname": "assessment_type",
					"fieldtype": "Select",
					"options": "Entry\nMonthly\nPhase Checkpoint\nBlock Gate",
					"label": "Assessment Type",
					"reqd": 1,
					"insert_after": "status",
				},
				{
					"fieldname": "audio_recording",
					"fieldtype": "Attach",
					"label": "Audio Recording",
					"insert_after": "summary",
				},
				{
					"fieldname": "rubric_scores",
					"fieldtype": "Table",
					"options": "Oral Rubric Score",
					"label": "Rubric Scores",
					"insert_after": "audio_recording",
				},
			]
		}
	)
