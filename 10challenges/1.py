# Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians.
# The function should convert the radians into degrees and then return that value.

from math import *

def Zad1 (num):
    if type(num) == int:
        return (num*180/pi)
    else:
        return ("Zły format")



print(Zad1(1))