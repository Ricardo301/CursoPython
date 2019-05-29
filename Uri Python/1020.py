n = int(input())
ano = n//365
mes = (n//30)-ano*12
dia=(n%365)%30


print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
