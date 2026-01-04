from classes import Tasks, Json


lista = Tasks()
arquivo = Json("tasks.json")


def salvar_tarefa(task, archive):
    archive.write(task)


lista.adicionar_tarefa("Estudar Python")
arquivo.write(lista.tarefas)
