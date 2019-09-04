from flask_script import Manager, Server, Command
from app import create_app
from db import db

server = Server(host='0.0.0.0')
manager = Manager(create_app)


class CreateDB(Command):

    def run(self):
        db.create_all()


class DropDB(Command):

    def run(self):
        db.drop_all()


manager.add_command('runserver', server)
manager.add_command('create_db', CreateDB)
manager.add_command('drop_db', DropDB)

if __name__ == '__main__':
    manager.run()
