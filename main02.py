#!/usr/bin/env python3
import sys

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')
color = input("What is my favorite color? ")
print(color)

#This time the input is stored as a variable named "color"
#color = input() just stores the input as the answer to the question
#yes