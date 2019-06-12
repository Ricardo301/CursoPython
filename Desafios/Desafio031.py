Num = float(input('Qual a distancia da viagem: '))

if Num >200:
    valor = Num*0.45
    print('Voce vai pagar R${:.2f}'.format(valor))
else:
    valor = Num *0.5
    print('Voce vai pagar R${:.2f}'.format(valor))