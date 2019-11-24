# Loops in Python
# simple solution
n = int(input())
[print(i**2) for i in range(n)]

#little complex
n = int(input())
print(*[num**2 for num in range(n)], sep = '\n')
