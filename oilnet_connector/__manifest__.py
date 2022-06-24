{
    'name': "OilNet Connector",
    'summary': """
        Syncs partners products and invoices with Oilnet Platform
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["ParadisoCrisian"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",
    'depends': ['base', 'sale','account'],
    'data': [
        'data/ir_cron.xml',
        'views/account_move_views.xml',
        'views/product_template_views.xml',
        'views/res_company_views.xml',
    ],
}