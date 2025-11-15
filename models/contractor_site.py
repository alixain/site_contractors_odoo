from odoo import models, fields


class Contractor(models.Model):
    _name = 'res.partner.contractor'
    _description = 'Contractors for Company'


    parent_partner_id = fields.Many2one('res.partner', string='Company')
    name = fields.Char(required=True)
    details = fields.Text()
site_ids = fields.One2many('res.partner.contractor.site', 'contractor_id', string='Sites')


class ContractorSite(models.Model):
    _name = 'res.partner.contractor.site'
    _description = 'Sites under Contractor'


    contractor_id = fields.Many2one('res.partner.contractor', string='Contractor', required=True)
    name = fields.Char(required=True)
    details = fields.Text()


class Partner(models.Model):
    _inherit = 'res.partner'


    contractor_ids = fields.One2many('res.partner.contractor', 'parent_partner_id', string='Contractors')


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    contractor_id = fields.Many2one('res.partner.contractor', string="Contractor")
    site_id = fields.Many2one('res.partner.contractor.site', string="Site")


    def _search_contractor(self, operator, value):
        return [('contractor_id.name', operator, value)]


    def _search_site(self, operator, value):
        return [('site_id.name', operator, value)]