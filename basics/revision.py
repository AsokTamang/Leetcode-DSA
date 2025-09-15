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
        palindrome=True
        prev=None
        while m2:
            front = m2.next
            m2.next=prev
            prev=m2
            m2=front
        itr=self.head   
        x=prev #here we are storing the prev in x 
        while prev:
            if itr.data!=prev.data:  #if any of the datas at the corresponding positions of the splitted half of the linked list,  are not same then we just return false
                palindrome= False
            itr=itr.next
            prev=prev.next
        prev=None
        while x:
            front=x.next
            x.next=prev
            prev=x
            x=front
        m1.next=prev   
        return palindrome    
    #time complexity : O(N)
    #space complexity : O(1)
    #delete the middle node of the linked list
    #brute approach
    def brutedelmidnode(self):
        itr=self.head
        a=[]
        while itr:
            a.append(itr.data)
            itr=itr.next
        middleindex=len(a)//2
        a.pop(middleindex)
        self.head=Node(a[0],None)
        itr=self.head
        for data in a[1:]:
            itr.next=Node(data,None)
            itr=itr.next
        return self.head
    #time complexity : O(N)
    #space complexity : O(N)

   










    #optimal approach
    def deletemidnode(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        #this slow gives us the middle node
        midnode=slow
        a=self.head
        while a:
            if a.next==midnode:
                a.next=a.next.next
                a=a.next
            else:
                a=a.next
        return self.head        
    #time complexity : O(N)        
    #space complexity : O(1)



a = llist()
a.head = Node(8, None)
a.head.next = Node(2, None)
a.head.next.next = Node(3, None)
a.head.next.next.next = Node(4, None)
a.head.next.next.next.next = Node(1, None)
print(a.optimalpalindrome())
print(a.printdatas())


#Generate Binary Strings Without Consecutive 1s
def generatebinarystrings(n):  #here n is the length of the string
    ans=[]
    nums=['0']*n
    def solvebinarystrings(condition,index,ans,nums,n):
        #base case, is when the index becomes greater than or equal to the n then it means we are our of the index , then we just append the nums of size n in our ans variable
        if index==n:
            ans.append(''.join(nums))
            return 
        nums[index]='0'  #we always have an option of inserting 0 at the given index
        solvebinarystrings(True,index+1,ans,nums,n)
        if condition == True:
            nums[index]='1'  
            solvebinarystrings(False,index+1,ans,nums,n)
            nums[index]='0'  #while backtracking we make the current index value to 0, otherwise the inserted 1 will cause an error if we donot change it to 0
        


    solvebinarystrings(True,0,ans,nums,n) 
    return ans   
print(generatebinarystrings(3))
#time complexity : O(2^N)
#space complexity : O(N + 2^N*N)  N is the length of the given string and 2^N * N is for the ans variable

#Generate Parentheses
#Given an integer n.Generate all possible combinations of well-formed parentheses of length 2 x N.
def generateparentheses(n):
    ans=[]
    nums=[]
    def solveparentheses(index,opentag,closetag,ans,nums,n):
    
        if index>=n and  opentag==closetag==n:
            ans.append(''.join(nums))
            return
        if opentag<n:
            nums.append('(')
            solveparentheses(index+1,opentag+1,closetag,ans,nums,n)
            nums.pop()  #while backtracking
        if closetag<opentag:
            nums.append(')')
            solveparentheses(index+1,opentag,closetag+1,ans,nums,n)
            nums.pop()  #while backtracking            

    solveparentheses(0,0,0,ans,nums,n)    
    return ans
print(generateparentheses(3))
#time complexity : O(2^N)
#space complexity : O(N*2^N)


#power set
#Given an array of integers nums of unique elements. Return all possible subsets (power set) of the array.
#Do not include the duplicates in the answer.
def powerset(array):  #here we need to find the power set or subssquence of this  given array
    ans=[]
    nums=[]
    def solvepowerset(index,ans,nums):
        if index>=len(array):
            ans.append([''.join(nums.copy())])
            return
        nums.append(str(array[index]))
        solvepowerset(index+1,ans,nums)
        nums.pop()
        
        solvepowerset(index+1,ans,nums)
    solvepowerset(0,ans,nums)
    return ans
print(powerset([1,2,3]))    



