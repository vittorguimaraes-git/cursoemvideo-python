cidade = input('Digite o nome de uma cidade: ').strip().title()
if cidade.startswith('Santo'):
    print(f'A cidade {cidade} começa com "Santo"')
else:
    print(f'A cidade {cidade} não começa com "Santo"')