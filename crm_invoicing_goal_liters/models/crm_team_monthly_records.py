from odoo import models, fields

class CrmTeamMonthlyRecords(models.Model):
    _name = 'crm.team.monthly.records'
    _description = 'Monthly team record to goal invoicing for GLB'

    team_id = fields.Many2one("crm.team","Team")
    registered_month = fields.Char("Month")
    planned_liters = fields.Float("Planned Liters")
    current_liters = fields.Float("Current liters")

