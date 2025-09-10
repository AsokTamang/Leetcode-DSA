#flattening of a linked list
class Node:
    def __init__(self,data,next,child):
        self.data=data
        self.next=next
        self.child=child
    def __str__(self):
        return str(self.data)
class flattenlist:
    def __init__(self):
        self.head=None
    def  flattenll(self):
        itr=self.head
        a=[]
        while itr:
            a.append(itr.data)
            current=itr
            if itr.child:
             while itr.child:
                itr=itr.child
                a.append(itr.data)
            itr=current.next        
        
        
        a=sorted(a)
        self.head=Node(a[0],None,None)
        itr=self.head
        for data in a[1:]:
            itr.next=Node(data,None,None)
            itr=itr.next
        return self.head  
    #time complexity : O(logN*C+NC)
    #space complexity : O(N*C)  
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.next
        return ','.join(v) 


a=flattenlist()
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
a.flattenll()
print(a.printdatas())









