#Desafio Escreva um programa que leia um número N inteiro qualquer e mostre na
# tela os N primeiros elementos de uma Sequência de Fibonacci.
termo = int(input('Quantos termos você quer ver? '))
contador = 3
t1 = 0
t2 = 1
print('{} → {}'.format(t1,t2), end=' → ')
while contador <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    contador += 1
    print(t3, end=' → ')
print('Fim')