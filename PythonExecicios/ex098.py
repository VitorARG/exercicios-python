# 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1  b) de 10 até 0, de 2 em 2  c) uma contagem personalizada
from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if f < i and p > 0:
        p = -p
    if f < 0:
        f += -2
    for c in range(i, f + 1, p):
        print(c, end=' ')
        sleep(0.75)
    print('Fim')
    print('-=' * 20)


contador(1, 10, 1)
contador(10, 0, -2)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)

# não funciona quando inicio e pas sõa negativos ao mesmo tempo resolva
