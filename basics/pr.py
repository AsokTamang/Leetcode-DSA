class Node:
    def __init__(self,data,child,next):
        self.data=data
        self.child=child
        self.next=next
    def __str__(self):
        return str(self.data)
class linkedlist:
    def mergerll(self,l1,l2):
        dummynode=Node(-1,None,None)
        temp=dummynode
        while l1 and l2:  #here we are taking the two nodes and try to merge them in the sorted order, based on the datas between them and we go on to the child of the nodes 
            if l1.data<l2.data:
                temp.child=l1
                temp=temp.child
                l1=l1.child
            else:
                temp.child=l2
                temp=temp.child
                l2=l2.child
        if l1:
            temp.child=l1   
        else:
            temp.child=l2     
        self.head=dummynode.child
        return self.head


    def flattenll(self,head):
        if head is None or head.next is None:  
            return head
        head.next=self.flattenll(head.next)
        return self.mergerll(head,head.next)
    #time complexity : O(N*C)
    #space complexity : O(1)
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.child
        return ','.join(v)
a=linkedlist()
a.head=Node(3,None,None)  #next comes first and child comes second
a.head.next=Node(2,None,None)
a.head.next.next=Node(1,None,None)
a.head.next.next.next=Node(4,None,None)
a.head.next.next.next.next=Node(5,None,None)
a.head.child=None
a.head.next.child=Node(10,None,None)
a.head.next.child.child=None
a.head.next.next.child=Node(7,None,None)
a.head.next.next.child.child=Node(11,None,None)
a.head.next.next.child.child.child=Node(12,None,None)
a.head.next.next.child.child.child.child=None
a.head.next.next.next.child=Node(9,None,None)
a.head.next.next.next.child.child=None
a.head.next.next.next.next.child=Node(6,None,None)
a.head.next.next.next.next.child.child=Node(8,None,None)
a.head.next.next.next.next.child.child.child=None
a.flattenll(a.head)
print(a.printdatas())
        

        
