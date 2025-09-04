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
a.head=Node(1,None)
a.head.next=Node(1,None)
a.head.next.next=Node(3,None)
print(a.optimalpalindrome())
