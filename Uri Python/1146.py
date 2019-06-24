while True:
    X = int(input())
    if X == 0:
        break
    else:
        for x in range(1,X+1):
            if x==X:
                 print(x,end='')
            else:
                 print(x,end=' ')