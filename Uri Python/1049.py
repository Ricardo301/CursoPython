Nome1 = input()
Nome2 = input()
Nome3 = input()

if Nome1 == 'vertebrado':
    if Nome2 == 'ave':
        if Nome3== 'carnivoro':
            print('aguia')
        elif Nome3 == 'onivoro':
            print('pomba')
    if Nome2 == 'mamifero':
        if Nome3== 'onivoro':
            print('homem')
        elif Nome3== 'herbivoro':
            print('vaca')
elif Nome1 == 'invertebrado':
    if Nome2=='inseto':
        if Nome3=='hematofago':
            print('pulga')
        if Nome3=='herbivoro':
            print('lagarta')
    if Nome2 == 'anelideo':
        if Nome3 == 'hematofago':
            print('sanguessuga')
        if Nome3 == 'onivoro':
            print('minhoca')