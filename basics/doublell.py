#Delete all occurrences of a key in DLL
class Node:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(self.data)
class doublell:
    def __init__(self):
        self.head=None
    def removekey(self,k):
        #first of all , we are checking the head of our double linked list and removing the k from it.
        if self.head.data==k:
            self.head=self.head.next
            self.head.prev=None
        itr=self.head  
        while itr:
            if itr.data == k:  #first of all we are checking if the current node consits of the data k
                if itr.next:  #then we check if its not the last node which consists of k then
                    itr.prev.next=itr.next   
                    itr.next.prev=itr.prev
                else:  #if its the last node then we destroy the current node by pointing the next of the previous node to none
                    itr.prev.next=None
            itr=itr.next  #as usual we always move to the next node after all the calculation and comparisons.   
        return self.head
    #time complexity : O(N)
    #space complexity : O(1)


       
        
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.next
        return ','.join(v)    
c=doublell()
c.head=Node(2,None,None)
c.head.next=Node(3,c.head,None)
c.head.next.next=Node(1,c.head.next,None) 
c.head.next.next.next=Node(4,c.head.next.next,None) 
c.head.next.next.next.next=Node(2,c.head.next.next.next,None) 
print(c.removekey(2))
print(c.printdatas())
     

