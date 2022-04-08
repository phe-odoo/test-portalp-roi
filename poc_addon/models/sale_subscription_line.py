# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleSubscriptionLine(models.Model):
    _name = "sale.subscription.line"
    _inherit = ["sale.subscription.line", "uuid.mixin", 'mail.thread']

    date_start = fields.Date()
    date_end = fields.Date()

    equipment_id = fields.Many2one(comodel_name="maintenance.equipment")
    template_id = fields.Many2one(comodel_name="sale.subscription.template", string="Period")
    supplier_id = fields.Many2one(comodel_name="res.partner")
