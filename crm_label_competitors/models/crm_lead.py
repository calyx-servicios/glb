from odoo import api, fields, models, _

class Lead(models.Model):
    _inherit = "crm.lead"
    
    competitors_tags = fields.Many2one('crm.label.competitors.registry', string='Competitors')
