# DESAFIO Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorPeso = 0
menorPeso = 0
for pe in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pe)))
    if pe == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso lido foi {}Kg'.format(maiorPeso))
print('o menor peso lido foi {}Kg'.format(menorPeso))