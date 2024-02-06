# 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a
# mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.
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
    return res if not fo else moeda(res)


def moeda(valor=0, mo='R$'):
    return f'{mo}{valor:.2f}'.replace('.', ',')
