soma = 0
total = 0
while True:
    n = int(input())
    if n <0:
        break
    else:
        total += 1
        soma += n

print('{:.2f}'.format(soma/total))

