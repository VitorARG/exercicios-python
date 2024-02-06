# Desafio 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro
# de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados.
# c) Times em ordem alfabética. d) Em que posição está o time da Vasco.
clubes = ('botafogo', 'palmeiras', 'Flamengo', 'Fluminese',
          'gremio', 'Athletico-PR', 'Bragantino', 'Fortaleza',
          'Cuiaba', 'São paulo', 'Atletico-MG', 'Cruzeiro',
          'Corintias ', 'Internacinal', 'goias', 'Baia',
          'santos', 'Vasco', 'Coritiba', 'america-MG')
print(f'Lista de times: \n{clubes}')
print('-=' * 30)
print(f'Os 5 primeiros colocacdos do brasileirão são: \n{clubes[0:5]}')
print('-=' * 30)
print(f'Os ultimos 4 colocados são: \n{clubes[-4:]}')
print('-=' * 30)
print(f'Lista de times em ordem alfabetica: \n{sorted(clubes)}')
print('-=' * 30)
print(f'o vasco esta na posição: {clubes.index("Vasco")+1}')

