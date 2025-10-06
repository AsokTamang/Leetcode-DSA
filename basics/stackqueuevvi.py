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

   



