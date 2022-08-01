import datetime
import dateutil.relativedelta
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
        total_planned_ltr = []
        total_current_ltr = []

        for team in self.search([]):
            if not team.id in team_ids:
                total_planned_ltr.clear()
                team._compute_current_liters_for_team()
                total_current_ltr.append(team.current_liters)
                
                for user in team.member_ids:
                    total_planned_ltr.append(user.planned_liters)

                team.update({'team_monthly_records_ids': [(0,0, {
                    'team_id' : team.id,
                    'planned_liters' : sum(total_planned_ltr),
                    'current_liters' : sum(total_current_ltr),
                    'registered_month' : datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
                })]})

                team.write({'current_liters': 0})
                team_ids.append(team.id)
