from colorama import init
init()
num = int(input('Digite um valor: '))
cont = 0

for x in range(1, num+1):
    if num % x == 0:
        cont += 1
        print("\033[32m{}\033[m".format(x), end=" ")
    else:
        print("\033[31m{}\033[m".format(x), end=" ")


if cont == 2:
    print('É primo')
else:
    print('Não é primo')
