# Desafio FaÇa um programa que leia o preço de um produto e mostre
# o novo preço com 5% de desnconto
preco = float(input('Informe o preço do produto R$'))
print('O produto de valor R${:.2f}  com 5% de desconta saira por '
      'um total de {:.2f}'.format(preco,preco*0.95))


