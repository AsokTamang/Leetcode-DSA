class Node:  #here we are making a class of node ,
    #this class is responsible for creating a node
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    #this class is mainly responsible for creating the linked list and the linked list always has the head. so , we must create a head of this linked list
    def __init__(self):  
        self.head=None
    def insert_at_beginning(self,data):  #here to insert the new data at the beginning of the linked list , we first need to create a node having its next as the self.head which is the previous head of the linked list
        value = Node(data,self.head)
        self.head=value        #here self.head means we are creating a new head which is this newly created node
    def insert_at_end(self,data):
        itr=self.head  #here we are storing the head of the linked list in a var called itr
        while itr.next:  #then as long as this itr.next exists which we try to avoid or move
            itr=itr.next     #by making it's value the next node from it
        #Then at last we come to the node where the itr.next does not exists then this itr's next will be the newly created node that we have.    
        new_value=Node(data,None)  #as at the last node the next will be none   
        itr.next=new_value    #in this way, we insert the value at the last of the linked list
    def print(self):
        itr = self.head  
        value=''
        while itr:
            value+=str(itr.data)+','
            itr=itr.next
        return value
    def countlength(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count
    def searchelem(self,pos):
        itr = self.head
        count = 0
        value = ''
        if pos==0:
            value+=self.head.data
            return value
        if pos<0 or pos>=self.countlength():
            raise Exception('Invalid index')
        while itr:
            if count==pos-1:
                value+=itr.next.data  #here the count must be pos-1 , then it's next node data will be the required data that is needed to search
                return value


           
            itr=itr.next
            count+=1

        

    def removethenode(self,pos):
        count = 0
        itr = self.head
        if pos == 0:  #if we want to remove the first or the head of the linked list then the self.head will be changed into self.head.next
            self.head=self.head.next
            return
        if pos<0 or pos>=self.countlength():
            raise Exception('Invalid index')  #if the targeted index is lesser than 0 and greater than or equal to the length of the linked list then we raise an exceptional error.
        while itr:
            if count == pos - 1:   #here this is like a trick or you can say a formulae ,if the current count is same as that of the index-1 then we come to the targeted itr or head whose next is the head we want to remove
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def insertdatas(self,datalist):
        for data in datalist:
            self.insert_at_beginning(data)   
    def insertatindex(self,index,data):
        if index == 0:
            self.head=Node(data,self.head)
        if index<0 and index>=self.countlength():
            raise ValueError('Invalid index') 
        itr=self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next=Node(data,itr.next)
                return  #here we are inserting the data at that particular index when the condition of count == index - 1 matches and this current newly added itr's next will be the next of the previous itrnext 
            itr=itr.next
            count+=1                 
            


        




if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beginning('77')
    ll.insert_at_end('11')
    ll.insert_at_end('22')
    print(ll.countlength())
    print(ll.print())
    ll.insertdatas(['apple','orange','banana'])
    print(ll.print())
    print(ll.searchelem(1))
    


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
def optimalreverselist(head):
    itr=head
    prev=None
    while itr:
        front=itr.next
        itr.next=prev
        prev=itr
        itr=front
    head=prev
    return prev


#in the recursive approach what we do is we start from the last element and use the recursive nature to reverse the link or connection between the elements in a given string
def reverselist(head):
    if head is None or head.next is None:
        return head
    mainhead=reverselist(head.next)
    front=head.next  #here we are storing the next node of the current head in a variable called front
    front.next=head   #then the next of this front will ofcourse be the current head as we are reversing the linked list
    head.next=None   #then the next of this current head will be none
    return mainhead
def printdatas(head):
    itr=head
    value=' '
    while itr:
        value+=str(itr.data)+','

        itr=itr.next
    return value
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
a=optimalreverselist(head)
print(printdatas(a))



class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):   #this string constructor helps us to print the node in it's string data format
        return str(self.data)    
class linkedlistt:
   
    def __init__(self):
       self.head=None
    def checkcycle(self):
        itr=self.head
        count = 0
        m={}
        while itr:
            if itr in m:
                return m[itr]   #which returns the position of the connecting node or linking point
            m[itr]=count  #here we are storing the node and its position as the key-value pai
            count+=1
            itr=itr.next 
        return False
    #time complexity : O(N)
    #space complexity : O(N)  as we are using the dictionary of size m
    #in order to detect the starting position of the nested loop in a linked list, we are using the tortorise and hare method 

    def optimalstartingpoint(self):
        slow = self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:   #then if there exists a nested loop in a linked list , then ofcourse we will come to a node where slow will become the fast
                slow=self.head  #after slow becomes equal to fast
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow  #then the value of slow here is the starting node
        return -1  #we are returning -1 if there exists no nested loop in a linked list        
        



    
    #in the optimal approach of checking the cycle , we are using the tortorise and rabbit pace method.
    def opimalcheckcycle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False    
    
   

    def printDatas(self):
        val=''
        itr=self.head   
        while itr:
            val+=str(itr.data) + ','
            itr=itr.next
        return val
b=linkedlistt()  #here we are storing the linkedlistt constructor in a b variable
b.head=Node(1,None)  #then we are defining the head of the b
b.head.next=Node(2,None)  #then the next of the head of the b is defined here
b.head.next.next=Node(3,None)
b.head.next.next.next=b.head.next  
print(b.brutecheckpalindrome())
print(b.optimalstartingpoint())
print(b.opimalcheckcycle())


