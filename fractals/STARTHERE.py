#!/usr/bin/python

import os

os.system("cd /home/pi/raspberry-pi/fractals/")


response = 'y'

while response == 'y':
    os.system("clear")
    print '\n\n~~~~Welcome to the Fractal Demo!~~~~\n\nTo start type y, to quit, type n:\n'
    response = raw_input()
    if response == 'Y':
        os.system("python ./fractaldemo.py")
        response = 'y'
    elif response == 'y':
        os.system("python ./fractaldemo.py")
    elif response == 'N':
        print "\n\nThanks so much! Have a good day!\n\n"
    elif response == 'n':
        print "\n\nThanks so much! Have a good day!\n\n"
    else:
        print "\n\nSorry, I didn't understand. Please type either y or n.\n"
        response = 'y'
