{
    'name': 'Sale Partner Contractors',
    'version': '16.0.1.0.0',
    'summary': 'Manage contractors & sites under Contacts and add contractor/site to Sale Orders',
    'description': 'Contractors are child contacts flagged as contractors; sites are child contacts of contractors. Adds contractor/site on sale.order with domain filtering.',
    'author': 'Aspire Analytica',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/contractor_views.xml',
        'views/site_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
}