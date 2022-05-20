from multiprocessing import Manager
from app import create_app,db
# from flask_migrate import Migrate
from app.models import Admin, Blog, User


app = create_app()


@app.shell_context_processor
def make_shell_context():
    # return {'db':db, 'Admin':Admin, 'Blog':Blog}
    return dict(app = app, db = db, User = User, Blog =Blog, Admin =Admin)


# migrate=Migrate(app, db)
# Manager.add_command('db')


if __name__=='__main__':
	app.run()