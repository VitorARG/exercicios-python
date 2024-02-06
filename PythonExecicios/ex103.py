# 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a
# ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(jo='<desconhecido>', num=0):
    print(f'O jogaodr {jo} Fez {num} gol(s) no campeonato')


# programa proncipal
jogador = str(input('Nome do jogador? '))
gol = input('Numero de gols? ')
if gol.isnumeric():
    int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(num=gol)
else:
    ficha(jogador, gol)


# Não gostei dessa resposta tentar fazer de novo depos

