# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    @api.multi
    def desglose_oferta(self):
        for product in self.move_lines:
            if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                for pro in product.product_id.combo_product_id:
                    self.move_lines = [(0, 0, {'product_id': pro.product_id.id, 'name': pro.product_id.name, 'product_uom': pro.product_id.uom_id, 'product_uom_qty':pro.product_quantity * product.product_uom_qty,'company_id': pro.product_id.company_id, 'date': self.date, 'date_expected': self.scheduled_date, 'location_id': self.location_id, 'location_dest_id': self.location_dest_id})]
        print(product)
        print(product.id)
        self.move_lines = [(3,product.id)]

