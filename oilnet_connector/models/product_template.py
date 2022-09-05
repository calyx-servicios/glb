from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = "product.template"

    oilnet_id = fields.Integer()