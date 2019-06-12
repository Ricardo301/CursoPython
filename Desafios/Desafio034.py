salario = float(input('Salario :'))

if salario > 1250:
    nsal = (salario*0.10) + salario
else:
    nsal = (salario * 0.15) + salario

print('Quem ganahva R${:.2f} agora ganha R${:.2f}'.format(salario,nsal))