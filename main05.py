#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color.lower() == 'red'):
    print('Correct!')
else:
    print('Sorry, try again.')


#line 9 should change "color" to all lowercase letters and then compares it to "red" so that capitalization in the input shouldn't matter
#the capitalization error
#it will not work