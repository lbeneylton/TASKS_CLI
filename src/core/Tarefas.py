from datetime import datetime as dt
from .Arquivo import Json

STATUS = ["Pendente", "Em andamento", "Concluída"]
FILE = Json("tasks.json")


def pegar_hora() -> str:
    return dt.now().strftime("%d-%m-%Y %H:%M:%S")


class Tasks:
    def __init__(self) -> None:
        self.tarefas: list[dict] = []
        self._ler_dados()

    def _criar_id(self) -> str:
        return dt.now().strftime("%Y%m%d%H%M%S%f")

    def _pegar_tarefa(self, id_tarefa: str) -> dict | None:
        for tarefa in self.tarefas:
            if tarefa["id_tarefa"] == id_tarefa:
                return tarefa
        return None

    def _ler_dados(self):
        """Recupera os dados do arquivo"""
        self.tarefas = FILE.read()

    def _escrever_dados(self):
        """Salva os dados no arquivo"""
        FILE.write(self.tarefas)

    # ================ CHANGE STATUS ================

    def _mudar_status(self, id_tarefa: str, status: int) -> dict | str:
        if status >= len(STATUS):
            return "Status inválido"

        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"

        tarefa["status"] = STATUS[status]
        tarefa["atualizada"] = pegar_hora()
        self._escrever_dados()  # salva alteração no arquivo
        return tarefa

    # ================ CREATE TASK ================

    def adicionar_tarefa(self, descricao, status=STATUS[0]) -> dict:
        if status not in STATUS:
            status = STATUS[0]

        hora: str = pegar_hora()
        data: dict = {
            "id_tarefa": self._criar_id(),
            "descricao": descricao,
            "status": status,
            "criada": hora,
            "atualizada": hora,
        }
        self.tarefas.append(data)
        self._escrever_dados()  # salvando alteração no arquivo
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

        self._escrever_dados()  # salvando alteração no arquivo
        return tarefa

    # ================ DELETE TASK ================
    def deletar_tarefa(self, id_tarefa: str) -> list | str:
        tarefa = self._pegar_tarefa(id_tarefa)
        if tarefa is None:
            return "Tarefa não encontrada"

        self.tarefas = [t for t in self.tarefas if t["id_tarefa"] != id_tarefa]
        self._escrever_dados()  # salvando alteração no arquivo
        return self.tarefas

    # --------------------------------------------------------------------------------

    # ================ MARK STATUS ================

    def marcar_tarefa_pendente(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 0)

    def marcar_tarefa_em_andamento(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 1)

    def marcar_tarefa_concluida(self, id_tarefa: str) -> dict | str:
        return self._mudar_status(id_tarefa, 2)

    def listar_tarefas(self, status: int | None = None) -> list[dict]:
        """Lista todas as tarefas ou por status específico"""
        if status is None or status >= len(STATUS):
            return self.tarefas
        status_filtro = STATUS[status]
        return [tarefa for tarefa in self.tarefas if tarefa["status"] == status_filtro]


if __name__ == "__main__":
    # Testes rapidos
    tasks = Tasks()

    # Adicionar
    t1 = tasks.adicionar_tarefa("Estudar Python")
    t2 = tasks.adicionar_tarefa("Fazer exercício")

    # Atualizar
    tasks.atualizar_tarefa(t1["id_tarefa"], "Estudar Python 3")

    # Mudar status
    tasks.marcar_tarefa_concluida(t1["id_tarefa"])

    # Deletar
    tasks.deletar_tarefa(t2["id_tarefa"])

    # Listar
    print(tasks.listar_tarefas())  # todas
    print(tasks.listar_tarefas(2))
