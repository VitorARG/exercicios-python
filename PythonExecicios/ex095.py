jogador = dict()
time = list()
gol = list()
while True:
    joggol = totgol = 0
    jogador.clear()
    jogador['nome'] = str(input('Nome Do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(partidas):
        joggol = (int(input(f'Quantos gols na partida {c + 1}? ')))
        gol.append(joggol)
        totgol += joggol
    jogador['gols'] = gol[:]
    jogador['total'] = totgol
    gol.clear()
    time.append(jogador.copy())
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta in 'Nn':
        break
print('-=' * 50)
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('_' * 50)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('mostra dado de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'Erro! não existe jogador com codiogo {busca}')
    else:
        print(f'Levatamento do jogador {time[busca]["nome"]}')
        for i, v in enumerate(time[busca]['gols']):
            print(f'No jogo {i + 1} fez {v}')



