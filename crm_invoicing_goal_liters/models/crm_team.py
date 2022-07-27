# -*- coding: utf-8 -*-
from psutil import users
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
        

    team_monthly_records_ids = fields.One2many('crm.team.monthly.records', 'team_id', 'Monthly records for sales team')
    current_liters = fields.Integer(_("Current Liters"), compute=_compute_current_liters_for_team)

    def cron_monthly_calculation_ig_team(self):
        team_ids = []
        users = []

        for team in self.search([]):
            if not team.id in team_ids:
                users.append(self.env['res.users'].search([('id', 'in', team.member_ids.ids)]))
                team.team_monthly_records_ids = [(6,0,{
                    'team_id': team.id,
                    'planned_liters' : sum([user.planned_liters for user in users])
                })]
                team_ids.append(team.id)
        

        
