from odoo import api, fields, models

class HRTransportPlan(models.Model):
    _name = 'hr.transport.plan'
    _inherit = ['mail.thread']
    _description = 'HR Transport Plan'

    name = fields.Char(string="Name", required=True, tracking=True)
    vehicle_id = fields.Many2one('hr.transport.vehicle', string="Vehicle", required=True, tracking=True)
    route_id = fields.Many2one('hr.transport.route', string="Route", required=True, tracking=True)
    shift_id = fields.Many2one('hr.transport.shift', string="Shift", required=True, tracking=True)
    day_ids = fields.Many2many('hr.transport.day', string="Days")
    employee_ids = fields.Many2many('hr.employee', string="Employees")
    plan_type  = fields.Selection(string="Plan Type", selection=[("inbound-shuttle" ,"Inbound Shuttle"), ("outbound-shuttle" ,"Outbound Shuttle")])
    empty_seats = fields.Integer(
        string="Empty Seats",
        compute="_compute_empty_seats",
        store=False,
        readonly=True
    )
    active = fields.Boolean(default=True, tracking=True)

    @api.depends('vehicle_id.capacity', 'employee_ids')
    def _compute_empty_seats(self):
        for rec in self:
            if rec.vehicle_id and rec.vehicle_id.capacity:
                rec.empty_seats = rec.vehicle_id.capacity - len(rec.employee_ids)
            else:
                rec.empty_seats = 0



