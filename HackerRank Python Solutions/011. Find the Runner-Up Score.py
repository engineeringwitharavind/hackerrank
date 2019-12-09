n = int(input())
arr = list(map(int, input().split()))
l = max(arr)

for i in range(n):
    if l == max(arr):
        arr.remove(max(arr))

print(max(arr))
