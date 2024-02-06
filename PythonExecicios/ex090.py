# 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Media do {ficha["nome"]} '))
if ficha['media'] < 5:
    ficha['situação'] = 'Reprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Aprovado'
print('-=' * 30)
for k, v in ficha.items():
    print(f' - {k} é igual a {v}')
