#  Desafio 89: Crie um programa que leia nome e duas notas de vários alunos e guarde
#  tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e
#  permita que o usuário possa mostrar as notas de cada aluno individualmente.
temp = list()
final = list()
while True:
    temp.append(input('NOME: '))
    temp.append(float(input('NOTA 1: ')))
    temp.append(float(input('NOTA 2: ')))
    final.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-'*20)
print('n°   Nome     Nota')
print('-'*20)
for c, z in enumerate(final):
    media = (z[1] + z[2]) / 2
    print(f'{c:2} {z[0]:^10} {media:^4.1f}')
print('-'*30)
while True:
    print('999 para parar')
    mostrar = int(input('Mostrar notas de qual aluno? N°'))
    if mostrar == 999:
        break
    print(f'Notas de {final[mostrar][0]} foram {final[mostrar][1]} e {final[mostrar][2]} ')
    print('-'*30)
print('Obrigado volte sempre')


# RESPOSTA PROFESSOR
ficha = list()
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2 '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'{"NO":<4}{"NOME":^10}{"Media":>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<< VOLTE SEMPRE >>>>')





