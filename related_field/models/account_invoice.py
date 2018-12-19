from odoo import models, fields, api


class InvoiceGrey(models.Model):
    _inherit = 'account.invoice'


grey = fields.Boolean(related='move_id.grey', string="Grey", store=True)
