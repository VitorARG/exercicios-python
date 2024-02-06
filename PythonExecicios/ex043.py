# Desafio Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu Índice de Massa Corporal (IMC) e mostre seu status,  de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso Entre 18,5 e 25: Peso Ideal 25 até 30: Sobrepeso
# 30 até 40: Obesidade Acima de 40: Obesidade Mórbida
peso = int(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
ideal = 21.75 * (altura ** 2)
print('Seu imc é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso')
elif imc < 25:
    print('Parabens você esta dentro do seu peso ideal')
elif imc < 30:
    print('Você esta com sobrepeso')
elif imc < 40:
    print('Você esta com obesidade')
else:
    print('Cuidado você esta com obesidade Mórbida')
print('peso ideal {:.0f}'.format(ideal))