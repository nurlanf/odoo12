# -*- coding: utf-8 -*-

# noinspection PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences,PyUnresolvedReferences
from odoo import models, fields, api


# class testmodule(models.Model):
#     _name = 'testmodule.testmodule'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 10

class Grey(models.Model):
    _inherit = 'account.move'

    grey = fields.Boolean(string="Grey", store=True)


#class InvoiceGrey(models.Model):
#    _inherit = 'account.invoice'

#   grey = fields.Boolean(related='move_id.grey', string="Grey", store=True)
