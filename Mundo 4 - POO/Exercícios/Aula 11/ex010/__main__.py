from ex010 import Avaliacao
from rich import inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.nota = 10
    inspect(av1, private=True)
    # inspect(av1)
    print(f"{av1.nome} tirou {av1.nota} em {av1.disciplina}")

if __name__ == '__main__':
    main()