# Desafio 75: desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número ')), int(input('Digite mais um número ')),
       int(input('Digite outro número ')), int(input('Digite o ultimo número ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O numero 3 apareceu primeiro na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não aparece na tupla')
print('Os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
