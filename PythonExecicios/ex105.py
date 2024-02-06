# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de
# alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)
def nota(*n, sit=False):
    """
    A Função nota é uma função para analiasr e avaliar notas de varios alunos
    :param n: um ou mais notas dos alunos (aceita vairos)
    :param sit: valor opcional que serve para mostrar a situação da turma
    :return: retorna dom varias informaçoes sobre a situação da turma
    """
    turma = {}
    media = 0
    turma['total'] = len(n)
    for c in n:
        if len(turma) == 1:
            turma['maior'] = c
            turma['menor'] = c
        else:
            if c > turma['maior']:
                turma['maior'] = c
            if c < turma['menor']:
                turma['menor'] = c
        media += c
    float(media)
    media /= len(n)
    turma['media'] = media
    if sit:
        if media >= 7:
            turma['situação'] = 'Boa'
        elif media < 5:
            turma['situação'] = 'Ruim'
        else:
            turma['situação'] = 'Razoavel'

    return turma


# Progrma principal
rsp = nota(5, 9, 6, 9, 7.2)
print(rsp)
help(nota)