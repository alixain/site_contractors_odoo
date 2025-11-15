{
    'name': 'Sale Contractor & Site',
    'version': '16.0.1.0',
    'summary': 'Adds Contractor and Site fields to Sale Order',
    'description': 'Adds contractor and site fields linked to res.partner, with site filtered by contractor.',
    'author': 'Aspire Analytica',
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
