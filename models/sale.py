# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class saleorder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def check_combo(self):

        for record in self:
            product = record.env['product.product'].search([('id', '=', record.order_line.id)])
            if product.is_combo:
                for combo_prod in product.combo_product_id:
                    print("product: ", combo_prod )
                    print(combo_prod.id)
                    print("//"*50)
                    
