from odoo import models

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
        for sale in sale_orders:
            sale.send_note()
        return super().create_invoices()