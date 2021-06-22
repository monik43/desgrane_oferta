# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def aaaa_check_combo(self):
        for product in self.move_lines:
            print(product)
            print(product.product_id)
            print(product.product_id.id)
            print(product.product_id.name)
            if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                for pro in product.product_id.combo_product_id:
                    print(pro.product_id.id)
                    print(pro.product_id.name)
                    self.move_lines = [(0, 0, {'product_id': pro.product_id.id, 'name': pro.product_id.name, 'product_uom': pro.product_id.uom_id, 'company_id': pro.product_id.company_id, 'date': self.date, 'date_expected': self.scheduled_date, 'location_id': self.location_id, 'location_dest_id': self.location_dest_id})]
                    """self.write({'move_lines': [(1, pro.product_id.id, {'product_uom_qty': pro.product_quantity, 'state':product.state})]})"""
