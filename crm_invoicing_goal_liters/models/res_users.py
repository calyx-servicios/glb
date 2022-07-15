import datetime
import dateutil.relativedelta
from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    """ Bring liters of sales orders that are of the "Fuel" category and belong to the team member. """
    def _compute_current_liters(self):
        values = []
        sale_orders = self.env['sale.order'].search([('user_id','=', self.id), ('order_line.product_id.categ_id.name', '=', 'Combustibles')])
        
        for so in sale_orders:
            for line in so.order_line:
                values.append(line.product_uom_qty)

        self.current_liters = sum(values)
    
    current_liters = fields.Float("Current Liters",compute=_compute_current_liters)
    planned_liters = fields.Float("Planned Liters")

    monthly_records_ids = fields.One2many('crm.team.monthtl.records', 'res_user_id', string='Monthly records')
    
    def cron_monthly_calculation_ig(self):
        records = self.env['res.users'].search([])
        monthly_records_model = self.env['crm.team.monthtl.records']
        values_so = []
        date = datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
        for user in records:
            for so in user.sale_order_ids.search([('user_id', '=', user.id)]):
                for line in so.order_line:
                    values_so.append(line.product_uom_qty)

            monthly_records_model.create({
                'registered_month': date ,
                'res_user_id': user.id,
                'planned_liters' : user.planned_liters,
                'current_liters' : sum(values_so)
            })
