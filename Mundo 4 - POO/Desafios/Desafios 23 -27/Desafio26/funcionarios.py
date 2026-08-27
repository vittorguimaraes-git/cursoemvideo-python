from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):

    def __init__(self, nome, sal_bruto, salario, sal_min= 1612, inss = 0.075):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = sal_min
        self.inss = inss


    @abstractmethod
    def calcular_salario(self):
        pass


    def analisar_salario(self):

        salario_liquido = self.calcular_salario()
        salarios_min =  salario_liquido / self.sal_min
        analise = Panel(f"O salário de [blue]{self.nome}[/] ([purple]{self.__class__.__name__}[/]) é de [green]R${salario_liquido}[/] e "
                        f"corresponde a [yellow]{salarios_min:.1f} salários mínimos[/].", width= 55, title="Análise de Salário")

        print(analise)



class FuncionarioHorista(Funcionario):

    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome, valor_hora, qtd_horas)

        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas


    def calcular_salario(self):
        salario_bruto = self.valor_hora * self.qtd_horas
        desconto_inss = salario_bruto * self.inss
        salario_liquido = salario_bruto - desconto_inss
        return salario_liquido


class FuncionarioMensalista(Funcionario):

    def __init__(self, nome, salario_bruto):
        super().__init__(nome, salario_bruto, salario_bruto)

        self.salario_bruto = salario_bruto


    def calcular_salario(self):
        desconto_inss = self.salario_bruto * self.inss
        salario_liquido = self.salario_bruto - desconto_inss
        return salario_liquido
