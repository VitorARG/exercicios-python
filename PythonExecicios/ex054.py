# DESAFIO Crie um programa que leia o anonas de nascimento de sete pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
menores = 0
maiores = 0
data = date.today().year
for c in range(1,8):
    ano = int(input('Digite o anonas que a {}° nasceu '.format(c)))
    idade = data - ano
    if idade < 18:
        menores += 1
    else:
        maiores += 1
print('Dos 7 anos de nascimento digitado \n temos {} que correspondem a pessoas maiores de idade \n'
      ' E {} que correspondem a menores de idade'.format(maiores, menores))
