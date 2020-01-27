#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = ''
color = input("What is my favorite color? ")
while (color != 'red'):
    color = color.lower().strip()
    if (color == 'red'):
        print('Correct!')
    elif (color == 'pink'):
        print('Close!')
    else:
        print('Sorry, try again.')


#it creates a loop that will continue until a condition is met
#they are within the loop
#it would happen outside of the loop and the user would only be able to input once
