from odoo import models, fields

class AccountPaymentTerm(models.Model):
    _inherit = "account.payment.term"

    oilnet_gesal_code = fields.Integer('Oilnet Code Gesal')
    oilnet_barranca_code = fields.Integer('Oilnet Code La Barranca')