from datetime import date, datetime
from odoo import models, fields

class ResUsersMonthlyRecords(models.Model):
    _name = 'res.users.monthly.records'
    _description = 'Monthly users record to goal invoicing'

    res_user_id = fields.Many2one(string='User record')
    
    registered_month = fields.Char(
        string='Month'
    )
    
    planned_liters = fields.Float("Planned Liters")
    current_liters = fields.Float("Current liters")