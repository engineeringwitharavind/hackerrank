# Lists in Python:

n = int(input())
lst = []
for _ in range(n):
    s = input().split()
    if s[0] == "print":
        print(lst)
    else:
        eval("lst." + s[0] + "(" + ",".join(s[1:]) + ")")
