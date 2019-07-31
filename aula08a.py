import random
num=int(input('Digite um numero: '))

nome=list(map(str,input().split()))

sorte=random.choice(nome)

print(sorte)
