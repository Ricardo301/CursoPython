X= int(input())
Y= int(input())

if X>Y:
    for x in range(X,Y):
        if x%5==2 or x%5==3:
            print(x)
else:
    for x in range(Y, X):
        if x % 5 == 2 or x % 5 == 3:
            print(x)