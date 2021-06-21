# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class saleorder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def aaaa_check_combo(self):
        for product in self.order_line:
            print(self.product)
            print(self.product.id)
            print("-------------")
