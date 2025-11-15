from odoo import models, fields



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    contractor_id = fields.Many2one('partner.contractor', string='Contractor', help='Contractor for this sale order')
    site_id = fields.Many2one('partner.contractor.site', string='Site', help='Site linked to selected contractor', domain="[('contractor_id','=', contractor_id)]")