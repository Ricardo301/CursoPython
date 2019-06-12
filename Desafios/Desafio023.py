'''Num = input()
print(Num[:1])
print(Num[1:2])
print(Num[2:3])
print(Num[3:4])'''

Num = int(input())
print('Numero digitado: {}'.format(Num))
print('Unidade: {}'.format(Num//1%10))
print('Dezena: {}'.format(Num//10%10))
print('Centena: {}'.format(Num//100%10))
print('Milhar: {}'.format(Num//1000%10))