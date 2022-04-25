from odoo import models, fields, api, _

import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    # _____________SALES TAB_______________
    zone = fields.Selection(
        [("A", "A"), ("B", "B"), ("C", "C"), ("SL1", "SL1"), ("SL2", "SL2")],
        string="Zone",
    )
    main_activity = fields.Selection(
        [
            ("agro_producer", "Agricultural Producer"),
            ("transport", "Transporter"),
            ("industry", "Industry"),
            ("agro_contractor", "Agricultural Contractor"),
            ("producer_contractor", "Producer/Contractor"),
        ],
        string="Main Activity",
    )
    decision_maker = fields.Selection(
        [
            ("manager", "Manager"),
            ("owner", "Owner"),
            ("user", "User"),
            ("other", "Other"),
        ],
        string="Decision Maker",
    )
    # ____________PROFILE TAB______________
    #   ___GENERAL___
    inhouse_storage = fields.Boolean(string="Inhouse Storage")
    cubic_capacity = fields.Float(string="Cubic Capacity")
    vehicle_qty = fields.Integer(string="Vehicle Qty")
    average_mileage = fields.Float(string="Average Mileage")
    #   ___AGRO___
    #       ___CROPS___
    operates_grain_exchange = fields.Boolean(string="Operates Grain Exchange")
    plantable_area = fields.Float(string="Plantable Area")
    # crop_ids = fields.Many2many(comodel_name='partner.crop', string="Example Plants")
    soy = fields.Boolean(string="Soy")
    corn = fields.Boolean(string="Corn")
    peanuts = fields.Boolean(string="Peanuts")
    other_crop = fields.Text(string="Other Crop")
    #       ___MACHINERY___
    tractor = fields.Boolean(string="Tractor")
    harvester = fields.Boolean(string="Harvester")
    seeder = fields.Boolean(string="Seeder")
    fumigator = fields.Boolean(string="Fumigator")
    shreder = fields.Boolean(string="Shreder")
    ripper = fields.Boolean(string="Ripper")
    brands_and_models = fields.Text(string="Brands and Models")
    # ___________CONSUMPTION TAB___________
    #   ___LUBRICANT___
    #       ___BRANDS___
    shell_oil = fields.Boolean(string="Shell Oil")
    ypf_oil = fields.Boolean(string="YPF Oil")
    castrol_oil = fields.Boolean(string="Castrol Oil")
    john_deere_oil = fields.Boolean(string="John Deere Oil")
    other_lubricant_brand = fields.Text(string="Other Lubricant Brand")
    #       ___TYPES___
    urea = fields.Boolean(string="Urea")
    transmission_oil = fields.Boolean(string="Transmission Oil")
    motor_oil = fields.Boolean(string="Motor Oil")
    hidraulic_oil = fields.Boolean(string="Hidraulic Oil")
    grease = fields.Boolean(string="Grease")
    other_lubricant_type = fields.Text(string="Other Lubricant Type")
    #   ___ANNUAL CONSUMPTION___
    #       ___FUEL___
    grade_2_diesel = fields.Selection(
        [
            ("1000-5000", "1000-5000"),
            ("5000-10000", "5000-10000"),
            ("10000-15000", "10000-15000"),
            (">15000", "More than 15000"),
        ],
        string="Grade 2 Diesel",
    )
    grade_3_diesel = fields.Selection(
        [
            ("1000-5000", "1000-5000"),
            ("5000-10000", "5000-10000"),
            ("10000-15000", "10000-15000"),
            (">15000", "More than 15000"),
        ],
        string="Grade 3 Diesel",
    )
    #       ___LUBRICANT___
    urea_qty = fields.Selection(
        [
            ("0-200", "0-200"),
            ("200-600", "200-600"),
            ("600-1000", "600-1.000"),
            ("1.000-1.500", "1.000-1.500"),
            (">1500", "More than 1.500"),
        ],
        string="Urea Qty",
    )
    transmission_oil_qty = fields.Selection(
        [
            ("0-200", "0-200"),
            ("200-600", "200-600"),
            ("600-1000", "600-1000"),
            ("1000-1500", "1000-1500"),
            (">1500", "More than 1500"),
        ],
        string="Transmission Oil Qty",
    )
    motor_oil_qty = fields.Selection(
        [
            ("0-200", "0-200"),
            ("200-600", "200-600"),
            ("600-1000", "600-1000"),
            ("1000-1500", "1000-1500"),
            (">1500", "More than 1500"),
        ],
        string="Motor Oil Qty",
    )
    hidraulic_oil_qty = fields.Selection(
        [
            ("0-200", "0-200"),
            ("200-600", "200-600"),
            ("600-1000", "600-1000"),
            ("1000-1500", "1000-1500"),
            (">1500", "More than 1500"),
        ],
        string="Hidraulic Oil Qty",
    )
    grease_qty = fields.Selection(
        [
            ("0-200", "0-200"),
            ("200-600", "200-600"),
            ("600-1000", "600-1000"),
            ("1000-1500", "1000-1500"),
            (">1500", "More than 1500"),
        ],
        string="Grease Qty",
    )
    other_lubricant_type_qty = fields.Text(string="Other Lubricant Type Qty")
