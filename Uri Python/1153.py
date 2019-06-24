def fat(n):
    F = 1

    for x in range(n,0,-1):
       F*=x
    '''while n > 1:
        F*=n
        n-=1'''
    return F


Num = int(input())
if 0 < Num <13:
    print('{}'.format(fat(Num)))
