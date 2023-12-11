from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    trainer_ids = fields.One2many('perruqueria.formacio', 'trainer_id', string="Formacions")