from sys import maxsize
maior = 0  # menor = 0

for x in range(5):
    peso = float(input('Digite o peso da {}ª pessoa: '))
    if x == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {:.2f}KG'.format(maior))
print('O menor peso é {:.2f}KG'.format(menor))
