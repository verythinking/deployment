from views.servers import ServerView
from models.servers import Server
from db import db


server_view = ServerView(Server, db.session, name='服务器信息',
                         category='服务器', endpoint='servers')
