from flask import jsonify, request
from services.usuario_service import UsuarioServices

class UsuarioController():

    @staticmethod
    def valida_dados(dados):
        if not dados or not isinstance(dados, dict):
            return jsonify({"erro": "JSON inválido"}), 400

        nome = dados.get("nome")
        if not nome or not str(nome).strip() or len(str(nome)) < 3:
            return jsonify({"erro": "Nome é obrigatório e deve ter no mínimo 3 caracteres"}), 400

        email = dados.get("email")
        if not email or not str(email).strip() or "@" not in str(email):
            return jsonify({"erro": "E-mail inválido (deve conter @)"}), 400

        return None 
    @staticmethod
    def index():
        return "Hello World!"
        
    @staticmethod
    def listar():
        resultado = UsuarioServices.consulta_usuarios()
        return jsonify(resultado)

    @staticmethod
    def cadastrar():
        dados = request.json
        erro = UsuarioController.valida_dados(dados)
        if erro:
            return erro

        usuario = UsuarioServices.cadastra_usuario(
        nome=dados["nome"],
        email=dados["email"],
        setor=dados.get("setor")
        )

        return jsonify({
            "mensagem": "Usuario cadastrado",
            "id": usuario.id
        })

    @staticmethod
    def atualizar(id):
        dados = request.json
        erro = UsuarioController.valida_dados(dados)
        if erro:
            return erro

        usuario = UsuarioServices.atualiza_usuario(
            id=id,
            nome=dados["nome"],
            email=dados["email"],
            setor=dados.get("setor")
        )

        if not usuario:
            return jsonify({"erro": "Usuario não encontrado"}), 404

        return jsonify({
            "mensagem": "Usuario atualizado",
            "id": usuario.id
        })

    @staticmethod
    def excluir(id):
        usuario = UsuarioServices.exclui_usuario(id)
        if not usuario:
            return jsonify({"erro": "Usuario não encontrado"}), 404
        return jsonify({
            "mensagem": "Usuario excluído",
            "id": usuario.id
        })
