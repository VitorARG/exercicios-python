# Exercício Python 081: crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
listanum = []
while True:
    n = int(input('Digite um numero '))
    listanum.append(n)
    pergunta = str(input('Quer continuar? [S/N] '))
    if pergunta in 'Nn':
        break
listanum.sort(reverse=True)
print(f'Forma digitados {len(listanum)} Valores')
print(f'A lista em Forma decrecente é a seguinte {listanum} ')
if 5 in listanum:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
