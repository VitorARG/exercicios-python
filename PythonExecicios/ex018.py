# Desafio faça um programa que leia um agulo qualquer e diga seu seno cosseno e tangente
from math import radians,sin,cos,tan
angulo = float(input('Digite um angulo'))
'''sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))'''
print('O angulo de {} tem o seno {:.2f}'.format(angulo,sin(radians(angulo))))
print('o angulo de {} tem o cosseno {:.2f}'.format(angulo,cos(radians(angulo))))
print('o angulo de {} ten a tangente {:.2f}'.format(angulo,tan(radians(angulo))))
