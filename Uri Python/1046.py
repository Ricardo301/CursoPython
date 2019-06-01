inicio,final=map(int,input().split())

if inicio>final or inicio==final:
    print('O JOGO DUROU {} HORA(S)'.format(24-(inicio-final)))
else:
    print('O JOGO DUROU {} HORA(S)'.format(final-inicio))