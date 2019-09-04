from flask import Flask
from admin import admin

from conf import DevConfig
from db import db


def create_app(config=DevConfig):

    app = Flask(__name__)
    app.config.from_object(config)

    config.init_app(app)
    admin.init_app(app)
    db.init_app(app)

    return app
