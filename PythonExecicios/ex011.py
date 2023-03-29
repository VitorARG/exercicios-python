# Desaio programa que leia a leia a largura e altura de um aparede em metros,
# calcule a sua area e diga diga a quantidade necessario de tinta para pintala,
# sabendo que cada litro de tinta pinta 2m²
l = float(input('Diga a largura da parede em metros'))
a = float(input('Diga a altura da parede em metros'))
mq = l*a
print('Sua parede tem {:.2f}m² e precisará aproximadamente de {:.1f} litros de tinta para'
      ' pintala por completo'.format(mq,mq/2))


