nome = input('Digite o seu nome completo:  ').strip().title()
primeiro_nome = nome.split()[0]

if primeiro_nome == nome:
    print(f"Digite um nome completo!")


elif not primeiro_nome == nome:
    if 'Silva' in nome:
        print(f'O nome {nome} possui "Silva"')

    else:
         print(f'O nome {nome} não possui "Silva"')





# Função do split():

# Imagine comigo uma lista, e nessa lista possui um elemento,
# esse elemento é uma "string", e essa "string" é o nome completo de uma pessoa,
# e o split() é a função que vai pegar essa "string" e dividir ela em partes,
# e cada parte vai ser um elemento da lista, então se o nome completo for
# "Vittor Guimarães Rocha" a função split() vai dividir essa "string" em três partes: "Vittor", "Guimarães" e "Rocha",
# e cada parte vai ser um elemento da lista, então a lista vai ficar assim: ["Vittor", "Guimarães", "Rocha"].
# Cada elemento possui um indice, o primeiro elemento tem indice 0, o segundo elemento tem indice 1, e assim por diante.
# Utilizando essa logica é possivel pegar apenas o primeiro nome da pessoa.

# Lógica do if:
# A lógica do if é simples, a variável "primeiro_nome" recebe a função split() e o indice 0,
# então a variável "primeiro_nome" recebe o primeiro elemento da lista, que é o primeiro nome da pessoa.
# Como sabemos a função split() retorna uma lista, e o indice 0 é o primeiro elemento da lista,
# então a lógica por tras é simples, caso a variavel "nome" possua apenas um elemento na lista,
# mostre a mensagem "Digite um nome completo!", a variavel "primeiro_nome" serve apenas para guardar
# a função split() e o indice 0, porque se eu não tiver o primeiro elemento da lista, eu não vou conseguir pegar o primeiro nome da pessoa.

