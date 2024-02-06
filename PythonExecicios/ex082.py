# Desafio 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente. Ao final, mostre o conteúdo das três listas geradas.
valores = []
par = []
impar = []
while True:
    num = int(input('Digite um valor '))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar in 'Nn':
        break
print(f'Você digitou os seguintes numeros {valores}')
print(f'Os valores pares são {par}')
print(f'Os valores impares são {impar}')
