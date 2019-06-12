N = int(input())
num=1

for x in range(N):
    for l in range(4):

        if num%4==0:
            print('PUM')
        else:
            print(num, end=' ')

        num+=1