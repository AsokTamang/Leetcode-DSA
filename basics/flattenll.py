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
            itr.child=Node(data,None,None)
            itr=itr.child
        return self.head  
    #time complexity : O(logN*C+NC)
    #space complexity : O(N*C)  
    def mergelist(self,l1,l2):
        dummynode=Node(-1,0,0)
        temp=dummynode
        while l1 and l2:
            if l1.data<l2.data:
                temp.child=l1
                temp=temp.child
                l1=l1.child
            else:
                temp.child=l2
                temp=temp.child
                l2=l2.child
           
        if l1:
            temp.child=l1  #as our child nodes are already sorted , we just need to do temp.child = l1
        else:
            temp.child=l2 
        self.head=dummynode.child           
        return self.head  #the next of the dummynode will be the head            

    def optimalflatten(self,head):
        if head is None or head.next is None:
            return head
        #when the base case is hit or the last node is reached then this returned head will be the next of the head of the previous callstack
        #then we merge the head and the head.next
        head.next=self.optimalflatten(head.next)  #this code uses the recursion method to go deep into the  linked nodes till the base case is hit
        return self.mergelist(head,head.next)
        
                

           

    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.child
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









