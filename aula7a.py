n1 = int(input('Digite um numero'))
n2 = int(input('Diggite outro numero'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n1
p = n1 ** n2

print('A soma é {} a subtraçao é {} a multiplicadao é {} a divisao é {:.3f}'.format(s, su, m, d), end=' ')
print('A divisao inteira é {} a potencia é {}'.format(di, p))
