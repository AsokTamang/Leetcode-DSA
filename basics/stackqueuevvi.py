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