import datetime

sexo = input("Qual seu sexo? [M/F] ").upper().strip()

if sexo == "F":
    print("Serviço Militar obrigatório somente apenas para pessoas do sexo M.")

elif sexo == "M":
    nascimento = int(input("Digite o seu ano de nascimento: "))
    print()

    ano = datetime.date.today().year
    idade = ano - nascimento
    anos_em_atraso = idade - 18
    anos_para_alistar = 18 - idade

    if idade == 18:
        print("Você já pode realizar seu processo de alistamento.")

    elif idade < 18:
        print("Idade insuficiente")
        print(f"Seu alistamento sera em: {ano + anos_para_alistar} ")

    elif idade > 18:
        print("Você deve realizar seu processo de alistamento o mais rápido possível na junta militar mais próxima.")
        print(f"Anos em atraso: {anos_em_atraso}")
        print(f"Você deveria ter se alistado em: {ano - anos_em_atraso}")

else:
    print("ERRO: Digite um opção válida.")



