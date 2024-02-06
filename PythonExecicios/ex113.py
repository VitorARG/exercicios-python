def leiaint(msg):
    while True:

        try:
            n = int(input(f'{msg} '))
        except (ValueError, TypeError):
            print('\033[31mErro Por favor digite um numero inteiro valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntarada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(f'{msg} '))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor digite um numero real\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntarada de dados interrompida pelo usuario\033[m')
            return 0
        else:
            return n


num1 = leiaint('Digite um numero inteiro')
num2 = leiafloat('Digite um numero real')
print(f'Você digitou {num1}')
print(f'Você digitou {num2}')

