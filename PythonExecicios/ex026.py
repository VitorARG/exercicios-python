# Desafio Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra “A”, em que posição ela
# aparece a primeira vez e em que posição ela aparece a última
frase = str(input('Digite uma frase')).strip().lower()
print('A prmeira letra A aparece {} Vezes'.format(frase.count('a')))
print('Aprimeira letra A aprece na posição {}'.format(frase.find('a')+1))
print('A ultima Letra A aparece na posição {}'.format(frase.rfind('a')+1))
