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

