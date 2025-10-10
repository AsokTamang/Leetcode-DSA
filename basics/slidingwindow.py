#Sliding Window Maximum
#Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.
#brute approach
def bruteslidingwindow(arr,k):
    if len(arr) == k:  #if the length of the given array is equal to the value of k , then we just return the maximum value from the given array
        return max(arr)
    ans = []
    i=0
    while i<=len(arr)-k:  #
        subarr=arr[i:i+k]
        ans.append(max(subarr))  #this gives us the maximum value from the obtained subarray
        i+=1
    return ans
print(bruteslidingwindow([1, 3, -1, -3, 5, 3, 6, 7], k = 3))    
#time complexity : O(N*logN)
#space complexity : O(N)

#optimal approach
#in the optimal approach what we do , is we just design the dq in monotonic manner , where the greater number will be at the 0 index of dq, 
#and in every iteration , we remove the elemnent which lies out of the new sliding window ,
#and then if we reach the first sliding window , then our work of inserting the maximum number which is the leftmost number of dq in ans start on loop
from collections import deque
def optimalslidingwindow(arr,k):
    ans = []
    n=len(arr)
    if n * k ==0:
        return []
    elif k == 1:  #if the length of the sliding window is just one then we just return the array as it is ,
        return arr  
    dq=deque()
    for i in range(n):
        #so first of all we have to code the condition of removing the element that no longer fits in the sliding window length for the current index i
        if dq and dq[0]<=i-k:
            dq.popleft()  #removing the very first index of the dq ,
        while dq and arr[dq[-1]]<=arr[i]:  #removing the smaller elements of the dq compared to the current i indexed number , as we are designing the monotonic array
            dq.pop() 
        dq.append(i)  #after removing all the smaller elements than the currrent i indexed number from dq , we can append the current i index as the left most index in dq
        #after this above while loop , the larger number will be the leftmost element of the dq
        if i >=k-1: #if the index becomes greater or equal to the k-1 value , then it means we have reached the first window and the same loop will go on
            ans.append(arr[dq[0]]) #as the maximum value will be stored as the leftmost element
    return ans
print(optimalslidingwindow([1, 3, -1, -3, 5, 3, 6, 7], k = 3))
#time complexity : O(N)
#space complexity : O(N*K)




