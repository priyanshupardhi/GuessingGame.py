#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 12:14:28 2022

@author: Priyanshu

Guessing Game in Python
"""

# importing the random module
import random
rand_number = random.randint(1,10)

# prompt the player to guess an integer between 1 and 10.
# the output will be string
guess = input ("Enter number between 1-10:")
# convert the type of guess to int
guess = int(guess)

# run the while loop,
# Since you want to be able to make multiple guesses until you find the correct integer
while(guess != rand_number):
    # Compare guess with rand_number
    if(guess>rand_number):
       print("The guess is too high!")
       # prompt again
       guess = int(input ("Enter number between 1-10:"))
    else:
       print("The guess is too low!")
       guess = int(input ("Enter number between 1-10:"))
# end the while loop when you found the integer
print("You got it!")