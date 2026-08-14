from flask import jsonify, request
from services.chamado_service import ChamadoServices
from services.usuario_service import UsuarioServices

class ChamadoController():

    @staticmethod
    def valida_dados(dados):
        if not dados or not isinstance(dados, dict):
            return jsonify({"erro": "JSON inválido"}), 400

        titulo = dados.get("titulo")
        if not titulo or not str(titulo).strip() or len(str(titulo)) < 3:
            return jsonify({"erro": "Título é obrigatório e deve ter no mínimo 3 caracteres"}), 400

        descricao = dados.get("descricao")
        if not descricao or not str(descricao).strip():
            return jsonify({"erro": "Descrição é obrigatória"}), 400

        prioridade = dados.get("prioridade")
        if not prioridade or str(prioridade).strip() not in ["Baixa", "Média", "Alta"]:
            return jsonify({"erro": "Prioridade inválida (deve ser Baixa, Média ou Alta)"}), 400

        status = dados.get("status")
        if not status or str(status).strip() not in ["Aberto", "Em Andamento", "Fechado"]:
            return jsonify({"erro": "Status inválido (deve ser Aberto, Em Andamento ou Fechado)"}), 400

        usuario_id = dados.get("usuario_id")
        if not usuario_id or not isinstance(usuario_id, int):
            return jsonify({"erro": "usuario_id é obrigatório e deve ser um número inteiro"}), 400

        return None

    @staticmethod
    def index():
        return "Hello World!"
        
    @staticmethod
    def listar():
        resultado = ChamadoServices.consulta_chamados()
        return jsonify(resultado)

    @staticmethod
    def cadastrar():
        dados = request.json
        erro = ChamadoController.valida_dados(dados)
        if erro:
            return erro

        chamado = ChamadoServices.cadastra_chamado(
        titulo=dados["titulo"],
        descricao=dados["descricao"],
        prioridade=dados["prioridade"],
        status=dados["status"],
        tecnico=dados.get("tecnico"),
        usuario_id=dados["usuario_id"],
        )

        return jsonify({
            "mensagem": "Chamado cadastrado",
            "id": chamado.id
        })

    @staticmethod
    def atualizar(id):
        dados = request.json
        erro = ChamadoController.valida_dados(dados)
        if erro:
            return erro

        chamado = ChamadoServices.atualiza_chamado(
            id=id,
            titulo=dados["titulo"],
            descricao=dados["descricao"],
            prioridade=dados["prioridade"],
            status=dados["status"],
            tecnico=dados.get("tecnico"),
            usuario_id=dados["usuario_id"],
        )

        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404

        return jsonify({
            "mensagem": "Chamado atualizado",
            "id": chamado.id
        })

    @staticmethod
    def excluir(id):
        chamado = ChamadoServices.exclui_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404
        return jsonify({
            "mensagem": "Chamado excluído",
            "id": chamado.id
        })
    
    @staticmethod
    def listar_por_usuario(id):
        resultado = ChamadoServices.consulta_chamados_por_usuario(id)
        return jsonify(resultado), 200

    @staticmethod
    def iniciar(id):
        chamado = ChamadoServices.iniciar_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404

        return jsonify({
            "mensagem": "Chamado alterado para Em atendimento",
            "id": chamado.id,
            "status": chamado.status
        }), 200

    @staticmethod
    def encerrar(id):
        chamado = ChamadoServices.encerrar_chamado(id)
        if not chamado:
            return jsonify({"erro": "Chamado não encontrado"}), 404

        return jsonify({
            "mensagem": "Chamado encerrado com sucesso",
            "id": chamado.id,
            "status": chamado.status
        }), 200
    
    @staticmethod
    def listar_abertos():
        resultado = ChamadoServices.consulta_chamados_abertos()
        return jsonify(resultado), 200

    @staticmethod
    def listar_prioridade_alta():
        resultado = ChamadoServices.consulta_chamados_prioridade_alta()
        return jsonify(resultado), 200
    @staticmethod
    def estatisticas():
        resultado = ChamadoServices.consulta_estatisticas()
        return jsonify(resultado), 200