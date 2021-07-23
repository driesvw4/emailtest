# -*- coding: utf-8 -*-
# from odoo import http


# class Emails(http.Controller):
#     @http.route('/emails/emails/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/emails/emails/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('emails.listing', {
#             'root': '/emails/emails',
#             'objects': http.request.env['emails.emails'].search([]),
#         })

#     @http.route('/emails/emails/objects/<model("emails.emails"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('emails.object', {
#             'object': obj
#         })
