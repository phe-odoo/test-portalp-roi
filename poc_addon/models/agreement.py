# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class Agreement(models.Model):
    _name = "agreement"
    _description = "An agreement with multiple contracts"
    _inherit = ["uuid.mixin", 'mail.thread']

    name = fields.Char(required=True)
    partner_id = fields.Many2one(comodel_name="res.partner", required=True, string="Client")
    contract_ids = fields.One2many(comodel_name="sale.subscription", inverse_name="agreement_id")
    contract_qty = fields.Integer(compute="_compute_contract_qty")

    @api.depends('contract_ids')
    def _compute_contract_qty(self):
        for agreement in self:
            agreement.contract_qty = len(agreement.contract_ids)

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        conflict_contracts = self.contract_ids.filtered(lambda c: c.partner_id != self.partner_id)
        if self._origin and conflict_contracts:
            raise UserError(_('You cannot change the client to %s for this agreement, because it has contracts linked to following contacts: %s' % (self.partner_id.display_name, ", ".join(conflict_contracts.partner_id.mapped('display_name')))))

