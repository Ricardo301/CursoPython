N = int(input())
if N < 10000:
    for x in range(1,10001):
        if x%N==2:
            print(x)
