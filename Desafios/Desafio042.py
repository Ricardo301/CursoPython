from colorama import init
init()
A = float(input('Primeiro lado '))
C = float(input('Segundo lado '))
B = float(input('Terceiro lado '))

if abs(B-C) < A < (B+C) and abs(A-C) < B < (A+B) and abs(A-B) < C < (A+B):
    print('Forma triangulo : ',end='')
    if A != B and B != C and A != C:
        print('\033[34mEscaleno')
    elif A == B and C == A:
        print('\033[34mEquilatero')
    else:
        print('\033[34mIsoleces\033[m')

else:
    print('\033[31mNao e triangulo')
