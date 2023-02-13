from __future__ import unicode_literals
import frappe
from frappe import _



def execute(filters=None):
    columns, data = [], []

    woo_so_sql = """ SELECT `tabSales Order`.customer,`tabAddress`.country from `tabSales Order` RIGHT  JOIN `tabAddress` ON `tabSales Order`.customer_address = `tabAddress`.name"""
    data = frappe.db.sql(woo_so_sql, as_dict=1)
    if len(data) == 0:
        frappe.msgprint('No data!!!')
        return [], []


    columns = [ 
		{ "fieldname": "customer", "label": _("Customer"), "fieldtype": "Data", "width": 200},
	{ "fieldname": "country", "label": _("Total"), "fieldtype": "Currency", "width": 200},

	]


    return columns, data