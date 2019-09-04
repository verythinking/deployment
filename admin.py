from flask_admin import Admin, AdminIndexView
from view_config import server_view


class MyAdmin(Admin):

    def __init__(self, **kwargs):
        super(MyAdmin, self).__init__(
            name='部署系统', index_view=AdminIndexView(
                url='/', name='首页', template='base.html'))


admin = MyAdmin()

admin.add_view(server_view)
