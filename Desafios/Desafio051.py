primeiro = int(input('Digite o primeiro termo da PA'))
razao = int(input('Digite a razão da PA '))

for x in range(0, 10):
    if x == 0:
        print(primeiro, end=" ")
    else:
        primeiro = primeiro + razao
        print(primeiro+razao, end=" ")
