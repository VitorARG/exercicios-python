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


def linha(tam=42):
    return '-' * tam


def cabecalo(msg):
    print(linha())
    print(msg.center(42))
    print(linha())


def menu(lista):
    cabecalo('menu principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\33[32mSua opção:\033[m')
    return opc

