from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do TAsk For management'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Task Name")
    assign_to = fields.Many2one('res.partner', string="Assign To")
    description = fields.Text(string="Description")
    date = fields.Date(string="Due Date")
    status= fields.Selection([
        ('new', 'New'),
        ('in progress', 'In progress'),
        ('completed', 'Completed'),
    ])
    active = fields.Boolean(default=True)