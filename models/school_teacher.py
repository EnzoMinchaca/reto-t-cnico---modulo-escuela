from odoo import fields, models

class Teacher(models.Model):
    _name = "school.teacher"
    _description = "Profesor"
    
    name = fields.Char("Nombre", required=True)
    profile = fields.Text("Perfil", required=True)
    subject_ids = fields.One2many("school.subject", "teacher_id", string="Asignaturas")