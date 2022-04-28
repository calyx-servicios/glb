# -*- coding: utf-8 -*-
{

    'name': "CRM Labels competitors",

    'summary': """
        Module to add field of competence to CRM losses
    """,

    'description': """
        Add competitors for CRM module
    """,

    "author": "Calyx Servicios S.A.",
    "maintainers": [""],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Custom",
    "version": "13.0.1.0.0",

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/crm_add_menu_competitors.xml',
        'wizards/crm_lead_lost_custom.xml'
    ]

}
