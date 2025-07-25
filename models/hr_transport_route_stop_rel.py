from odoo import api, fields, models

class HRTransportRouteStopRel(models.Model):
    _name = 'hr.transport.route.stop.rel'
    _inherit = ['mail.thread']
    _description = 'HR Transport Route Stop Order'
    _order = 'sequence asc'

    route_id = fields.Many2one('hr.transport.route', required=True)
    stop_id = fields.Many2one('hr.transport.stop', required=True)
    sequence = fields.Integer(string="Sequence", default="1")
