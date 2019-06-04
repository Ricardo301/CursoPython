N=int(input())
entre10=0
fora10=0
if N<10000:
    for x in range(0,N):
        Y = int(input())
        if -10**7 < Y <10**7:
            if Y >=10 and Y<=20:
                entre10+=1
            else:
                fora10+=1
print('{} in'.format(entre10))
print('{} out'.format(fora10))