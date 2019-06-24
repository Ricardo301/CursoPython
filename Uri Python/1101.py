Soma = 0

while True:
    N,M = map(int,input().split())
    if M<=0 or N<=0:
       break
    else:
        if M>N:
            maior = M
            menor = N
        else:
            maior = N
            menor = M

        for x in range(menor,maior+1):
            print('{}'.format(x),end=' ')
            Soma+=x
        print('Sum={}'.format(Soma))
        Soma=0
