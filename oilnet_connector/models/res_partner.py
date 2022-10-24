from odoo import models, fields

class ResPartner(models.Model):
    _inherit = "res.partner"

    oilnet_gesal_code = fields.Integer('Oilnet Code Gesal')
    oilnet_barranca_code = fields.Integer('Oilnet Code La Barranca')

