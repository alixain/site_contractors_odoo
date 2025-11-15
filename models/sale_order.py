from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contractor_id = fields.Many2one(
        'res.partner',
        string='Contractor',
        domain=[('is_company', '=', True)],
        help="Select the contractor for this project."
    )

    site_id = fields.Many2one(
        'res.partner',
        string='Site',
        domain="[('parent_id', '=', contractor_id)]",
        help="Select the site linked to the contractor."
    )
