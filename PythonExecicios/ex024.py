# Desafio  Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cidade = str(input("que cidade você nasceu?")).strip()
#dividido = cidade.split()
#print('santo' in  dividido[0].lower())
print(cidade[:5].lower() == 'santo')
