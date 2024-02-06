# DESAFIO 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
jogador = dict()
ranking = list()
for c in range(4):
    jogador[f'jogador{c + 1}'] = randint(1, 6)
print('<<< VAlORES SORTEADOS >>>')
for k, v in jogador.items():
    print(f'O {k} Tirou {v} no Dado')
    sleep(0.75)
print('-=' * 30)
print('  == RANKING DO JOGADORES ==')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'  {i+1}° Lugar: {v[0]}  com {v[1]}')
    sleep(0.75)



