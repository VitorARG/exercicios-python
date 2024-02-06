# 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a
# soma entre todos os valores pares sorteados pela função anterior.
from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 numeros ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.4)
    print('Pronto')


def somapar(num):
    soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
    print(f'somando os valores pares de {num} temos {soma}')


# programa principal
numeros = list()
sorteia(numeros)
somapar(numeros)
