// Copyright (c) 2023, libracore and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Woocommerce Global"] = {
	"filters": [
		{ "fieldname": "company", "label": __("Company"), "fieldtype": "Link", "options": "Company", "default": frappe.defaults.get_user_default("Company"), "reqd": 1 },
		{ "fieldname": "Country", "label": __("Country"), "fieldtype": "Link", "options": "Country", "default": "Deutschland", "reqd": 1 },
		{ "fieldname": "from_date", "label": __("From Date"), "fieldtype": "Date", "default": frappe.datetime.month_start(), "reqd": 1 },
		{ "fieldname": "to_date", "label": __("To Date"), "fieldtype": "Date", "default": frappe.datetime.month_end(), "reqd": 1 },


	]
};
