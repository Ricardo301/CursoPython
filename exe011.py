# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
num1= float(input('Digite a altura'))
num2=float(input('Digite a largura 0x50'))

are=num1*num2

tina=are/2

print('Sua parade tem a dimensao de {}x{} e sua área é de {}m'.format(num1,num2,are))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tina))