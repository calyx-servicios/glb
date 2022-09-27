from odoo import models, fields, _
from odoo.exceptions import Warning
import requests

class SaleOrder(models.Model):
    _inherit = "sale.order"
 
    oilnet_id = fields.Char('Oilnet Id')
    state = fields.Selection(selection_add=[
        ('pending','Pending'),
        ('financial_auth','Financial Authorization'),
        ('logistics_auth','Logistics Authorization'),
        ('done',)
    ])

    def oilnet_company(self):
        company_name = self.company_id.name.upper() 
        if 'GESAL' in company_name and self.partner_id.oilnet_gesal_code != 0:
            return 'GESAL'
        elif 'BARRANCA' in company_name and self.partner_id.oilnet_barranca_code != 0:
            return 'BARRANCA'
        else:
            return True

    def check_partner_sinc(self, field_company):
        auth = self.company_id.oilnet_login()
        url = self.company_id.oilnet_url
        url = url + "/Api/Cuenta/?cuit=" + str(self.partner_id.vat)
        r = requests.get(
            url,
            headers={"Authorization":auth ,"Content-Type": "application/json"},
            verify=False,
        )
        if r.status_code == 200:
            partner_dict = eval(r.text.replace("null","False").replace("false","False"))
            if partner_dict.get("resultado","") == "":
                if field_company == 'GESAL':
                    self.partner_id.oilnet_gesal_code = int(partner_dict.get("cuenta",False).get("id",False))
                elif field_company == 'BARRANCA':
                    self.partner_id.oilnet_barranca_code = int(partner_dict.get("cuenta",False).get("id",False))
            else:
                raise Warning(partner_dict.get("resultado",False))
        else:
            raise Warning(_('Something went wrong this is what we got, status code: ') + str(r.status_code))
    
    def action_pending(self):
        if self.state not in ['pending']:
            self.write({
                'state': 'pending'
            })
            
    def action_logistics_auth(self):
        self.write({
            'state': 'logistics_auth'
        })
    
    def action_financial_auth(self):
        self.write({
            'state': 'financial_auth'
        })
    
    def action_quotation_send(self):
        result = self.oilnet_company()
        if result != True:
            self.check_partner_sinc(result)
        return super().action_quotation_send()

    def action_send_whatsapp(self):
        result = self.oilnet_company()
        if result != True:
            self.check_partner_sinc(result)
        return super().action_send_whatsapp()

    def prepare_note_line(self):
        note_lines = []
        for line in self.order_line:
            note_lines.append({
                "articulo_id": int(line.product_template_id.oilnet_id),
                "cantidad": line.product_uom_qty,
                "precio": line.price_subtotal})
        return note_lines
    
    def prepare_note(self, oilnet_id):
        note = {}
        note['id'] = 0
        note['cliente_id'] = int(oilnet_id)
        if self.date_order:
            note['fecha'] = self.date_order.strftime("%Y-%m-%dT%H:%M:%S")
        if self.commitment_date:
            note['fechaEntrega'] = self.commitment_date.strftime("%Y-%m-%dT%H:%M:%S")
        if self.partner_id.street:
            note['domicilioEntrega'] = self.partner_id.street
        if self.payment_term_id:
            note['formaPago'] = self.payment_term_id.name
        note['items'] = self.prepare_note_line()
        return note

    def send_note(self):
        oilnet_id = 0
        result = self.oilnet_company()
        if result != True:
            if result == 'GESAL':
                oilnet_id = self.partner_id.oilnet_gesal_code
            else:
                oilnet_id = self.partner_id.oilnet_barranca_code
        data = self.prepare_note(oilnet_id)
        auth = self.company_id.sudo().oilnet_login()
        url = self.company_id.oilnet_url
        url = url + "/Api/NotaPedido"
        r = requests.post(
            url,
            headers={"Authorization":auth ,"Content-Type": "application/json"},
            data=str(data),
            verify=False,
        )
        if r.status_code == 200:
            self.oilnet_id = int(eval(r.text))
        else:
            raise Warning(r.text +_(" with status code ")+ str(r.status_code))

    def action_confirm(self):
        confirm = super().action_confirm()
        self.send_note()
        return confirm 

    def cron_update_notes_status(self):
        sale_orders = self.env['sale.order'].search([('oilnet_id','!=',""),'|','|',('state','=','pending'),('state','=','financial_auth'),('state','=','sale')])
        for order in sale_orders:
            auth = self.company_id.oilnet_login()
            base_url = self.company_id.oilnet_url            
            url = base_url + "/Api/NotaPedido/?numero=" + str(order.oilnet_id)
            r = requests.get(
                url,
                headers={"Authorization":auth ,"Content-Type": "application/json"},
                verify=False,
            )
            if r.status_code == 200:
                status = eval(r.text.replace("true","True").replace("false","False").replace("null","False"))
                if status.get("np_numero",-1) == -1:
                    order.write({"state":"cancel"})
                else:
                    if status.get("auto_financiera",False) and not status.get("auto_logistica",False):
                        order.action_financial_auth()
                    if status.get("auto_logistica",False) and status.get("auto_financiera",False):
                        order.action_logistics_auth()
            else:
                raise Warning(_('Something went wrong this is what we got, status code: ') + str(r.status_code))

