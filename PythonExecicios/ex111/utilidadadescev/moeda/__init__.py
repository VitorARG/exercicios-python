# 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
# mantenha tudo funcionando.
def aumentar(val=0, al=10, fo=False):
    res = val + ((al * val) / 100)
    return res if fo is False else moeda(res)


def diminuir(val=0, di=10, fo=False):
    res = val - ((di * val) / 100)
    return res if fo is False else moeda(res)


def dobro(num=0, fo=False):
    res = num * 2
    if fo:
        return moeda(res)
    else:
        return res


def metade(num=0, fo=False):
    res = num / 2
    return res if fo is False else moeda(res)


def resumo(p=0, al=10, di=10):
    print('_' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('_' * 30)
    print(f'{"preço analisado:":<}\t{moeda(p)}')
    print(f'Dobro do preço \t\t{dobro(p, True)}')
    print(f'{"metade do preço:"}\t{metade(p, True)}')
    print(f'{al}% de aumento: \t{aumentar(p, al, True)}')
    print(f'{di}% de redução  \t{diminuir(p, di, True)}')
    print('_'* 30)


def moeda(valor=0, mo='R$'):
    return f'{mo}{valor:.2f}'.replace('.', ',')
