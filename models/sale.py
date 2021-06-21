# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class saleorder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def check_combo(self):
        for product in self.order_line:
            print(self.order_line)
