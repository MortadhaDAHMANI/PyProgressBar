# -*- coding: utf-8 -*-

import time
import sys
import os

os.system('clear')

unitColor = '\033[0;41m'
resColor = '\033[m'
endColor = '\033[0;0m\033[0;0m'
count = 45
for i in range(count):
    incre = int(50.0 / count * i)
    if i != count - 1:
        sys.stdout.write('|%s%s%s%s| %d%%' % (unitColor, '\033[37;41m' + ' '*incre + ' \033[27m', endColor, ' '*(49-incre), 2*incre))
    else:
        sys.stdout.write('|%s%s%s| %d%%' % (unitColor, '\033[37;41m' + ' '*20 + 'I Love You <3' + ' '*21 + ' \033[27m', endColor, 100))
    sys.stdout.flush()
    time.sleep(0.15)
    sys.stdout.write('\r')

sys.stdout.write('\n')
print('\033[8;40;100t')
print("\n\n\n")
print("             ██─"+unitColor+"▄███▄███▄"+resColor+"─██▄──▄██──▄███▄──██──██")
print("             ██─█████████──▀████▀──██▀─▀██─██──██")
print("             ██──▀█████▀─────██────██▄─▄██─██──██")
print("             ██────▀█▀───────██─────▀███▀──▀████▀")
print("\n\n\n")




