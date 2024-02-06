# 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o anonas de
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
# OBRIGATÓRIO nas eleições.
def voto(nas):
    from datetime import datetime
    ano = datetime.now().year
    idade = ano - nas
    if idade < 16:
        return f"Com {idade} Anos. Não vota!"
    elif 16 <= idade <= 18 or idade >= 65:
        return f"Com {idade} anos. O Voto é opcional "
    else:
        return f"Com {idade} anos. O Voto é Obrigatorio"


# programa principal
print('-' * 25)
anonas = int(input(' Em que ano você nasceu? '))
print(voto(anonas))
