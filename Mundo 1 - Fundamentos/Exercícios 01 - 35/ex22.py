name = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome em maiúsculas é: "{name.upper()}"')
print(f'Seu nome em minúsculas é: "{name.lower()}"')
print(f'Seu nome possui "{len(name.strip())}" letras ')
print(f'Seu primeiro nome possui "{len(name.split()[0])}" letras')

