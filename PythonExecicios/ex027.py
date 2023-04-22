# Desafio faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('digite seu nome completo')).strip()
'''p = int(nome.find(' '))
u = int(nome.rfind(' '))
print('seu primeiro nome é {}'.format(nome[:p]))
print('O seu ultimo nome é{}'.format(nome[u:]))'''
# Resposta professor
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))





