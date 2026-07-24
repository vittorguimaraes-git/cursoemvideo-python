def notas(*nota, sit=False):

    """

    funcão para analisar notas e situações de vários alunos.
    :param nota: Nota de aluno
    :param sit: Valor opcional, indicando se deve ou não adicionar a situacao da turma
    :return: dicionário com notas
    
    """

    turma = dict()
    total = 0
    notas_cadastradas = 0
    maior = None
    menor = None




    for n in nota:
        if maior is None or n > maior:
            maior = n

        if menor is None or n < menor:
            menor = n

        total += n
        notas_cadastradas += 1


    media = total / len(nota)

    turma["maior_nota"] = maior
    turma["menor_nota"] = menor
    turma["media"] = media
    turma["notas"] = notas_cadastradas

    if sit:
        if media >= 7:
            turma["situacao"] = "Boa"
        elif 7 < media > 5 :
            turma["situacao"] = "Razoável"

    return turma

escola = notas(10, 10, 6.5, 6.5, sit=True)

print(escola)