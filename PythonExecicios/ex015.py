# Desafio escrever um programa de aluguel de carro que pergunte a quantidade
# de dias que ele foi alugado e quantos km pecorridos e diga o valor a pagar
# considerando R$60 por dia e R$0.15 por km
dia = int(input('Quantos dias alugados?'))
km = float(input('quantos km rodados?'))
preco = (dia * 60) + (km * 0.15)
print('O Veiculo foi alugado por {} dias e percorreu {}Km o valor a '
      'pagar é de R${:.2f}!'.format(dia,km,preco))

