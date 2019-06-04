N = int(input())

if N <10000:
    for x in range(0,N):
        Num = int(input())
        if -10**7 < Num <10**7:
            if Num %2==0 and Num!=0:
                print('EVEN', end=' ')
            elif Num%2==1 and Num!=0:
                print('ODD' ,end=' ')
            if Num >0:
                print('POSITIVE')
            elif Num<0:
                print('NEGATIVE')
            else:
                print('NULL')