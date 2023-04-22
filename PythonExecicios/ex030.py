# Desafio Criar um progrma que leia um numero inteiro e diga se é par pu impar
num = int(input('Digite um numero'))
if num%2 == 0:
    print('O numero \033[32m{}\033[m é \033[21;32m par \033[m'.format(num))
else:
    print('o numero \033[33m{}\033[m é \033[21;33m impar \033[m'.format(num))
