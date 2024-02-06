# Exercício Python 079: crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
num = []

while True:
    n = (int(input('Digite um valor ')))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso?  ')
    else:
        print('Valor diplicado não vou adicionar')
    continuar = str(input('Quer continuar? [S/N]  ')).upper()
    if continuar in 'Nn':
        break
num.sort()
print(num)
