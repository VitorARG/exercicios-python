#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o seu sexo [M/F] ')).upper().strip()
while not sexo == 'M' and not sexo == 'F':
    print('Sexo invalido tente novamente')
    sexo = str(input('Digite o seu sexo [M/F] '))
if sexo == 'M':
    sexo = 'MASCULINO'
else:
    sexo = 'FEMININO'
print('Sexo {} Cadatrado com sucesso '.format(sexo))
