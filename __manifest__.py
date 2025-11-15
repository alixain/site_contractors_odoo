{
    'name': 'Sale Partner Contractors',
    'version': '16.0.1.0.0',
    'summary': 'Manage contractors & sites under Contacts and add contractor/site to Sale Orders',
    'description': 'Contractors are child contacts flagged as contractors; sites are child contacts of contractors. Adds contractor/site on sale.order with domain filtering.',
    'author': 'Aspire Analytica',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': ['base', 'sale'],    
    'data': [
        'views/contractor_site_views.xml',
    ],
    'installable': True,
}