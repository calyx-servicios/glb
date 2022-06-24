from odoo import models, fields, _
from requests.models import Response
import requests
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = "sale.order"

    oilnet_id = fields.Integer()
        
    def action_quotation_send(self):
        if not self.partner_id.oilnet_id:
            self.check_partner_sinc()
        return super().action_quotation_send()
    
    def check_partner_sinc(self):
        auth = self.env.company.oilnet_login()
        url = self.env.company.oilnet_url
        url = url + "/Api/Cuenta/?cuit=" + str(self.partner_id.vat)
        r = requests.get(
            url,
            headers={"Authorization":auth ,"Content-Type": "application/json"},
            verify=False,
        )
        if r.status_code == 200:
            partner_dict = eval(r.text.replace("null","False").replace("false","False"))
            if partner_dict.get("resultado","") == "":
                self.partner_id.oilnet_id = int(partner_dict.get("cuenta",False).get("id",False))
            else:
                raise Warning(partner_dict.get("resultado",False))
        else:
            raise Warning(_('Something went wrong this is what we got, status code: ') + str(r.status_code))

    def prepare_note(self):
        note = {}
        note['id'] = 0
        note['cliente_id'] = int(self.partner_id.oilnet_id)
        if self.date_order:
            note['fecha'] = self.date_order.strftime("%Y-%m-%dT%H:%M:%S")
        if self.commitment_date:
            note['fechaEntrega'] = self.commitment_date.strftime("%Y-%m-%dT%H:%M:%S")
        note['domicilioEntrega'] = self.partner_id.street
        if self.payment_term_id:
            note['formaPago'] = self.payment_term_id.name
        note['items'] = self.prepare_note_line()
        return note
    
    def prepare_note_line(self):
        note_lines = []
        for line in self.order_line:
            note_lines.append({
                "articulo_id": int(line.product_template_id.oilnet_id),
                "cantidad": line.product_uom_qty,
                "precio": line.price_subtotal})
        return note_lines

    def send_note(self):
        data = self.prepare_note()
        auth = self.env.company.oilnet_login()
        url = self.env.company.oilnet_url
        url = url + "/Api/NotaPedido"
        r = requests.post(
            url,
            headers={"Authorization":auth ,"Content-Type": "application/json"},
            data=str(data),
            verify=False,
        )
        if r.status_code == 200:
            self.oilnet_id = r.text
        else:
            raise Warning(r.text +_(" with status code ")+ str(r.status_code))
