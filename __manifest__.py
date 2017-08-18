# -*- coding: utf-8 -*-
{
    'name': "bedit_ecoles",

    'summary': """
        Modulle permetant la gestion d'écoles""",

    'description': """
        Ce module permet la gestion de diverse écoles.
    """,

    'author': "Geode",
    'website': "http://opengeode.be",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'web_tree_image',
                'base_geoengine'],

    # always loaded
    'data': [
        'security/data.xml',
        'security/ir.model.access.csv',
        'views/geo.xml',#Adding custom geo views
        'views/bedit_ecoles.xml',#Adding custom view/form for bedit_ecoles
        'views/menu_administration.xml',#Adding custom administration menu
        'views/views.xml',
        'views/web.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
