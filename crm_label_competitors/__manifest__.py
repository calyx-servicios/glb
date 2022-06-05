{

    'name': "CRM Labels competitors",

    'summary': """
        Module to add field of competence to CRM losses
    """,

    'description': """
        Add competitors for CRM module
    """,

    "author": "Calyx Servicios S.A.",

    "maintainers": ["DeykerGil","PerezGabriela"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",

    'depends': ['base', 'crm'],

    'data': [
        'security/ir.model.access.csv',
        'views/crm_add_menu_competitors.xml',
        'views/crm_lead_views.xml',
        'wizards/crm_lead_lost_custom.xml'
    ]

}
