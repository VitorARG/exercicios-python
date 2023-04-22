# Desafio Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
km = float(input('A Quantos Quilômetro por hora você esta? '))
if km > 80:
    print('Você foi  multado em R${:.2f}'.format((km - 80) * 7.00))
print('Tenha um bom dia. Dirija com segurança')

