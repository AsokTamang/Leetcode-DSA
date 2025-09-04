class Node:
    def __init__(self,data,next=None):
       self.data=data
       self.next=next
    def __str__(self):
       return str(self.data)   


class llist:
    def __init__(self):
        self.head=None
    def brutecheckpalindrome(self):
        itr=self.head
        a=[]
        while itr:
            a.append(itr.data)
            itr=itr.next
        if a==a[::-1]:
            return True
        return False    
    #time complexity : O(N)
    #space complexity : O(N)
    
    
    #Remove Nth node from the back of the LL
    def removenthnode(self,index):
        if index == 0:
            self.head=self.head.next
        itr=self.head
        prev=None
        while itr:
            front=itr.next
            itr.next=prev
            prev=itr
            itr=front
        self.head=prev    #then the new head of the linked list will be the last node of the linked list
        #the above code will reverse the linked list
        # and we are reversing the linked list cause the question is asking us to remove the nth node from the back side

        c=1
        itr=self.head
        while itr:
            if c==index-1:
                itr.next=itr.next.next
                itr=itr.next
                c+=1
            else:
                c+=1
                itr=itr.next
        #the above code is for removing the node from the nth position from tha back side        


        itr=self.head
        prev=None
        while itr:
            front=itr.next
            itr.next=prev
            prev=itr
            itr=front
        self.head=prev  
        return self.head


    def printdatas(self):
        val=''
        itr=self.head
        while itr:
            val+=str(itr.data)+','
            itr=itr.next
        return val           





    def optimalpalindrome(self):
        slow =self.head
        fast=self.head
        while fast and fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        m1=slow  #here m1 is the last node of the first half of the linked list
        m2=slow.next  #and m2 is the last node of the second half of the linked list
        prev=None
        while m2:
            front = m2.next
            m2.next=prev
            prev=m2
            m2=front
        itr=self.head    
        while prev:
            if itr.data!=prev.data:  #if any of the datas at the corresponding positions of the splitted half of the linked list,  are not same then we just return false
                return False
            itr=itr.next
            prev=prev.next
        return True    
    #time complexity : O(N)
    #space complexity : O(1)



a=llist()
a.head=Node(5,None)
a.head.next=Node(6,None)
a.head.next.next=Node(7,None)
print(a.optimalpalindrome())
print(a.removenthnode(3))
print(a.printdatas())
