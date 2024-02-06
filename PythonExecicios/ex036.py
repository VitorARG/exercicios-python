# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor do imovel: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos pretende parcelar o imovel? '))
parcela = casa / (anos * 12)
if parcela > (salario * 30) / 100:
    print('Emprestimo\033[31m NEGADO! \033[m')
else:
    print('Emprestimo\033[32m APROVADO! \033[m')
print(' Valor da parcela {:.2f} \n messes finaciados {} '.format(parcela,anos * 12))



