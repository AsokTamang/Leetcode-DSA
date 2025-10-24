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
class mergelinkedlist:
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
    def finalmerge(self,left,right):
        dummynode=Node(-1)
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
        return dummynode.next



    def findmidindex(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow    

    #for the optimal approach of sorting the linked list having only os and 1s, we again use merge sort algorithm
    def optimalmergesort(self,head):
        if head is None or head.next is None:
            return head
        mid=self.findmidindex(head)
        right=mid.next  #we are storing the mid.next inside our right variable
        mid.next=None
        lefthead=self.optimalmergesort(head)
        righthead=self.optimalmergesort(right)
        return self.finalmerge(lefthead,righthead)  
    
    
    #Find the intersection point of Y LL
    #Given the heads of two linked lists A and B, containing positive integers. Find the node at which the two linked lists intersect. If they do intersect, return the node at which the intersection begins, otherwise return null.
    #The Linked List will not contain any cycles. The linked lists must retain their original structure, given as per the input, after the function returns.
    
    def bruteintesectionpoint(self,f,s):  #here f means the head of the first linked list and s means head of the second linked list
        itr1=f  
        itr2=s
        visited=set()  #this stores all the nodes from the head f
        while itr1:
         visited.add(itr1)  
         itr1=itr1.next
           
        while itr2:
            if itr2 in visited:
                return itr2
            itr2=itr2.next    
        return -1
    #time complexity : O(N+M)  
    #space complexity : O(N)
    
    #optimal approach
    #so in the optimal approach what we do is we just keep moving to the next node from the given two nodes until both of them are same
    #and if one of them becomes none then we make that iteration the head of the second linkedlist, viceversa for the another node
    def optimalintersection(self,f,s):
       itr1=f
       itr2=s
       while itr1!=itr2:  
           if itr1==None:
               itr1=s
           if itr2==None:
               itr2=f    
           itr1=itr1.next
           itr2=itr2.next
       return itr1
    #time complexity : O(N)
    #space complexity : O(1)
    
       
             




        


 

l=mergelinkedlist()
l.head=Node(1,None)
l.head.next=Node(2,None)
l.head.next.next=Node(3,None)
common=Node(4)
l.head.next.next.next=common
l.head.next.next.next.next=Node(5,None)

b=mergelinkedlist()
b.head=Node(7,None)
b.head.next=Node(8,None)
b.head.next.next=common
b.head.next.next.next=Node(5,None)
c=mergelinkedlist()
print(c.optimalintersection(l.head,b.head))




    
