# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expre = str(input('Digite uma expressão'))
pilha = []
for caracter in expre:
    if caracter == '(':
        pilha.append('(')
    elif caracter == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if pilha == 0:
    print('É uma exoressão valida')
else:
    print('Não é uma espressão valida')
