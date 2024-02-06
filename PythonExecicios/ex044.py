# Desafio Exercício Python 44: Elabore um programa que calcule o valor a
# ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto, à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal  3x ou mais no cartão: 20% de juros
print('='*10,end='')
print(' Loja do Vitão ', end='')
print('='*10)
preco = float(input('Valor da compra R$'))
print('''Formas de pagamento
[1] A vista dinheiro/cheque
[2] A vista cartão
[3] 2X no cartão
[4] 3x mo cartão''')
opcao = int(input('Escolha sua opção'))
if opcao == 1:
    valor = preco - (preco * 10)/100

elif opcao == 2:
    valor = preco - (preco * 5) / 100
elif opcao == 3:
    valor = preco
    print('Sua compra sera parcelada em 2x de {:.2f} sem juros'.format(preco/2))
elif opcao == 4:
    valor = preco + (preco * 20) / 100
    vezes = int(input('Quantidade de parcelas? '))
    parcela = valor / vezes
    print('sua compra sera parcelada em {}X de {:.2f} Com juros'.format(vezes, parcela))
else:
    valor = preco
    print('Opção invalida por favor tente novamente!')
print('Sua compra de {:.2f} ira custar {:.2f} no final!'.format(preco, valor))
