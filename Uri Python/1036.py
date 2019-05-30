from math import sqrt
num=input().split()
A=float(num[0])
B=float(num[1])
C=float(num[2])
Delta = B**2 -4*A*C

if Delta < 0 or 2*A == 0:
    print('Impossivel calcular')
    exit()
else:
    R1 = (-B +(sqrt(Delta)))/(2*A)
    R2 = (-B -(sqrt(Delta)))/(2*A)
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))