'''frase = input('Digite uma frase: ')
frase = frase.strip().replace(" ", "").upper()

analizador = frase[::-1]
print('O inverso de {} é {}'.format(frase,analizador))
if frase == analizador:
    print('É palindromo')
else:
    print('Não é palin')'''

frase = input('Digite uma frase: ')
frase = frase.strip().replace(" ", "").upper()
new = ''
for x in range(len(frase)-1, -1, -1):
    new += frase[x]
print('a frase {} ao contrario é {}'.format(frase, new))

if frase == new:
    print('É palindromo')
else:
    print('Não é palindromo')
