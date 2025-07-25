from odoo import api, fields, models

class HRTransportDay(models.Model):
    _name = 'hr.transport.day'
    _inherit = ['mail.thread']
    _description = 'HR Transport Day'
    _rec_name = 'display_name'

    day_of_week = fields.Selection(string="Day of Week", selection=[
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'), ], required=True)

    display_name = fields.Char(string='Display Name', compute='_compute_display_name', store=True)

    @api.depends('day_of_week')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = dict(self._fields['day_of_week'].selection).get(rec.day_of_week, '')

