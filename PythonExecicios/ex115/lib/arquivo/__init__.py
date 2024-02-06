def criararq(nome):
    try:
        with open(f'{nome}', 'a'):
            print('Arquivo criado com sucesso')
    except PermissionError:
        print('Não há permissão para escrever no arquivo {nome}.')
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo: {e}")


def testar(nome):
    try:
        with open(f'{nome}', 'r'):
            print(f'{nome}')
    except FileNotFoundError:
        return False
    else:
        return True


def ler(nome):
    try:
        with open(f'{nome}', 'r') as arq:
            linhas = arq.readlines()
            contlinha = 0
            for linha in linhas:
                contlinha += 1
                partes = linha.strip().split(';')
                if len(partes) == 2:
                    print(f'{partes[0]:<30} {partes[1]:>3} anos')
                else:
                    if linha == '':
                        print()
                    else:
                        print(f'\033[31mOcorreu um erro inessperado na linha {contlinha}\033[m')
    except FileNotFoundError:
        print('Ocorreu um erro.')


def cadastar(nome):
    n = str(input('Nome: ')).strip()
    idade = int((input('Idade: ')))
    with open(nome, 'a') as arq:
        arq.write(f'{n};{idade}\n')
        print(f'{n} Cadatrado com sucesso')
