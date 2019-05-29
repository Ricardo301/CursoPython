trin=input().split()
A=float(trin[0])
B=float(trin[1])
C=float(trin[2])

area= (A*C)/2
areacir = 3.14159 * C**2
areatrap = ((A+B)*C)/2
areaqua = B*B
arearet = A*B

print('TRIANGULO: {:.3f}'.format(area))
print('CIRCULO: {:.3f}'.format(areacir))
print('TRAPEZIO: {:.3f}'.format(areatrap))
print('QUADRADO: {:.3f}'.format(areaqua))
print('RETANGULO: {:.3f}'.format(arearet))
