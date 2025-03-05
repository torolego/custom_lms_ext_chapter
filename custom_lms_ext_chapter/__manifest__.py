{
    'name': 'LMS Chapter Extension',
    'version': '16.0.1.0.0',
    'summary': 'Extends Odoo LMS (website_slides) to add chapter pages',
    'author': 'QuickStart2',
    'category': 'Website',
    'depends': ['website_slides'],
    'data': [
        'security/ir.model.access.csv',
        "views/slide_chapter_views.xml",
        "views/slide_course_views.xml",
        "views/slide_lesson_views.xml",
        "templates/slide_channel_chapters_template.xml",
        "templates/slide_chapter_template.xml",
    ],
    'installable': True,
    'application': False,
    "auto_install": False,
    'license': 'LGPL-3',
}
