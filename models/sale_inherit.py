from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError


class SaleOrderModel(models.Model):
    _inherit = "sale.order"

    @api.constrains('partner_id')
    def onchange_partner_id(self):
        total_discount = 0
        disc_limit = float(self.env['ir.config_parameter'].sudo().get_param('discount_limit.disc_limit'))
        date = fields.Datetime.today() - relativedelta(months=1)
        obj = self.search([('create_date', '>=', date)])
        for i in obj:
            total_discount += i.amount_undiscounted - i.amount_untaxed
        if total_discount >= disc_limit and self.order_line.discount != 0:
            raise UserError(' Total Discount Exceeded')
