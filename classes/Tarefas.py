from datetime import datetime as dt

STATUS = ['Pendente', 'Em andamento', 'Concluída']


def pegar_hora() -> str:
    return dt.now().strftime("%d-%m-%Y %H:%M:%S")


class Tasks():
    def __init__(self) -> None:
        self.tarefas: list[dict] = []

    def criar_id(self) -> str:
        return dt.now().strftime("%Y%m%d%H%M%S%f")

    def _pegar_tarefa(self, id_tarefa: str) -> dict | None:
        for tarefa in self.tarefas:
            if tarefa['id_tarefa'] == id_tarefa:
                return tarefa
        return None

    # ================ CHANGE STATUS ================

    def _mudar_status(self, id_tarefa: str, status: int) -> dict | str:
        if status >= len(STATUS):
            return "Status inválido"

        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"

        tarefa["status"] = STATUS[status]
        tarefa["atualizada"] = pegar_hora()
        return tarefa

    # ================ CREATE TASK ================

    def adicionar_tarefa(self, descricao, status=STATUS[0]) -> dict:
        if status not in STATUS:
            status = STATUS[0]

        hora: str = pegar_hora()
        data: dict = {
            "id_tarefa": self.criar_id(),
            "descricao": descricao,
            "status": status,
            "criada": hora,
            "atualizada": hora}
        self.tarefas.append(data)
        return data

    # ================= READ TASK =================
    def ler_tarefa(self, id_tarefa: str) -> dict | str:
        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"
        return tarefa

    # ================ UPDATE TASK ================
    def atualizar_tarefa(self, id_tarefa: str, descricao: str):
        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"

        tarefa["descricao"] = descricao
        tarefa["atualizada"] = pegar_hora()

        return tarefa

    # ================ DELETE TASK ================
    def deletar_tarefa(self, id_tarefa: str) -> list | str:
        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"

        self.tarefas = [t for t in self.tarefas if t["id_tarefa"] != id_tarefa]
        return self.tarefas

# --------------------------------------------------------------------------------

    # ================ MARK STATUS ================

    def marcar_tarefa_pendente(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 0)

    def marcar_tarefa_em_andamento(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 1)

    def marcar_tarefa_concluida(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 2)
