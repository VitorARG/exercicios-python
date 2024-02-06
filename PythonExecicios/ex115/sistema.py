from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'

if not testar(arq):
    criararq(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'sair do sistema'])
    if resposta == 1:
        cabecalo('Ver pessoas cadastradas')
        ler(arq)
    elif resposta == 2:
        cabecalo('Cadastrar nova pessoa ')
        cadastar(arq)
    elif resposta == 3:
        cabecalo('Saido do sitema... ate logo')
        break
    else:
        print('\033[31mErro. Digite uma opção valida\033[m')
    sleep(2)

