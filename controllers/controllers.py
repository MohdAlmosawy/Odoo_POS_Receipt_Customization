# -*- coding: utf-8 -*-
# from odoo import http


# class PointOfSaleCustomReceipt(http.Controller):
#     @http.route('/point_of_sale_custom_receipt/point_of_sale_custom_receipt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/point_of_sale_custom_receipt/point_of_sale_custom_receipt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('point_of_sale_custom_receipt.listing', {
#             'root': '/point_of_sale_custom_receipt/point_of_sale_custom_receipt',
#             'objects': http.request.env['point_of_sale_custom_receipt.point_of_sale_custom_receipt'].search([]),
#         })

#     @http.route('/point_of_sale_custom_receipt/point_of_sale_custom_receipt/objects/<model("point_of_sale_custom_receipt.point_of_sale_custom_receipt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('point_of_sale_custom_receipt.object', {
#             'object': obj
#         })

