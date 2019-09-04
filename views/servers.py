from . import MyView


class ServerView(MyView):

    column_list = ['name', 'ip']

    column_labels = {
        'name': '服务器名称',
        'ip': 'IP地址'
    }
