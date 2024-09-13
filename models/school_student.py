from odoo import fields, models, api

class Student(models.Model):
    _name = "school.student"
    _description = "Estudiante"
    
    name = fields.Char("Nombre", required=True)
    birth_date = fields.Date("Fecha de Nacimiento", required=True)
    age = fields.Integer("Edad", readonly=True, compute="_compute_age", store=True)
    student_subject_ids = fields.One2many("school.student_subject", "student_id", string="Asignaturas")
    #subject_ids = fields.Many2many('school.subject', string='Asignaturas')
    average_grade = fields.Float("Promedio de Notas", compute="_compute_average_grade")
    
    #Funcion para calcular la edad en base a la fecha de nacimiento declarada
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
    
    #Funcion para calcular el promedio de todas las notas de examenes finales de cada asignatura para el estudiante
    @api.depends('student_subject_ids.final_exam_grade')
    def _compute_average_grade(self):
        for record in self:
            total_grades = 0.0
            grade_count = 0
            for student_subject in record.student_subject_ids:
                if student_subject.final_exam_grade:
                    total_grades += student_subject.final_exam_grade
                    grade_count += 1
            
            if grade_count > 0:
                record.average_grade = total_grades / grade_count
            else:
                record.average_grade = 0.0