a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
MaiorAB =(a+b+abs(a-b))//2
MaiorC =(MaiorAB+c+abs(MaiorAB-c))//2
Maior = (MaiorAB+MaiorC+abs(MaiorAB-MaiorC))//2
print('{} eh o maior'.format(Maior))
