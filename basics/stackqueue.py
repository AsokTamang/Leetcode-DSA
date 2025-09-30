#so stack is the algorithm of following the rule lastin first out
#as an example for stack , a stack of plates- the last plate you put on top is the first one you take out.
#and queue is the algorithm of following the rule first in first out
#as an example for the queue , the first one to enter the restaurant will be served first.

#stack and queue using the classes
#for stack
#stack is the algorithm following the rule of lastin first out

#USING THE ARRAYS
class Stack: 
    def __init__(self,size,currsize):
        self.size = size  #this will be the fixed size or the fix length of the stack
        self.top = -1  #which is the initial top value
        self.stack = [None] * size   #here we are making a stack of length given size having no values ,
        self.currsize = 0  #the initial current size of the stack will always be 0 
    def isempty(self):
        return self.top == -1  #if the top's value is still -1 then it means there are no datas in the stack
     



    def pop(self):
        if self.isempty():
            return 'the stack is empty'
        currelem=self.stack[self.top]
        self.stack[self.top] = None  #removing or popping the element which is the first out process
        if self.currsize == 1 :
            self.top = -1
            self.currsize-=1
            
        else:
            self.top-=1
            self.currsize-=1
        return currelem    
        

        
    def push(self,x):
        if self.top == self.size - 1:  #if we are at the last index then we cannot push any datas further more
            return 'stack overflow'
        
        self.top +=1
        self.stack[self.top] = x
        self.currsize+=1   
        return self.stack[self.top]      

        
                 

    def peek(self):
        if self.isempty():
            return 'no datas in the stack'
        currelem = self.stack[self.top]
        return currelem
    def display(self):
        a= [ ]
        for num in self.stack:
            a.append(num)
        return a    
            


#time complexity : O(1)
#space complexity : O(assigned size of the stack)



#now for queue which follows the rule of first in first out
#where the start indexed data will be change most of the time rather than the end index
class Queue:
    def __init__(self,size): 
        self.size = size
        self.currsize = 0  #initial length of the queue
        self.start = -1
        self.end = -1
        self.stack = [None] * size
    def isempty(self):
        return self.currsize == 0
    def isfull(self):
        return self.currsize == self.size  #if the current size is equal to the fixed length of the array then our queuse is full.
            
    def push(self,x):
        if self.isfull(): #if our end is at the last index then we cannot push the datas further
            return 'queue overflow'
        if self.currsize == 0:
            self.start=0
            self.end=0
            self.stack[self.end] =x
            self.currsize+=1
        else:
            self.end=(self.end+1) % self.size
            self.stack[self.end] =x
            self.currsize+=1
        return self.stack[self.end]
        
        


    def pop(self):
        if self.isempty():
            return 'no any datas left in the queue'
        if self.currsize == 1:  #if we are at the very first index  and the current size is 1 then we just reset everything
            self.stack[self.start]=None
            self.currsize-=1
            self.start-=1
            self.end-=1
        else:
            self.stack[self.start]=None
            self.currsize-=1
            self.start=(self.start+1) % self.size   

    def peek(self):
        if self.currsize == 0:
            return 'no any datas left in the queue'
        return self.stack[self.start]  #here we always represent the top most data which is the first data inserted in the queue
    def display(self):
        a= [ ]
        for num in self.stack:
            a.append(num)
        return a
q=Queue(4)
(q.push(1))
(q.push(2))
(q.push(3))
(q.push(4))
q.pop()
q.pop()
q.pop()
(q.push(4))
(q.push(4))
(q.push(4))
print(q.push(4))

print(q.display())
#time complexity : O(1)
#space complexity : O(Q)  size of the queue

    


#USING THE LINKED LIST  
#for stack  #last in first out
class Node:  #creating a class of node for the stack of linked list
    def __init__(self,data,nxt):
       self.data=data
       self.nxt=nxt
class stackll:
    def __init__(self,size):  
        self.size = size
        self.top = None
        self.currsize = 0  #initially there will be no values or datas in the stack
    def isfull(self):
        return self.currsize == self.size
    def isemppty(self):
        return self.currsize == 0
    def push(self,x):
        if self.isfull():   #if the stack is full then we cannot add the datas further more
            return 'stack overflow'
        newnode = Node(x,None)
        newnode.nxt = self.top
        self.top = newnode
        self.currsize += 1  #increasing the current size of the stack

    def pop(self):
        if self.isemppty():
            return 'no any datas in the stack linkedlist'  
        else:
            temp = self.top  
            self.top=temp.nxt
            temp=None  #deleting the top most node as we have already made the next of the top , THE TOP
            self.currsize-=1
   
    def peek(self):
        return self.top.data  #returning the data of the top most node which follows last in first out
    def displaydata(self):
        itr=self.top
        a = []
        while itr:
            a.append(itr.data)
            itr=itr.nxt
        return a
sll=stackll(5)
sll.push(5)  
sll.push(4)  
sll.push(3)  
sll.push(2)  
sll.push(1)
print(sll.peek())
sll.pop()
sll.pop()   
print(sll.displaydata())
#time complexity : O(1)
#space complexity : O(N)  N denotes the size of the  stack

#queue implementation using linkedlist.
class Node1:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class Queuell:
    def __init__(self,size):  #size will be the fixed length of the queue to be designed
      self.size = size
      self.currsize = 0  #initially the current size will always be 0
      self.start = None
      self.end = None
    def isempty(self):
        return self.currsize == 0
    def isfull(self):
        return self.currsize == self.size   #if the current size becomes equal to the given fixed size, then our linkedlist queue is full
            
    def push(self,x):
        if self.isfull():
            return 'queue overflow'
        if self.isempty():
            newnode = Node1(x,None)
            self.start=self.end=newnode
            self.currsize+=1   

        else:
            newnode = Node1(x,None)
            
            self.end.next=newnode
            self.end=newnode
            self.currsize+=1    
    def pop(self):
        if self.isempty():
            return 'No any datas available in the queue'
        if self.currsize==1:
            self.end=self.start=None
            self.currsize-=1
        else:
            self.start = self.start.next  #deleting the data which was inserted at the very beginning in the queue, cause the queue follows the algorithm of first in first out.
            self.currsize-=1

             
    def peek(self):
        return self.start.data
    def printdatas(self):
        itr=self.start
        a=[]
        while itr:
            a.append(itr.data)
            itr=itr.next
        return a    
qll=Queuell(5)
qll.push(5) 
qll.push(4) 
qll.push(3) 
qll.push(2) 
qll.push(1)   
qll.pop() 
qll.pop() 
print(qll.peek())
print(qll.printdatas())
#time complexity : O(1)
#space complexity : O(Q)  Q is the size of the queue


#from this learning , I learned that for stack we just need one variable to change the data which is let's say top , as it follows last in first out rules.
#for the queues , we need two variables which are start and end , as it follows first in first out rules



#implementation of stack using queue
#so our main goal is to follow the rule of last in first out using the first in first out algorithm

from collections import deque
class stackq:
    def __init__(self,size):
        self.size = size
        self.currsize = 0 
        self.q=deque()
    def isfull(self):
        return self.currsize == self.size
    def isempty(self):
        return self.currsize==0

    def push(self,x):
        if self.isfull():
            return 'stack overflow'
        self.q.append(x)  #here we are inserting the given or passed data in our queue data structure by appending as we do in the list normally
        self.currsize+=1
        for i in range(len(self.q)-1):  #here we are running the for loop until the length of our q -1 inorder to ignore the recently added data or number
            self.q.append(self.q.popleft())   #this appends the leftmost data in the the  queue
            #self.q.popleft() removes the left most element from the data 
            #and we are doing this inorder to follow lastin first out rule of stack using queue to mimick this algorithm
    def pop(self):
        if self.isempty():
            return 'No any datas in the stack to remove'
        else:
             removed=self.q.popleft()
             self.currsize-=1
             return removed
    def displaydata(self):
        a=[]
        for data in self.q:
            a.append(data)   
        return a     
sq=stackq(5)
sq.push(5)
sq.push(4)
sq.push(3)
sq.push(2)
sq.push(1)
sq.pop()
print(sq.displaydata())
#time complexity : O(N)  for the push method otherwise its O(1) for other methodss
#space complexity : O(N)


    