#Next Greater Element
#brute approach
def nextgreaterelement(arr):
    ans = []
    for i in range(len(arr)): 
         ansnum = -1  
         for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                ansnum = (arr[j])  #as soon as we find the number which is greater as well as nearest , then we append this particular number in our ans variable and return
                break
         ans.append(ansnum)  #if we didn't find any number greater than the i indexed number then we just append -1 in our ans variable 
    return ans
print(nextgreaterelement([6, 8, 0, 1, 3])) 
#time complexity : O(N^2)
#space complexity : O(N)        


#optimal solution
def optimalnext(arr):
    stack = []   #this stores the very next numbers greater than the corresponding number at the current iteration
    ans = [-1] * len(arr)   #making a ans variable which stores the answer
    for i in range(len(arr)-1,-1,-1):  #looping from the last index of the given array
        while stack and stack[-1]<=arr[i]:  #for the very first loop or lets say the very last indexed number this while loop won't run casue there are no numbers or values in the stack and also ,
            #the next greater number for this last indexed number will always be -1
            stack.pop()

        
        if stack:  #if there is still numbers or values in the stack which means we have found a number greater than the i indexed number just very close to it.
            ans[i] = stack[-1]  #the last value will be the next greater number for this i indexed number    
        stack.append(arr[i])  #appending the i indexed number from array in the stack 
    return ans
print(optimalnext([6, 8, 0, 1, 3]))
#time complexity : O(N)
#space complexity : O(N)



#Next Greater Element - 2
#Given a circular integer array arr, return the next greater element for every element in arr.
#The next greater element for an element x is the first element greater than x that we come across while traversing the array in a clockwise manner.
#If it doesn't exist, return -1 for that element.

def optimalnextgreater(arr):
    n=len(arr) 
    stack = []
    ans = [-1] * n #this variable stores our ans
    for i in range( 2 * n , -1 , -1):  #and here we are running the loop twice cause 
        while stack and stack[-1]<=arr[i%n]:  #the logic remains the same , where we just keep on popping the number from the last position of the stack, 
            stack.pop()
        if stack:  #and if the stack still remains then the last number of the stack is ofcourse the required greater number for the current i indexed number
            ans[i%n] = stack[-1]
        stack.append(arr[i%n])  
    return ans
print(optimalnextgreater([3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]))          
#time complexity : O(N)
#space complexity : O(N)


#Next Smaller Element
#Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
#The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
#If there is no smaller element to the right, then the NSE is -1.

def nextsmallerelement(arr):
    stack = []
    ans = [-1] * len(arr)
    for i in range(len(arr)-1,-1,-1):   #looping from the very last element
        while stack and stack[-1]>=arr[i]:  
            stack.pop()
        if stack:
            ans[i]=stack[-1]  #if the stack still remains , then the top most number of the stack is the very next smaller number for the i indexed number
        stack.append(arr[i])    
    return ans
print(nextsmallerelement([4, 8, 5, 2, 25]))    
#time complexity : O(N)
#space complexity : O(N)        

#Number of Greater Elements to the Right
def numberofgreater(arr,indices):
    first = indices[0]  #first index   
    second = indices[1] #second index
    c1=0
    c2=0
    for i in range(len(arr)-1,first,-1):
        if arr[i] > arr[first]:
            c1+=1
    for j in range(len(arr)-1,second,-1):
        if arr[j] > arr[second]:
            c2+=1     
    return [c1,c2] 
print(numberofgreater([1, 2, 3, 4, 1],  [0, 3]))     
#time complexity : O(N)
#space complexity : O(1)    



#optimal solution 
def nges(arr,indices):
    ans =[]
    for index in indices:
        count = 0
        for i in range(index+1,len(arr)):
            if arr[i] > arr[index]:
                count+=1
        ans.append(count)
    return ans
print(nges( [3, 4, 2, 7, 5, 8, 10, 6],[0, 5]))    
#time complexity : O(N*M) M is the number of given indices
#space complexity :  O(1)        




#find the prefix max
   



#brute approach
#Trapping Rainwater
#Given an array of non-negative integers, height representing the elevation of ground. Calculate the amount of water that can be trapped after rain.

def trappingrainwater(height):
    def prefixmax(h):  #here h acts as the index , where we must find the prefix max
        ans =[0] * len(height) #creating an ans variable of length same as that of the arr
        ans[0] = height[0]  #the very first element of the ans will be same as that of the arr
        for i in range(1,len(height)):
            ans[i] = max(ans[i-1],height[i])  #this will insert the value according to the maximum value between the previous and the current indexed number in the array
        return ans[h]    



    #find the suffix max
    def suffixmax(h):#here h acts as the index , where we must find the suffix max
        n=len(height)
        ans=[0] * len(height)  
        ans[n-1] = height[n-1]   #last value of the ans will be same as that of the given arr, as we are trying to find the suffix max
        for i in range(n-2,-1,-1):
            ans[i] = max(ans[i+1],height[i])
        return ans[h]  #then we just return the suffixmax at the index h
    totalamount = 0
    for i in range(len(height)):
        if  height[i] < prefixmax(i) and height[i] < suffixmax(i):
            totalamount+=min(prefixmax(i),suffixmax(i)) - height[i]
    return totalamount
print(trappingrainwater( [4, 2, 0, 3, 2, 5]))  
#time complexity : O(N)
#space complexity : O(N)       

#optimal solution 
def optimaltrainingwater(height):
    n=len(height)  #length of the given height
    l=0     #the very first index 
    r=n-1  #the very last index
    #in this optimal solution what we do , is first of all we assign the left l and right r pointer to the very first and very last index of the given array respectively,
    leftmax = height[l]  #initally the left max will be the value of very first index
    rightmax=height[r]   #the right max will be the value of very last index
    total = 0
    while l!=r:
        #the logic is we traverse from that index whose max value is smaller compared to the other one
        if leftmax <=rightmax:  
            l+=1
            if height[l] < leftmax:   #if the new left indexed value is greater than the left max then it means we can store the water which is 
                total+=leftmax-height[l] #which is this 
            else:    
                leftmax = height[l]  #and we also update the left max
        else:
            r-=1
            if height[r] < rightmax:
                total +=  rightmax - height[r]
            else:    
                rightmax=height[r]
    return total
print(optimaltrainingwater( [4, 2, 0, 3, 2, 5]))
#time complexity : O(N)
#space complexity : O(1)                   


#optimal solution 
def optimaltrainingwater(height):
    n=len(height)  #length of the given height
    l=0     #the very first index 
    r=n-1  #the very last index
    #in this optimal solution what we do , is first of all we assign the left l and right r pointer to the very first and very last index of the given array respectively,
    leftmax = height[l]  #initally the left max will be the value of very first index
    rightmax=height[r]   #the right max will be the value of very last index
    total = 0
    while l!=r:
        #the logic is we traverse from that index whose max value is smaller compared to the other one
        if leftmax <=rightmax:  
            l+=1
            leftmax = max(leftmax,height[l])
            total+=leftmax - height[l]  #water amount trapped at that position
        else:
            r-=1
            rightmax=max(rightmax,height[r])
            total+=rightmax - height[r]
    return total
print(optimaltrainingwater( [4, 2, 0, 3, 2, 5]))
#time complexity : O(N)
#space complexity : O(1)                    



#Sum of Subarray Minimums
#Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
#brute approach
def sumsubarraymin(arr):
    n=len(arr)
    s = 0
    for i in range(n):
        for j in range(i,n):
         subarray = arr[i:j+1]
         mini=min(subarray)
         s+=mini
    return s
print(sumsubarraymin([11,81,94,43,3]))    
#time complexity : O(N^3)
#space complexity : O(N)  


#better solution
def bettersubarraymini(arr):
    n=len(arr)
    totalsum = 0
    for i in range(n):
        mini=arr[i]
        for j in range(i,n):
            mini=min(mini,arr[j])
            totalsum+=mini
    return totalsum
print(bettersubarraymini([11,81,94,43,3]))  
#time complexity :O(N^2)
#space complexity : O(1)       



def optimalsubarraymini(arr):
    n=len(arr)
   
    def previousminiequal(arr,indexx):
        stack = []
        ans=[0] * n   
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1   #if the stack still exists then the previous smaller or equal element will be the remaining top element or last elment of the stack otherwise we can go till the very first index
            stack.append(i)
        return ans[indexx]    #this ans stores the index where we found the smaller element in the previous or past direction compared to the passed index      

            
    def nextmini(arr,indexx):
        stack =[]
        ans = [0] * n  #storing the next smaller element
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            ans[i]=stack[-1] if stack else n
            stack.append(i)
        return ans[indexx]  #this returns the index we found the number smaller than the passed indexed number , which lies in the next or future direction
    totalsum = 0
    for i in range(n):
        totalsum+=(nextmini(arr,i) - i) * (i- previousminiequal(arr,i)) * arr[i]    #here what we are doing is just calculating the number of subarray that can be created in both forward and backward direction where this i indexed number will be the minimum number in the subarray
    return totalsum
print(optimalsubarraymini([3,1,2,4]))
#time complexity : O(N)
#space complexity : O(N)
        



#asteroid collision
#LIFO approach

def optimalasteroid(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i] > 0:
            stack.append(arr[i])
        else:
            while stack and stack[-1] > 0:
                if stack[-1] < abs(arr[i]):
                    stack.pop()
                    continue  #continue means continuing with the current while loop
                elif stack[-1] == abs(arr[i]):  #if both of them are same
                    stack.pop()
                break  #this break is for both the condition when the top most element of the stack and the i indexed element are same or thei indexed element is lesser than the top most elemment of the stack     
            else:  #if there is no stack or the top most element of the stack is lesser than 0 then it means the i indexed and this number are moving in the same direction , so we just append this i indexed number in the stack
                stack.append(arr[i])

    return stack           
print(optimalasteroid( [5, 10, -5, -10, 8, -8, -3, 12]))
#time complexity : O(N)
#space complexity : O(N)


#Sum of Subarray Ranges
#Given an integer array nums, determine the range of a subarray, defined as the difference between the largest and smallest elements within the subarray. Calculate and return the sum of all subarray ranges of nums.
#A subarray is defined as a contiguous, non-empty sequence of elements within the array.

#here what the question is asking us is to determine the sum of range of all possible subarrays from the given array, and this range can be found by calculating the maximum value and minimum value from an obtained subarray




#brute approach
def brutesubarrayrange(nums):
    n=len(nums)
    total = 0
    for i in range(n):
        minim=nums[i]
        maxim=nums[i]
        for j in range(i,n):  #inside this loop we are finding the maximum as well as the minimum value that will be found in every possible subarray generated , respectively
            minim=min(minim,nums[j])
            maxim=max(maxim,nums[j])
            total+=maxim-minim
    return total
print(brutesubarrayrange([1, 3, 3]))      
#time complexity : O(n^2)
#space complexity : O(1)   


#optimal solution of sum of subarray range
def optimalsubarrayrange(nums):
    n=len(nums)
    def previousmininextmini(nums):
        stack = []
        nextmini=[n] * n
        previousmini = [-1] * n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                nextmini[stack.pop()]=i  #if the i indexed number is lesser than the number at the  index which is at the top of stack, then the nextminimum number for this top indexed will be the i indexed number so we put i for nextmini[stack.pop()]
            if stack:
                previousmini[i] = stack[-1]
            stack.append(i)
        return nextmini,previousmini         
        
  
    def previousgreaternextgreater(nums):
        stack = []
        previousgreater=[-1] * n
        nextgreater = [n] * n
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                nextgreater[stack.pop()]=i
            if stack:
                previousgreater[i] = stack[-1]  #looping from the clockswise direction will always given the previous index whether its a smaller or greater , it depends upon the sign
            stack.append(i)
        return previousgreater,nextgreater
    nextmini,prevmini=previousmininextmini(nums)
    prevgreater,nextgreater=previousgreaternextgreater(nums)
    total = 0
    for i in range(n):
        minim=(i-prevmini[i]) * (nextmini[i]-i)
        maxim=(i-prevgreater[i]) * (nextgreater[i]-i)
        total+=nums[i] * (maxim - minim)  #this gives us the number of subarrays where this i indexed number will be the maximum as well as minimum
    return total    
print(optimalsubarrayrange([1, 2, 3]))
#time complexity : O(N)
#space complexity : O(N)


#optimal solution
#remove k digits
def removekdigits(nums,k):
   stack = []
   for i in range(len(nums)):
       while k>0 and stack and stack[-1] >nums[i]:
           k-=1  #here this calculation determines how many numbers are left to removed as well as how many we have already removed
           stack.pop()
       stack.append(nums[i]) 
   if k > 0 :  #if we still have some numbers to be removes then it means we stopped finding the numbers which are lesser ,in contrast we found the numbers in the increasing order
           stack=stack[:-k]  #here we are using the stack cause all the numbers are already appended in the stack caused by the for loop,thats why we remove the most larger numbers that are ofcourse found at the ending of the given  stack , so we remove from the last
           
     #.lstrip('0') removes the leading 0     
   result = ''.join(stack).lstrip('0')
   return result if result else '0'  
print(removekdigits( "1002991", 3))    
#time complexity : O(N)
#space complexity : O(N)



#Largest rectangle in a histogram
#Given an array of integers heights representing the histogram's bar height where the width of each bar is 1 return the area of the largest rectangle in the histogram.
#brute approach
#so inorder to be a rectangle from the current index, the current indexed number must be minimum ,towards its left and towards its right 
#so we need to find the number of subarrays, where it can be minimum and multiply it by this i indexed number
def brutelargestrec(heights):
    area=0
    n=len(heights)
    def prevsamller(heights,indexx):
        stack = []
        ans = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]   #this will be the index at the preceding position where the number smaller than the current i indexed number is found,until this obtained index the current i indexed number will always be minimum
            stack.append(i)  
        return ans[indexx]          
    def nextsmaller(heights,indexx):
        stack=[]
        ans=[n] * n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:  #as we are popping the index where the values are greater compared to the current i indexed number
                stack.pop()
            if stack:  #if the stack still exists then it means we found a index where the number is smaller than the current indexed number but in the proceding position or direction
                ans[i] = stack[-1]
            stack.append(i)
        return ans[indexx]   #this ans gives us the index,and the value before this index will have the passed indexxed number as the minimum value ,          
    for i in range(n):
        width = nextsmaller(heights,i) - prevsamller(heights,i) -1  #here the formula is :
        #nextsmaller[i] - 1 -(prevsmaller[i]+1) +1  as we cannot include the indices where we find the prevsmaller so we add 1 to it , and nextsmaller so we deduct 1 from it.
        itsarea=width * heights[i]
        area=max(area,itsarea)
    return area
print(brutelargestrec( [2, 1, 5, 6, 2, 3]))    
#time complexity : O(N)
#space complexity : O(N)



#optimal solution
def optmlargestrec(heights):
    stack = []
    n=len(heights)
    area=0
    for i in range(n):
        while stack and heights[stack[-1]]>heights[i]:
            calculatingelem=heights[stack.pop()]   #the popped index will be the index of the calculating element as we found the next smaller element of this calcualting elment
            prevsmaller = stack[-1] if stack else -1
            nextsmaller = i  #the next smaller elmenent's index will be the current i
            width = nextsmaller-prevsmaller - 1
            currentarea=calculatingelem * width   #here the calculating element acts as the length or the height of the element at the given index
            area=max(area,currentarea)
        stack.append(i)
            
    while stack:
        calculatingelem=heights[stack.pop()]
        nextsmaller = n  #if the stack still remains even after looping through every numbers from the array of given heights then it means the index having the smaller element compared to the current index is n, which is out of bound
        prevsmaller = stack[-1] if stack else -1  
        width = nextsmaller - prevsmaller - 1
        currentarea=calculatingelem*width  #as the calculting elem is the height
        area=max(area,currentarea)


    return area
print(optmlargestrec([2, 1, 5, 6, 2, 3]))    
#time complexity : O(N)
#space complexity : O(N)


#maximum rectangle
#Given a m x n binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#the question is asking us to find the maximum area of a rectangle from a given 2D matrix , which can be solved by using the same logic of finding the maximum area of a rectangle from a given histogram
def maximrectangle(matrix):
    r=len(matrix) #number of rows
    c=len(matrix[0])  #number of columns
    #now we need to create a 2D matrix of same length but every index having the total height of a lets say building , at every index except for the index having value as a zero.
    prefixsum = [[0 for _ in range(c)] for _ in range(r)]  #creating r number of rows having c number of columns
    #this down below first for loop is for calculating the total height of the supposed building at every index of the given matrix 
    for j in range(c):  #looping through every row index of every column
        for i in range(r):
            if matrix[i][j]==0:
                prefixsum[i][j]=0
            else:    
             prefixsum[i][j] = matrix[i][j] + (prefixsum[i-1][j]  if i >0 else 0)   #if the current i and j indexed number is not 0 then it means the i and j indexed prefix sum matrix number will be addition of current i and j indexed value of matrix and previous row and j indexed value of prefix sum
    maxarea=0
    def maxareainasinglearray(array):  #the real calculation happens here 
        stack = []
        n=len(array)
        area=0
        for i in range(n):
            while stack and array[stack[-1]] > array[i]:  #if the element at the top most index of the stack is greater than the i indexed number then of course the nextsmaller index of the stack.pop() will be the current i
                currelem=array[stack.pop()]
                nextsmaller=i
                prevsmaller=stack[-1] if stack else -1  #and the previous smaller index of the stack.pop() indexed number will be the new top most index if the stack still exists otherwise it will be -1,which shows out of the bounds
                width = nextsmaller-prevsmaller-1
                currarea=width * currelem  #breadth * length or height
                area=max(area,currarea)
                
            stack.append(i)    
        while stack:
            currelem=array[stack.pop()]
            nextsmaller=n
            prevsmaller=stack[-1] if stack else -1
            width = nextsmaller-prevsmaller - 1
            currarea = width * currelem
            area=max(area,currarea)  #as we need to return the maximum area from the given area , we are usign max function here
        return area
    for i in range(r):
        maxarea=max(maxarea,maxareainasinglearray(prefixsum[i]))   #we pass every row of the prefixsum 2D matrix in our function called maxareainasinglearray which gives us the area of the current i indexed row

    
    return maxarea
print(maximrectangle( [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1]]))
#time complexity : O((N*M)+2*N) 
#space complexity : O((N*M) + N)  









