from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    vehicle_ids = fields.One2many('hr.transport.vehicle', 'driver_id', string="Assigned Vehicles")
