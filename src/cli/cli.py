import argparse
from core import Tasks


def main():
    parser = argparse.ArgumentParser(
        prog="task",
        description="Uma ferramenta de linha de comando para gerenciar tarefas.",
        epilog="Use 'task <comando> --help' para ver opções específicas."
    )

    subparsers = parser.add_subparsers(
        dest="comando",
        required=True,
        title="Comandos disponíveis",
        metavar="<comando>"
    )

    # ADD ==========================================================
    add_parser = subparsers.add_parser(
        "add",
        help="Adicionar uma nova tarefa"
    )
    add_parser.add_argument(
        "tarefa",
        type=str,
        help="Descrição da tarefa a ser adicionada"
    )

    # UPDATE =======================================================
    update_parser = subparsers.add_parser(
        "update",
        help="Atualizar uma tarefa existente"
    )
    update_parser.add_argument(
        "id_tarefa",
        type=int,
        help="Id da tarefa para atualizar"
    )
    update_parser.add_argument(
        "atualizacao",
        type=str,
        help="Nova descrição da tarefa"
    )

    # DELETE =======================================================
    delete_parser = subparsers.add_parser(
        "delete",
        help="Excluir uma tarefa."
    )
    delete_parser.add_argument(
        "id_tarefa",
        type=int,
        help="Id da tarefa a ser excluída."
    )

    # LIST TASKS ===================================================
    list_parser = subparsers.add_parser(
        "list",
        help="Listar tarefas."
    )
    status_group = list_parser.add_argument_group(
        title="Filtros de status (opcional)"
    )
    status_group.add_argument(
        "--done",
        action="store_const",
        const="done",
        dest="status",
        help="Filtrar tarefas concluídas"
    )
    status_group.add_argument(
        "--todo",
        action="store_const",
        const="todo",
        dest="status",
        help="Filtrar tarefas pendentes"
    )
    status_group.add_argument(
        "--in-progress",
        action="store_const",
        const="in_progress",
        dest="status",
        help="Filtrar tarefas em andamento"
    )
    # MARK TASK ====================================================
    mark_parser = subparsers.add_parser(
        "mark",
        help="Marcar tarefa com um status"
    )
    mark_parser.add_argument(
        "id_tarefa",
        type=int,
        help="Id da tarefa."
    )
    mark_group = mark_parser.add_mutually_exclusive_group(required=True)
    mark_group.add_argument(
        "--done",
        action="store_const",
        const="done",
        dest="status",
        help="Marcar como concluída"
    )
    mark_group.add_argument(
        "--in-progress",
        action="store_const",
        const="in_progress",
        dest="status",
        help="Marcar como em andamento"
    )
    mark_group.add_argument(
        "--todo",
        action="store_const",
        const="todo",
        dest="status",
        help="Marcar como pendente"
    )

    args = parser.parse_args()

    if args.comando == "add":
        print(f"Tarefa adicionada: {args.tarefa}")

    elif args.comando == "update":
        print(f"Atualizando {args.id_tarefa}: {args.atualizacao}")

    elif args.comando == "delete":
        print(f"Deletando tarefa {args.id_tarefa}")

    elif args.comando == "list":
        if args.status:
            print(f"Listando tarefas com status {args.status}")
        else:
            print("Listando todas as tarefas")

    elif args.comando == "mark":
        print(f"Marcando tarefa {args.id_tarefa} como {args.status}")

    else:
        print("Não existe esse comando")


if __name__ == "__main__":
    main()
