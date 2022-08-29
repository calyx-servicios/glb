from odoo import models, fields, _
from dateutil.relativedelta import relativedelta
from datetime import datetime


class CrmTeam(models.Model):
    _inherit = 'crm.team'
    
    def _compute_current_liters_for_team(self):
        """ Bring liters from each team member for the total actual liters."""
        values = []
        for rec in self:
            for member in rec.member_ids:
                if member.current_liters:
                    values.append(member.current_liters)
                
        self.current_liters = sum(values)
        
    team_monthly_records_ids = fields.One2many('crm.team.monthly.records', 'team_id', 'Monthly records for sales team')
    current_liters = fields.Integer(_("Current Liters"), compute=_compute_current_liters_for_team)

    def cron_monthly_calculation_ig_team(self):
        date = datetime.now() + relativedelta(months=-1)
        records = self.search([])
        user_monthly_model = self.env['res.users.monthly.records']
        month_date = self.env['res.users'].get_month_to_date(date) + " - " + str(date.year)

        for team in records:
            total_planned_ltr = []
            total_current_ltr = []
            for user in team.member_ids:
                team_current_liters = user_monthly_model.search([('registered_month','=', month_date) ,('res_user_id', '=', user.id)])
                if team_current_liters:
                    planned_liters = team_current_liters.planned_liters
                    current_liters = team_current_liters.current_liters
                else:
                    planned_liters = 0
                    current_liters = 0
                    
                total_planned_ltr.append(planned_liters)
                total_current_ltr.append(current_liters)
            
            team.update({'team_monthly_records_ids': [(0,0, {
                'team_id' : team.id,
                'planned_liters' : sum(total_planned_ltr),
                'current_liters' : sum(total_current_ltr),
                'registered_month' : month_date
            })]})

