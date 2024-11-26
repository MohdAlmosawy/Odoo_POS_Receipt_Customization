# -*- coding: utf-8 -*-
{
    'name': "Point of Sale Custom Receipt",
    'summary': "Customize the POS receipt header",
    'description': """Customizes the POS receipt header by adding a thank-you message.""",
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Point of Sale',
    'version': '0.1',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets_prod': [
            'point_of_sale_custom_receipt/static/src/js/receipt_header.js',
            'point_of_sale_custom_receipt/static/src/xml/receipt_header.xml',
        ],
    },
    'installable': True,
    'application': False,
}
