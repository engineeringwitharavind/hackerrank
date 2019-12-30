# Find a String in Python
def count_substring(string, sub_string):
    count = 0
    for n in range(len(string),0,-1):
        try:
            if string[n - len(sub_string) : n] == sub_string:
                count += 1 
        except IndexError : break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
