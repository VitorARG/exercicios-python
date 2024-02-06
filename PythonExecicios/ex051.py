# DESAFIO Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
termo = int(input('Primeiro termo '))
razao = int(input('Razão '))
for pa in range(termo, razao * 10 + termo, razao):
    print(pa, end=' → ')
print('Acabou')