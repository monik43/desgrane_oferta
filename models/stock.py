# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def aaaa_check_combo(self):
        for product in self.move_lines:
            if product.product_id.is_combo & product.product_id.name.find("OFERTA") != -1:
                for pro in product.product_id.combo_product_id.product_id:
                    print(pro)
                    print(pro.id)
                    print(pro.name)
