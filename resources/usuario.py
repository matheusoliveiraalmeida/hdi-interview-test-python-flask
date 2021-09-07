from flask import request
from flask_restplus import Resource, fields
from db import db
from models.usuario import UsuarioModel
from schemas.usuario import UsuarioSchema
from models.contato import ContatoModel
from schemas.contato import ContatoSchema

from server.instance import server

usuario_ns = server.usuario_ns
contato_ns = server.contato_ns

USUARIO_NAO_ENCONTRADO = "Usuario não encontrado."


usuario_schema = UsuarioSchema()
usuario_list_schema = UsuarioSchema(many=True)
contato_schema = ContatoSchema()
contato_list_schema = ContatoSchema(many=True)

contato_obj = contato_ns.model('Contato', {
    'email': fields.String('Contato E-mail'),
    'telefone': fields.Integer('Contato telefone'),
    'flagPrincipal': fields.Integer('Contato telefone')
})

usuario_obj = usuario_ns.model('Usuario', {
    'documento': fields.Integer('Usuario documento'),
    'nome': fields.String('Usuario nome'),
    'contatos': fields.List(fields.Nested(contato_obj))
})


class Usuario(Resource):

    def get(self, documento):
        usuario_data = UsuarioModel.find_by_documento(documento)
        if usuario_data:
            return usuario_schema.dump(usuario_data)
        return {'message': USUARIO_NAO_ENCONTRADO}, 404

    def delete(self, documento):
        usuario_data = UsuarioModel.find_by_documento(documento)
        if usuario_data:
            usuario_data.delete_from_db()
            return '', 204
        return {'message': USUARIO_NAO_ENCONTRADO}, 404


class UsuariosList(Resource):
    @usuario_ns.doc('Retorna todos os usuarios')
    def get(self):
        return usuario_list_schema.dump(UsuarioModel.find_all()), 200

class UsuarioCadastro(Resource):
    @usuario_ns.expect(usuario_obj)
    def post(self):
        usuario_json = request.get_json()

        usuario_data = usuario_schema.load(usuario_json, session=db.session)

        usuario_data.save_to_db()
        return usuario_schema.dump(usuario_data), 200

    @usuario_ns.expect(usuario_obj)
    def put(self):
        usuario_json = request.get_json()
        usuario_data = UsuarioModel.find_by_documento(usuario_json['documento'])

        if usuario_data:
            usuario_data.nome = usuario_json['nome']
        else:
            usuario_data = usuario_schema.load(usuario_json, session=db.session)

        usuario_data.save_to_db()
        return usuario_schema.dump(usuario_data), 200     
