# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Fields",
    "summary": """
            Add GLB fields to partners
        """,
    "author": "Calyx Servicios S.A.",
    "maintainers": ["marcooegg"],
    "website": "http://odoo.calyx-cloud.com.ar/",
    "license": "AGPL-3",
    "category": "Contacts",
    "version": "13.0.0.0.1",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {"python": [], "bin": []},
    "depends": ['base','contacts','sale', 'account', 'l10n_ar_ux'],
    "data": [
        "views/res_partner_views.xml",
    ],
}
