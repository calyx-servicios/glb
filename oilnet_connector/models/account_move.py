from odoo import models, fields, _
from requests.models import Response
import requests

class AccountMove(models.Model):
    _inherit = "account.move"

    oilnet_id = fields.Integer(compute="get_sale_order_oilnet_id")
    commercial = fields.Boolean()
    logistic = fields.Boolean()
    financial = fields.Boolean()

    def get_sale_order_oilnet_id(self):
        for invoice in self:
            sale_order = self.env['sale.order'].search([('name','=',invoice.invoice_origin)])
            if sale_order.oilnet_id:
                invoice.oilnet_id = sale_order.oilnet_id
            else:
                invoice.oilnet_id = False

    def cron_update_notes_status(self):
        invoices = self.env['account.move'].search([('oilnet_id','!=',0),'|','|',('commercial','=',False),('logistic','=',False),('financial','=',False)])
        auth = self.env.company.oilnet_login()
        base_url = self.env.company.oilnet_url
        for invoice in invoices:
            url = base_url + "/Api/Cuenta/?numero=" + str(invoice.oilnet_id)
        r = requests.get(
            url,
            headers={"Authorization":auth ,"Content-Type": "application/json"},
            verify=False,
        )
        if r.status_code == 200:
            status = eval(r.text.replace("true","True").replace("false","False"))
            invoice.commercial = status.get("auto_comercial",False)
            invoice.logistic = status.get("auto_logistica",False)
            invoice.financial = status.get("auto_financiera",False)
        else:
            raise Warning(_('Something went wrong this is what we got, status code: ') + str(r.status_code))
        if invoice.financial and invoice.logistic and invoice.commercial:
            invoice.post()