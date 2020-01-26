# Set.add() in Python

# using set.add()
s = set()
for i in range(int(input())):
    new_input = input()    
    s.add(new_input)
print(len(s))

# alternate solution without using set.add() 
print(len({input() for i in range(int(input()))}))

