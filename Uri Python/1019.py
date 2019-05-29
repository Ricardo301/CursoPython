n = int(input())


min = (n%3600)//60
hora = n//3600
sec = (n%3600)%60

print('{}:{}:{}'.format(hora,min,sec))