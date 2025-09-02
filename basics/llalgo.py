class Node:
    def __init__(self,data,next):
        self.next=next
        self.data=data
class LinkedList:
    def __init__(self):
      self.head=None
   
    def optimalmiddlelist(self):
        fast= self.head
        slow=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data    
    #time complexity : O(N)
    def brutemiddlelist(self):
        itr=self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        mid=count // 2 #this gives us the middle value or middle index in our doubly linked list
        c=0
        itr=self.head
        while c<mid:  #here again we are declaring c = 0 which takes us to the mid indexed node , then we return this particular node
            c+=1
            itr=itr.next
        return itr.data 
    #time complexity : O(N)   
    #space complexity : O(1)

    def adddatas(self,datas):
        self.head=Node(datas[0],None)  #here we are making the very first element of a given array the head of the linked list
        current = self.head    
        
        for data in datas[1:]:  #then we loop from the index 1 to the last
            current.next=Node(data,None)   
            current=current.next
        return self.head    


        
ll=LinkedList()
ll.adddatas([1,2,3,4,5])
print(ll.brutemiddlelist())
print(ll.optimalmiddlelist())



#Reverse Linked List
#Given the head of a singly linked list, reverse the list, and return the reversed list.
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class Lnkedlst:
    def __init__(self):
      self.head=None
    def adddatas(self,datas):
        self.head=Node(datas[0],None)
        itr=self.head
        for data in datas[1:]:
            itr.next=Node(data,None)
            itr=itr.next
        return self.head
    #brute approach
    def brutereversal(self):
        a=[]
        itr=self.head
        while itr:
            a.append(itr.data)
            itr=itr.next
        return ','.join(a[::-1])  #this code reverses the obtained linked list
    #time complexity : O(N)
    #space complexity : O(N)        
         
    def printdatas(self):
        itr=self.head
        value=''
        while itr:
            value+=str(itr.data)+','
            itr=itr.next        
        return value
ll1=Lnkedlst()
ll1.adddatas(['a','b','c','d','e'])
print(ll1.brutereversal())
print(ll1.printdatas())    

       


    