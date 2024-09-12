from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "school.student"
    _description = "Estudiante"
    
    name = fields.Char("Nombre", required=True)
    birth_date = fields.Date("Fecha de Nacimiento", required=True)
    age = fields.Integer("Edad", readonly=True, compute="_compute_age", store=True)
    student_subject_ids = fields.One2many("school.student_subject", "student_id", string="Asignaturas")
    
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )

    # @api.constrains('subject_ids')
    # def _check_subject_capacity(self):
    #     for student in self:
    #         for subject in student.subject_ids:
    #             if len(subject.student_ids) > subject.max_students:
    #                 raise ValidationError(
    #                     f"La asignatura {subject.name} ha alcanzado su máxima capacidad de {subject.max_students} estudiantes. "
    #                     f"Ya no se permite añadirse a dicha asignatura."
    #                 )