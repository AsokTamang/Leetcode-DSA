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

    def printdatas(self):
        itr = self.head
        v = ""
        while itr:
            v += str(itr.data)
            itr = itr.next
        return v
    def reversethelist(self,head):  #this is our function for reversing the linked list
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
    def addtwonumbers(self,l1,l2):
        a=self.reversethelist(l1)  #reverse form of first linked list
        b=self.reversethelist(l2)  #reverse form of second linked list
        asum=self.addsum(a)  #sum of datas as a string from reversed head a 
        bsum=self.addsum(b)  #sum of datas as a string from reversed head b
        return int(asum)+int(bsum)
    #time complexity:O(N+M)
    #space complexity :O(N+M) 




n = LL()
n.head = Node(9)
n.head.next = Node(8)
n.head.next.next = Node(9)
n.head.next.next.next = Node(9)
f=LL()
f.head = Node(4)
f.head.next = Node(5)
f.head.next.next = Node(6)
s=LL()
s.head = Node(1)
s.head.next = Node(2)
s.head.next.next = Node(3)
print(n.addtwonumbers(f.head,s.head))

