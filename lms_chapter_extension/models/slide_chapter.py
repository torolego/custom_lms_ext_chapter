from odoo import models, fields


from odoo import models, fields

class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    chapter_ids = fields.One2many('slide.chapter', 'course_id', string="Chapters")

class SlideChapter(models.Model):
    _name = "slide.chapter"
    _description = "Course Chapter"

    name = fields.Char(required=True)
    course_id = fields.Many2one("slide.channel", string="Course", required=True)
    lesson_ids = fields.One2many("slide.slide", "chapter_id", string="Lessons")


