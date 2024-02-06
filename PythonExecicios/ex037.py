# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um numero '))
print('''Digite o numero corespondente para escolher a base de conversão 
[1] Para Binario
[2]Para Octal
[3]Para Hexadecimal''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print('{} Convertido para binario é  {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} Convertido para octal é  {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} Convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')