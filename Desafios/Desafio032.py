from datetime import date
Ano = int (input())
if Ano==0:
    Ano=date.today().year

if Ano%4==0 and Ano%100!=0 or Ano%400==0:
    print('{} Ano Bissexto'.format(Ano))
else:
    print('{} Nao é bisxxesto'.format(Ano))