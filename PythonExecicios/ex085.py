# Desafio 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
# lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e
# ímpares em ordem crescente.
lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}ª numero '))
    if num % 2 == 0:
        lista[0].append(num)
        lista[0].sort()
    else:
        lista[1].append(num)
        lista[1].sort()
print(lista)
print(f'A lista dos pares é {lista[0]}')
print(f'A lista dos impares é {lista[1]}')