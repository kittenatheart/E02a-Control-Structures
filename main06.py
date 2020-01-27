#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower().strip() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')


#line 9 has an additional function added to it
#as you said in class, .strip() strips the spaces from the beginning/end of the input
#if you put spaces between the letters (i.e. "r e d"), it will not work