from odoo import api, fields, models

class HRTransportRoute(models.Model):
    _name = 'hr.transport.route'
    _inherit = ['mail.thread']
    _description = 'HR Transport Route'

    name = fields.Char(string="Name", required=True, tracking=True)
    stop_ids = fields.One2many('hr.transport.route.stop.rel', 'route_id', string="Stops")
    active = fields.Boolean(default=True, tracking=True)



