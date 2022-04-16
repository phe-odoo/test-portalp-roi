# -*- coding: utf-8 -*-
from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _name = "maintenance.equipment"
    _inherit = ["maintenance.equipment", "uuid.mixin"]

    distributor_id = fields.Many2one(comodel_name="res.partner")
    contract_line_id = fields.Many2one(comodel_name="sale.subscription")
    contract_id = fields.Many2one(related="contract_line_id.agreement_id")

    bom_id = fields.Many2one(comodel_name="mrp.bom")
    location_id = fields.Many2one(comodel_name="res.partner", string="Site")
    equipment_detail_ids = fields.One2many(comodel_name="maintenance.equipment.details", inverse_name="equipment_id")

    warranty_start_date = fields.Date()

    # For other dates, we could use standard fields ?
    # effective_date = date de mise en service ?
    # assign_date = installation ?



