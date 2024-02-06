# 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.  Aula Anterior
from time import sleep


def maior(* num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    maiornum = 0
    for c in num:
        print(c, end=' ')
        sleep(0.5)
        if maiornum == 0:
            maiornum = c
        if c > maiornum:
            maiornum = c
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maiornum}')


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()
