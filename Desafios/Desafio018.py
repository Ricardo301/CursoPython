from math import sin,cos,tan,radians
angulo = float(input())
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))

print('Seno: {:.2f}'.format(seno))
print('Coseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(tan))