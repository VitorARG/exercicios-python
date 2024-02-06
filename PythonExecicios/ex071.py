# DEsafio 71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
ced50 = ced20 = ced10 = ced1 = 0
valor = int(input('Qual é o valor você deseja sacar? R$'))
while True:
    if valor >= 50:
        valor -= 50
        ced50 += 1
    else:
        if valor >= 20:
            valor -= 20
            ced20 += 1
        else:
            if valor >= 10:
                valor -= 10
                ced10 += 1
            else:
                if valor < 10:
                    valor -= 1
                    ced1 += 1
    if valor == 0:
        break
print(f'Total de {ced50} cedulas de 50\nTotal de {ced20} cedulas de 20 ')
print(f'Total de {ced10} cedulas de 10\nTotal de {ced1} cedulas de 1 ')
