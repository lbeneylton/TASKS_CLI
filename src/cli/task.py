import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="task",
        description="Uma ferramenta de linha de comando para "
                    "gerenciar tarefas."

    )
    return parser


if __name__ == "__main__":
    parser = main()
    parser.print_help()
