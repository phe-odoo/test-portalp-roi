# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleSubscriptionLine(models.Model):
    _name = "sale.subscription.line"
    _inherit = ["sale.subscription.line", "uuid.mixin", 'mail.thread']

    date_start = fields.Date()
    date_end = fields.Date()



