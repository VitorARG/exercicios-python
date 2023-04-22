# Desafio  Crie um programa que leia o nome de uma pessoa e
# diga se ela tem “SILVA” no nome
nome = str(input('Qual é o seu nome completo')).strip()
#print('Seu nome tem silva? {}'.format(nome.lower().count('silva') >= 1))
print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
