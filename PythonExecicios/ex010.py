#Desafio ler o quanto de dinheiro o usuario tem na carteira e
# mostrar quantos dolares ele pode comprar considerando us$1.00 = 3,27 (sdds kk)
rs = float(input('Quanto dinheiro você tem na carteira? R$'))
print('com R${:.2f} você comsegue comprar US${:.2f} '.format(rs,(rs/3.27)))

