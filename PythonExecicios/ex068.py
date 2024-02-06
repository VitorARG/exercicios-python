# Desafio 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
print('=' * 54)
print('Vamos jogar par ou impar!!!')
print('=' * 54)
vitoria = derrota = 0
while True:
    num = int(input('Digite um valor '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou impar? [P/I] ').strip().upper()[0]
    computador = int(randint(0, 10))
    soma = computador + num
    if escolha == 'P':
        if soma % 2 == 0:
            print(f'O computador jogou {computador} o resultado foi {soma} Você Ganhou')
            vitoria += 1
            print('=-' * 27)
        else:
            print(f'O computador jogou {computador} o resultado foi {soma} você perdeu')
            derrota += 1
            print('=-' * 27)
    elif escolha == 'I':
        if soma % 2 == 0:
            print(f'O computador jogou {computador} o resultado foi {soma} Você perdeu')
            derrota += 1
            print('=-' * 27)
        else:
            print(f'O computador jogou {computador} o resultado foi {soma} você Ganhou')
            vitoria += 1
            print('=-' * 27)
    if derrota != 0:
        break
if vitoria == 0:
    print(f'Infelizmete você teve {vitoria} Vitorias')
elif vitoria == 1:
    print(f'Você teve {vitoria} vitoria Parabens.')
else:
    print(f'Você teve {vitoria} vitorias Parabens.')
