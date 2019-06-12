import random
from time import sleep
num = random.randint(0,5)
print('-='*20)
valor = int(input('Digite um numero: '))
print('-='*20)
print('Processando...')
sleep(2)
if valor == num:
    print('Voce acertou')
else:
    print('Voce errou')
print('Valor sorteado {}'.format(num))
