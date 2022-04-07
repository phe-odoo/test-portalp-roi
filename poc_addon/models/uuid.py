# -*- coding: utf-8 -*-
from odoo import fields, models

class Uuid(models.Model):
    _name = "uuid"
    _description = "An uuid related to model/id pair"

    uuid = fields.Char()
    model = fields.Char()
    res_id = fields.Integer()



