# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductPicture(models.Model):
    _name = "product.picture"
    _description = "A picture for a product"

    product_id = fields.Many2one(comodel_name="product.template")
    picture = fields.Binary(required=True)
