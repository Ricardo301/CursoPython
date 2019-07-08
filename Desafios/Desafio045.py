import random
from time import sleep
from colorama import init
init()
escolha = str(input('Pedra, Papel ou Tesoura? ').capitalize())
comp = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('\033[35m-=\033[m'*20)
print('\033[34m{:^40}'.format('Jo'))
sleep(0.3)
print('{:^40}'.format('KEN'))
sleep(0.3)
print('{:^40}'.format('PO'))
sleep(0.3)
print('\033[35m-=\033[m'*20)

if comp == 'Pedra' and escolha == 'Papel':
    print(
        '\033[32mVocê ganhou!\033[m O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Pedra' and escolha == 'Tesoura':
    print(
        '\033[31mVoce Perdeu\033[m O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Pedra' and escolha == 'Pedra':
    print('Empate  O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Papel' and escolha == 'Tesoura':
    print(
        '\033[32mVocê ganhou!\033[m  O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Papel' and escolha == 'Pedra':
    print(
        '\033[31mVoce Perdeu\033[m O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Papel' and escolha == 'Papel':
    print('Empate O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Tesoura' and escolha == 'Pedra':
    print(
        '\033[32mVocê ganhou!\033[m O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Tesoura' and escolha == 'Papel':
    print(
        '\033[31mVoce Perdeu\033[m O Computador escolheu \033[1;36m{}'.format(comp))

elif comp == 'Tesoura' and escolha == 'Tesoura':
    print('Empate O Computador escolheu \033[1;36m{}'.format(comp))
sleep(10)
