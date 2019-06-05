cont=0
ind=1
for x in range(100):
    N = int(input())
    cont+=1
    if cont == 1:
        maior = N
    else:
        if N>maior:
            maior = N
            ind=cont
print(maior)
print(ind)