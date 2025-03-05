from odoo import models, fields, api

class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    chapter_ids = fields.One2many('slide.chapter', 'course_id', string="Chapters")


class Slide(models.Model):
    _inherit = 'slide.slide'

    completed = fields.Boolean(string="Completed", default=False)
    chapter_id = fields.Many2one("slide.chapter", string="Chapter")
    image = fields.Binary(string="Lesson Image")
    description = fields.Text(string="Short Description")


class SlideChapter(models.Model):
    _name = "slide.chapter"
    _description = "Course Chapter"

    is_published = fields.Boolean(tracking=1)
    name = fields.Char(required=True)
    course_id = fields.Many2one("slide.channel", string="Course", required=True)
    lesson_ids = fields.One2many("slide.slide", "chapter_id", string="Lessons")
    image = fields.Binary(string="Chapter Image")

#    @api.depends('lesson_ids.completed')
#    def _compute_progress(self):
#        for chapter in self:
#            total_lessons = len(chapter.lesson_ids)
#            completed_lessons = sum(1 for lesson in chapter.lesson_ids if lesson.completed)
#            chapter.progress = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0

#    progress = fields.Float(string="Progress (%)", compute="_compute_progress")



