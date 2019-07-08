import colorama
colorama.init()

ValorCasa = float(input('Qual é o valor da casa R$ '))
salario = float(input('Qual é o seu salário? '))
ano = int(input('Em qunatos anos será percelada ?'))
presmensal = ValorCasa / (ano*12)
percentualSal = salario * 0.3

if presmensal > percentualSal:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação serpa de R${:.2f} você ganha R${:.2f} é muito pouco'.format(
        ValorCasa, ano, presmensal, salario))
    print('Emprestimo Negado')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação serpa de R${:.2f} você ganha R${:.2f} '.format(
        ValorCasa, ano, presmensal, salario))
    print('Emprestimo concedido')
