A = float(input('Primeiro lado '))
C = float(input('Segundo lado '))
B = float(input('Terceiro lado '))

if abs(B-C) < A < (B+C) and abs(A-C) < B < (A+B) and abs(A-B) < C < (A+B):
    print('Forma triangulo')
    if A!=B and B!=C and A!=C:
        print('Escaleno')
    elif A==B and C==A:
        print('Equilatero')
    elif A==B or B==C:
        print('Isoleces')

else:
    print('Nao e triangulo')