def vota(ano):
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano

    if idade < 16:
        return f"Com {idade } anos: NÃO VOTA"

    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL"

    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"



nascimento = int(input("Digite o ano de nascimento: "))
print("-"*35)
print(vota(nascimento))
print("-"*35)
