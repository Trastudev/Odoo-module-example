# -*- coding: utf-8 -*-
{
    'name': "perruqueria",

    'summary': 'Gestiona esdeveniments organitzats per proveidors',

    'description': """
        Aplicació per a la gestió d'esdeveniments organitzats per proveidors, 
        permet crear esdeveniment i gestionar assistència, persona responsable i poersona formadora
    """,

    'author': "IOC",
    'website': "https://ioc.xtec.cat/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'event'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/res_partner.xml',
        'demo/demo.xml',
        'report/event_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
