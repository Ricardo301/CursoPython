alcol = 0
gasolina = 0
diesel = 0
entrada = 0

while entrada != 4:
    entrada = int(input())
    if entrada > 0:
        if entrada == 1:
            alcol += 1
        elif entrada == 2:
            gasolina += 1
        elif entrada == 3:
            diesel += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcol))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))

