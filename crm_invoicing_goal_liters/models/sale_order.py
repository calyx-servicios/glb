
from odoo import models, fields, _
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    authorized_date = fields.Date('Authorized date')