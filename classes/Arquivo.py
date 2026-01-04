import json
import os


class Json:
    def __init__(self, file) -> None:
        self.file = file
        if not os.path.exists(file):
            with open(self.file, 'w') as f:
                json.dump([], f)
        else:
            # se existir mas não for lista, corrige
            try:
                with open(self.file, 'r') as f:
                    data = json.load(f)
                if not isinstance(data, list):
                    with open(self.file, 'w') as f:
                        json.dump([], f)
            except json.JSONDecodeError:
                with open(self.file, 'w') as f:
                    json.dump([], f)

    def read(self) -> list:
        try:
            with open(self.file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
        except IOError as e:
            print(f"Erro ao ler o arquivo: {e}")
            return []

    def write(self, data: list) -> None:
        try:
            with open(self.file, 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Erro ao salvar arquivo: {e}")
