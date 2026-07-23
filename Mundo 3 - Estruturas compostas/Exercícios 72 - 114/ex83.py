pilha = []
valida = True

expressao = str(input('Digite uma expressão: '))


for simbolo in expressao:

    if simbolo == '(':
        pilha.append('(')

    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()

        else:
            valida = False
            break






if len(pilha) == 0 and valida:
    print('Sua expressão é valida')



else:
    print('Sua expressão é inválida!')






