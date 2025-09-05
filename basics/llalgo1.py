#second half of the linked list
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
class LL:  #this is our class of linked list
    def bruteadd1(self):
        itr=self.head
        v=''
        while itr:
            v+=str(itr.data)
            itr=itr.next
        v=str(int(v) + 1) 
        self.head=Node(v[0],None)  #head of our linked list
        itr=self.head
        for data in v[1:]:
            itr.next=Node(data,None)
            itr=itr.next
        return self.head  
    #time complexity : O(N)
    #space complexity : O(N)
    def printdatas(self):
        itr=self.head
        v=''
        while itr:
            v+=(str(itr.data))
            itr=itr.next
        return v    


n=LL()
n.head=Node(1)
n.head.next=Node(2)
n.head.next.next=Node(3)
print(n.bruteadd1()) 
print(n.printdatas())        
