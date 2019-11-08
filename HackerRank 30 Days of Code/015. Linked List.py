#LinkedList
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        if head == None:
            self.head=Node(data)
        else:
            temp = self.head
            while self.head.next != None:
                self.head = self.head.next
            self.head.next = Node(data)
            self.head = temp
        return self.head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  
