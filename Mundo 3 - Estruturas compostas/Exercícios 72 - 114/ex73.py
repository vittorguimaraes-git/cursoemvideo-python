tabela = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo", "Atlético-MG", "Athletico-PR", "Cruzeiro",
         "Botafogo", "Santos", "Bahia", "Fluminense", "Corinthians", "Chapecoense", "Ceará", "Vasco", "América-MG",
         "Sport", "Vitória", "Paraná")

print(f'Lista de Times:\n \n {tabela}')
print()
print(f'Os cinco primeiros:\n \n {tabela[:5]} ')
print()
print(f'Os quatro últimos:\n \n {tabela[-5:]} ')
print()
print(f'A {tabela[13]} está na posição 13')
print()
print(f'Times em ordem alfabética:')


print("-"*30)
for times in tabela:
    print(f'{times}')

print("-"*30)



