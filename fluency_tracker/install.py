import frappe


def after_install():
	add_certificate_evaluation_custom_fields()


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
