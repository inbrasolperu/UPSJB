# -*- coding: utf-8 -*-
##-----------------------------------------------------------------------------##
#
#    Copyright (C) 2021-TODAY Inbrasol.
#    Author      :  Inbrasol Web Services
#    WebSite     : https://iws.inbrasol.pe
#
#    This program is copyright property of the author mentioned above.
#    You can"t redistribute it and/or modify it.
#
##-----------------------------------------------------------------------------##
{
    'name': "POS - Search SUNAT",
    "summary": "Get information of client from SUNAT or RENIEC",
    "description": "Obtain customer information from SUNAT with RUC or RENIEC with DNI",
    'author': "POS: Search from SUNAT",
    "website": "http://iws.inbrasol.pe",
    "author": "Inbrasol Perú",
    "maintainer": "Inbrasol Odoo Team",
    'category': 'Customizations',
    'version': '15.0.1.3',
    'license': 'GPL-3',
    'depends': ['point_of_sale', 'l10n_latam_base','contacts'],
    'assets': {
        'point_of_sale.assets': [
            'inb_pe_pos_sunat_search_ruc/static/src/js/models.js',
            'inb_pe_pos_sunat_search_ruc/static/src/js/screens.js',
        ],
        'web.assets_qweb': [
            'inb_pe_pos_sunat_search_ruc/static/src/xml/**/*',
        ],
    }, 
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
}