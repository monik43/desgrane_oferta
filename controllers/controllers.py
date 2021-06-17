# -*- coding: utf-8 -*-
from odoo import http

# class DesgraneOferta(http.Controller):
#     @http.route('/desgrane_oferta/desgrane_oferta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/desgrane_oferta/desgrane_oferta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('desgrane_oferta.listing', {
#             'root': '/desgrane_oferta/desgrane_oferta',
#             'objects': http.request.env['desgrane_oferta.desgrane_oferta'].search([]),
#         })

#     @http.route('/desgrane_oferta/desgrane_oferta/objects/<model("desgrane_oferta.desgrane_oferta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('desgrane_oferta.object', {
#             'object': obj
#         })