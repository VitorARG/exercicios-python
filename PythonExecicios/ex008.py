# desafio 08 leia u numero em mentros e converta ele e centimetros e milimetros
#n = float(input(' Escreva um numero em metros'))
#c = n*100
#m = n*1000
#print('{} metros é igual a {:.0f} centimetros e {:.0f} milimetros'.format(n,c,m))

# Desafio parte 2 km hm dam m dm cm mm
medida = float(input('Escreva uma medida em metros'))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print('A medida {} m corresponde a'.format(medida))
print('{:.4f}km\n{:.3f}hm\n{:.2f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm '.format(km,hm,dam,dm,cm,mm))




