# 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n =
# leiaInt(‘Digite um n: ‘)
def leiaunt(msg):
    ok = False
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            int(numero)
            ok = True
            break
        else:
            print('\033[91mERRO! Digite um numero inteiro valido\033[m')
    if ok:
        return numero


# Progrma principal
nu = leiaunt('Digite um numero: ')
print(f'Você acabou de digitar o numero {nu}')