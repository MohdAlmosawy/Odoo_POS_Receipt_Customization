# -*- coding: utf-8 -*-
{
    'name': "Point of Sale Custom Receipt",
    'summary': "Customize POS receipt layout and content",
    'description': """
        This module modifies the Point of Sale receipt by:
        - Removing tax details section
        - Removing 'Powered by Odoo' text
        - Adding complete company address display
        - Enhancing product name display
        - Removing product variant attributes
        
        The module provides a cleaner and more professional receipt layout
        with comprehensive company address information.
    """,
    'author': "Technology Pill Business Solution",
    'website': "https://www.tecpill.com",
    'category': 'Point of Sale',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets_prod': [
            'point_of_sale_custom_receipt/static/src/js/receipt_header.js',
            'point_of_sale_custom_receipt/static/src/xml/receipt_header.xml',
            'point_of_sale_custom_receipt/static/src/js/orderline.js',
            'point_of_sale_custom_receipt/static/src/xml/orderline.xml',
            'point_of_sale_custom_receipt/static/src/js/receipt.js',
            'point_of_sale_custom_receipt/static/src/xml/receipt.xml',
        ],
    },
    'installable': True,
    'application': False,
}
