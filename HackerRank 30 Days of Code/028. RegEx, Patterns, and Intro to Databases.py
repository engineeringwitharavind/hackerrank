# RegEx, Patterns and Intro to Databases in Python

#!/bin/python3

import math
import os
import random
import re
import sys

gmail_names = []
n = int(input())
for _ in range(n):
  first_name, emailID = input().split()
  if emailID[-10:] == "@gmail.com":
    gmail_names.append(first_name)
for name in sorted(gmail_names):
  print(name)
