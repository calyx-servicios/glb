# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CrmLabelCompetitors(models.Model):
    _name = 'crm.label.competitors.registry'
    _description = 'Model registry of competitors'

    name_competitor = fields.Char('Nombre de competidor')