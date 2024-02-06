# Desafio Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('CASA', 'BARRACA', 'MESA', 'BARCO', 'FAROL', 'MARUJO', 'SEREIA')
for i in palavras:
    print(f'na palavra {i} temos as letras', end=' ')
    for letra in i:
        if letra in 'AEIOU':
            print(letra, end=' ')
    print('')