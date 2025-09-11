#Clone a LL with random and next pointer
#so the question is asking us to clone a linked list which has a next pointer that points to its next node and the random pointer which points to its random nodes or even null or none too

class Node:
    def __init__(self,data,next,random):
        self.data=data
        self.next=next
        self.random=random
    def __str__(self):
        return self.data
class linkedlist:
    def __init__(self):
        self.head=None
    def clonell(self):
        m={}  #this is our map dictionary
        itr=self.head
        while itr:
            m[itr]=Node(itr.data,None,None)  #here we are copying the node from the given or original linked list with the node and its data as key value pair            
            itr=itr.next
        itr=self.head
        while itr:
            m[itr].next=m[itr.next]  #as we need to copy both the next pointer as well as the random pointer, we are copying the next as well as the random pointer.
            m[itr].random=m[itr.random]
            itr=itr.next
        self.head=m[self.head]   #as we have already copied the self.head in our dictionary, we are using m[self.head]
        return self.head  
    #time complexity : O(N)
    #space complexity : O(N)
    def optimalclonell(self):
        itr=self.head
        while itr:  #this loop is for creating the copied node inbetween the node and it's next node
            itr.next=Node(itr.data,itr.next,None)  #here what we are doing is , we are just putting the copied node of the current itr inbetween the itr and it's next node
            itr=itr.next.next if itr.next.next else None #then we move to the next node escaping the copied node
        itr=self.head
        while itr:  #this loop is for assigning the random pointer to the copied nodes based on its original nodes
            itr.next.random=itr.random.next  if itr.random else None  #as we have placed the cloned or copied node of each itr inbetween the itr and itrs corresponding next node , then its random pointer will also point to next of corresponding random node
            itr=itr.next.next if itr.next.next else None
        itr=self.head
        dummynode=Node(-1,None,None)  #here we are creating a dummynode inorder to create a new linked list
        temp=dummynode
        while itr:
            temp.next=itr.next
            temp=temp.next
            current=itr  #here inorder to build the original list back , we are storing the current node at current and then assigning its next to the next of temp node.
            itr=temp.next if temp.next else None
            current.next=temp.next  if temp.next else None  #restoring the original linked list while making a copied version of original linked list
        self.head=dummynode.next  #then the new head of our new linked list will be the next node of the dummynode
        return self.head
    #time complexity : O(N)
    #space complexity : O(1)
    def printdatas(self):   
        itr=self.head
        a=[]
        while itr:
            randomvalue=itr.random.data if itr.random else -1  #as the question has stated that if the node doesnot has a random pointer then its random data will be -1
            a.append(str(randomvalue)) 
            itr=itr.next
        return ','.join(a)    
a=linkedlist() 
a.head=Node(1,None,None)
a.head.next=Node(2,None,None)
a.head.next.next=Node(3,None,None)
a.head.next.next.next=Node(4,None,None)
a.head.next.next.next.next=Node(5,None,None)
a.head.random=None
a.head.next.random=a.head
a.head.next.next.random=a.head.next.next.next.next
a.head.next.next.next.random=a.head.next
a.head.next.next.next.next.random=a.head.next.next
a.optimalclonell()
print(a.printdatas())

           
