from odoo import models, fields




class ResPartner(models.Model):
    _inherit = 'res.partner'


    contractor_ids = fields.One2many('partner.contractor', 'partner_id', string='Contractors')