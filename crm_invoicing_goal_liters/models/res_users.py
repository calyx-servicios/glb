from odoo import models, fields, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    planned_liters = fields.Integer(_("Planned Liters")) #Litros planificados
    current_liters = fields.Integer(_("Current Liters")) #Litros actuales