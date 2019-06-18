num = int(input('Digite um valor: '))
print('''Digite a opção de converção:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal ''')
opcao = int(input('Escreva a opçao: '))

if opcao == 1:
    print('O valor {} em binário é {}'.format(num,bin(num)[2:]))

elif opcao == 2:
    print('O valor {} em octal é {}'.format(num, oct(num)[2:]))

elif opcao == 3:
    print('O valor {} em hexadecimal é {}'.format(num, hex(num)[2:]))

else:
    print('Valor invalido')

