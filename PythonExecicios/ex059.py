#Exercício Python 059: Crie um programa que leia dois valores e mostre um lib na tela:
#[ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = int(input('Primeiro valor '))
num2 = int(input('Segundo valor '))
comando = 0
while not comando == 5:
    print('=' * 20)
    print('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa')
    comando = int(input('Digite sua escolha '))
    print('=' * 20)
    if comando == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, (num1 + num2)))
    elif comando == 2:
        print('A multipliceção de {} e {} é {}'.format(num1, num2, (num1 * num2)))
    elif comando == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} tem o maior valor o numero {}'.format(num1, num2, maior))
    elif comando == 4:
        num1 = int(input('Primeiro valor '))
        num2 = int(input('Segundo Valor '))
    elif comando == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. tente novamente')
    sleep(2)
print('Programa finalizado')