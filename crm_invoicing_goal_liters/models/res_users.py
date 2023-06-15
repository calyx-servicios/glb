from odoo import models, fields, _
from datetime import datetime, timedelta

import logging
logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _compute_current_liters(self):
        """ Bring liters of sales orders that are of the "Fuel" category and belong to the team member. """
        today = datetime.now()
        first_day_previous_month = datetime(today.year, today.month, 1) - timedelta(days=1)
        first_day_previous_month = datetime(first_day_previous_month.year, first_day_previous_month.month, 1)
        date = first_day_previous_month
        for rec in self:
            rec.current_liters = self.get_sum_values(date, rec)

    current_liters = fields.Float("Current Liters", compute=_compute_current_liters)
    planned_liters = fields.Float("Planned Liters")
    user_monthly_records_ids = fields.One2many('res.users.monthly.records', 'res_user_id', 'Monthly records', readonly=False)

    def last_day_of_month(self, any_day):
        next_month = any_day.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)

    def get_sum_values(self, start_date, rec):
        last_day = self.last_day_of_month(start_date)
        values = []
        domain = [
            ('user_id','=', rec.id),
            ('state', '=', 'logistics_auth'),
            ('authorized_date', '>=', start_date.date()),
            ('authorized_date', '<=', last_day.date())
        ]
        sale_orders = self.env['sale.order'].search(domain)

        for so in sale_orders:
            for line in so.order_line:
                if line.product_id.categ_id.name == 'Combustibles':
                    values.append(line.product_uom_qty)
        return sum(values)

    def cron_monthly_calculation_ig(self):
        today = datetime.now()
        first_day_previous_month = datetime(today.year, today.month, 1) - timedelta(days=1)
        first_day_previous_month = datetime(first_day_previous_month.year, first_day_previous_month.month, 1)
        date = first_day_previous_month

        user_monthly_model = self.env['res.users.monthly.records']
        month_date = self.get_month_to_date(date) + " - " + str(date.year)

        for user in self.search([]):
            record = user_monthly_model.search([('res_user_id', '=', user.id), ('registered_month', '=', month_date)])
            if record:
                record.write({
                    'current_liters': self.get_sum_values(date, user),
                })
            else:
                logger.warning(_('No record found for the user: {}').format(user))

    def get_month_to_date(self, date_period):
        dict_month = {
            "1": _("January"), "2": _("February"), "3": _("March"),
            "4": _("April"), "5": _("May"), "6": _("June"),
            "7": _("July"), "8": _("August"), "9": _("September"),
            "10": _("October"), "11": _("November"), "12":  _("December")
        }
        month = dict_month[str(date_period.month)]
        return month

    def generate_records_by_year(self):
        year = datetime.now().year
        existing_records = self.env['res.users.monthly.records'].search([
            ('registered_month', 'like', '%' + str(year) + '%'),
            ('res_user_id', '=', self.id)
        ])

        records_to_create = []
        for month in range(1, 13):
            month_name = self.get_month_to_date(datetime(year, month, 1))
            month_date = month_name + " - " + str(year)

            if month_date not in existing_records.mapped('registered_month'):
                current_liters = self.get_sum_values(datetime(year, month, 1), self)
                records_to_create.append((0, 0, {
                    'registered_month': month_date,
                    'res_user_id': self.id,
                    'planned_liters': self.planned_liters,
                    'current_liters': current_liters,
                }))

        if records_to_create:
            self.write({'user_monthly_records_ids': records_to_create})


