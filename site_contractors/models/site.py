from odoo import models, fields

class PartnerContractorSite(models.Model):
    _name = 'partner.contractor.site'
    _description = 'Site under Contractor'


    name = fields.Char(required=True, string='Name')
    contractor_id = fields.Many2one('partner.contractor', string='Contractor', required=True, ondelete='cascade')
    details = fields.Text(string='Details')