# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class stockpicking(models.Model):
    _inherit = 'stock.picking'

    there_are_combo_prod = fields.Boolean(compute='_get_combo_prod')

    def _get_combo_prod(self):
        for record in self:
            record.there_are_combo_prod = False
            for product in record.move_lines:
                if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                    record.there_are_combo_prod = True

    @api.onchange('move_lines')
    def recheck_so(self):
        for record in self:
            if record.sale_id == False:
                print(record.env['sale.order'].search([('name', '=', record.origin)]).id)
                

    @api.multi
    def desglo_ofer(self):
        for record in self:
            ids_oferta = []
            sale = record.sale_id
            if self.sale_id.warehouse_id != 1:
                self.sale_id.warehouse_id == 1
            for product in record.move_lines:
                if product.product_id.is_combo and product.product_id.name.find("OFERTA") != -1:
                    gid = product.group_id.id
                    print(gid, ' ', product.group_id.id)
                    ptid = product.picking_type_id.id
                    ids_oferta.append(product.id)
                    for pro in product.product_id.combo_product_id:
                        if pro.product_id.type != "service":
                            record.write(
                                {'move_lines': [(0, 0, {'product_id': pro.product_id.id, 'name': pro.product_id.name, 'product_uom': pro.product_id.uom_id.id, 'location_id': product.location_id.id,
                                 'location_dest_id': product.location_dest_id.id, 'product_uom_qty': pro.product_quantity * product.product_uom_qty, 'picking_type_id': ptid, 'group_id': gid})]})
        self.group_id = self.env['procurement.group'].search(
            [('name', '=', self.sale_id.name)]).id
        for id in ids_oferta:
            self.move_lines = [(3, id)]
        self.sale_id = sale
        self.state = "confirmed"
