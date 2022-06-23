from odoo import models, fields, _
from requests.models import Response
import requests
from odoo.exceptions import Warning

class ResCompany(models.Model):
    _inherit = "res.company"

    oilnet_url = fields.Char()
    oilnet_user = fields.Char()
    oilnet_password = fields.Char()
    oilnet_auth = fields.Char()
    oilnet_logged = fields.Boolean()

    def oilnet_login(self):
        url = self.env.company.oilnet_url
        user = self.env.company.oilnet_user
        password = self.env.company.oilnet_password
        data = {"username": user,"password": password}
        url = url + "/Api/Login"
        r = requests.post(
            url,
            headers={ "Content-type": 'application/x-www-form-urlencoded'},
            data=data
        )
        if r.status_code == 200:
            self.oilnet_auth = eval(r.text).get("token",False)
            self.oilnet_login = True
            return self.oilnet_auth
        else:
            raise Warning(_('Wrong Credencials ') + str(r.status_code))