# Desafio  Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salario do funcionario? R$'))
if salario > 1250.00:
   aumento = (salario * 10) / 100
else:
   aumento = (salario * 15) / 100
print('Quem ganhava \033[32mR$ {:.2f} \033[m passa a ganhar \033[32m R$ {:.2f} \033[m'.format(salario, salario + aumento))