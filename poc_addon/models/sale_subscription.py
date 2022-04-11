# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleSubscription(models.Model):
    _name = "sale.subscription"
    _inherit = ["sale.subscription", "uuid.mixin"]

    agreement_id = fields.Many2one(comodel_name="agreement")    # Todo: requis?
    equipment_id = fields.Many2one(comodel_name="maintenance.equipment")
    # location_id
    location_id = fields.Many2one(related="equipment_id.location_id")
    distributor_code = fields.Many2one(related="equipment_id.distributor_id")

    template_id = fields.Many2one(comodel_name="sale.subscription.template", string="Period")

    sell_date = fields.Date()

