A = float(input('Primeiro lado '))
C = float(input('Segundo lado '))
B = float(input('Terceiro lado '))

if abs(B-C) < A < (B+C) and abs(A-C) < B < (A+B) and abs(A-B) < C < (A+B):
    print('Forma triangulo')
else:
    print('Nao e triangulo')