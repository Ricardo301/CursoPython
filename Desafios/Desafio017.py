from math import hypot
catop = float(input('Cateto opsto: '))
catad = float(input('Cateto adjacente '))
h=hypot(catop,catad)
print('Hipotenusa: {:.2f}'.format(h))

