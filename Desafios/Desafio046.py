from time import sleep
from colorama import init
init()

for x in range(10, -1, -1):
    print(x)
    sleep(1)
print('\033[36mFogos ***')
