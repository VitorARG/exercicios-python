# 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
# números como um valor monetário formatado.
def aumentar(val=0, al=10):
    return al, val + ((al * val) / 100)


def diminuir(val=0, di=10):
    return di, val - ((di * val) / 100)


def dobro(num=0):
    return num * 2


def metade(num=0):
    return num / 2


def moeda(valor=0, mo='R$'):
    return f'{mo}{valor:.2f}'.replace('.', ',')

