N1 = float(input('Nota1: '))
N2 = float(input('Nota2: '))
m = (N1+N2)/2
print('O aluno tem media de {} e esta na situação: '.format(m),end='')
if m < 5:
    print('Reprovado')
elif m>=5 and m <7:
    print('Recuperaçao')
else:
    print('Aprovado')

