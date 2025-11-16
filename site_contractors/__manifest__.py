{
    'name': 'Sale Partner Contractors',
    'version': '16.0.1.0.1',
    'summary': 'Manage contractors & sites under Contacts and add contractor/site to Sale Orders',
    'description': """
   <img src="/site_contractors/static/description/cover.jpg" style="width:100%;"/>

<h2>Contractors & Sites Management</h2>
<p>Simple, clean module to manage contractors and sites per customer.</p>

<ul>
  <li>Contractors → linked to company</li>
  <li>Sites → linked to contractor</li>
  <li>Sale order selection with filtering</li>
</ul>

<p><strong>Aspire Analytica</strong></p>
    """,
    'description_file': 'static/description/description.html',
    'author': 'Aspire Analytica',
    'website': 'https://aspireanalytica.com',
    'depends': ['base', 'sale', 'contacts'],
    'license': 'LGPL-3',
    'category': 'Sales',
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml',
        'views/contractor_views.xml',
        'views/site_views.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/icon.png',
               'static/description/cover.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 5.0,
    'currency': 'USD',
}