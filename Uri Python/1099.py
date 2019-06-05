N = int(input())

for cot in range(N):
    X,Y=map(int,input().split())
    soma=0
    if X<Y:
        for x in range(X+1,Y):
            if x%2==1:
                soma+=x
    else:
        for x in range(Y+1,X):
            if x%2==1:
                soma+=x


    print(soma)





