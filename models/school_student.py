from odoo import fields, models, api

class Student(models.Model):
    _name = "school.student"
    _description = "Estudiante"
    
    name = fields.Char("Nombre", required=True)
    birth_date = fields.Date("Fecha de Nacimiento", required=True)
    age = fields.Integer("Edad", readonly=True, compute="_compute_age", store=True)
    student_subject_ids = fields.One2many("school.student_subject", "student_id", string="Asignaturas")
    #subject_ids = fields.Many2many('school.subject', string='Subjects')
    
    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )