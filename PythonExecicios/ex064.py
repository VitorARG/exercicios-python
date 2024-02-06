# Desafio Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
# o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag).
print('Digite 999 para parara ')
numero = cont = soma = 0
numero = int(input('Digite um numero para somar '))
while numero != 999:
    soma += numero
    cont += 1
    numero = int(input('Digite um numero para somar '))
print('Você digitou {} numeros e a soma deles é {}'.format(cont, soma))
