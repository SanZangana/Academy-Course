from odoo import models, fields

class AcademyCourse(models.Model):
    _name = "academy.course"
    _description = "Academy Course"

    name = fields.char(string = "Title", required = True)
    description = fields.Text(string ="Description")
    responsible_id = fields.Many2one('res.users', string ="responsible")
    
    