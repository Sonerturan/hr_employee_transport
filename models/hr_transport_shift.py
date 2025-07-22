from odoo import api, fields, models

class HRTransportShift(models.Model):
    _name = 'hr.transport.shift'
    _inherit = ['mail.thread']
    _description = 'HR Transport Shift'

    name = fields.Char(string="Name", required=True, tracking=True)
    departure_time = fields.Float(string="Departure Time")
    shift = fields.Selection(string="Shift", selection=[("morning" ,"Morning"), ("noon" ,"Noon"), ("evening" ,"Evening"), ("eight" ,"Night")], required=True)
    active = fields.Boolean(default=True, tracking=True)
