#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
numero = int(input('Digite um numero para ver seu fatorial '))
fatorial = numero
c = 1
print('calculando {}!'.format(numero),end=' ')
while fatorial > 0:
    print('{}'.format(fatorial),end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    c *= fatorial
    fatorial -= 1
    numero = numero * fatorial
print(c)