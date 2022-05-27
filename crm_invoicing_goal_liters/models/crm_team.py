# -*- coding: utf-8 -*-
from odoo import models, fields, _


class CrmTeam(models.Model):
    _name = 'crm.team'
    _inherit = ['mail.alias.mixin', 'crm.team']

    current_liters = fields.Integer(_("Current Liters"))

