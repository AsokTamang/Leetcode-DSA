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

       