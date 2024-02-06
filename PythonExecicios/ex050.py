# esenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for rep in range(0,6):
    num = int(input('Digite um numero '))
    if num % 2 == 0:
        soma = soma + num
        cont += 1
print('Você informou {} numeros PARES e a soma deles foi {}'.format(cont, soma))