def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string), k):
        print(''.join(sorted(set(string[i:i+k]),key=string[i:i+k].index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
