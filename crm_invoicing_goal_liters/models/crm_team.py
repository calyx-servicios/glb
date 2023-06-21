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
        user_monthly_model = self.env['res.users.monthly.records']
        month_date = self.env['res.users'].get_month_to_date(date) + " - " + str(date.year)

        teams = self.search([])
        for team in teams:
            team_monthly_record = team.team_monthly_records_ids.filtered(lambda r: r.registered_month == month_date)

            planned_liters = []
            current_liters = []

            for user in team.member_ids:
                user_monthly_record = user_monthly_model.search([('registered_month', '=', month_date), ('res_user_id', '=', user.id)])
                planned_liters.append(user_monthly_record.planned_liters if user_monthly_record else 0)
                current_liters.append(user_monthly_record.current_liters if user_monthly_record else 0)

            values = {
                'team_id': team.id,
                'planned_liters': sum(planned_liters),
                'current_liters': sum(current_liters),
                'registered_month': month_date
            }

            if team_monthly_record:
                team_monthly_record.write(values)
            else:
                team.team_monthly_records_ids.create(values)




