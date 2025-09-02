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
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def optimalreversal2(head):
        if head is None or head.next is None:
            return head
        mainhead=optimalreversal2(head.next)  
        front = head.next
        front.next=head
        head.next=None
        return mainhead 
def printdatas(head):
    itr=head
    value=''
    while itr:
        value+=str(itr.data) + ','
        itr=itr.next
    return value    
#recursion output
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
headd=optimalreversal2(head)
print(printdatas(headd))






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
    #in the optimal approach 1 of reversing the linked list , what we are doing is storing the previous of the itr as prev,
    def optimalreversal1(self):
        itr=self.head
        prev=None
        while itr:
            front = itr.next
            itr.next=prev  #the next of the current node will be the previous 
            prev=itr   #And this prev will change to the current node 

            itr=front  #and as we need to move to our next node we are doing itr=front as front has stored our original next or inital next of the node
        self.head=prev
        return prev  #here at the last iteration , the head of the linked list will be stored in a prev. So, we are returning the prev.
    #time complexity : O(N)
    #space complexity : O(1)


    #in the second optimal approach of reversing the linked list , what we are doing is using the recusrion method of breaking down the  larger or longer linked list into smaller linked list


  


        
        
        
        



    def printdatas(self):
        itr=self.head
        value=''
        while itr:
            value+=str(itr.data)+','
            itr=itr.next        
        return value
ll1=Lnkedlst()
ll1.adddatas(['a','b','c','d','e'])
print(ll1.optimalreversal1())
print(ll1.printdatas())    

       


    