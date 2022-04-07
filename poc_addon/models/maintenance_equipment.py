# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class MaintenanceEquipment(models.Model):
    _name = "maintenance.equipment"
    _inherit = ["maintenance.equipment", "uuid.mixin"]

    supplier_id = fields.Many2one(comodel_name="res.partner")
    bom_id = fields.Many2one(comodel_name="mrp.bom")
    equipment_detail_ids = fields.One2many(comodel_name="maintenance.equipment.details", inverse_name="equipment_id")



