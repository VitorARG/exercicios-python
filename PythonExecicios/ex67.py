# Desafio  67: Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('=' * 50)
print('Gerador de tabuada')
print('=' * 50)
while True:
    num = int(input('Deseja ver a tabuada de qual valor? '))
    print('-' * 20)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{cont:2} X {num} = {cont * num}')
print('Fim')
