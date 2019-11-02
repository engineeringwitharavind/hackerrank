# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

phonebook = {}

for _ in range(n):
    input_list = input().split()
    phonebook[input_list[0]] = input_list[1]

for _ in range(n):
    try:
        name = input()
    except:
        break
    
    if name in phonebook:
        print(name, '=', phonebook[name], sep = '')
    else : print("Not found")
