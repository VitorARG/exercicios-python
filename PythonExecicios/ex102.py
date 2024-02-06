# 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
# ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    """
    Função que calcula o fatorial de um numero
    :param n: É o numero a ser calculado
    :param show: Mostra ou não a conta
    :return: Retorna o valor de n fatorial
    """
    num = n
    resultado = 1
    for c in range(1, n + 1):
        resultado *= c
        if show:
            print(f'{num}', end='')
            if num != 1:
                print(' X ', end='')
            if num == 1:
                print(' = ', end='')
            num -= 1

    return resultado


print(fatorial(5))


def fatorial(n=1, show=False):
    num = 1
    for c in range(n, 0, -1):
        num *= c
        if show:
            print(f'{c}', end='')
            if c != 1:
                print(' X ', end='')
            else:
                print(' = ', end='')

    return num


# programa principal
print(fatorial(5))