from db import db
from typing import List
from models.contato import ContatoModel

class UsuarioModel(db.Model):
    __tablename__ = "usuarios"

    documento = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    contatos = db.Column(db.PickleType())

    #contatos_ids = relationship('UsuarioModel', primaryjoin='contatos.id == any_(foreign(usuarios.contatos))',uselist=True)

    def __init__(self, documento, nome, contatos):
        self.documento = documento
        self.nome = nome
        self.contatos = contatos

    def __repr__(self):
        return f'UsuarioModel(nome={self.nome}, contatos={self.contatos})'

    def json(self):
        return {'nome': self.nome, 'contatos': self.contatos}

    @classmethod
    def find_by_documento(cls, _documento) -> "UsuarioModel":
        return cls.query.filter_by(documento=_documento).first()

    @classmethod
    def find_all(cls) -> List["UsuarioModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
