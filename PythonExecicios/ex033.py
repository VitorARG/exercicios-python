# Desafio Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('primeiro numero'))
n2 = int(input('segundo numero'))
n3 = int(input('terceiro numero'))
# testando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# testando o maior
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n2 and n3 > n1:
    maior = n3
print('\033[42m O maior é \033[31m{}!\033[m \n\033[42m O menor é \033[31m{}!\033[m '.format(maior,menor))



