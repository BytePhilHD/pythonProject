# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from IPython.display import clear_output

import psutil as psutil
import sys, os
import cpuinfo


username = 'null'


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('aaa')

if username == 'null':
    print('')

if username == 'null':
    print('Hi')

# for x in range(20):
#    print ('-',flush=True, end='')
#    sleep(0.5)

'''while (1):
    cpupercent = int(psutil.cpu_percent(0.1))
    for i in range(0, cpupercent):
        print('-', flush=True, end='')

    print(cpupercent)
    sleep(0.5)
    os.system('cls||clear')
'''

print('', end='')
username = input('Please enter your name: ')
print('Hallo, ' + username + '! Willkommen im TestProjekt!')
sleep(0.5)
print(' ')
print('Informationen über dein System: ')
print('Threads: ' + str(psutil.cpu_count()))
print('Frequenz: ' + str(psutil.cpu_freq()))
print('Auslastung: ' + str(psutil.cpu_percent(0)))