{

    'name': "CRM invoicing goal liters",

    'summary': """
        CRM - Invoicing goal and liter counter
        
    """,

    'description': """
        Module to add goal for sales equipment invoicing and liter counter per commercial user.
    """,

    "author": "Calyx Servicios S.A.",

    "maintainers": ["DeykerGil"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",

    'depends': ['base', 'crm', 'sale'],
    
    'data': [
        'views/crm_team_views.xml',
        'views/res_users_views.xml'
    ]

}
