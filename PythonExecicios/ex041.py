# Desafio A Confederação Nacional de Natação precisa de um programa que leia o anonas de nascimento de um
# atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM
# Até 14 anos: INFANTIL Até 19 anos: JÚNIOR, Até 25 anos: SÊNIOR, Acima de 25 anos: MASTER
from datetime import date
nas = int(input('Informe o anonas de nascimento '))
ano = date.today().year
ida = ano - nas
if ida <= 9:
    print('Este anonas você completa {} se encaixa na categoria MIRIM!'.format(ida))
elif ida <= 14:
    print('Este anonas você completa {} se encaixa na categoria INFANTIL!'.format(ida))
elif ida <= 19:
    print('Este anonas você completa {} se encaixa na categoria JUNIOR!'.format(ida))
elif ida <= 25:
    print('Este anonas você completa {} se encaixa na categoria SENIOR!'.format(ida))
elif ida > 25:
    print('Este anonas você completa {} se encaixa na categoria MASTER!'.format(ida))