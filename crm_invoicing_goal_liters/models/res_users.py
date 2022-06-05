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
    
    current_liters = fields.Float(_("Current Liters"),compute=_compute_current_liters) #Litros actuales
    planned_liters = fields.Float(_("Planned Liters")) #Litros planificados