A,B,C =map(int,input().split())
'''
num=[A,B,C]
if A<B and A<C:
    if B<C:
        print(A)
        print(B)
        print(C)
    else:
        print(A)
        print(C)
        print(B)
elif B<A and B<C:
    if A<C:
        print(B)
        print(A)
        print(C)
    else:
        print(B)
        print(C)
        print(A)
else:
    if A<B:
        print(C)
        print(A)
        print(B)
    else:
        print(C)
        print(B)
        print(A)

print()
print(A)
print(B)
print(C)
'''
num = [A, B, C]
num.sort()
print(*num, sep='\n')
print()
print(A)
print(B)
print(C)