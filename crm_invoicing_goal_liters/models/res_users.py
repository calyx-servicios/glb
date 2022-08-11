import datetime
import dateutil.relativedelta
from odoo import models, fields, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _compute_current_liters(self):
        """ Bring liters of sales orders that are of the "Fuel" category and belong to the team member. """
        date = datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
        for rec in self:
            rec.current_liters = self.get_sum_values(date, rec)
    
    current_liters = fields.Float("Current Liters",compute=_compute_current_liters)
    planned_liters = fields.Float("Planned Liters")
    user_monthly_records_ids = fields.One2many('res.users.monthly.records', 'res_user_id', 'Monthly records')

    def last_day_of_month(any_day):
        next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
        return next_month - datetime.timedelta(days=next_month.day)  

    def get_sum_values(self,date, rec):
        last_day = self.last_day_of_month(date)
        values = []
        domain = [
            ('user_id','=', rec.id), 
            ('order_line.product_id.categ_id.name', '=', 'Combustibles'), 
            ('state', '=', 'logistics_auth'), 
            ('authorized_date','>=',date), 
            ('authorized_date','<=',last_day)
        ]

        sale_orders = self.env['sale.order'].search(domain)
        for so in sale_orders:
            for line in so.order_line:
                values.append(line.product_uom_qty)

        return sum(values)
    
    def cron_monthly_calculation_ig(self):
        date = datetime.datetime.now() + dateutil.relativedelta.relativedelta(months=-1)
        records = self.env['res.users'].search([])
        user_monthly_model = self.env['res.users.monthly.records']
        month_date = self.env['res.users'].get_month_to_date(date)

        for user in records:
            user_monthly_model.create({
                'registered_month': month_date ,
                'res_user_id': user.id,
                'planned_liters' : user.planned_liters,
                'current_liters' : user.get_sum_values(date, user)
            })
            user.write({
                'planned_liters' : 0,
            })

    def get_month_to_date(self, date_period):
        dict_month = {
            "1": _("January"), "2": _("February"), "3": _("March"), 
            "4": _("April"), "5": _("May"), "6": _("June"),
            "7": _("July"), "8": _("August"), "9": _("September"), 
            "10": _("October"), "11": _("November"), "12":  _("December")
        }
 
        month = dict_month[str(date_period.month)]
        return month