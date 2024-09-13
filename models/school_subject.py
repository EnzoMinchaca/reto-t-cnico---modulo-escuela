from odoo import fields, models

class Subject(models.Model):
    _name = "school.subject"
    _description = "Asignatura"
    
    name = fields.Char("Nombre", required=True)
    credits = fields.Integer("Créditos", required=True)
    max_students = fields.Integer("Cantidad Máxima de Estudiantes", required=True)
    active = fields.Boolean("Activo", default=True)
    student_subject_ids = fields.One2many("school.student_subject", "subject_id", string="Estudiantes")
    #student_ids = fields.Many2many('school.student', string='Students')
    teacher_id = fields.Many2one("school.teacher", string="Profesor", required=True) 