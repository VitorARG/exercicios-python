# 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
# tudo em uma lista composta.
from random import randint
from time import sleep
sorteado = list()
jogo = []
num = 0
print('-'*30)
print('     Gerador de jogos     ')
print('     Para a mega sena     ')
print('-'*30)
quantidade = int(input('Quantos jogos você deseja sortear? '))
for c in range(quantidade):
    while True:
        num = randint(1, 61)
        if num not in sorteado:
            sorteado.append(num)
        if len(sorteado) == 6:
            break
    sorteado.sort()
    jogo.append(sorteado[:])
    sorteado.clear()
print('-='*30)
for c in range(len(jogo)):
    print(jogo[c])
    sleep(1)
print('-='*30)
print('Boa sorte em seus jogos')