# DESAFIO Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
nomeOLd = ''
mediaIdade = 0
idadeOLd = 0
FmenosV = 0
for rg in range(1, 5):
    print('Digite as seguintes informaçoes da {}ª pessoa'.format(rg))
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO. M ou F: ')).upper().strip()
    mediaIdade += idade
    if sexo == 'M' and idade > idadeOLd:
        idadeOLd = idade
        nomeOLd = nome
    if sexo == 'F' and idade < 20:
        FmenosV += 1
print('A media de idade do grupo é {}'.format(mediaIdade/4))
print('O homen mais velho tem {} anos e seu nome é {}'.format(idadeOLd, nomeOLd))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(FmenosV))