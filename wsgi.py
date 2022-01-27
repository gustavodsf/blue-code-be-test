import os
import unittest
import time
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app.src import create_app, db  
from app import blueprint
from app.src.short_urls import entity


app = create_app('dev')
app.register_blueprint(blueprint)


migrate = Migrate(app, db)
app.app_context().push()

cli = FlaskGroup(app)

@cli.command('test')
def cli_test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    cli()