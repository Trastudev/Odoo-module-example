# -*- coding: utf-8 -*-
# from odoo import http


# class Perruqueria(http.Controller):
#     @http.route('/perruqueria/perruqueria', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/perruqueria/perruqueria/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('perruqueria.listing', {
#             'root': '/perruqueria/perruqueria',
#             'objects': http.request.env['perruqueria.perruqueria'].search([]),
#         })

#     @http.route('/perruqueria/perruqueria/objects/<model("perruqueria.perruqueria"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('perruqueria.object', {
#             'object': obj
#         })
