from odoo import api, fields, models

class HRTransportVehicle(models.Model):
    _name = 'hr.transport.vehicle'
    _inherit = ['mail.thread']
    _description = 'HR Transport Vehicle'

    name = fields.Char(string="Name", required=True, Tracking=True)
    driver_id = fields.Many2one('hr.employee', string="Driver", required=True)
    vehicle_type = fields.Selection(string="Vehicle Type", selection=[("bus" ,"Bus"), ("minibus" ,"Minibus")], required=True)
    capacity = fields.Integer(string="Capacity", required=True, Tracking=True, hepl="Total passenger capacity")
    vehicle_license_plate = fields.Char(string="Vehicle License Plate", Tracking=True)
    current_km = fields.Integer(string="Current Km")


