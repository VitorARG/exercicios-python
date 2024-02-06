# Desafio 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
# de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
numeros = ('zero', 'um', 'dois', 'tres', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezessete', 'dezoito',
           'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20 '))
    if 0 <= num <= 20:
        print(f'Você digitou o numero {numeros[num]}')
        continuar = (input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            break
    else:
        print('Numero invalido tente novamente')
print('Programa finalizado')
