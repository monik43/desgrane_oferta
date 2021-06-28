# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    there_are_combo_prod = fields.Boolean(compute='_get_combo_prod')

    @api.multi
    def print_move_line_test(self):
        for record in self:
            print(record.move_lines)
            for movelines in record.move_lines:
                fields_dict = {}
                for key in movelines.fields_get():
                    fields_dict[key] = movelines[key]
            for key in fields_dict:
                print(key, '  ', fields_dict[key])

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

        record.state = "confirmed"
        record.group_id = record.env['procurement.group'].search(
            [('name', '=', record.sale_id.name)])
        for id in ids_oferta:
            self.move_lines = [(3, id)]

        self.sale_id = sale
