#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(mealCost, tipPercent, taxPercent):
 
    tip = mealCost * tipPercent / 100
    tax = mealCost * taxPercent / 100
    totalCost = mealCost + tip + tax
    return round(totalCost)
    
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

print("The total meal cost is "  + str(solve(mealCost, tipPercent, taxPercent)) + " dollars.")
