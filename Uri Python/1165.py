def FunPrimo(n):
    ehprimo = 0
    for x in range(1,n+1):
        if n%x==0:
            ehprimo+=1
    return ehprimo


N = int(input())
if 1<= N <=100:
    for x in range(N):
        Num = int(input())

        if 1<= Num <=10**7:
            primo = FunPrimo(Num)

        if primo == 1 or primo ==2:
            print('{} eh primo'.format(Num))
        else:
            print('{} nao eh primo'.format(Num))