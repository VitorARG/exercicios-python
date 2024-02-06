# Desafio Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from  time import sleep
opcoes = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input('''escolha uma opção
[0] Pedra
[1] Papel
[2] Tesoura
Sua opção? '''))
maquina = randint(0, 2)
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('Poo!!')
sleep(1)
print('=' * 25)
print('jogador jogou {}'.format(opcoes[jogador]))
print('Computador jogou {}'.format(opcoes[maquina]))
print('=' * 25)
'''if jogador == maquina:
    print('EMPATOU')
elif jogador == 1 and jogador != 2:
    print('Você ganhou')
elif jogador == 2 and jogador != 3:
    print('Você Venceu')
elif jogador == 3 and jogador != 1:
    print('Você Venceu')
else:
    print('Você perdeu')'''
# Resposta professor
if maquina == 0:
    if jogador == 0:
        print('Empatou')
    elif jogador == 1:
        print('Você Venceu')
    elif jogador == 2:
        print('Você perdeu')
elif maquina == 1:
    if jogador == 0:
        print('Você Perdeu')
    elif jogador == 1:
        print('Empatou')
    elif jogador == 2 :
        print('Você venceu')
elif maquina == 2:
    if jogador == 0:
        print('Você Venceu')
    elif jogador == 1:
        print('Você perdeu')
    elif jogador == 2:
        print('Empatou')
