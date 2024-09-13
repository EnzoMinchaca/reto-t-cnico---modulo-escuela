from odoo import fields, models, api

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
    enrolled_students = fields.Integer("Cantidad de Estudiantes Inscriptos", compute="_compute_enrolled_students", store=True, readonly=True)
    
    #Funcion para ver la cantidad de estudiantes inscriptos en la asignatura
    @api.depends('student_subject_ids')
    def _compute_enrolled_students(self):
        for subject in self:
            subject.enrolled_students = len(subject.student_subject_ids)