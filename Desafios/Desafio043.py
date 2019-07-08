peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/ (altura**2)
print('Seu imc é de : {}'.format(imc))

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('sobre peso')
elif 30 <= imc < 40:
    print('Obseso')
else:
    print('Obesidade morbida')