from ex107 import moeda

valor = int(input('Digite um preço R$'))
metade = moeda.metade(valor)
dobro = moeda.dobro(valor)
almentar = moeda.aumentar(valor)
print(f'a metade de {valor} é {metade:.2f} ')
print(f'O dobro de {valor} é {dobro}')
print(f'Aumentando {almentar[0]}% de {valor} da {almentar[1]:.2f}')