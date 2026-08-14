from models.chamado import Chamado
from models.usuario import Usuario
from database import db
from datetime import datetime

class ChamadoRepository():
    @staticmethod
    def consulta_tudo():
        return Chamado.query.order_by(Chamado.titulo).all()

    @staticmethod
    def consulta_um(chamado_id):
        return Chamado.query.filter(id = chamado_id).first()

    @staticmethod
    def cadastrar_chamado(dados):
        chamado = Chamado(
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            prioridade=dados["prioridade"],
            status=dados["status"],
            tecnico=dados.get("tecnico"),
            usuario_id=dados["usuario_id"],
        )
        db.session.add(chamado)
        db.session.commit()
        return chamado


    @staticmethod
    def atualizar_chamado(id, dados):
        chamado = Chamado.query.filter_by(id=id).first()
        if not chamado:
            return None
        chamado.titulo = dados['titulo']
        chamado.descricao = dados['descricao']
        chamado.prioridade = dados['prioridade']
        chamado.status = dados['status']
        chamado.tecnico = dados['tecnico']
        chamado.usuario_id= dados['usuario_id']
        db.session.commit()
        return chamado
    
    @staticmethod
    def excluir_chamado(id):
        chamado = Chamado.query.filter_by(id=id).first()
        if not chamado:
            return None
        db.session.delete(chamado)
        db.session.commit()
        return chamado

    @staticmethod
    def buscar_por_usuario(usuario_id):
        return Chamado.query.filter_by(usuario_id=usuario_id).all()
    

    @staticmethod
    def iniciar_chamado(id):
        chamado = Chamado.query.get(id)
        if not chamado:
            return None
        chamado.status = "Em atendimento"
        db.session.commit()
        return chamado

    @staticmethod
    def encerrar_chamado(id):
        chamado = Chamado.query.get(id)
        if not chamado:
            return None
        chamado.status = "Encerrado"
        db.session.commit()
        return chamado
    
    @staticmethod
    def buscar_por_status(status):
        return Chamado.query.filter_by(status=status).all()

    @staticmethod
    def buscar_por_prioridade(prioridade):
        return Chamado.query.filter_by(prioridade=prioridade).all()
    
    @staticmethod
    def obter_estatisticas():
        total_usuarios = Usuario.query.count()
        total_chamados = Chamado.query.count()
        abertos = Chamado.query.filter_by(status="Aberto").count()
        em_atendimento = Chamado.query.filter_by(status="Em atendimento").count()
        encerrados = Chamado.query.filter_by(status="Encerrado").count()

        return {
            "usuarios": total_usuarios,
            "chamados": total_chamados,
            "abertos": abertos,
            "em_atendimento": em_atendimento,
            "encerrados": encerrados
        }