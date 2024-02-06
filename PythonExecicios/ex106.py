# 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará. Importante: use cores.
from time import sleep

c = ('\033[m',          # 0 = sem cores
     '\033[0;30;41m',   # 1 = Vermelho
     '\033[0;30;43m',   # 2 = amarelo
     '\033[0;30;44m',   # 3 = azul
     '\033[107;30m',   # 4 = branco
     )


def ajuda(msg):
    titulo(f'Manual do comando {msg}', 3)
    print(c[4], end='')
    print(help(msg))
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(f'{c[cor]}~' * tamanho)
    print(f'{msg}')
    print('~' * tamanho)
    print(c[0], end='')
    sleep(1)


while True:
    titulo('Sistema de ajuda pyhelp', 2)
    sleep(0.5)
    comando = str(input('Função ou biblioteca '))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('fim do programa', 1)