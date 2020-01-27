#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
if (color == 'Red'):
    print('Correct!')
else:
    print('Sorry, try again.')

#This time, there is an if/else statement that tells you if you correctly guessed the favorite color
#Lines 9-12 determine whether you answered the question with the correct answer or not and tells you
#They only happen if the conditions in the statement are met (or not, for the else)
#then you are wrong
#whatever you input for "color" must be exactly the same as "Red" for it to work