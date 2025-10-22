import heapq
#Check if an array represents a min heap
#Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
#A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.


def checkminheap(nums):
    n=len(nums)
    for i in range(n//2):  #we only loop through the non-leaf nodes of the heap
        leftind=(2*i) + 1
        rightind = (2 * i) + 2
        if leftind < n and nums[leftind] < nums[i]:
            return False
        if rightind<n and nums[rightind] < nums[i]:
            return False
    return True
print(checkminheap([10, 20, 30, 21, 23]))    
#time complexity : O(N/2)
#space complexity : O(1)