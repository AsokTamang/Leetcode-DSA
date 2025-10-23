import heapq
#Check if an array represents a min heap
#Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
#A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.

def convertmintomax(nums):
    n = len(nums)
    
    def heapifymax(i):
        leftind = 2 * i + 1
        rightind = 2 * i + 2
        larger = i
        
        if leftind < n and nums[leftind] > nums[larger]:
            larger = leftind
        if rightind < n and nums[rightind] > nums[larger]:
            larger = rightind
        
        if larger != i:
            nums[i], nums[larger] = nums[larger], nums[i]
            heapifymax(larger)  # recursively heapify the affected subtree
    #we must loop from that node which is non leaf , which means it is a branch but not a leaf i.e it has a child elements
    for i in range(n//2 - 1, -1, -1):
        heapifymax(i)
    return nums    
    
    


print(convertmintomax([2, 6, 3, 100, 120, 4, 5]))
#time complexity : O(N)
#space complexity : O(1)


#K-th Largest element in an array
#here we have to use the logic of priority queue inorder to find the kth largest element
def kthlargest(nums,k):
    n=len(nums)
    def heapifymax(i,size):
        maximum = i
        leftind = (2*i) + 1
        rightind = (2*i) + 2
        if leftind < size and nums[leftind] > nums[maximum]:
            maximum = leftind
        if rightind < size and nums[rightind] > nums[maximum]:
            maximum = rightind
        if maximum!=i:
            nums[maximum],nums[i] = nums[i] , nums[maximum]
            heapifymax(maximum,size)   
    for i in range((n//2) - 1 , -1 , -1):
        heapifymax(i,n)
    #until this  point we have designed the maxheap property in a given binary tree,
    #now we need to extract the maximum from this obtained tree k-1 times so that , the root element is the required k-th largest element
    size = n
    for i in range(1,k):  
        nums[0],nums[size-1] = nums[size-1],nums[0]  #here we are extracting the current root element by replacing with the last element,
        size-=1
        heapifymax(0,size)  #as we have extracted the maximum which is always at the root index , so we heapify at that root index
        #and this process continues till k-1 times
         
    return nums[0]  #as we have removed the maximum elements k-1 times , the kth maximum number will always be at the root , so we are returning this root indexed number
print(kthlargest([-5, 4, 1, 2, -3], k = 5))    
#time complexity : O(N)
#space complexity : O(1)


