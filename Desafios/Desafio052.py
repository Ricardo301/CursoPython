num = int(input('Digite um valor'))
cont = 0

for x in range(1, num+1):
    if num % x == 0:
        cont += 1

if cont <= 2:
    print('É primo')
else:
    print('Não é primo')
