from database import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    setor = db.Column(db.String(80), nullable=True)
    chamados = db.relationship('Chamado', backref='usuario', lazy=True)