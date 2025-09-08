
class Node:
    def __init__(self,data,prev,next):
        self.data=data
        self.prev=prev
        self.next=next
    def __str__(self):
        return str(self.data)
    #Delete all occurrences of a key in DLL
class doublell:
    def __init__(self):
        self.head=None
    def removekey(self,k):
        #first of all , we are checking the head of our double linked list and removing the k from it.
        if self.head.data==k:
            self.head=self.head.next
            self.head.prev=None
        itr=self.head  
        while itr:
            if itr.data == k:  #first of all we are checking if the current node consits of the data k
                if itr.next:  #then we check if its not the last node which consists of k then
                    itr.prev.next=itr.next   
                    itr.next.prev=itr.prev
                else:  #if its the last node then we destroy the current node by pointing the next of the previous node to none
                    itr.prev.next=None
            itr=itr.next  #as usual we always move to the next node after all the calculation and comparisons.   
        return self.head
    #time complexity : O(N)
    #space complexity : O(1)
    def bruteremovekey(self,k):
        a=[]
        itr=self.head
        while itr:
            a.append(str(itr.data))
            itr=itr.next
        a=[num for num in a if num!=str(k)]    #this loop is for removing the target k from a and as our datas are stored as string, we are comparing the string version of k with the datas
        self.head=Node(a[0],None,None)
        itr=self.head
        for data in a[1:]:
            itr.next=Node(data,itr,None)
            itr=itr.next
        return self.head   
    #time complexity : O(N)
    # space complexity : O(N) 

    #Find Pairs with Given Sum in Doubly Linked List
    #brute appeoach
    def brutefindsum(self,k):
        itr=self.head
        a=[]
        while itr:
            a.append(int(itr.data))
            itr=itr.next
        n=len(a) #length of the total datas
        ans = []
        for i in range(n):
            for j in range(i+1,n):
                if a[i] + a[j] == k:
                    ans.append([min(a[i],a[j]),max(a[i],a[j])])
        return ans            
    #time complexity : O(N+M)  here N is the length of the given double linked list and M is the length of the answer
    #space complexity : O(N^2)
    def optimalalfindsum(self,k):
        itr=self.head
        a=[]
        while itr:
            a.append(int(itr.data))
            itr=itr.next
        n=len(a)    
        #here a is the collection of datas of nodes of a double linked list
        left = 0   #this is our first index
        right = n-1   #this is our last index
        ans=[]
        while left<=right:
            if a[left] + a[right] == k:
                ans.append([a[left],a[right]])
                left+=1
                right-=1
            elif a[left] + a[right] > k:
                right-=1
            elif a[left] + a[right] < k:
                left += 1
        return ans
    #time complexity : O(N)
    #space complexity : O(N+M)
                    




       
        
    def printdatas(self):
        itr=self.head
        v=[]
        while itr:
            v.append(str(itr.data))
            itr=itr.next
        return ','.join(v)    
c=doublell()
c.head=Node(1,None,None)
c.head.next=Node(2,c.head,None)
c.head.next.next=Node(4,c.head.next,None) 
c.head.next.next.next=Node(5,c.head.next.next,None) 
c.head.next.next.next.next=Node(6,c.head.next.next.next,None) 
print(c.optimalalfindsum(7))
print(c.printdatas())
     

