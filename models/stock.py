# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    there_are_combo_prod = fields.Boolean(compute='_get_combo_prod')

    def _get_combo_prod(self):
        there_are_combo_prod = False

        for product in self.move_lines:
            if product.product_id.is_combo == -1:
                there_are_combo_prod = True

    @api.multi
    def desglo_ofer(self):
        ids_oferta = []
        for product in self.move_lines:
            if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                ids_oferta.append(product.id)
                for pro in product.product_id.combo_product_id:
                    if pro.product_id.type != "service":
                        self.move_lines = [(0, 0, {'product_id': pro.product_id.id, 'name': pro.product_id.name, 'product_uom': pro.product_id.uom_id, 'product_uom_qty': pro.product_quantity * product.product_uom_qty,
                                            'company_id': pro.product_id.company_id, 'date': self.date, 'date_expected': self.scheduled_date, 'location_id': self.location_id, 'location_dest_id': self.location_dest_id})]

        for id in ids_oferta:
            self.move_lines = [(3, id)]
