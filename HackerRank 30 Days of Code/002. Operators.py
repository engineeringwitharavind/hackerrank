#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def getmealcost():

    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    totalCost = int(round(meal_cost + tip + tax))
    
    return int(totalCost)

print(getmealcost())

