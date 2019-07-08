import datetime
AnoComputador = datetime.date.today().year
ano = int (input('Ano de Nascimento: '))
idade = AnoComputador-ano
print('O atleta tem {} anos.'.format(idade))
if idade <=9:
    print('MIRiM')
elif idade>9 and idade<=14:
    print('Infatil')
elif idade>14 and idade<=19:
    print('Junior')
elif idade>19 and idade<=25 :
    print('Senior')
else:
    print('Master')
