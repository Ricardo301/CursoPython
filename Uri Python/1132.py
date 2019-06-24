X = int(input())
Y = int(input())
maior = X
if Y>maior:
    maior = Y
    menor = X
else:
     menor = Y
soma = 0
for x in range(menor,maior+1):
    if x%13!=0:
        soma+=x

print(soma)        
