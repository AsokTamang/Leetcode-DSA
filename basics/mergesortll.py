#this file only consists of the linkedlist
#Sort LL
#Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and return the head of the modified linked list.
#Sort a LL of 0's 1's and 2's


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)
class linkedlist:
    def __init__(self):
      self.head=None
    def merge(self,left,right):
        dummynode=Node(-1)  #this acts as a head of the merged linked list
        temp=dummynode
        while left and right:
            if left.data<=right.data:
                temp.next=left
                left=left.next
                temp=temp.next
            else:
                temp.next=right
                right=right.next
                temp=temp.next
        while left:
            temp.next=left
            left=left.next
            temp=temp.next
        while right:
            temp.next=right
            right=right.next
            temp=temp.next
        return dummynode.next  #then we are returning the next of the dummynode cause we must return the head of the linekd list    


    
    def findmidindex(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow   #this slow is the midindex of the linked list from the given head    

    def optimalsort(self,head):
        if head is None or head.next is None:
            return head
        mid=self.findmidindex(head)  #here we are passing the head of the linked list inorder to find the mid index
        #so that we can split the linked list into two halves
        right=mid.next
        mid.next=None  #here we are destroying the mid.next inorder for the linked list to be splitted into two halves
        lefthead=self.optimalsort(head)  #this head will only go until the mid not further than mid cause we already destroyed the mid.next
        righthead=self.optimalsort(right)
        return self.merge(lefthead,righthead)
    def printdatas(self):
        val=''
        itr=self.head
        while itr:
            val+=str(itr.data)+','
            itr=itr.next
        return val    
    #brute approach of sorting the linked list based on 0,1, and 2
    def brutesort(self):
        itr=self.head
        a=[]
        while itr:
            a.append(itr.data)
            itr=itr.next
        a=sorted(a)
        self.head=Node(a[0],None)
        itr=self.head
        for data in a[1:]:
            itr.next=Node(data,None)
            itr=itr.next
        return self.head  
    #time complexity : O(NlogN)
    #space complexity : O(N)  


 

l=linkedlist()
l.head=Node(1,None)
l.head.next=Node(0,None)
l.head.next.next=Node(2,None)
l.head.next.next.next=Node(0,None)
l.head.next.next.next.next=Node(1,None)
print(l.brutesort())
print(l.printdatas())



    
