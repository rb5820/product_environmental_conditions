# -*- coding: utf-8 -*-
{
    'name': 'Product Environmental Conditions',
    'version': '18.0.1.0.10',
    'category': 'Inventory/Inventory',
    'summary': 'Add environmental condition specifications to products',
    'author': 'RB5820',
    'website': "https://www.attiesatelier.be",
    'license': 'LGPL-3',
    'depends': [
        'base',
        'product',
        'uom',
        'stock',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/protection_rating_views.xml',
        'data/protection_rating_data.xml',
        #'data/product_7072739000012.xml',
    ],
    'demo': [
        'data/product_environmental_conditions_demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'description': """
Product Environmental Conditions
===============================

This module extends product information with detailed environmental operating conditions:

* Temperature range (minimum and maximum operating temperature)
* Humidity range (minimum and maximum operating humidity)
* Altitude range (minimum and maximum operating altitude)
* IP rating (Ingress Protection) for dust and water resistance
* IK rating for mechanical impact resistance
* Additional environmental specifications:
  * Vibration resistance
  * UV resistance
  * Salt spray resistance
  * Chemical resistance
  * Shock resistance

Key Features:
------------
* Track operating temperature ranges (°C and °F)
* Monitor humidity tolerances (%)
* Specify altitude limitations (meters and feet)
* Define IP (Ingress Protection) ratings for dust and water resistance
* Record IK ratings for impact resistance
* Store environmental testing certifications and test results
* Searchable and filterable based on environmental specifications
"""
}
