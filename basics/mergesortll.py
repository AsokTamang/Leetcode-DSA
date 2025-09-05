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

    def optimalintersection(self,f,s):
       itr1=f
       itr2=s
       while itr1!=itr2:
          itr1=s if itr1==None else itr1.next
          itr2=f if itr2==None else itr2.next
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




    
