#Add one to a number represented by LL
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
class linkedlist:
    def __init__(self):
        self.head=None
    def addone(self):
        itr=self.head
        prev=None
        while itr:
            front=itr.next
            itr.next=prev
            prev=itr
            itr=front
        self.head=prev  #the last node  will be the head of our reversed linked list.
        itr=self.head   
        c=1  #as the question is asking us to add 1, we are using here carry as c which is equal to 1 
        while itr:
            if itr.data + c < 10:
                itr.data+=c
                c=0
                break
            else:
                itr.data=0
                c=1
                last=itr  #then inorder to store the last node in a certain variable which will be used for creating a new node, we are storing node of every iteration in last
                itr=itr.next
        if c==1:  #if the carry still exists after looping through the whole reversed linked list then we need to create a new linked list consisting of the value 1.
            last.next=Node(1,None)  
        prev=None
        itr=self.head
        while itr:
            front =itr.next
            itr.next=prev
            prev=itr
            itr=front
        self.head=prev
        return self.head   
    #time complexity : O(N)
    #space complexity : O(1)
    def printdatas(self):
        itr=self.head
        a=[]
        while itr:
            a.append(str(itr.data))
            itr=itr.next
        return ','.join(a)              
        


c=linkedlist()
c.head=Node(9,None)
c.head.next=Node(9,None)
print(c.addone())
print(c.printdatas())

