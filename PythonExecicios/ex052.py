# Desafio Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero para saber se ele é primo '))
total = 0
for cont in range(1, num + 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(cont, end=' ')
print('\n\033[m O numero {} foi dividido {} vezes'.format(cont, total))
if total == 2:
    print('Logo Ele é um numero primo')
else:
    print('Logo ele não é um numero primo')