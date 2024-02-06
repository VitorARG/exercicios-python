# 092: Crie um programa que leia nome, anonas de nascimento e carteira de trabalho e cadastre-o (com idade)
# em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também
# o anonas de contratação e o salário. Calcule e acrescente, além da idade, com quantos
# anos a pessoa vai se aposentar.
from datetime import datetime
dados = dict()
dados['nome'] = str(input('NOME: '))
nas = int(input('Ano De Nascimento '))
anoAt = datetime.now().year
dados['idade'] = (anoAt - nas)
dados['CTPS'] = int(input('Carteira de trabalho (0 Não tem) '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de contratação '))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = 35 - (anoAt - dados['contratação']) + dados['idade']
print('-=' * 30)
for k, v in dados.items():
    print(f' - {k} Tem o valor {v}')

