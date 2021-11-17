# -*- coding: utf-8 -*-
# from odoo import http


# class HnAkosCpInvoice(http.Controller):
#     @http.route('/hn_akos_cp_sar/hn_akos_cp_sar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hn_akos_cp_sar/hn_akos_cp_sar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hn_akos_cp_sar.listing', {
#             'root': '/hn_akos_cp_sar/hn_akos_cp_sar',
#             'objects': http.request.env['hn_akos_cp_sar.hn_akos_cp_sar'].search([]),
#         })

#     @http.route('/hn_akos_cp_sar/hn_akos_cp_sar/objects/<model("hn_akos_cp_sar.hn_akos_cp_sar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hn_akos_cp_sar.object', {
#             'object': obj
#         })
