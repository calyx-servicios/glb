# -*- coding: utf-8 -*-

from odoo import api, fields, models


class CrmLeadLostCustom(models.TransientModel):
    _inherit = 'crm.lead.lost'

    label_competitors_ids = fields.Many2many('crm.label.competitors.registry', 'crm_label_competitors_rel',  string='Competitors')


