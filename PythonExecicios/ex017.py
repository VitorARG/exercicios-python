# programa que leia os dois catetos e diga o comprimento da hopotenusa
import math
ca = float(input('Digite o cateto Ad'))
co = float(input('digite o outro cateto'))
hipo = math.sqrt((ca**2) + (co**2))
hp = math.hypot(ca,co)
print('o comprimento da hipotenusa equivale ah',hp)

