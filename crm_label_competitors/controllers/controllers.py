# -*- coding: utf-8 -*-
# from odoo import http


# class CrmLabelCompetitors(http.Controller):
#     @http.route('/crm_label_competitors/crm_label_competitors/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_label_competitors/crm_label_competitors/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_label_competitors.listing', {
#             'root': '/crm_label_competitors/crm_label_competitors',
#             'objects': http.request.env['crm_label_competitors.crm_label_competitors'].search([]),
#         })

#     @http.route('/crm_label_competitors/crm_label_competitors/objects/<model("crm_label_competitors.crm_label_competitors"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_label_competitors.object', {
#             'object': obj
#         })
