from flask_restplus import Api
from flask import Blueprint

from app.src.short_urls.controller import api as shorter_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Blue Code Test API',
          version='1.0',
          description='a boilerplate for blue code test'
          )

api.add_namespace(shorter_ns, path='/sh')
