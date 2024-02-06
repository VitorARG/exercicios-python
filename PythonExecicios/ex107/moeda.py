# 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa
# que importe esse módulo e use algumas dessas funções.
def aumentar(val, al=10):
    return al, val + ((al / val) * 100)


def diminuir(val, di=10):
    return di, val - ((di / val) * 100)


def dobro(num):
    return num * 2


def metade(num):
    return num / 2


