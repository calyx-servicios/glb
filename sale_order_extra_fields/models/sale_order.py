from odoo import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    condition = fields.Selection([('won', 'Won'), ('in_progress', 'In Progress'), ('lost', 'Lost')],
        string='Condition', readonly=True, store=True, compute='_compute_condition')
    reason = fields.Selection([('price', 'Price'), ('quality', 'Quality'), ('logistics', 'Logistics'), ('deadlines', 'Deadlines'), ('others', 'Others')],
        string='Reason Won or Lost', store=True, compute='_compute_condition')
    competitor = fields.Selection([('ypf', 'YPF'), ('shell', 'SHELL'), ('puma', 'PUMA'), ('other', 'OTHER')],
        string='Competitor', readonly=False, store=True)
    observations = fields.Text(string='Observations')

    @api.depends('state')
    def _compute_condition(self):
        for order in self:
            if order.state in ['sale', 'done', 'logistics_auth', 'financial_auth']:
                order.condition = 'won'
            elif order.state in ['draft', 'sent', 'pending']:
                order.condition = 'in_progress'
            elif order.state == 'cancel':
                order.condition = 'lost'
            if order.condition == 'won' or order.condition == 'lost':
                order.reason = ''
