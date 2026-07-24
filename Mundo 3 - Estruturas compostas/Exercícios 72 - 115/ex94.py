pessoas = list()
dados = dict()
mulheres = list()
acima_media = list()


total_cadastro = 0
idade_grupo = 0


print("Cadastro de pessoas".center(50, "-"))
print()


while True:
    dados['nome'] = input('Nome: ').capitalize()
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = input('Sexo: ').upper()
    print()

    total_cadastro += 1
    idade_grupo += dados['idade']
    media_idade = idade_grupo / total_cadastro

    pessoas.append(dados.copy())
    continuar = input('Continuar? [S/N]').strip().upper()[0]
    print()
    print("-"*50)

    if continuar == "N":
        print()
        break


for pessoa in pessoas:
    if pessoa['sexo'] == "F":
        mulheres.append(pessoa['nome'])

    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa.copy())




print('Grupos de cadastro'.center(50))
print('-'*50)
print()

print(f"Total de pessoas cadastradas: {total_cadastro}")
print(f"Média de idade do grupo: {media_idade} anos")
print(f"Grupo feminino: {mulheres}")
print()
print("Grupo acima da média de idade:")
print("-"*50)
print()

for pessoa in acima_media:
    print(f"Nome: {pessoa['nome']} - Idade: {pessoa['idade']} - Sexo: {pessoa['sexo']}")











