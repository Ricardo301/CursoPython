sal = float(input())

if sal <= 400:
    reajuste = sal*0.15
    print('Novo salario: {:.2f}'.format(sal+reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 15 %')

elif 400 < sal <= 800:
    reajuste = sal * 0.12
    print('Novo salario: {:.2f}'.format(sal + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 12 %')

elif 800 < sal <= 1200:
    reajuste = sal * 0.10
    print('Novo salario: {:.2f}'.format(sal + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 10 %')

elif 1200 < sal <= 2000:
    reajuste = sal * 0.07
    print('Novo salario: {:.2f}'.format(sal + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 7 %')

else:
    reajuste = sal * 0.04
    print('Novo salario: {:.2f}'.format(sal + reajuste))
    print('Reajuste ganho: {:.2f}'.format(reajuste))
    print('Em percentual: 4 %')


