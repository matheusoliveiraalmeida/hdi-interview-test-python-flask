from db import db
from typing import List

class ContatoModel(db.Model):
    __tablename__ = "contatos"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    flagPrincipal = db.Column(db.Boolean, nullable=False)

    def __init__(self, email, telefone, flagPrincipal):
        self.email = email
        self.telefone = telefone
        self.flagPrincipal = flagPrincipal

    def __repr__(self):
        return f'ContatoModel(email={self.email}, telefone={self.telefone}, flagPrincipal={self.flagPrincipal})'

    def json(self):
        return {'email': self.email, 'telefone': self.telefone, 'flagPrincipal': self.flagPrincipal}

    @classmethod
    def find_by_email(cls, email) -> "ContatoModel":
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_all(cls) -> List["ContatoModel"]:
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
