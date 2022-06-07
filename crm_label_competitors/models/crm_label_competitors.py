from odoo import models, fields, _
class CrmLabelCompetitors(models.Model):
    _name = 'crm.label.competitors.registry'
    _description = _('Model registry of competitors')
    _rec_name = 'name_competitor'

    name_competitor = fields.Char(_('Name competitor'))