
print('-' * 30)
print('Loja Super baratão')
print('-' * 30)
soma = maisDmil = maisBarato = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('preço: R$'))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ').strip().upper()[0]
    soma += preco
    if preco >= 1000:
        maisDmil += 1
    if maisBarato <= 0:
        maisBarato = preco
        nomeBarato = produto
    if maisBarato > preco:
        maisBarato = preco
        nomeBarato = produto
    if resposta == 'N':
        break
print(f'O total comprado foi {soma:.2f}')
print(f'Temos {maisDmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa {maisBarato}')