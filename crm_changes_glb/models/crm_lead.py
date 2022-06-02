from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit = "crm.lead"

    estimated_sale_liters = fields.Integer(_("Estimated sale in liters"))

    @api.constrains('estimated_sale_liters')
    def _check_estimated_sale_liters_field(self):
        if not int(self.estimated_sale_liters):
            raise UserError(_('Field Estimated sale in liters must be an integer.'))    