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



#queues using stack
#now we have to follow the rule of queue which is first in first out but using the stack
class queuestack:
    def __init__(self,size):
        self.size = size
        self.currsize = 0
        self.s1 = []
        self.s2 = []
    def isfull(self):
        return self.currsize == self.size    
    def isempty(self):
        return self.currsize == 0
    def push(self,x):
        if self.isfull():
            return 'The queue is full'
        self.s1.append(x)
        self.currsize+=1
        while self.s1:
            self.s2.append(self.s1.pop())       #appending the elements in the differengt list called s2 from s1 , from the very last element
    def pop(self):
        if self.isempty():
            return 'The queue is empty'
        self.currsize-=1
        return self.s2.pop()
    def top(self):
        if self.isempty():
            return 'The queue is empty'
        return self.s2[-1]  #the very last element of the s2 list is the very first element that we appended in the list.
    def displaydata(self):
        a=[]
        for data in self.s2:
            a.append(data)
        return a    
qs=queuestack(5)
qs.push(5)
qs.push(4)
qs.push(3)
qs.push(2)
qs.push(1)
qs.pop()
print(qs.top())
qs.pop()
print(qs.displaydata())
#time complexity : push:O(n), pop:O(1), top: O(1)
#space complexity : O(1)
