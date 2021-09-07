from flask import Flask, Blueprint
from flask_restplus import Api
from ma import ma
from db import db

from marshmallow import ValidationError


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint, doc='/doc', nome='API Swagger')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.usuario_ns = self.usuario_ns()
        self.contato_ns = self.contato_ns()

        super().__init__()

    def usuario_ns(self, ):
        return self.api.namespace(name='Usuarios', description='CRUD usuarios', path='/')

    def contato_ns(self, ):
        return self.api.namespace(name='Contatos', description='CRUD contatos', path='/')    

    def run(self, ):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0'
        )


server = Server()
