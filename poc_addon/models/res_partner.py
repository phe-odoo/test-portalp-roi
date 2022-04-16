# -*- coding: utf-8 -*-
from odoo import models, fields


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = ["res.partner", "uuid.mixin"]

    vendor_state = fields.Selection(
        selection=[
            ('unconfirmed', 'Unconfirmed'),
            ('confirmed', 'Confirmed'),
        ],
        default='unconfirmed',
    )

    management_center_id = fields.Many2one(comodel_name="crm.team")
    is_client = fields.Boolean()
    is_seller = fields.Boolean()
    is_location = fields.Boolean()


    def action_confirm_vendor(self):
        self.vendor_state = 'confirmed'

