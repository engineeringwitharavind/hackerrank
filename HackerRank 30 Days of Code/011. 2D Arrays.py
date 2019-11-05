#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hourglass_sum = []
    for i in range(0,4):
        for j in range(0,4):
            total = sum([sum(x[i:i+3]) for x in arr[j:j+3]]) - arr[j+1][i] - arr[j+1][i              +2]
            hourglass_sum.append(total)

    print(max(hourglass_sum))
