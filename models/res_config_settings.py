from odoo import models, fields


class ResConfigSettingsModel(models.TransientModel):
    _inherit = "res.config.settings"

    disc_limit = fields.Float(string="Maximum Discount Limit For a Month", config_parameter='discount_limit.disc_limit')
