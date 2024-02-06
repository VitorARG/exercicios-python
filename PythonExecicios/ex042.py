# DESAFIO Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado: EQUILÁTERO: todos os lados iguais.
# ISÓSCELES: dois lados iguais, um diferente. ESCALENO: todos os lados diferentes
seg1 = float(input('Primeiro seguimento'))
seg2 = float(input('Segundo seguimento'))
seg3 = float(input('Terceiro seguimento'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
   print('Os Seguimentos digitados podem formar um triangulo ', end='')
   if seg1 == seg2 == seg3:
       print('EQUIlÁTERO')
   elif seg1 != seg2 != seg3 != seg1:
       print('ESCALENO')
   else:
       print('ISÓSCELES')
else:
    print('Os segumentos não podem formar tiangulo')