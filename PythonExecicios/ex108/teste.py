from ex108 import moeda

valor = int(input('Digite um preço R$'))
print(f'a metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))} ')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando {moeda.aumentar(valor)[0]}% de {valor} da {moeda.moeda(moeda.aumentar(valor)[1])}')
print(f'Diminuindo {moeda.diminuir(valor,20)[0]}% de {valor} da {moeda.moeda(moeda.diminuir(valor,20)[1])}')
