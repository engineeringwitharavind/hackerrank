#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
	
if N % 2 == 1:
    print('Weird')
elif N % 2 == 0:
    if N >=6 and N <= 20:
        print('Weird')
    elif N == 2 or N == 4 or N > 20:
        print('Not Weird')
		
###################################################################################################

## Alternate Code:

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())

check={True:'Not Weird', False:'Weird'}
print(check[N%2==0 and (N in range(2,6) or N>20)])
		
