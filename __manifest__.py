{
    'name': 'To Do Tasks',
    'version': '17.0.1.0.0',
    'summary': 'Manage Todo Tasks',
    'description': 'A module to manage TAsks.',
    'category': 'Projects',
    'author': 'Sayed Mohamed',
    'website': 'http://www.ToDotask.com',
    'depends': ['base', 'mail',
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
    ],
    'installable': True,
    'application': True,
}