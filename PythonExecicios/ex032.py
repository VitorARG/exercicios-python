# Desafio Faça um programa que leia um ano qualquer e diga se ele é bissexto
from datetime import date
ano = int(input('Que ano você deseja analisar? Se deseja analisar o ano atual insira o digto 0 '))
c1 = '\033[32m'
c2 = '\033[m'
c3 = '\033[31m'
if ano == 0:
   ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{}{}{} É um ano {}bissexto{}'.format(c1,ano,c2,c1,c2))
else:
    print('{}{}{} Não é {}bissexto{}'.format(c3,ano,c2,c3,c2))