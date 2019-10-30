# Optimal Solution:

for i in range(int(input())): s = input();print(*["".join(s[::2]),"".join(s[1::2])])



# Alternative Simple Solution

n = int(input())  # number of strings
for _ in range(n):
    string = input()
    print(string[::2], string[1::2])  # print even letters, odd letters
