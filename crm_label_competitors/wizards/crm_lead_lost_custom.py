# -*- coding: utf-8 -*-
from odoo import fields, models


class CrmLeadLostCustom(models.TransientModel):
    _inherit = 'crm.lead.lost'

    label_competitors_ids = fields.Many2one('crm.label.competitors.registry', string='Competitors')

    
    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        return leads.action_set_lost(lost_reason=self.lost_reason_id.id, competitors_tags=self.label_competitors_ids.id)

