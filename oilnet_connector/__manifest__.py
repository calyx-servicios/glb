{
    'name': "OilNet Connector",
    'summary': """
        Syncs partners products and invoices with Oilnet Platform
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["ParadisoCrisian","PerezGabriela"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.2.1.0",
    'depends': [
        'base',
        'sale',
        'account'
    ],
    'data': [
        'data/ir_cron.xml',
        'views/product_template_views.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
}