N = int(input())

if 5<N<2000:
    for x in range(2,N+1):
        if x %2==0:
            print('{}^2 = {}'.format(x,x**2))