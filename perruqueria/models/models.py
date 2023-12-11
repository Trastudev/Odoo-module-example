from odoo import models, fields, api

class Formacio(models.Model):
    _name = 'perruqueria.formacio'
    _description = 'Training for barbershops'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    manager_id = fields.Many2one('hr.employee', string='Manager', required=True)
    trainer_id = fields.Many2one('res.partner', string='Trainer', required=True)
    customer_ids = fields.Many2many('res.partner', string='Customer', required=True)
    event_id = fields.Many2one('perruqueria.event', string='Event', required=True)

class Event(models.Model):
    _name = 'perruqueria.event'
    _description = 'Training Event'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Datetime(string='Data', compute="_compute_event_date", store=True) # Calcular data en funció a valor de data d'event
    prize = fields.Float(string='Prize')
    event_id = fields.Many2one('event.event', string='Event', required=True)

    @api.depends('event_id.date_begin')
    def _compute_event_date(self):
        if self.event_id.mapped('date_begin'):
            self.date = self.event_id.mapped('date_begin')[0]
