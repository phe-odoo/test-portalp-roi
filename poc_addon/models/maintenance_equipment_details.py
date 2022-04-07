# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MaintenanceEquipmentDetails(models.Model):
    _name = "maintenance.equipment.details"
    _description = "A component details for an equipment"

    equipment_id = fields.Many2one(comodel_name="maintenance.equipment")
    serial_number = fields.Char()
    product_id = fields.Many2one(comodel_name="product.product")
    description = fields.Text()
