# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Employee Transport',
    'version': '17.0.1.0.0',
    'sequence': 1,
    'category': 'Human Resources',
    'summary': 'Manage employee transportation, vehicle routes, stops and assignments',
    'description': """
        This module allows HR departments to manage employee transportation services.
        Features include vehicle assignment, route planning, stop ordering, shift schedules,
        driver linking and seat availability tracking.
    """,
    'author': 'Soner Turan',
    'website': 'https://github.com/Sonerturan/hr_employee_transport',
    'license': 'LGPL-3',
    'depends': ['mail', 'base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_transport_vehicle.xml',
        'views/hr_transport_route.xml',
        'views/hr_transport_stop.xml',
        'views/hr_transport_shift.xml',
        'views/hr_transport_plan.xml',
        'views/hr_transport_day.xml',
        'views/menu.xml',
        'data/hr_transport_day_data.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # 'hr_employee_transport_route/static/src/css/styles.css',
            # 'hr_employee_transport_route/static/src/js/custom.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}