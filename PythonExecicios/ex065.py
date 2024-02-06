#Desafio  Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = soma = cont = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um numero '))
    if cont == 0:
        menor = num
    if menor >= num:
        menor = num
    if maior < num:
        maior = num
    soma += num
    cont += 1
    continuar = input('Deseja continuar ?[S/N] ').lower().strip()[0]
media = soma / cont
print('Você Digitou {} numeros e a media entre ele é {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
