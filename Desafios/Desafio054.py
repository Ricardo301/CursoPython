import datetime
year = datetime.date.today().year
maior = 0
menor = 0
for x in range(7):
    ano = int(input('Digite a idade da {} pessoa: '.format(x+1)))
    idade = year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('A quantidad de maior é {}'.format(maior))
print('A quantidad de menor é {}'.format(menor))
