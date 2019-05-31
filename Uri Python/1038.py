num = input().split()
Cod = int(num[0])
X =int(num[1])

if Cod == 1:
    print('Total: R$ {:.2f}'.format(4*X))
elif Cod == 2:
    print('Total: R$ {:.2f}'.format(4.5*X))
elif Cod == 3:
    print('Total: R$ {:.2f}'.format(5*X))
elif Cod == 4:
    print('Total: R$ {:.2f}'.format(2*X))
elif Cod == 5:
    print('Total: R$ {:.2f}'.format(1.5*X))