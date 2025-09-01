class Node:
    def __init__(self,data,next):
        self.next=next
        self.data=data
class LinkedList:
    def __init__(self):
      self.head=None
   
    def optimalmiddlelist(self):
        fast= self.head
        slow=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data    
    #time complexity : O(N)
    def brutemiddlelist(self):
        itr=self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        mid=count // 2 #this gives us the middle value or middle index in our doubly linked list
        c=0
        itr=self.head
        while c<mid:  #here again we are declaring c = 0 which takes us to the mid indexed node , then we return this particular node
            c+=1
            itr=itr.next
        return itr.data 
    #time complexity : O(N)   
    #space complexity : O(1)

    def adddatas(self,datas):
        self.head=Node(datas[0],None)  #here we are making the very first element of a given array the head of the linked list
        current = self.head    
        
        for data in datas[1:]:  #then we loop from the index 1 to the last
            current.next=Node(data,None)   
            current=current.next
        return self.head    


        
ll=LinkedList()
ll.adddatas([1,2,3,4,5])
print(ll.brutemiddlelist())
print(ll.optimalmiddlelist())

    


    