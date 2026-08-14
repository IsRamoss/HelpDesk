from repositories.chamado_repository import ChamadoRepository

class ChamadoServices():

    @staticmethod
    def consulta_chamados():
        chamados = ChamadoRepository.consulta_tudo()

        resultado = []

        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,   # <-- Vírgula adicionada
                "status": chamado.status,           # <-- Vírgula adicionada
                "tecnico": chamado.tecnico,         # <-- Vírgula adicionada
                "data_abertura": chamado.data_abertura.isoformat() if chamado.data_abertura else None,
                "usuario_id": chamado.usuario_id
            })
        return resultado

    @staticmethod
    def cadastra_chamado(**kwargs):
        kwargs['status'] = "Aberto"

        prioridade = kwargs.get('prioridade')
        usuario_id = kwargs.get('usuario_id')

        if prioridade == "Alta":
            qtd_altos_ativos = ChamadoRepository.contar_chamados_altos_ativos(usuario_id)
            if qtd_altos_ativos >= 5:
                raise ValueError("O usuário não pode possuir mais de 5 chamados com prioridade Alta que não estejam encerrados.")

        return ChamadoRepository.cadastrar_chamado(**kwargs)

    @staticmethod
    def consultar_email(email):
        return ChamadoRepository.pesquisa_email(email)

    @staticmethod
    def atualiza_chamado(id, **kwargs):
        chamado = ChamadoRepository.atualizar_chamado(id, kwargs)
        return chamado

    @staticmethod
    def exclui_chamado(id):
        chamado = ChamadoRepository.excluir_chamado(id)
        return chamado

    @staticmethod
    def consulta_chamados_por_usuario(usuario_id):
        chamados = ChamadoRepository.buscar_por_usuario(usuario_id)

        resultado = []
        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "tecnico": chamado.tecnico,
                "data_abertura": chamado.data_abertura.isoformat() if chamado.data_abertura else None,
                "usuario_id": chamado.usuario_id
            })
            
        return resultado

    @staticmethod
    def iniciar_chamado(id):
        chamado = ChamadoRepository.iniciar_chamado(id)
        return chamado

    @staticmethod
    def encerrar_chamado(id):
        chamado = ChamadoRepository.encerrar_chamado(id)
        return chamado

    @staticmethod
    def consulta_chamados_abertos():
        chamados = ChamadoRepository.buscar_por_status("Aberto")
        
        resultado = []
        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "tecnico": chamado.tecnico,
                "data_abertura": chamado.data_abertura,
                "usuario_id": chamado.usuario_id
            })
        return resultado

    @staticmethod
    def consulta_chamados_prioridade_alta():
        chamados = ChamadoRepository.buscar_por_prioridade("Alta")
        
        resultado = []
        for chamado in chamados:
            resultado.append({
                "id": chamado.id,
                "titulo": chamado.titulo,
                "descricao": chamado.descricao,
                "prioridade": chamado.prioridade,
                "status": chamado.status,
                "tecnico": chamado.tecnico,
                "data_abertura": chamado.data_abertura,
                "usuario_id": chamado.usuario_id
            })
        return resultado

    @staticmethod
    def consulta_estatisticas():
        return ChamadoRepository.obter_estatisticas()