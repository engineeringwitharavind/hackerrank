# Loops in Python
# solution-1
n = int(input())
[print(i**2) for i in range(n)]

# solution-2
n = int(input())
print(*[num**2 for num in range(n)], sep = '\n')
