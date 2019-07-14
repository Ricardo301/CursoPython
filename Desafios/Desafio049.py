Num = int(input('Digite o valor da tabuada que quer ver: '))

for x in range(1, 11):
    print('{} x {:02} = {:02}'.format(Num, x, x*Num))
