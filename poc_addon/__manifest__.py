# -*- coding: utf-8 -*-

{
    'name': "PortalP POC addon",
    'category': "",
    'version': "15.0.1.0.0",
    'installable': True,
    'sequence': 1,
    
    'license': "OEEL-1",
    'author': "Odoo PS",
    'website': "https://www.odoo.com",
    
    'depends': [
        'crm',
        'maintenance',
        'purchase',
        'mrp',
        'sale_subscription',
        'base_geolocalize',
    ],
    "assets": {
        "web.assets_backend": [],
    },
    
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/agreement.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/maintenance_equipment.xml',
        'views/sale_subscription.xml',
        'views/uuid.xml',
        # Menus
        'views/menu_items.xml',
    ],
    
    'qweb': [],
}
