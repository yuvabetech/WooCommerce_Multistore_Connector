# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
import requests.exceptions
from frappe.model.document import Document
from woocommerceconnector.woocommerce_requests import get_request
from woocommerceconnector.exceptions import woocommerceSetupError

class WooCommerceConfig(Document):
    def validate(self):
        if self.enable_woocommerce == 1:
            self.validate_access_credentials()
    
    def validate_access_credentials(self):
        if len(self.store_configs) == 0:
            frappe.msgprint(_("Please add at least one store configuration"), raise_exception=woocommerceSetupError)
        else:
            for store in self.store_configs:
                if not store.api_key or not store.api_secret or not store.woocommerce_url:
                    frappe.msgprint(_("Missing value for Consumer Key, Consumer Secret, or woocommerce URL"), raise_exception=woocommerceSetupError)
                else:
                    try:
                        r = get_request('settings', {"api_key": store.api_key,
                            "api_secret": store.get_password(fieldname='api_secret',raise_exception=False), "woocommerce_url": store.woocommerce_url, "verify_ssl": store.verify_ssl})

                    except requests.exceptions.HTTPError:
                        # disable woocommerce!
                        frappe.db.rollback()
                        store.set("enable_woocommerce", 0)
                        frappe.db.commit()

                        frappe.throw(_("""Error Validating API"""), woocommerceSetupError)


@frappe.whitelist()
def get_series():
        return {
            "sales_order_series" : frappe.get_meta("Sales Order").get_options("naming_series") or "SO-woocommerce-",
            "sales_invoice_series" : frappe.get_meta("Sales Invoice").get_options("naming_series")  or "SI-woocommerce-",
            "delivery_note_series" : frappe.get_meta("Delivery Note").get_options("naming_series")  or "DN-woocommerce-",
            "item_code_naming_series" : frappe.get_meta("Item").get_options("naming_series")  or "Item-woocommerce-"
        }
