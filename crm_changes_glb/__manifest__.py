# -*- coding: utf-8 -*-
{

    'name': "CRM Changes GLB",

    'summary': """
        CRM - Changes to GLB project 
    """,

    'description': """
        Module to add and customize general GLB changes.
    """,

    "author": "Calyx Servicios S.A.",

    "maintainers": ["DeykerGil"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'sale'],

    # always loaded
    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
    ]

}