N = int (input())
totalCoelho=0
totalRato=0
totalSapo=0
for x in range(N):
    cobia = input().split()
    cobia[0]=int(cobia[0])
    if 1 <= cobia[0] <= 15:
        if cobia[1] == 'C':
         totalCoelho += int(cobia[0])
        elif cobia[1] == 'R':
            totalRato += int(cobia[0])
        elif cobia[1] == 'S':
            totalSapo += int(cobia[0])

total=totalSapo+totalRato+totalCoelho
psapo = (totalSapo*100)/total
pcoelho = (totalCoelho*100)/total
prato = (totalRato*100)/total

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(totalCoelho))
print('Total de ratos: {}'.format(totalRato))
print('Total de sapos: {}'.format(totalSapo))
print('Percentual de coelhos: {:.2f} %'.format(pcoelho))
print('Percentual de ratos: {:.2f} %'.format(prato))
print('Percentual de sapos: {:.2f} %'.format(psapo))