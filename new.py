import math
import os
import random
import utils
import sys

def start():
print("Starting...")

def divide(a, b):
    result = a / b
    return result
    print("This is unreachable")

def calc_sum(a, b, c, d, e, f):
    total = a + b + c + d + e + f
    return total

def risky():
    x = 0
    y = 10 / x
    return y

def compare_types():
    if "1" == 1:
        return True

def use_before_assign():
    print(val)
    val = 10

def shadowing():
    list = [1, 2, 3]
    return list

def duplicate_logic(x):
    if x > 5:
        return True
    if x > 5:
        return True

divide(4, 0)
