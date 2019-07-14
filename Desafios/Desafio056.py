somai = 0
maiori = 0
nomeH = ''
contF = 0
for x in range(4):
    print('----- {}ª Pessoa -----'.format(x+1))
    nome = input('Nome :')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somai += idade

    if x == 0 and sexo in 'Mm':
        maiori = idade
        nomeH = nome
    if sexo in 'Mm' and idade > maiori:
        maiori = idade
        nomeH = nome

    if sexo in 'Ff' and idade < 20:
        contF += 1
print('A média da idade do grupo é {}'.format(somai/4))
print('Homem mais velho nome : {} idade {}'.format(nomeH, maiori))
print('Existem {} mulhes menores que 20'.format(contF))
