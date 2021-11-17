# -*- coding: utf-8 -*-
{
    'name': "HN AKOS - CAPA PAIS(SAR)",
    'version': '15.0.1.0.1',
    'category': 'Accounting',
    'summary': 'Modulo de capa pais AKOS Honduras, con referencia al servicio de administracion de rentas.',
    'description': 'SAR.',
    'sequence': '1',
    'author': "Marlon J. Zelaya",
    'support': 'marlon.zelaya@consisa.com',
    'website': "www.consisa.com",
    'depends': ['account'],
    'demo': [],
    'data': [
        #'security/groups.xml',
        #'security/ir.model.access.csv',
        'views/hn_account_journal_inherit.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}