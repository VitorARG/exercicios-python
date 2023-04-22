# Desafio criar um programa que leia o nome de uma pessoa e mostre
# todas as letras maiuculas e todas minusculas o quantas letras tem e quantas letras tem o primeiro nome
nome = input('Escreva seu nome completo').strip()
print('O seu nome em maiuculo é',nome.upper())
print('o seu nome em minusculo é',nome.lower())
print('O seu nome tem ao todo {} letras'.format(len(nome.replace(' ',''))))
dividido = nome.split()
print('O Seu primeiro nome é {} e ele tem {} Letras'.format(dividido[0],len(dividido[0])))
