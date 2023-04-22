# Desafio Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.
km = float(input('Qual é a distancia da sua viagem em km '))
if km <=200:
    print('Sua passagem foi cobrada \033[32mR$ 0.50 \033[m por km e saiu por \033[32m R${:.2f} \033[m'.format(km*0.5))
else:
    print('Sua passagem foi cobrada \033[32m R$0.45 \033[m por km e saiu por \033[32m R${:.2f} \033[m'.format(km*0.45))
print('--fim--')
