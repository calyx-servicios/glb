from odoo import models, fields, _
from odoo.exceptions import Warning
import requests

class ResCompany(models.Model):
    _inherit = "res.company"

    oilnet_url = fields.Char('Oilnet Url')
    oilnet_user = fields.Char('Oilnet User')
    oilnet_password = fields.Char('Oilnet Password')

    def oilnet_login(self):
        url = self.oilnet_url
        user = self.oilnet_user
        password = self.oilnet_password
        data = {"username": user,"password": password}
        url = url + "/Api/Login"
        r = requests.post(
            url,
            headers={ "Content-type": 'application/x-www-form-urlencoded'},
            data=data
        )
        if r.status_code == 200:
            return eval(r.text).get("token",False)
        else:
            raise Warning(_('Wrong Credencials ') + str(r.status_code))

