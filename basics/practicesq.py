#practicing of stack and queue
#implementation of stack using queue
from collections import deque  #deque acts as the queue where we are actually following the rule of LIFO for stack

class stackqueue:
    def __init__(self,size):
        self.size = size
        self.currsize = 0 
        self.q = deque()
    def isempty(self):
        return self.currsize == 0
    def isfull(self):
        return self.currsize == self.size
    def push(self,x):
        if self.isfull():
            return 'stack overflow'
        else:
            self.q.append(x)
            self.currsize+=1
            for _ in range(len(self.q)-1):
                self.q.append(self.q.popleft())  #popleft() function removes the left most element from the queue,  where this is the very new element that we just added
    
    def pop(self):
        if self.isempty():
            return 'no datas in the stack'
        self.q.popleft()
        self.currsize-=1
    def top(self): 
        if self.isempty():
            return 'no datas in the stack'  
        return self.q[0]  #returns the first number or element which is the very new element we just added, but it appeared at the very beginning cause we just used the for loop inorder to make this newly added number or element to come at the very first and the rest of the element follows the same logical order. 
    def displaydata(self):
        a= [ ]
        for data in self.q:#reversing the order inorder to display the data in the entered wise way
            a.append(data)           
        return a
sq=stackqueue(5)
sq.push(5)
sq.push(4)
sq.push(3)
sq.push(2)
sq.push(1)
sq.pop()
sq.push(2)
sq.pop()
sq.pop()
print(sq.top())
print(sq.displaydata())
#time complexity : push : O(N)  pop:O(1)  : top:O(1)
#space complexity : O(N)


