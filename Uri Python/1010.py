pord1=input().split()
prod2 = input().split()

cod1=int(pord1[0])
num1=int(pord1[1])
valor1=float(pord1[2])

cod2=int(prod2[0])
num2=int(prod2[1])
valor2=float(prod2[2])

final=(num1*valor1)+(num2*valor2)

print('VALOR A PAGAR: R$ {:.2f}'.format(final))
