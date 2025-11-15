from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    contractor_id = fields.Many2one(
        'partner.contractor', string='Contractor', 
        help="Select contractor linked to the customer"
    )
    site_id = fields.Many2one(
        'partner.contractor.site', string='Site', 
        help="Select site linked to the contractor"
    )

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        """When customer changes, filter contractors and reset contractor/site."""
        for order in self:
            if order.partner_id:
                # Reset dependent fields
                order.contractor_id = False
                order.site_id = False

                # Set domain for contractor based on partner
                contractors = order.partner_id.contractor_ids.ids if order.partner_id.contractor_ids else []
                return {
                    'domain': {
                        'contractor_id': [('id', 'in', contractors)],
                        'site_id': []  # site domain will be set after contractor is selected
                    }
                }
            else:
                # No partner selected: clear domains and values
                order.contractor_id = False
                order.site_id = False
                return {
                    'domain': {
                        'contractor_id': [],
                        'site_id': []
                    }
                }

    @api.onchange('contractor_id')
    def _onchange_contractor_id(self):
        """When contractor changes, filter sites and reset site."""
        for order in self:
            if order.contractor_id:
                order.site_id = False
                return {
                    'domain': {
                        'site_id': [('contractor_id', '=', order.contractor_id.id)]
                    }
                }
            else:
                order.site_id = False
                return {
                    'domain': {
                        'site_id': []
                    }
                }
