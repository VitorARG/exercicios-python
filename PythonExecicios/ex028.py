# Desafio Escreva um programa que faça o computador “pensar” em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
# número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
from random import randint
from time import sleep
numero = randint(0,5)
print('\033[32m-=-' *20)
print('Vou pensar em um numero entre 0 e 5 tente adivinhar')
print('-=-' *20,'\033[m')
n1 = int(input('Que numero eu pensei?' ))
print('Processando...')
sleep(2)
if n1==numero:
    print('\033[33m Parabens\033[m você acertou o numero é {}!'.format(n1))
else:
    print('Você disse \033[31m{}\033[m e o numero foi \033[33m{}\033[m Boa sorte na proxima'.format(n1,numero))
print('Vamos jogar de novo!')
