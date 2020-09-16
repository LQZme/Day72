from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_script import Server
from application import app
from application import db
import traceback
import www

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(port=app.config['SERVER_PORT'],
                                        use_debugger=app.config['DEBUG']))

if __name__ == "__main__":
    try:
        manager.run()
    except Exception as err:
        traceback.print_exc(err)
