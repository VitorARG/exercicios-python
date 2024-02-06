# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.
'''from random import randint
numero = randint(0, 10)
print('\033[34m-*-' * 20)
print('Vou pensar em um numero entre 0 e 10 tente adivinhar')
print('-*-' * 20, '\033[m')
n1 = int(input('Que numero eu pensei? '))
tentativas = 1
while n1 != numero:
    tentativas += 1
    if n1 > numero:
        print('\033[31mMenos\033[m. tente novamente ')
        n1 = int(input('Que numero eu pensei? '))
    else:
        print('\033[33mMais\033[m. tente novamente')
        n1 = int(input('Que numero eu pensei? '))
print('\033[32mParabens\033[m você acertou em {} Tetativas o numero é {}'.format(tentativas, numero))'''
from random import randint
numero = randint(0, 10)
print('\033[34m-*-' * 20)
print('Vou pensar em um numero entre 0 e 10 tente adivinhar')
print('-*-' * 20, '\033[m')
tentativas = 0
acertou = False
while not acertou:
    jogador = int(input('Que numero eu estou pensando? '))
    tentativas +=1
    if jogador == numero:
        acertou = True
    else:
        if jogador > numero:
            print('menos... Tente novamente ')
        else:
            print('Mais... Tente novamente ')
print('Parabens você acertou com {} tentativas '.format(tentativas))
