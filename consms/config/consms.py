from __future__ import unicode_literals
import frappe
from frappe import _


def get_data():
    return [
        {
            "label": _("Transaction"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Project",
                    "description": _("Project."),
                },
                {
                    "type": "doctype",
                    "name": "Task",
                    "description": _("Task."),
                },
                {
                    "type": "doctype",
                    "name": "Daily Work Progress",
                    "description": _("Daily Work Progress."),
                },
                {
                    "type": "doctype",
                    "name": "Equipment Repair",
                    "description": _("Equipment Maintenance Requisition."),
                },
                {
                    "type": "doctype",
                    "name": "Handing Over",
                    "description": _("Handing Over."),
                },
                {
                    "type": "doctype",
                    "name": "Plant and Equipment Operation Log Sheet",
                    "description": _("Plant and Equipment Operation Log Sheet."),
                },
            ]
        }
    ]
