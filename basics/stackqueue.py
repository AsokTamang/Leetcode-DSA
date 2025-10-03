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
        self.size = size   #this will be the fixed size of our stack
        self.currsize = 0  #this will be the changing size of our stack based on the push and pop operation that we do  
        self.q=deque()     #this is our queue imitating as a stack
    def isfull(self):
        return self.currsize == self.size
    def isempty(self):
        return self.currsize==0

    def push(self,x):
        if self.isfull():
            return 'stack overflow'
        self.q.append(x)  #here we are inserting the given or passed data in our queue data structure by appending as we do in the list normally
        self.currsize+=1
        for i in range(len(self.q)-1):  #here we are running the for loop until the current length of our q stack inorder to ignore the recently added data or number
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
#push time complexity : O(N)  for the push method otherwise its O(1) for other methodss
#pop time complexity : O(1) 
#space complexity : O(N)

class queuestack:
    def __init__(self,size):
        self.size = size    #this is the fixed size of our queue being used as stack but still follows the algorithm of firstinfirst out
        self.currsize = 0   #this is the current size of our queue
        self.s1=[]
        self.s2 = []  
    def isfull(self):
        return self.currsize == self.size
    def isempty(self):
        return self.currsize == 0


    def push(self,x):
        if self.isfull():
            return 'The queuestack is already full'
        
        self.s1.append(x)
        self.currsize+=1
    def pop(self):
        if self.isempty():
            return 'No any datas in the queue'
        elif len(self.s2) == 0:
            while self.s1:
                self.s2.append(self.s1.pop())
            self.s2.pop()
            self.currsize-=1
        else:
            self.s2.pop()
            self.currsize-=1

    def top(self):
        if len(self.s2) == 0:
            while self.s1:  #as long as there are values in s1 queue
                self.s2.append(self.s1.pop())
            return self.s2[-1]  #returning the top which is the first element that we appended , but it's looking like we are returnring the last element like we did in the stack as LIFO but actually we are following the algorithm of FIFO
        else:
            return self.s2[-1]
    def displaydata(self):
        a= [ ]
        for data in self.s2:
            a.append(data)
        return a[::-1] + self.s1
qs=queuestack(5)
qs.pop()
qs.push(5)
qs.push(4)
qs.push(3)
qs.pop()
qs.push(3)
qs.push(2)
qs.pop()
qs.pop()
qs.pop()
print(qs.top())

print(qs.displaydata())
#time complexity : O(2N) for pop and top operation
#time complexity : O(1) for push operation
#space complexity : O(N)


#Balanced Paranthesis
#Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.
#inorder to solve this problem ,we have to use the algorithm of last in first out
def balancedparan(str):
    stack=[]
    m={')':'(','}':'{',']':'['}
    for char in str:
        if char in m.values():   #as m.values() are representing the opening brackets , 
            stack.append(char)
        elif char in m:
            if stack and stack.pop()!=m[char]:
                return False
   
    return not stack   #here if the stack still exists then it means the given string is not valid , so it return false otherwise it return true               
print(balancedparan('[()'))    
#time complexity: O(N)
#space complexity : O(N)
            


#balanced paranthesis
def balancedthesis(string):
    stack=[]
    m={'}':'{',']':'[',')':'('}
    for char in string:
        if char in m.values():
            stack.append(char)
        elif char in m:
            if stack and m[char]!=stack.pop():
                return False
    return not stack  #if there are still characters in the stack then it means all the opening brackets donot has a closing ones
print(balancedthesis( '()[{}()]'))
#time complexity : O(N)
#space complexity : O(N)
            

#Implement Min Stack
#Design a stack that supports the following operations in constant time: push, pop, top, and retrieving the minimum element.


#minstack
class Minstack:
    def __init__(self,size):
        self.size = size
        self.currsize = 0
        self.stack = []
        self.minimum = 10 **9  #here we are initially assissgning the self.minimum as the largest possible value
    def isempty(self):
        return self.currsize == 0
    def isfull(self):
        return self.currsize == self.size 
    def push(self,x):
        if self.isfull():
            return 'stack overflow'
        elif self.isempty():
            self.stack.append(x)
            self.minimum = x
            self.currsize+=1
        else:
            if x < self.minimum:  #if the current pushing number is lesser than the minimum number then we append the decoded number which is 2 * x - self.minimum
                self.stack.append(2*x - self.minimum) 
                self.minimum = x     #and  the self.minimum will be x
                self.currsize+=1
            else:
                self.stack.append(x)
                self.currsize+=1


    def pop(self):
       if self.isempty():
           return 'stack underflow'
       else:
           delete = self.stack.pop()  #deleting the last element
           self.currsize-=1
           if delete < self.minimum :  #if the deleted or popped element is lesser than the self.minimum then it means it is the decoded element
               decoded=self.minimum
               self.minimum = 2 * self.minimum - delete
               return decoded     #we returns the decoded value
            
           else:
               return delete  #otherwise we return the same undecoded value
          
                

    def top(self):
        if self.isempty():
            return 'The stack is empty'
        else:
            peak = self.stack[-1]  #last element of the stack
            if peak < self.minimum : 
                return self.minimum   #if the last or the peak number is decoded then we return the minimum value which is our actual top element
            else:
                return peak
            
           
    def getmin(self):
        if self.isempty():
            return 'stack underflow'
        return self.minimum
    def displaydatad(self):
        a = []
        for data in self.stack[::-1]:#and here we are using the reverse form of self.stack to do the comparison bertween the latest pushed number and the current self.minimum to check whether the number in the stack is decoded or not.
            if data < self.minimum :
                  #if the current data is lesser than the minimum value then it means it is the decoded value
                a.append(self.minimum)
                self.minimum = 2*self.minimum - data  #then we need to change the data
            else:
                a.append(data)  #otherwise we can just append the undecoded data
        return a[::-1]    #inorder to return the a in the right format we are using the reverse again     
mss=Minstack(5)
mss.push(5)
mss.push(4)
mss.push(3)
mss.push(2)
mss.push(1)
print(mss.pop())
print(mss.top())
mss.push(8)
print(mss.displaydatad())
#time complexity : O(1)   only for displaying the data which is not asked by the question , as we are using the reverse method , the time complexity is O(logN)
#space complexity : O(1)  but for dispalying the data , the space complexity will be O(N)

class Minstackk:
    def __init__(self,size):
        self.size=size
        self.currsize = 0
        self.minimum=(10**9)  #here initially we are asssigining the minimum value as one of the largest possible value
        self.stack=[]
    def isempty(self):
        return self.currsize==0    
    def isfull(self):
        return self.currsize == self.size
    def push(self,x):
        if self.isfull():
            return 'stack overflow'
        elif self.isempty():
            self.stack.append(x)
            self.minimum=x
            self.currsize+=1
            return
        else:
           if x < self.minimum : 
               self.stack.append( 2 * x - self.minimum)
               self.minimum = x
           else:
               self.stack.append(x)   
           self.currsize+=1     
    def pop(self):
        if self.isempty():
            return 'stack underflow'
        dell=self.stack[-1]  
        self.stack.pop()   #deleting the last most element from the stack
        self.currsize-=1
        if dell< self.minimum:  #if the last element of the stack is lesser than the current minimum value then it means we have modified the appended element as well as change the small element , 
            v=self.minimum
            self.minimum = 2 * self.minimum - dell #if the current top element is lesser than the current minimum value then it means we had changed the minimum value , so we also need to change the current minimum value to the previous one
            return v
        return dell 
    def top(self):
        if self.isempty():
            return 'no datas in the stack'
        peak=self.stack[-1]
        if peak < self.minimum:
           return self.minimum  #if the current top element is lesser than the current minimum value then it means we had changed the minimum value , so we also need to change the current minimum value to the previous one
        else:
            return peak
    def getminimum(self):
        if self.isempty():
            return 'no datas in the stack'
        return self.minimum
        
    def displaydata(self):
        if self.isempty():
            return 'no datas in the stack'
        else:
            a=[]
            for data in self.stack[::-1]:
                if data<self.minimum:
                    a.append(self.minimum)
                    self.minimum = 2 * self.minimum - data
                else:    
                 a.append(data)
            return a    

minstk=Minstackk(5)
minstk.push(5)
minstk.push(4)
minstk.push(3)
minstk.push(2)
minstk.push(1)
minstk.pop()
minstk.push(8)
print(minstk.getminimum())
print(minstk.displaydata())
#time complexity : O(1)
#space complexity : O(1)



#Infix to Postfix Conversion
#You are given a string expression representing a valid infix mathematical expression. Your task is to convert this expression into its equivalent postfix notation, also known as Reverse Polish Notation (RPN).

def infixtopostfix(str): #here str is a string
    operators = ['+',' -', '*', '/', '^']    #lower the index lower will be the range of the operator
    stack = []  #this will be our stack variable which stores the operators and based on the highest to lowest range , we add it's pop to the output variable
    output=''
    def precendence(op):
        if op =='+' or op == '-':
            return 1
        elif op== '*' or op =='/':
            return 2
        elif op == '^':
            return 3
        return 0  
    def isleftassociative(op):
        return op!='^'     
    for char in str:
        if char.isalpha() or char.isdigit():
            output+=char
        else:
            if not stack:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char ==')':  #if the current character is ')' then we pop the numbers from the stack till it's '(' and while popping we also add those popped elements in the stack
                while stack and stack[-1]!='(':
                    output+=stack.pop()     #we keep on adding the popped operators in the output till we meet the '(' symbol in the stack
                stack.pop()      #then this '(' symbol is also removed from the stack
            else:
                if char =='^':
                    stack.append(char)
                else:
                 while stack and stack[-1]!='(' and precendence(stack[-1])> precendence(char) or precendence(stack[-1]) == precendence(char) and  isleftassociative(char):
                    output+=stack.pop()
                 stack.append(char)
    while stack:  #if there are still oeprators then we just add those oeprators to the output
        output+=stack.pop()                 
    return output          
print(infixtopostfix('"a+b*c^d-e^f*g+h'))   
#time complexity : O(N)
#space complexity : O(N)

 






    






    