import argparse


def main():
    parser = argparse.ArgumentParser(description="Exemplo de CLI com argparse")
    parser.add_argument("nome", help="Seu nome")
    parser.add_argument("-i", "--idade", type=int, help="Sua idade", default=0)
    parser.add_argument("-v", "--verbose",
                        action="store_true", help="Modo verboso")

    args = parser.parse_args()

    if args.verbose:
        print(f"Olá {args.nome}, você tem {args.idade} anos.")
    else:
        print(f"Olá {args.nome}!")


if __name__ == "__main__":
    main()
