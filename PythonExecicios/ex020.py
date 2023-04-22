# Desafio sortear de uma listade nome uma ordem aleatoria
from random import shuffle
n1 = input('primeiro aluno')
n2 = input('segundo aluno')
n3 = input('terceiro aluno')
n4 = input('terceiro aluno')
lista = [n1, n2, n3, n4]
#random.shuffle(x) Embaralha a sequência x internamente
shuffle(lista)
print('a lista é')
print(lista)

