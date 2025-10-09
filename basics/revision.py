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

#Count all subsequences with sum K
#Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.
def countsubs(array,k):
    ans=[]
    nums=[]
    def solvesubs(index,summ,nums,k):
        if index>=len(array):
            if summ==k:
             ans.append(nums.copy())
            return
        nums.append(array[index])
        solvesubs(index+1,summ+array[index],nums,k)

        nums.pop()
        solvesubs(index+1,summ,nums,k)
    solvesubs(0,0,nums,k)
    return len(ans)  #as the question is asking us to return the length of the subsequences array having the sum k
print(countsubs([4, 9, 2, 5, 1],10)) 
#time complexity : O(2^N)
#space complexity : O(N*2^N)


#combination sum
def combinationsum(array,target):
    ans=[]
    nums=[]
    def solvecombination(index,presum,ans,nums):
        if index>=len(array) or presum>target:  #if the index becomes greater than the length of the array then we just stop the loop and also if the sum becomes greater than the  target then we also end the loop
            return
        if presum == target:
            ans.append(nums.copy())
            return
        nums.append(array[index])
        solvecombination(index,presum+array[index],ans,nums)   #continuing at the same index

        nums.pop() #not including the current index number
        solvecombination(index+1,presum,ans,nums)  #then going to the next index
    
          
    solvecombination(0,0,ans,nums)
    return ans
print(combinationsum([2, 3, 5, 4] ,7))
#time complexity : O(N * 2^N)  here N is the length of the given array
#space complexity : O(N*2^N)




#combination sum III
def combinationsumIII(k,target):
    ans=[]
    nums=[]
    def solvecombinationsumIII(index,presum):
        if len(nums)==k: #the index must be within the range of 1 to 9 and the length of the nums also must be equal to the value k
            if presum==target:
                ans.append(nums.copy())
            return
        for i in range(index,10):
         nums.append(i)
         solvecombinationsumIII(i+1,presum+i)  #this recursion is for moving deep into the index recursively while increasing the presum
         nums.pop()
    solvecombinationsumIII(1,0)    
    return ans
print(combinationsumIII(3,9))
#time complexity : O(9^K)
#space complexity : O(K)+O(9^K)


#letter combination of a phone number
#Given a string consisting of digits from 2 to 9 (inclusive). Return all possible letter combinations that the number can represent.

def lettercombination(digits):
    ans=[]
    nums=[]
    m={
        '2':'abc',
         '3':'def',
         '4':'ghi',
         '5':'jkl',
        '6':'mno',
         '7':'pqrs',
         '8':'tuv',
         '9':'wxyz',



    }
    def solvelettercombination(index):
        if index>=len(digits):
            ans.append(''.join(nums.copy()))
            return
        for char in m[digits[index]]:  #here we are looping through each characters of the given number at the current index from the given digit
            nums.append(char)
            solvelettercombination(index+1)
            nums.pop()  #this is for the backtracking

    solvelettercombination(0)  #and we are passing the 0 for the first iteration
    return ans
print(lettercombination('3'))


#palindrome partitioning
#Given a string s partition string s such that every substring of partition is palindrome. Return all possible palindrome partition of string s.

def palindromepartition(s):
    ans=[]
    nums=[]
    def ispalindrome(subs):
        return subs==subs[::-1]  #here this function is used for checking the palindrome
    def solvepalindromepartition(index):
        if index>=len(s):
            ans.append(nums.copy())
            return
        for i in range(index,len(s)):
            substring=s[index:i+1]   #here we are making every possible substring from the current 'index' which loop through every possible i from 'index'
            if ispalindrome(substring):  #only if the formed substring is palindrome ,  we append this  substring in our nums variable
                nums.append(substring)
                solvepalindromepartition(i+1)  #And then go deep into recursion
                nums.pop()  #backtracking

    solvepalindromepartition(0)
    return ans
print(palindromepartition("aabaa"))
#time complexity : O(N*2^N) here as we are going through every characters from the curren index to make every possible subset and we have two options , either the formed substring is palindrome , we append this substring into our nums variable otherwise , we skip it.
#space complexity : O(N*2^N)  


#word search
def wordsearch(board,target):
    rows = len(board)
    cols = len(board[0])  
    path=set()
    def dfs(r,c,index):
        if index == len(target):
            return True
        if r<0 or c<0 or r>=rows or c>=cols or target[index]!=board[r][c]:
            return False
        path.add((r,c)) #if the indexed character of the word matches with the board row and column indexed then we return add this row and column position in our set inorder to prevent the duplicates
        res=dfs(r+1,c,index+1) or dfs(r,c+1,index+1) or dfs(r-1,c,index+1) or dfs(r,c-1,index+1)
        return res
    
        
        
    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False        
print(wordsearch([ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] ,  "ABCCED"))


#nqueen
def nqueen(n):  #here we must make n*n boards inserting n queens in such a way that they won't cancel out eachother
    ans=[]
    nums=[['.']*n for _ in range(n)]  #this code is for making the chess board of n*n rows and columns
    def isvalid(row,col):
        for i in range(col):  #this code is for checking if another queen exists horizontally
            if nums[row][i]=='Q':
                return False
        r=row
        c=col
        while r>=0 and c>=0:  #this code is for checking if the queen is already in the vertically upward diagonal position compared to this current row and column position
            if nums[r][c]=='Q':
                return False
            r-=1
            c-=1 
        r=row
        c=col
        while r<n and c>=0:  #this code is for checking if the queen is already in the vertically downward diagonal position compared to this current row and column position
            if nums[r][c]=='Q': #if yes then we return false showing that this current passed row and column position is not valid
                return False
            r+=1
            c-=1 
        return True          
    def solvenqueen(col):
        if col==n:  #if the column index gets out of range , then it means we already passed the last column , which means we have inserted all n queens in our n*n chess board
            solution=[''.join(row) for row in nums]  #this creates n number of obtained rows where the numbers in each row is joined
            ans.append(solution)
            return

        for i in range(n):  #going through every rows 
            if isvalid(i,col):  #if the current row and column position is found valid to insert the queen then we insert the queen at this current row and column position
                nums[i][col]='Q'
                solvenqueen(col+1)  #only if the current row and column position is valid , we recursively go deep to another column
                nums[i][col]='.' #backtracking

    solvenqueen(0)  #passing for the first column
    return ans
print(nqueen(4))
#time complexity : O(N*2^N)
#space complexity : O(N*2^N)



#infix to postfix conversion
#higher the precedence of the operator , earlier the operator will be in the postfix 
def infixtopostfix(str):
    def precedence(op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op =='/':
            return 2
        elif op =='^':
            return 3
        else:
            return 0
    output = ''
    stack = []
    for char in str:
        if char.isalpha() or char.isdigit():
            output+=char
        elif char == '(':
            stack.append(char)
        elif char == ')':
             while stack and  stack[-1]!= '(':
              output+=stack.pop() 
             stack.pop()   #removing the ( from the stack 
        else:
           while stack and stack[-1]!='(' and ( char!='^' and precedence(char)<=precedence(stack[-1])) or (char == '^' and (precedence(char) < precedence(stack[-1]))):  #for the operator '^'  we cant pop from the stack , but we can push the ^ into the back of the stack
                output+=stack.pop()
           stack.append(char)
    while stack:
        output+=stack.pop()
    return output
print(infixtopostfix('a+b*c^d-e^f*g+h'))  
#time complexity : O(N)
#space complexity : O(N)              

#prefix to infix conversion
def prefixtoinfix(str):
    str=str[::-1]
    stack = []
    for char in str:
        if char.isalpha() or char.isdigit():
            stack.append(char)
        else:
            last=stack.pop()
            secondlast=stack.pop()
            newvalue ='('+ last + char + secondlast + ')'
            stack.append(newvalue)
    return stack[0]
print(prefixtoinfix('*+ab-cd'))   
#time complexity :O(N)
#space complexity : O(N)  


#prefix to postfix conversion
def prefixtopostfix(str):
    str=str[::-1]  #reversing the given string
    stack = []
    for char in str:
        if char.isalpha() or char.isdigit():
            stack.append(char)
        else:
            last=stack.pop()
            secondlast=stack.pop()
            newvalue = char + secondlast + last
            stack.append(newvalue)
    return stack[0][::-1]
print(prefixtopostfix('^a*bc'))            
#time complexity : O(N)
#space complexity : O(N)


#postfix into prefix conversion
def postfixtoprefix(str):
    stack = []
    for char in str:
        if char.isalpha() or char.isdigit():
            stack.append(char)
        else:
            last=stack.pop()
            secondlast=stack.pop()
            newvalue = char + secondlast + last
            stack.append(newvalue)
    return stack[0]
print(postfixtoprefix('ab+'))           
#time complexity : O(N)
#space complexity : O(N) 

#postfix to infix
def postfixtoinfix(str):
    stack = []
    for char in str:
        if char.isalpha() or char.isdigit():
            stack.append(char)
        else:
            last=stack.pop()
            secondlast=stack.pop()
            newvalue='(' + secondlast + char + last + ')'
            stack.append(newvalue)
    return stack[0]
print(postfixtoinfix('ab*c+'))            
#time complexity : O(N)
#space complexity : O(N)


#infix to prefix conversion
def infixtoprefix(str):
    str=str[::-1]  #reversing thre given string
    reverv=''
    def precedence(opr):  #here opr means the operator
        if opr == '^':
            return 3
        elif opr == '+' or opr == '-':
            return 1
        elif opr == '*' or opr == '/':
            return 2
        else:
            return 0

    for char in str:
        if char == '(':
            reverv+=')'
        elif char == ')':
            reverv+='('
        else:
            reverv+=char    
    stack =[]
    output = ''
    for char in reverv:
        if char.isalpha() or char.isdigit():
            output+=char   #if the character is alphabetic or a digit then we just directly add the charcter into our output
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] !='(':
                output+=stack.pop()
            stack.pop()#removing the ( character which is at the last position of the stack
        else:
            while stack and precedence(char)<=precedence(stack[-1]):
                output+=stack.pop()
            stack.append(char)
    while stack:
        output+=stack.pop()
    return output[::-1]  
print(infixtoprefix('(a+b)*c'))       
#time complexity : O(N)
#space complexity : O(N)        


#trapping rainwater
#Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.
                        
def brutetrappingrainwater(height):
    #in the brute approach what we do is , we just try to find the left max and right max using the different functions that calculate the prefixmax and suffix max of every index
    n=len(height)
    def previousmax(height,indexx):#prefix sum
        ans=[0] * n  #this stores the maximum value at every index compared to its left max
        ans[0] = height[0]
        for i in range(1,n):
            ans[i] = max(ans[i-1],height[i])  #calculating the previous max
        return ans[indexx]    

    def nextmax(height,indexx):#suffix sum
        ans=[0] * n  #this stores the maximum value at every index compared to its right
        ans[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            ans[i] = max(ans[i+1],height[i])
        return ans[indexx]    
    total=0
    for i in range(n):
        if height[i]<previousmax(height,i) and height[i]<nextmax(height,i):
            total+=min(previousmax(height,i),nextmax(height,i)) - height[i] 
    return total  
print(brutetrappingrainwater(  [4, 2, 0, 3, 2, 5]))     
#time complexity : O(N)
#space complexity : O(N)


#optimal solution of trapping rainwater
def optimaltrapping(height):
    #in the optimal solution what we do , is we use the two pointers and calculate the leftmax right as well as the amount of water that can be held at every index
    n=len(height)
    l,r = 0,n-1
    leftmax=height[0]   #the initial leftmax will be the value at the very first index
    rightmax = height[r]  #the initial rightmax will be the value at the very last index
    total=0
    while l!=r:
        if leftmax<rightmax:
            l+=1  #we traverse from that side which has the maximum value lesser compared to the maximum value of other side
            leftmax=max(leftmax,height[l])
            total+=leftmax-height[l]
        else:
            r+=1  #we traverse from that side which has the maximum value lesser compared to the maximum value of other side
            rightmax=max(rightmax,height[r])
            total+=rightmax-height[r]
    return total
print(optimaltrapping([4, 2, 0, 3, 2, 5]))
#time complexity : O(N)
#space complexity : O(1)
   
#Sum of Subarray Minimums
#brute approach of subarray minimums
#in the brute approach what we did was , looping through every elements in a nested loop and finding the minimum elment in the subarray creater, then calculating the total
def brutesubarraymini(arr):
    n=len(arr)
    total = 0
    for i in range(n):
        mini=arr[i]
        for j in range(i,n):
            mini=min(mini,arr[j])
            total+=mini
    return total
print(brutesubarraymini([3,1,2,4]))     
#time complexity : O(N^2)
#space complexity : O(1)    


#optimal solution
#in the optimal solution what we do is , we try to find the index where lies the number smaller than the number at the current index , in both forward and backwaard direction , then after getting those indices , we calculate the number of subarray that can be created where this current indexed number will be the minimum
def optimalsubarraymini(arr):
    n=len(arr)

    stack = []
    nextsmallerelem = [n] * n
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]>=arr[i]:
            stack.pop()
        nextsmallerelem[i]=stack[-1] if stack else n  #if the stack still exists then it means there exists a number smaller in the forward direction than current i indexed number in the givenarray
        #otherwise , no minimum number exists and we can create a subarray till n where this i indexed number is the minimum number
        stack.append(i)
    


   
    stack = []
    previoussmallerequal = [-1] * n
    for i in range(n):
        while stack and arr[stack[-1]]>arr[i]:
            stack.pop()
        previoussmallerequal[i]=stack[-1] if stack else -1  #if the stack still exists then it means there exists a number smaller in the backward direction than current i indexed number in the givenarray
        #otherwise , no minimum number exists and we can create a subarray till -1 which is till the very first index where this i indexed number is the minimum number
        stack.append(i)
    
    total = 0
    for i in range(n):
        total+=(nextsmallerelem[i] - i) * (i-previoussmallerequal[i]) * arr[i]
    return total  
print(optimalsubarraymini([3,1,2,4]))  
#time complexity : O(N)
#space complexity : O(N)


#Asteroid Collision
def asteroidcollision(arr):
    stack = [ ]  #here initially we will store only the positive values in the stack
    for i in range(len(arr)):
        if arr[i] > 0 :  
            stack.append(arr[i])
        else:   #if we find the number at the current i indexed to be negative , which means going in opposite direction as mentioned in the question , there's a process of collision,
            while stack and stack[-1] > 0:
                if stack and stack[-1] < abs(arr[i]):
                    stack.pop()
                    continue  #continuing the while loop
                elif stack and stack[-1]==abs(arr[i]):
                    stack.pop()
                #the break down below will happen if stack[-1] == abs(arr[i]) or stack[-1]>arr[i] , meaning we skip the current i indexed number as it is destroyed.
                break  #this break means breaking out of the while loop and we reach this break point only under two conditions , when the top element and the abs value of arr[i] are same, or stack[-1] > arr[i]    

            else:  #if the stack is empty or the top most element of the stack is also less than 0 then it means there's no chance of collision, then we just append the current i indexed number in the stack
                stack.append(arr[i])
    return stack
print(asteroidcollision([5, 10, -5, -10, 8, -8, -3, 12]))            
#time complexity : O(N)
#space complexity : O(N)


#Sum of Subarray Ranges
def sumsubarrayrange(nums):
    n=len(nums)
    def prevnextmin(nums):  #function to return the previous min and next min 
        prevmin=[-1] * n
        nextmin=[n] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nextmin[stack.pop()] = i
            if stack:
                prevmin[i] = stack[-1]
            stack.append(i) 
        return prevmin,nextmin           
    def prevnextmax(nums):
        prevmax=[-1] * n
        nextmax = [n] * n
        stack=[]
        for i in range(n):
            while stack and nums[stack[-1]]<nums[i]:
                nextmax[stack.pop()] = i
            if stack:
                prevmax[i]=stack[-1]
            stack.append(i) 
        return prevmax,nextmax       
    prevmin,nextmin=prevnextmin(nums)
    prevmax,nextmax=prevnextmax(nums)
    total=0
    for i in range(n):
        maxim=(i-prevmax[i] ) * (nextmax[i]-i)
        minim = (i-prevmin[i]) * (nextmin[i]-i)
        total+=(maxim - minim) * nums[i]
    return total
print(sumsubarrayrange([1, 3, 3]))    
#time complexity : O(N)
#space complexity : O(N)



#trapping rainwater
#in the brute approach we find the leftmax and the right max and find the min value between them and subtracts it by the i indexed height
def trappedwater(height):
    n=len(height)
    def leftmax(height,j):  #this function leftmax determines the maximum height at the left of every index given
        ans=[0] * n
        ans[0] = height[0]
        for i in range(1,n):
            ans[i] = max(ans[i-1],height[i])
        return ans[j]    
    def rightmax(height,j):  #this function rightmax determines the maximum height at every right of the given index
        ans=[0] * n
        ans[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            ans[i] = max(ans[i+1],height[i])
        return ans[j]
    total=0
    for i in range(n):
        if height[i]<leftmax(height,i) and height[i]<rightmax(height,i):
         total+=min(leftmax(height,i),rightmax(height,i)) - height[i]
    return total     
print(trappedwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
#time complexity : O(N)
#space complexity : O(N)


#optimal rainwater
#in the optimal approach what we do is we use the two-pointers method and calculate the left max and right max , and we traverse from that direction which has the lesser max
def opttrappedrainwater(height):
    n=len(height)
    l=0
    r=n-1
    total = 0
    leftmax=height[l]
    rightmax=height[r]
    while l!=r:
        
        if leftmax<=rightmax:
            l+=1
            leftmax=max(leftmax,height[l])
            total+=leftmax - height[l]
        else:
            r-=1
            rightmax=max(rightmax,height[r])
            total+=rightmax-height[r] 
    return total
print(opttrappedrainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))    
#time compelxity : O(N)
#space complexity : O(N)       

        
#its all about revision    
#next greater element
#Given an array arr of size n containing elements, find the next greater element for each element in the array in the order of their appearance.
#The next greater element of an element in the array is the nearest element on the right that is greater than the current element.
#If there does not exist a next greater element for the current element, then the next greater element for that element is -1.

def nge(arr):
    n=len(arr)
    stack =[]
    ans = [-1] * n  #here we are making a ans varible which stores the answer for every number of a given array ,which is the next greater element
    for i in range(n-1,-1,-1):
        while stack and arr[stack[-1]]<arr[i]:  #we keep on popping the top most element if the top most element is smaller than this current i indexed number,
            stack.pop()
        if stack:  #if the stack still exists then it means we have found the next greater element of the current i indexed number
            ans[i] = arr[stack[-1]]
        stack.append(i)
    return ans            
print(nge( [6, 8, 0, 1, 3]))
#time complexity : O(N)
#space complexity : O(N)