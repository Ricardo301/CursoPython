X= int(input())
Y= int(input())

if X>=Y:
    for x in range(Y+1,X):
        if x%5==2 or x%5==3:
            print(x)
elif Y>=X:
    for x in range(X+1, Y):
        if x % 5 == 2 or x % 5 == 3:
            print(x)