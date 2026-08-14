from flask import jsonify, request
from services.services import AlunoServices

class AlunoController():

    def valida_dados(dados):
        if not dados:
            return jsonify({"erro": "JSON inválido"}), 400
        
        if len(dados.get("nome", "")) < 3:
            return jsonify({"erro": "Nome inválido"}), 400
            
        email = dados.get("email")
        if not email:
            return jsonify({"erro": "Email obrigatório"}), 400
        if "@" not in email:
            return jsonify({"erro": "Email inválido"}), 400
            
        setor = dados.get("setor")
        if setor is not None and len(str(setor).strip()) == 0:
            return jsonify({"erro": "Setor inválido"}), 400

        return True
        
    @staticmethod
    def index():
        return "Hello World!"
        
    @staticmethod
    def listar():
        resultado = AlunoServices.consulta_alunos()
        return jsonify(resultado)

    @staticmethod
    def cadastrar():
        dados = request.json
        valida_dados = AlunoController.valida_dados(dados)
        if not valida_dados:
            return jsonify({"erro": "Não foi possível validar os dados"}), 400

        aluno = AlunoServices.cadastra_aluno(
            nome=dados["nome"],
            idade=dados["idade"],
            email=dados["email"],
            curso=dados["curso"],
            ativo=dados.get("ativo", True)
        )

        return jsonify({
            "mensagem": "Aluno cadastrado",
            "id": aluno.id
        })

    def atualizar(id):
        dados = request.json
        valida_dados = AlunoController.valida_dados(dados)
        if not valida_dados:
            return jsonify({"erro": "Não foi possível validar os dados"}), 400

        aluno = AlunoServices.atualiza_aluno(
            id=id,
            nome=dados["nome"],
            idade=dados["idade"],
            email=dados["email"],
            curso=dados["curso"]
        )

        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404

        return jsonify({
            "mensagem": "Aluno atualizado",
            "id": aluno.id
        })

    def excluir(id):
        aluno = AlunoServices.exclui_aluno(id)
        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404
        return jsonify({
            "mensagem": "Aluno excluído",
            "id": aluno.id
        })

    def ativar(id):
        aluno = AlunoServices.ativa_aluno(id)
        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404
        return jsonify({
            "mensagem": "Aluno ativado",
            "id": aluno.id
        })

    def desativar(id):
        aluno = AlunoServices.desativa_aluno(id)
        if not aluno:
            return jsonify({"erro": "Aluno não encontrado"}), 404
        return jsonify({
            "mensagem": "Aluno desativado",
            "id": aluno.id
        })

    def estatisticas():
        estatisticas = AlunoServices.gera_estatisticas()
        return jsonify(estatisticas)