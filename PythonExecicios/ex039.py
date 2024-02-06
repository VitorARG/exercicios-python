# Desafio Faça um programa que leia o anonas de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Em que anonas você nasceu?'))
al = date.today().year
idade = al - ano
if idade == 18:
    print('Este anonas você completa {} anos Ja é hora de se alistar'.format(idade))
elif idade < 18:
    print('Esse anonas você completa {} anos faltam {} anos para você se alistar'.format(idade, 18 - idade))
    print('Você tera que se alistar em {}'.format(al + (18 - idade)))
else:
    print('Esse anonas você completa {} anos ja passou {} anos da data do seu alistamento'.format(idade, idade - 18))
    print('Seu alistamento foi em {}'.format(al - (idade - 18)))
