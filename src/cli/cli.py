import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="task",
        description="Uma ferramenta de linha de comando para gerenciar tarefas.",
        epilog="Use 'task --help' para ver opções específicas."
    )

    parser.add_argument(
        "add",
        type=str,
        help="Adiciona uma nova tarefa."
    )

    args = parser.parse_args()
    print(args)
