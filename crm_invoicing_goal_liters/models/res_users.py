from odoo import models, fields, api, _
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import calendar


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _compute_current_liters(self):
        """ Bring liters of sales orders that are of the "Fuel" category and belong to the team member. """
        today = datetime.now()
        first_day_current_month = datetime(today.year, today.month, 1)
        date = first_day_current_month
        for rec in self:
            rec.current_liters = self.get_sum_values(date, rec)

    current_liters = fields.Float("Current Liters", compute=_compute_current_liters)

    planned_liters = fields.Float("Planned Liters")
    user_monthly_records_ids = fields.One2many('res.users.monthly.records', 'res_user_id', 'Monthly records', readonly=False)

    def last_day_of_month(self, any_day):
        _, last_day = calendar.monthrange(any_day.year, any_day.month)
        last_day_date = any_day.replace(day=last_day)
        return last_day_date

    def get_sum_values(self, start_date, end_date, rec):
        values = []
        domain = [
            ('user_id', '=', rec.id),
            ('state', '=', 'sale')
        ]
        sale_orders = self.env['sale.order'].search(domain)

        for so in sale_orders:
            for line in so.order_line:
                if line.product_id.categ_id.name == 'Combustibles' and start_date <= so.date_order <= end_date:
                    values.append(line.product_uom_qty)
        return sum(values)


    def cron_monthly_calculation_ig(self):
        
        today = datetime.now()

        # Calcula el primer día del mes actual
        start_date = today.replace(day=1)

        # Calcula el último día del mes actual
        end_date = start_date + relativedelta(months=1, days=-1)

        user_monthly_model = self.env['res.users.monthly.records']
        month_date = self.get_month_to_date(start_date) + " - " + str(start_date.year)

        for user in self.search([]):
            # Calcula el primer día y el último día del mes actual
            month_start = start_date
            month_end = end_date

            # Verifica si hoy es el primer día de un nuevo mes y actualiza las fechas en consecuencia
            if today.day == 1:
                # Si hoy es el primer día de un nuevo mes, actualiza month_start y month_end
                month_start = today
                month_end = today + relativedelta(day=1, months=1, days=-1)

            # Calcula los litros vendidos entre month_start y month_end
            liters_sold = self.get_sum_values(month_start, month_end, user)

            record = user_monthly_model.search([('res_user_id', '=', user.id), ('registered_month', '=', month_date)])

            if record:
                record.write({
                    'current_liters': liters_sold,
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
