# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
fra = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(fra)
inverso = ''
for pa in range(len(junto) - 1, - 1, -1):
    inverso += junto[pa]
print('{} alcontrario fica {}'.format(junto, inverso))
if junto == inverso:
    print('Portanto é um palindromo')
else:
    print('Portanto não é um palindromo')
