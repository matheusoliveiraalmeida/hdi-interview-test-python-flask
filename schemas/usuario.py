from ma import ma
from models.usuario import UsuarioModel
from schemas.contato import ContatoSchema

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    contatos = ma.Nested(ContatoSchema, many=True)

    class Meta:
        model = UsuarioModel
        load_instance = True
