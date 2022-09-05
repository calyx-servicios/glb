from odoo import models, fields
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    authorized_date = fields.Date('Authorized date')
    
    def action_logistics_auth(self):
        super(SaleOrder, self).action_logistics_auth()
        self.write({
            'authorized_date': datetime.now()
        })