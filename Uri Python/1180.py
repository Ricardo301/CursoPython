N = int(input())

if 1 < N < 1000:
    num = list(map(int, input().split()))
    print(f'Menor valor: {min(num)}')
    print(f'Posicao: {num.index(min(num))}')
