from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Subject(models.Model):
    _name = "school.subject"
    _description = "Asignatura"
    
    name = fields.Char("Nombre", required=True)
    credits = fields.Integer("Créditos", required=True)
    max_students = fields.Integer("Cantidad Máxima de Estudiantes", required=True)
    active = fields.Boolean("Activo", default=True)
    student_subject_ids = fields.One2many("school.student_subject", "subject_id", string="Estudiantes")
    teacher_id = fields.Many2one("school.teacher", string="Profesor", required=True)
    
    # @api.constrains("student_ids")
    # def _check_max_capacity(self):
    #     for record in self:
    #         if len(record.student_ids) > record.max_students:
    #             raise ValidationError("Ya se alcanzó la capacidad máxima de estudiantes para esta asignatura") 