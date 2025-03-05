from odoo import http
from odoo.http import request

class ChapterMain_Controller(http.Controller):

    def __init__(self):
        super().__init__()
        print("ChapterMain_Controller LOADED!")  # Questo deve comparire nel log



# http://localhost:8069/course/chapter/5
    @http.route('/course/chapter/<int:chapter_id>', type='http', auth='public', website=True)
    def course_chapter(self, chapter_id, **kwargs):
        print(f"Requested Chapter ID: {chapter_id}")  # Controlla se questo viene stampato nel log
        #chapter = request.env['slide.chapter'].sudo().browse(chapter_id)

        Chapter = request.env['slide.chapter'].sudo()
        chapter = Chapter.browse(chapter_id)


        if not chapter.exists():
            print("Chapter NOT found!")  # Debug
            return request.not_found()

        #return request.render('lms_ext_chapter_kanban.slide_chapter_template', {
        return request.render(f'{module_name}.slide_chapter_template', {
            'chapter': chapter
        })




