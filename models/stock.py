# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def aaaa_check_combo(self):
        for product in self.move_lines:
            if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                for pro in product.product_id.combo_product_id:
                    print(pro.product_id)
                    print(pro.product_id.id)
                    print(pro.product_id.name)
                    self.write({'move_lines': [(4, pro.product_id.id)]})
                    self.write({'move_lines': [(1, pro.product_id.id, {'product_uom_qty': pro.product_quantity, 'state':product.state})]})
