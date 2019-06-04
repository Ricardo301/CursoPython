contPar = 0
contImp = 0
contMaior = 0
contMenor = 0
for x in range(5):
    num = int(input())
    if num%2 == 0:
        contPar += 1
    else:
        contImp +=1
    if num >0:
        contMaior += 1
    elif num <0:
        contMenor +=1
print('{} valor(es) par(es)'.format(contPar))
print('{} valor(es) impar(es)'.format(contImp))
print('{} valor(es) positivo(s)'.format(contMaior))
print('{} valor(es) negativo(s)'.format(contMenor))
