#Clone a LL with random and next pointer
#so the question is asking us to clone a linked list which has a next pointer that points to its next node and the random pointer which points to its random nodes or even null or none too

class Node:
    def __init__(self,data,next,random):
        self.data=data
        self.next=next
        self.random=random
    def __str__(self):
        return self.data
class linkedlist:
    def __init__(self):
        self.head=None
    def clonell(self):
        m={}  #this is our map dictionary
        itr=self.head
        while itr:
            m[itr]=Node(itr.data,None,None)  #here we are copying the node from the given or original linked list with the node and value as key value pair            
            itr=itr.next
        itr=self.head
        while itr:
            m[itr].next=m[itr.next]
            m[itr].random=m[itr.random]
            itr=itr.next
        self.head=m[self.head]   #as we have already copied the self.head in our dictionary, we are using m[self.head]
        return self.head  
    #time complexity : O(N)
    #space complexity : O(N)
    def printdatas(self):   
        itr=self.head
        a=[]
        while itr:
            randomvalue=itr.random.data if itr.random else -1  #as the question has stated that if the node doesnot has a random pointer then its random data will be -1
            a.append(str(randomvalue)) 
            itr=itr.next
        return ','.join(a)    
a=linkedlist() 
a.head=Node(1,None,None)
a.head.next=Node(2,None,None)
a.head.next.next=Node(3,None,None)
a.head.next.next.next=Node(4,None,None)
a.head.next.next.next.next=Node(5,None,None)
a.head.random=None
a.head.next.random=a.head
a.head.next.next.random=a.head.next.next.next.next
a.head.next.next.next.random=a.head.next
a.head.next.next.next.next.random=a.head.next.next
print(a.printdatas())

           
