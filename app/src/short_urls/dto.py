from flask_restplus import Namespace, fields

class ShorterURLDto:
    api = Namespace('shorterURL', description='shorterURL related operations')
    shorterURL = api.model('shorterURL', {
        'original_url': fields.String(required=True, description='URL original'),
        'short_url': fields.String(required=False, description='URL de tamanho reduzida gerada pelo sistema'),
        'page_title': fields.String(required=False, description='título da página'),
        'number_access': fields.Integer(required=False, description='Número de acessos'),
        'created_at': fields.String(required=False, description='Data do primeiro acesso'),
    })