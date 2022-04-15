# -*- coding:utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'res.partner'

    instructor = fields.Char()
    instructor = fields.Boolean("Instructor", default=False)

    session_ids = fields.Many2many('openacademy.session', string="Attended Sessions", readonly=True)