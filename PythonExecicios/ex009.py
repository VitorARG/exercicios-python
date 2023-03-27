# desafio 9 tabuada leia um numero qualque e faça uma tabuada
n = int(input('digite um numero'))
n1 = n*1
n2 = n*2
n3 = n*3
n4 = n*4
n5 = n*5
n6 = n*6
n7 = n*7
n8 = n*8
n9 = n*9
n10 = n*10
print('{:=>10} tabuada de {} {:=<10}'.format('',n,''))
print('{} x 1 = {}'.format(n,n1), end=' ')
print('{:>15} x 2 = {}'.format(n,n2))
print('{} x 3 = {}'.format(n,n3), end=' ')
print('{:>15} x 4 = {}'.format(n,n4))
print('{} x 5 = {}'.format(n,n5), end=' ')
print('{:>15} x 6 = {}'.format(n,n6))
print('{} x 7 = {}'.format(n,n7), end=' ')
print('{:>15} x 8 = {}'.format(n,n8))
print('{} x 9 = {}'.format(n,n9), end=' ')
print('{:>15} x 10 = {}'.format(n,n10))

#Resposta professor
num = int(input('Digite um numero para ver sua tabuada'))
print('-' * 12)
print('{} x {:2} = {}'.format(num,1,num*1))
print('{} x {:2} = {}'.format(num,2,num*2))
print('{} x {:2} = {}'.format(num,3,num*3))
print('{} x {:2} = {}'.format(num,4,num*4))
print('{} x {:2} = {}'.format(num,5,num*5))
print('{} x {:2} = {}'.format(num,6,num*6))
print('{} x {:2} = {}'.format(num,7,num*7))
print('{} x {:2} = {}'.format(num,8,num*8))
print('{} x {:2} = {}'.format(num,9,num*9))
print('{} x {:2} = {}'.format(num,10,num*10))
print('-'* 12)