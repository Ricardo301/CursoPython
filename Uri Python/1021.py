N = float(input())
if 0 <= N <= 1000000.00:

    cem = int(N/100)
    troco = N % 100

    cinquenta = int(troco/50)
    troco = troco % 50

    vinte = int(troco/20)
    troco = troco % 20

    dez = int(troco/10)
    troco = troco % 10

    cinco = int(troco/5)
    troco = troco % 5

    dois = int(troco/2)
    troco = troco % 2

    um = int(troco/1)
    troco = (troco % 1)

    cincet = int(troco / 0.5)
    troco = (troco % 0.5)

    vintcet = int(troco / 0.25)
    troco = (troco % 0.25)

    dezcent = int(troco / 0.10)
    troco = (troco % 0.10)

    cincocent = int(troco / 0.05)
    troco = (troco % 0.05)

    umcent = int(troco / 0.01)
    troco = (troco % 0.01)

    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(cem))
    print('{} nota(s) de R$ 50.00'.format(cinquenta))
    print('{} nota(s) de R$ 20.00'.format(vinte))
    print('{} nota(s) de R$ 10.00'.format(dez))
    print('{} nota(s) de R$ 5.00'.format(cinco))
    print('{} nota(s) de R$ 2.00'.format(dois))
    print('MOEDAS:')
    print('{} moeda(s) de R$ 1.00'.format(um))
    print('{} moeda(s) de R$ 0.50'.format(cincet))
    print('{} moeda(s) de R$ 0.25'.format(vintcet))
    print('{} moeda(s) de R$ 0.10'.format(dezcent))
    print('{} moeda(s) de R$ 0.05'.format(cincocent))
    print('{} moeda(s) de R$ 0.01'.format(umcent))
