# Desafio 87: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha
matriz = [[], [], []]
somapar = terceira = maiorseg = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digitr o numero na posição {l},{c} ')))
for l in range(0,3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorseg:
                maiorseg = matriz[l][c]
    print()

print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma dos valores da terseira colula é {terceira}')
print(f'o numero {maiorseg} é o maior valor da segunda linha')



