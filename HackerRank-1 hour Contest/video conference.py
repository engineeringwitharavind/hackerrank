class node:
    def __init__(self):
        self.child = [None]*26
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = node()
    
    def insert(self, s):
        temp = self.root
        flag = 1
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            if not temp.child[index]:
                if flag == 1:
                    flag = 0
                    print(s[i], end='')
                temp.child[index] = node()
            else:
                print(s[i], end='')
            temp = temp.child[index]
        temp.count = 1
        print()
        
    def search(self, s):
        temp = self.root
        for i in range(len(s)):
            index = ord('a') - ord(s[i])
            if not temp.child[index]:
                return 0
            temp = temp.child[index]
        if temp != None and temp.count != 0:
            temp.count +=1
            return temp.count
        else:
            return 0
            
if __name__ == '__main__':

    n = int(input().strip())
    
    t = Trie()

    for _ in range(n):
        name = input()
        temp = t.search(name)
        if temp != 0:
            print(name, temp)
        else:
            t.insert(name)
