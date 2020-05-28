# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return [
        {
            "module_name": "consms",
            "category": "Modules",
            "label": _("Construction"),
            "color": "#1abc9c",
            # "icon": "fas fa-hard-hat",
            "icon": "octicon octicon-home",
            "type": "module"
        }
    ]
