from odoo import models, fields

class CrmLead(models.Model):
    _inherit = "res.partner"

    oilnet_id = fields.Integer()