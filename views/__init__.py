from flask_admin.contrib.sqla import ModelView


class MyView(ModelView):

    list_template = 'list.html'
    create_template = 'create.html'
    edit_template = 'edit.html'
    details_template = 'details.html'
