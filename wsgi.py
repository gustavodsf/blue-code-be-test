import os
import unittest

from flask.cli import FlaskGroup
from flask_migrate import Migrate
from app.src import create_app, db  

app = create_app(os.getenv('BLUE_CODE_ENV') or 'dev')
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