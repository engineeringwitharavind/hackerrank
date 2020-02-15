_, baseSet = input(), set(input().split())
for _ in range(int(input())):
    getattr(baseSet, input().split()[0])(set(input().split()))
print(sum(map(int, baseSet)))
