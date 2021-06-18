# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class productproduct(models.Model):
    _inherit = 'product.template'

    @api.onchange('hs_code')
    def iterate_combo_prod(self):
        for record in self:
            if record.is_combo:
                for product in record.combo_product_id:
                    print(product, "/"*25)
