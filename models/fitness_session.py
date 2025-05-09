from odoo import api, models, fields


class FitnessSession(models.Model):
    _name = 'fitness.session'
    _description = 'Fitness Session'

    # my field names
    session_name = fields.Char()
    session_date = fields.Datetime()
    heart_rate = fields.Integer()
    calories = fields.Integer()
    duration = fields.Integer()
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender")