# Desafio Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida: Média abaixo de 5.0: REPROVADO,
# Média entre 5.0 e 6.9: RECUPERAÇÃO, Média 7.0 ou superior: APROVADO
not1 = float(input('Digite a primeira nota '))
not2 = float(input('Digite a segunda nota '))
media = (not1 + not2) / 2
if media < 5.0:
    print('A media entre as notas {} e {} é {:.1f}'.format(not1, not2, media))
    print('O Aluno esta\033[31m REPROVADO! \033[m')
elif media > 6.9:
    print('A media entre as notas {} e {} é {:.1f}!'.format(not1, not2, media))
    print('O aluno esta\033[32m APROVADO! \033[m')
else:
    print('A media entre as notas {} e {} é {:.1f}!'.format(not1, not2, media))
    print('O Aluno esta \033[33m EM RECUPERAÇÃO! \033[m ')

