# Desafio Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.
c1 = '\033[m'
c2 = '\033[32m'
c3 = '\033[31m'
c4 = '\033[34m'
print('\033[33m-=' * 15)
print('Analisador de triangulo')
print('-=' * 15,'\033[m')
seg1 = float(input('{}Primeiro{} seguimento'.format(c2,c1)))
seg2 = float(input('{}Segundo{} seguimento'.format(c3,c1)))
seg3 = float(input('{}Terceiro{} seguimento'.format(c4,c1)))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 +seg2:
   print('Os Seguimentos digitados podem formar triangulo ')
else:
    print('Os segumentos não podem formar tiangulo')





