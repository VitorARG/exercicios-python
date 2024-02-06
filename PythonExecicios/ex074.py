# Desafio 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# meu apos ver o video
'''from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
print(num)
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor digitado foi {min(num)}')'''
# comentario bem parecido com a minha tentativa antrior mas com algumas falhas
'''from random import randint
l = ''
ma = me = 0
for c in range(0,5):
    r = (randint(0, 1000))
    l = l + str(r) + ' '
    if c == 0:
        ma = me = r
    else:
        if r > ma:
            ma = r
        if r < me:
            me = r
lista = l.split()
print(lista)
print(f'O maior valor é {ma} e o menor é {me}.')'''
# comentario corrigindo os erros de cima
'''from random import randint
tupla = ()
for c in range(5):
    n = randint(1, 9)
    tupla += n,
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')'''
# melhor resolução mas com dua falhas uma não podendo repitir
# numeros na tupça e outra que não realmente ta usando uma tupla mas sim uma lista
from random import sample , randint
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
print('-=' * 10)
# resposta chat gpt
random_numbers = tuple(randint(1, 10) for _ in range(5))
print("Números gerados:", random_numbers)
print("Menor valor:", min(random_numbers))
print("Maior valor:", max(random_numbers))
