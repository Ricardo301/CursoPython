def fibo(n):
    F = 0
    ant = 0
    for x in range(1,n+1):
        if x == 1:
            F=1
            ant=0
        else:
            F+=ant
            ant=F-ant
    return F

N =int(input())

if 0 < N < 46:
    for x in range(N):
        if x == N-1:
            print(fibo(x))
        else:
            print(fibo(x), end=' ')