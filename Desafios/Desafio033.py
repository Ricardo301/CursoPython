n1 = int(input('Primeiro valor :'))
n2 = int(input('Segundo valor :'))
n3 = int(input('Terceiro valor :'))
menor = n1
#Menor
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n1
#Maior
if n2>n1 and n2>n3:
    maior= n2
if n3>n2 and n3>n1:
    maior = n3
    
print('Maior: ',maior)
print('Menor ',menor)
