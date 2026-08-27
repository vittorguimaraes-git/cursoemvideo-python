from classes import Pessoa ,Aluno, Professor, Funcionario
from rich import inspect

def main():
    a1 = Aluno("Vittor", 21, "ADS", "Turma T")
    a1.fazer_matricula()
    a1.estudar()
    # inspect(a1, methods=True)

    p1 = Professor("Samuel", 37, "engenharia", "doutorado")
    p1.dar_aula()
    p1.estudar()
    # inspect(p1, methods=True)

    f1 = Funcionario("Claudia", 27, "secretária", "secretaria")
    f1.bater_ponto()
    f1.estudar()
    # inspect(f1, methods=True)


if __name__ == "__main__":
    main()