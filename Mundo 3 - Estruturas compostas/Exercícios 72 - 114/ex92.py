from datetime import datetime

ano_atual = datetime.now().year
dicionario = dict()

dicionario['Nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dicionario['Idade'] = ano_atual - nascimento
dicionario['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 se não tiver): '))

if dicionario['Carteira de Trabalho'] > 0:

    dicionario['Salário'] = float(input('Salário: '))
    dicionario['Contratação'] = int(input('Ano de contratação: '))
    dicionario['Aposentadoria'] = (dicionario['Contratação'] + 35) - nascimento

    print()
    print('-'*40)
    print()
    print(f'Nome: {dicionario["Nome"]}')
    print(f'Idade: {dicionario["Idade"]}')
    print(f"Salário: {dicionario['Salário']}")
    print(f"Ano de contratação: {dicionario['Contratação']}")
    print(f"Número da Carteira de Trabalho: {dicionario['Carteira de Trabalho']}")
    print(f"{dicionario['Nome']} vai se aposentar com {dicionario['Aposentadoria']} anos.")
    print()
    print('-'*40)
else:
    print(f"{dicionario['Nome']} não possui carteira de trabalho registrada.")




