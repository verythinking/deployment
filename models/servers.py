from sqlalchemy import Column, Integer, String

from db import db


class Server(db.Model):

    __tablename__ = 'server'

    """
        服务器信息模型
    """

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    ip = Column(String(123), unique=True)
