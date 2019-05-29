N=float(input())
if 0 < N < 1000000:
    troco=N

    cem = troco//100
    troco=troco-(cem*100)

    cinquenta = troco//50
    troco=troco-(cinquenta*50)

    vinte = troco//20
    troco=troco-(vinte*20)


    dez = troco//10
    troco=troco-(dez*10)


    cinco = troco//5
    troco=troco-(cinco*5)


    dois = troco//2
    troco=troco-(dois*2)


    um = troco//1
    troco=troco-(um*1)

    cincet= troco //0.5
    troco=troco-(cincet*0.5)

    vintcet = troco // 0.25
    troco = troco - (vintcet * 0.25)

    dezcent = troco // 0.10
    troco = troco - (cincet * 0.10)

    cincocent = troco // 0.05
    troco = troco - (cincocent * 0.05)
    print(N)
    print('{} nota(s) de R$ 100,00'.format(cem))
    print('{} nota(s) de R$ 50,00'.format(cinquenta))
    print('{} nota(s) de R$ 20,00'.format(vinte))
    print('{} nota(s) de R$ 10,00'.format(dez))
    print('{} nota(s) de R$ 5,00'.format(cinco))
    print('{} nota(s) de R$ 2,00'.format(dois))
    print('{} nota(s) de R$ 1,00'.format(um))
    print('{} moedas(s) de R$ 0,50'.format(cincet))
    print('{} moedas(s) de R$ 0,25'.format(vintcet))
    print('{} moedas(s) de R$ 0,10'.format(dezcent))
    print('{} moedas(s) de R$ 0,05'.format(cincocent))



    


