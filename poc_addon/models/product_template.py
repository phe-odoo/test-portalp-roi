# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = "product.template"

    length = fields.Float()
    width = fields.Float()
    height = fields.Float()
    # Todo : check if char?
    activity_domain = fields.Char()

    main_supplier_domain = fields.Many2many(comodel_name="res.partner", compute="_compute_main_supplier_domain")
    main_supplier_id = fields.Many2one(comodel_name="res.partner", domain="[('id', 'in', main_supplier_domain)]")


    @api.depends('seller_ids')
    def _compute_main_supplier_domain(self):
        for product in self:
            product.main_supplier_domain = product.seller_ids.name
