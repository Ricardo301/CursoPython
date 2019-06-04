X = int(input())
Y = int(input())
soma=0
for i in range(Y+1,X):
    if i%2==1:
        soma+=i
print(soma)