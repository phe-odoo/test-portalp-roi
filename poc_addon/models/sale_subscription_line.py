# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleSubscriptionLine(models.Model):
    _inherit = "sale.subscription.line"

    date_start = fields.Date()
    date_end = fields.Date()
