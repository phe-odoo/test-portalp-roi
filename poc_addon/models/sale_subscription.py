# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class SaleSubscription(models.Model):
    _name = "sale.subscription"
    _inherit = ["sale.subscription", "uuid.mixin"]


