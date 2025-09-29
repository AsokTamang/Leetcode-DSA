#so stack is the algorithm of following the rule lastin first out
#as an example for stack , a stack of plates- the last plate you put on top is the first one you take out.
#and queue is the algorithm of following the rule first in first out
#as an example for the queue , the first one to enter the restaurant will be served first.

#stack and queue using the classes
#for stack
#stack is the algorithm following the rule of lastin first out
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
            
s=Stack(4,0)
(s.push(5))
(s.push(4))
(s.push(3))
(s.push(2))
s.pop()
print(s.peek())
print(s.peek())

#time complexity : O(1)
#space complexity : O(assigned size of the stack)