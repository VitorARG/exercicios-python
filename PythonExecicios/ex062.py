# DESAFIO 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('=-' * 10)
print('Gerador de PA')
print('=-' * 10)
termo = int(input('Digite o primeiro termo '))
razao = int(input('Digite a razão da PA '))
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print(termo, end=' → ')
        termo += razao
        contador += 1
    print('pausa')
    mais = int(input('Quantas numeros a mais você deseja? '))
print('o total de termos da PA foi {}'.format(total))