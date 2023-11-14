{
    'name': "CRM invoicing goal liters",
    'summary': """
        CRM - Invoicing goal and liter counter
    """,
    'description': """
        Module to add goal for sales equipment invoicing and liter counter per commercial user.
    """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["DeykerGil","PerezGabriela","leandro090685"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.4.3.2",
    'depends': [
        'crm',
        'sale',
        'oilnet_connector'
    ],
    'data': [
        'data/ir_cron.xml',
        'security/monthly_records_views_access_security.xml',
        'security/ir.model.access.csv',
        'security/monthly_records_rule.xml',
        'views/monthly_records_views.xml',
        'views/crm_team_views.xml',
        'views/res_users_views.xml',
        'views/sale_order_view.xml'
    ]
}
