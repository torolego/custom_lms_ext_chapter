from odoo import models, fields

class SlideLesson(models.Model):
    _inherit = "slide.slide"

    chapter_id = fields.Many2one("slide.chapter", string="Chapter")
