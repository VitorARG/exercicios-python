# Desafio fazer um programa que leia um lista de nomes e escolha um nome aleatoriamente
from random import choice
nom1 = input('Primeiro auluno')
nom2 = input('segundo aluno')
nom3 = input('Terceiro aluno')
nom4 = input('quarto aluno')
# lista = []
escolido = choice([nom1, nom2, nom3, nom4])
print(escolido)



