# 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~
def titulo(txt):
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


# Progrma principal
titulo('Vitão')
titulo('Curso em video')
titulo('Macaco aranha')
titulo('Abelha')
