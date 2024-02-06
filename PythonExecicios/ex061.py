# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
print('=-' * 10)
print('Gerador de PA')
print('=-' * 10)
termo = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão da PA '))
contador = 0
while contador != 10:
    print(termo, end=' → ')
    termo += razao
    contador += 1
print('Fim da PA')