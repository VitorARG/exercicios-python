# sDesafio Separa quantas Unidades dezenas centenas e milhar tem um nume entre 0 9999
numero = int(input('Digite seu numero'))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analisando o numero {}'.format(numero))
print('unidade:{}'.format(u))
print('Dezenas:{}'.format(d))
print('centenas:{}'.format(c))
print('Milhar:{}'.format(m))
