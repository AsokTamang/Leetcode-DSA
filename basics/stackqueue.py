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


    