from  aluno import Aluno
from professor import Professor
from funcionario import Funcionario

a1 = Aluno("Vittor", 21, "ADS", "Turma T")
a1.fazer_matricula()
# inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Engenharia", "Doutorado")
p1.dar_aula()
# inspect(p1, methods=True)

f1 = Funcionario("Claudia", 27, "Secretária", "Secretaria")
f1.bater_ponto()
# inspect(f1, methods=True)