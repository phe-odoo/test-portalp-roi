# -*- coding: utf-8 -*-
from odoo import api, fields, models
import uuid


class UuidMixin(models.AbstractModel):
    _name = "uuid.mixin"
    _description = "UUID Mixin"

    uuid = fields.Char(tracking=True, readonly=True)
    uuid_id = fields.Many2one(comodel_name="uuid", string="UUID reference record", readonly=True)


    def generate_uuid(self):
        self.ensure_one()
        self.uuid_id = self.env['uuid'].sudo().create({
            'uuid': self._generate_unique_uuid(),
            'model': self._name,
            'res_id': self.id,
        })
        self.uuid = self.uuid_id.uuid

    def _generate_unique_uuid(self):
        unique_uuid = False
        while not unique_uuid or self.env['uuid'].sudo().search([('uuid', '=', unique_uuid)]):
            unique_uuid = str(uuid.uuid4())
        return unique_uuid


    @api.model
    def create(self, vals):
        res = super(UuidMixin, self).create(vals)
        res.generate_uuid()
        return res

    def unlink(self):
        self.uuid_id.unlink()
        return super(UuidMixin, self).unlink()


