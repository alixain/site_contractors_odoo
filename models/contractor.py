from odoo import models, fields


class PartnerContractor(models.Model):
    _name = 'partner.contractor'
    _description = 'Contractor linked to a Company'


    name = fields.Char(required=True, string='Name')
    partner_id = fields.Many2one('res.partner', string='Company', required=True, ondelete='cascade')
    details = fields.Text(string='Details')
    site_count = fields.Integer(compute='_compute_site_count', string='Sites')
    site_ids = fields.One2many('partner.contractor.site', 'contractor_id', string='Sites')


    def _compute_site_count(self):
        for rec in self:
            rec.site_count = len(rec.site_ids)