lar = float(input('Largura: '))
h = float(input('Altura: '))

a = lar*h

print('Sua parede tem a dimensão de {}x{} e sua area e de {}'.format(lar, h, a))
print('Necessario {} litros para pintar'.format(a/2))