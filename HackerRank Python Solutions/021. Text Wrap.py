# Text Wrap in Python:

string, max_width = input(),int(input()
for i in range(0, len(string), max_width):
    print(string[i : i + max_width])
                              

# Alternate Solution: This is for HackerRank Solution which is using "textwrap" module:

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
