num = int(input())
if 1 <= num <= 1000:

    for x in range(num+1):
        if x % 2 ==1:
            print(x)