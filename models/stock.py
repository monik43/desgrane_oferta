# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    there_are_combo_prod = fields.Boolean(compute='_get_combo_prod')

    @api.multi
    def print_move_line_test(self):
        print(self.sale_id.name)
        print(self.sale_id.warehouse_id)
        print(self.state)

    def _get_combo_prod(self):
        for record in self:
            record.there_are_combo_prod = False
            for product in record.move_lines:
                if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                    record.there_are_combo_prod = True

    @api.multi
    def desglo_ofer(self):
        for record in self:
            sale = record.sale_id
            ids_oferta = []
            for product in record.move_lines:
                if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                    ids_oferta.append(product.id)
                    for pro in product.product_id.combo_product_id:
                        if pro.product_id.type != "service":
                            record.write(
                                {'move_lines': [(0, 0, {'product_id': pro.product_id.id, 'name': pro.product_id.name, 'product_uom': pro.product_id.uom_id.id, 'location_id': product.location_id.id, 'location_dest_id': product.location_dest_id.id, 'product_uom_qty': pro.product_quantity * product.product_uom_qty})]})

        self.state = "confirmed"
        print(self.state)
        self.group_id = self.env['procurement.group'].search(
            [('name', '=', self.sale_id.name)])
        for id in ids_oferta:
            self.move_lines = [(3, id)]

        self.sale_id = sale

        if self.sale_id.warehouse_id != 1:
            self.sale_id.warehouse_id == 1
