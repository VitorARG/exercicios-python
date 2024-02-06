# 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
# números como um valor monetário formatado.
from ex109 import moeda

valor = int(input('Digite um preço R$'))
print(f'a metade de {moeda.moeda(valor)} é {moeda.metade(valor, fo=True)} ')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor,fo=True)}')
print(f'Aumentando 10% de {valor} da {moeda.aumentar(valor,fo=True)}')
print(f'Diminuindo 20% de {valor} da {moeda.diminuir(valor,20, fo=True)}')
