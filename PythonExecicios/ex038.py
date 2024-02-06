# Desafio Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem: O primeiro valor é maior;
# O segundo valor é maior; Não existe valor maior, os dois são iguais
num1 = int(input('Digite o primeiro numero '))
num2 = int(input('Digite o segundo numero '))
if num1 > num2:
    print('Entre {} e {} o primeiro é maior'.format(num1, num2))
elif num2 > num1:
    print('Entre {} e {} o segundo é maior'.format(num1, num2))
else:
    print('Entre {} e {} não existe maior os dos são iguais'.format(num1, num2))
