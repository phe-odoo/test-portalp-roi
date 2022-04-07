# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleSubscription(models.Model):
    _name = "sale.subscription"
    _inherit = ["sale.subscription", "uuid.mixin"]

    sell_date = fields.Date()
    guarantee_start_date = fields.Date()
    guarantee_end_date = fields.Date()
