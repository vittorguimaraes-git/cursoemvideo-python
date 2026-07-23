frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
frase_sem_espacos = ''.join(palavras)
palindromo = ''

for letra in range(len(frase_sem_espacos) - 1, -1, -1):
    palindromo += frase_sem_espacos[letra]

if frase_sem_espacos == palindromo:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo')