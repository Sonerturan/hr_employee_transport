from odoo import api, fields, models

class HRTransportStop(models.Model):
    _name = 'hr.transport.stop'
    _inherit = ['mail.thread']
    _description = 'HR Transport Stop'

    name = fields.Char(string="Name", required=True, tracking=True)
    latitude = fields.Float(string="Latitude")
    longitude = fields.Float(string="Longitude")
    active = fields.Boolean(default=True, tracking=True)
