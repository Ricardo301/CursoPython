N = int(input())

if 2< N < 1000:
    for x in range(1,11):
        print('{} x {} = {}'.format(x,N,N*x))