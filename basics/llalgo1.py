# second half of the linked list
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LL:  # this is our class of linked list
    def bruteadd1(self):
        itr = self.head
        v = ""
        while itr:
            v += str(itr.data)
            itr = itr.next
        v = str(int(v) + 1)
        self.head = Node(v[0], None)  # head of our linked list
        itr = self.head
        for data in v[1:]:
            itr.next = Node(data, None)
            itr = itr.next
        return self.head

    # time complexity : O(N)
    # space complexity : O(N)

    def optimaladd1(self):
        itr = self.head
        prev = None
        while itr:  # this code reverses the given linked list
            front = itr.next
            itr.next = prev
            prev = itr
            itr = front
        self.head = prev  # then the head of our new linked list will be the last node
        itr = self.head
        c = 1
        #here in this loop what we are doing is , we are first checking if the addition of the 1 to the current itr is singular or dounle digit
        #if its a singular digit then we just add the value and break out of the loop
        #otherwise we make the current itr data 0 and move to the next itr,and repeat  the process
        while itr:
         if itr.data+c < 10:
             itr.data+=c
             c=0
             break
         else:
             itr.data=0
             c=1
             itr=itr.next
        if c == 1:  #if the carry still exists which means c==1, then we make the new node containing data 1 , which will be the next of the current last node.
            itr.next=Node(1,None)         
        # then again we are reversing the linked list
        prev = None
        itr = self.head
        while itr:  # this code reverses the given linked list
            front = itr.next
            itr.next = prev
            prev = itr
            itr = front
        self.head = prev  # then our new linked list will be the last node
        return self.head
        # time complexity : O(N)
        # space complexity : O(1)

    def printdatas(self,head):
        itr = head
        v = ""
        while itr:
            v += str(itr.data)
            itr = itr.next
        return v
    def reversethelist(self,head):  #this is our function for reversing the linked list
        if head.next is None:
            return head
        prev=None
        itr=head
        while itr:
            front = itr.next
            itr.next=prev
            prev=itr
            itr=front
        self.head=prev
        return self.head    
    def addsum(self,head):
        itr=head
        v=''
        while itr:
            v+=str(itr.data)
            itr=itr.next
        return v    


    #Add two numbers in LL
    def bruteaddtwonumbers(self,l1,l2):
        return  #here we are returning the function at the beginning inorder to check our optimal function
        a=self.reversethelist(l1)  #reverse form of first linked list
        b=self.reversethelist(l2)  #reverse form of second linked list
        #here a is the head of the reversed form of first linked list and b is the head of the reversed form of the second linked list.
        asum=self.addsum(a)  #sum of datas as a string from reversed head a 
        bsum=self.addsum(b)  #sum of datas as a string from reversed head b
        total= int(asum)+int(bsum)
        total=str(total)
        self.head= Node(total[0],None)        
        itr= self.head
        for data in total[1:]:
            itr.next=Node(data,None)
            itr=itr.next
        return self.head        
    def optimaladdtwonumbers(self,l1,l2):
        #here a is the head of the reversed form of first linked list and b is the head of the reversed form of the second linked list.
        itr1=l1
        itr2=l2
        dummynode=Node(-1)
        temp=dummynode
        c=0
        while itr1 or itr2 or c:
            val1=itr1.data if itr1 else 0
            val2=itr2.data if itr2 else 0
            total=(val1+val2+c) 
            temp.next = Node(total%10)  #here the next of the temp will be the quotient divided by 10
            c = total // 10  #and this gives us the remainder which is the carry value
            itr1=itr1.next if itr1 else None
            itr2=itr2.next if itr2 else None
            temp=temp.next
        return self.reversethelist(dummynode.next)    
    #time complexity : O(N+M)
    #space complexity : O(1)




    
    #time complexity:O(N+M)
    #space complexity :O(N+M) 





f=LL()
f.head = Node(5)
f.head.next = Node(4)
s=LL()
s.head = Node(4)
a=(f.optimaladdtwonumbers(f.head,s.head))
print(f.printdatas(a))


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

           
