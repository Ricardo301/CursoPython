num = input().split()
X= float(num[0])
Y= float(num[1])

if X > 0 < Y:
    print('Q1')
elif X > 0 > Y:
    print('Q4')
elif X < 0 < Y:
    print('Q2')
elif X < 0 > Y:
    print('Q3')
elif X == 0 and Y != 0:
    print('Eixo Y')
elif X != 0 and Y == 0:
    print('Eixo X')
else:
    print('Origem')
