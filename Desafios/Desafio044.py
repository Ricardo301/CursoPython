valor = float(input('Qual o preço do produto?  R$:'))
print('-='*20)
print('FORMAS De PAGAMENTO ')

print('[ 1 ] à vista dinheiro')
print('[ 2 ] à vista cartao')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor,valor*0.9))
elif opcao == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor * 0.95))
elif opcao == 3:
    print('Sua sera parcela em 2x de {:.2f} '.format(valor/2))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, valor))
elif opcao == 4:
    pres = int(input('Em quantas vezes será a compra '))
    valorpres = (valor*1.2)/pres
    print('A compra sera paga em {}x de R${:.2f}'.format(pres,valorpres))
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, valor*1.2))