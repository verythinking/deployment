class Config(object):
    """
        基本通用配置
    """
    SECRET_KEY = 'this is a key!%$'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@/deployment'

    def init_app(app):
        pass


class DevConfig(Config):

    """
        开发环境基本配置
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProConfig(Config):

    """
        生产环境基本配置
    """

    DEBUG = False
    SQLALCHEMY_ECHO = False
