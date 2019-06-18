import datetime
year = datetime.date.today().year
ano = int(input('Ano de nascimento'))
idade = year-ano

if idade <18:
    falta = 18-idade
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano,idade,year))
    print('Ainda faltam {} anos para o alistamento.'.format(falta))
    print('Seu alistamento será em {}.'.format(year+falta))
elif idade >18:
    falta = idade -18
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade,year))
    print('Voce ja deveria ter se alistado há {} anos.'.format(falta))
    print('Seu alistamento foi em {}'.format(year - falta))
else:
    print('Quem nasceu em {} tem {} em {}.'.format(ano,idade,year))
    print('Você tem que se alistar agora!')