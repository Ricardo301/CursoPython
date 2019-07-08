N = int(input())
if 1 <= N <= 1000:
    mult2 = 0
    mult3 = 0
    mult4 = 0
    mult5 = 0

    Num = list(map(int, input().split()))
    for x in range(N):

        if Num[x] % 2 == 0:
            mult2 += 1
        if Num[x] % 3 == 0:
            mult3 += 1
        if Num[x] % 4 == 0:
            mult4 += 1
        if Num[x] % 5 == 0:
            mult5 += 1

    print('{} Multiplo(s) de 2'.format(mult2))
    print('{} Multiplo(s) de 3'.format(mult3))
    print('{} Multiplo(s) de 4'.format(mult4))
    print('{} Multiplo(s) de 5'.format(mult5))
