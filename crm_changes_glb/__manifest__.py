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

    'depends': ['base', 'crm', 'sale'],

    'data': [
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
    ]

}