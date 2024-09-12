from odoo import fields, models, api
from odoo.exceptions import ValidationError

class StudentSubject(models.Model):
    _name = "school.student_subject"
    _description = "Estudiante y Asignatura"
    
    student_id = fields.Many2one(
        "school.student", 
        string="Estudiante", 
        required=True,
    )
    subject_id = fields.Many2one(
        "school.subject", 
        string="Asignatura", 
        required=True,
    )
    teacher_id = fields.Many2one(
        "school.teacher", 
        string="Profesor", 
        related="subject_id.teacher_id", 
        store=True, 
        readonly=True,
    )
    final_exam_grade = fields.Float("Nota Final")
    
    _sql_constraints = [
        ('unique_student_subject', 'unique(student_id, subject_id)', "Un estudiante no puede estar registrado en la misma asignatura más de una vez.")
    ]
    
    @api.constrains('subject_id')
    def _check_max_students(self):
        for record in self:
            subject = record.subject_id
            if subject.student_subject_ids and len(subject.student_subject_ids) > subject.max_students:
                raise ValidationError(f"La asignatura '{subject.name}' ya ha alcanzado su capacidad máxima de {subject.max_students} estudiantes.")