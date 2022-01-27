from flask_restplus import Api
from flask import Blueprint
from celery import Celery

from app.src.short_urls.controller import api as shorter_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Blue Code Test API',
          version='1.0',
          description='a boilerplate for blue code test'
          )

api.add_namespace(shorter_ns, path='/sh')

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend='redis://localhost:6379/0',
        broker='redis://localhost:6379/0'
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery