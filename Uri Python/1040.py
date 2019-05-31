N1,N2,N3,N4 =map(float,input().split())
#num = input().split()
#N1 = float(num[0])
#N2 = float(num[1])
#N3 = float(num[2])
#N4 = float(num[3])

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
print('Media: {:.1f}'.format(media))
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif 5 <= media <= 6.9:
    print('Aluno em exame.')
    N5 = float(input())
    print('Nota do exame: {:.1f}'.format(N5))
    media = (media+N5)/2
    if media >= 5:
        print('Aluno aprovado.')
    elif media <= 4.9:
        print('Aluno reprovado.')
    print('Media fina: {:.1f}'.format(media))


