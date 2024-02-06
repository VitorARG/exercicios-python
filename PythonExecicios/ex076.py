# Desafio: 076: crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
# na sequência. No final, mostre uma listagem de preços, organizando os dado em forma tabular.
mercado = ('Lapis', 1.75,
           'Borracha', 2.00,
           'Caderno', 15.90,
           'Estojo', 25.00,
           'Tranferidor', 4.20,
           'Compaso', 9.99,
           'Mochilha', 120.32,
           'Canetas', 22.30,
           'livro', 34.90)
print('--' * 20)
print(f'{"Listagem de preços":^40}')
print('--' * 20)
for i in mercado:
    if isinstance(i, str):
        print(f'{i:.<30}', end='')
    else:
        print(f'R${i:>7.2f}')
print('--' * 20)
