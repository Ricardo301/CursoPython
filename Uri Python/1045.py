A,B,C = map(float,input().split())
num =[A,B,C]
num.sort()
A=num[2]
B=num[1]
C=num[0]
if A>= B+C:
    print('NAO FORMA TRIANGULO')
else:
    if A**2==B**2+C**2:
        print('TRIANGULO RETANGULO')
    if A**2 > B**2 + C**2:
        print('TRIANGULO OBTUSANGULO')
    if A**2<B**2 + C**2:
        print('TRIANGULO ACUTANGULO')
    if A==B and B==C:
        print('TRIANGULO EQUILATERO')
    elif A==B or B==C:
        print('TRIANGULO ISOSCELES')