#Rotate a LL
class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
class linkedlist:
    def __init__(self):
        self.head=None
    def countlength(self):   #here this function counts the number of nodes or calculate the length of the given linked list
        itr=self.head
        c=0
        while itr:
            itr=itr.next
            c+=1
        return c    
    def rotatell(self,k):  #here k is the number of rotations that we must do for the given linked list
     length=self.countlength()
     if k>length and k%length==0:  #if the value of k is the multiple of the length of the given linked list then the linked will stay unchanged after k number of rotations
         return self.head
     elif k>length:   #if the value of k is way greater and k is not exactly divided by the length of the linked list then the remainder that we get by dividing k with the length of the linked list is the required number of rotations
         k=k%length  
     k=int(k)
     tailnode=length-k
     itr=self.head
     while itr.next:
         itr=itr.next
     itr.next=self.head
     itr=self.head
     c=1
     while itr and c< tailnode:
         itr=itr.next
         c+=1
     self.head=itr.next
     itr.next=None
     return self.head 
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.next
        return ','.join(v)        

c=linkedlist()
c.head=Node(1,None)
c.head.next=Node(2,None)
c.head.next.next=Node(3,None)
c.head.next.next.next=Node(4,None)
c.head.next.next.next.next=Node(5,None)
c.rotatell(4)
print(c.printdatas())



         
