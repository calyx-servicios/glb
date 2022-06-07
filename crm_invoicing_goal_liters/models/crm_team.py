# -*- coding: utf-8 -*-
from odoo import models, fields, _


class CrmTeam(models.Model):
    _name = 'crm.team'
    _inherit = ['mail.alias.mixin', 'crm.team']
    
    """ Bring liters from each team member for the total actual liters."""
    def _compute_current_liters_for_team(self):
        values = []
        for member in self.member_ids:
            if member[0].current_liters:
                values.append(member[0].current_liters)
                
        self.current_liters = sum(values)

    current_liters = fields.Integer("Current Liters", compute=_compute_current_liters_for_team)

