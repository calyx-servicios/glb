from calendar import month
from datetime import date, datetime
from odoo import models, fields, api

class CrmTeamMonthlyRecords(models.Model):
    _name = 'crm.team.monthtl.records'
    _description = 'Monthly users record to goal invoicing'

    res_user_id = fields.Many2one(string='User record')
    
    registered_month = fields.Date(
        string='Month'
    )
    
    planned_liters = fields.Float("Planned Liters")
    current_liters = fields.Float("Current liters")