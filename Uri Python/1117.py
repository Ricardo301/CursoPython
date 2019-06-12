soma=0
cont=0
while cont<2:
    Nota = float(input())
    if Nota >=0 and Nota <=10:
        soma+=Nota
        cont+=1
    else:
        print('nota invalida')

print('media = {:.2f}'.format(soma/2))

