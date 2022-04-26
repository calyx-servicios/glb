# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class crm_label_competitors(models.Model):
#     _name = 'crm_label_competitors.crm_label_competitors'
#     _description = 'crm_label_competitors.crm_label_competitors'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
