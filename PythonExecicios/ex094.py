# 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dado de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas
# B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
cad = dict()
pessoas = list()
media = soma = 0
while True:
    cad['nome'] = str(input('Nome: '))
    while True:
        cad['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if cad['sexo'] in 'MmFf':
            break
        else:
            print('Erro! Por favor digite apenas M ou F')
    cad['idade'] = int(input('Idade: '))
    soma += cad['idade']
    pessoas.append(cad.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] '))
        if resposta in 'SsnN':
            break
        else:
            print('ERRO! Responda apenas S ou N')
    if resposta in 'Nn':
        break
print('-=' * 30)
print(f'A) A todo  foram cadastradas {len(pessoas)} Pessoas. ')
media = float(soma / len(pessoas))
print(f'B) A media de idade é {media:.2f}')
print('C) As mulheres Cadastradas foram', end='')
for m in pessoas:
    if m['sexo'] in 'Ff':
        print(f' {m["nome"]}, ', end='')
print()
print('D) Lista de pessoas que estão acima da Média')
for i, v in enumerate(pessoas):
    if v['idade'] > media:
        print(f'   Nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}  ')
