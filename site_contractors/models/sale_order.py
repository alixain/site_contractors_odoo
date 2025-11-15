from odoo import models, fields, api



class SaleOrder(models.Model):
    _inherit = "sale.order"

    contractor_id = fields.Many2one('partner.contractor', string='Contractor')
    site_id = fields.Many2one('partner.contractor.site', string='Site')

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            return {
                'domain': {
                    'contractor_id': [('partner_id', '=', self.partner_id.id)],
                    'site_id': [('contractor_id.partner_id', '=', self.partner_id.id)]
                }
            }
        else:
            return {
                'domain': {
                    'contractor_id': [],
                    'site_id': []
                }
            }

    @api.onchange('contractor_id')
    def _onchange_contractor_id(self):
        if self.contractor_id:
            return {
                'domain': {
                    'site_id': [('contractor_id', '=', self.contractor_id.id)]
                }
            }
        else:
            return {'domain': {'site_id': []}}
