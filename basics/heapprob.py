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


#k-th smallest element 
def kthsmallest(nums,k):
    n=len(nums)
    def heapify(i,size):
        minimum = i
        leftind = (2*i) + 1
        rightind = (2*i) + 2
        if leftind < size and nums[leftind] < nums[minimum]:
             minimum=leftind
        if rightind < size and nums[rightind] < nums[minimum]:
             minimum=rightind
        if minimum!=i:
            nums[minimum],nums[i] = nums[i],nums[minimum]
            heapify(minimum,size)
    for i in range(n//2):
        heapify(i,n) 
    #after this loop , we have designed a min-heap binary tree
    size = n
    for i in range(1,k):
        nums[0],nums[size-1]=nums[size-1],nums[0]
        size-=1
        heapify(0,size)    
    return nums[0]  


print(kthsmallest([7, 10, 4, 3, 20, 15], k = 3))
#time complexity : O(N)
#space complexity : O(1)

#sort k sorted array
#so in the given question , the array is sorted in k position , which mneans the element of array at every index i can be either i-k or i+k position in the given sorted array
#so we must sort this array
#so the logic for solving this problem is that we are appending the elements at the window of k+1 first 
import heapq
def ksorted(nums,k):
    n=len(nums)
    heap=[]
    for i in range(k+1):
        heapq.heappush(heap,nums[i])   #pushing the i indexed element into heap using heapq.heappush which internally arranges in the min-heap patterned binary tree
    index = 0
    for i in range(k+1,n):
        nums[index]=(heapq.heappop(heap))  #appending the smallest element in our ans with in the range k+1
        heapq.heappush(heap,nums[i])
        index+=1

    while heap and index<n:
        nums[index]=(heapq.heappop(heap))  #heapq.heappop(heap) always returns the smallest number available in the current heap
        index+=1
    return nums      
print(ksorted([2, 3, 1, 4],  k = 2 ))
#time complexity : O(nlogK)
#space complexity : O(K)  this is the auxillary space of heap


#merge k sorted lists
#Given heads of k sorted linked lists as an array called heads, merge them into one single sorted linked list and return the head of that list.
#brute approach

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next = next 
class Mergelist:
    def merge(heads):
        final = []
        for head in heads:
            while head:
                final.append(head.val)
                head=head.next
        #until this point we have appended all available values of nodes in our variable called final
        final.sort()  #now we have sorted our values
        dummynode = Node(0,None)
        current = dummynode
        for data in final:
            current.next=Node(data,None)
            current=current.next
        return dummynode.next    

           

    def buildlinkedlist(array):  #first of all what we did , was we built the linked list from the given matrix  , then we used this linked list to append their values in one variable or container and sorted them and ,
        #based on that we built a linked list
        dummynode = Node(0,None)
        current = dummynode
        for data in array:
            current.next=Node(data,None)
            current=current.next
        return dummynode.next    
    def printlist(head):
        ans = []
        while head:
            ans.append(head.val)
            head=head.next
        return ans    


list1=Mergelist.buildlinkedlist([1,2,3,4])
list2=Mergelist.buildlinkedlist([-4,-3])
list3=Mergelist.buildlinkedlist([-5 , -3 , 1 , 2 , 3 , 4])
total = [list1,list2,list3]
print(Mergelist.printlist(Mergelist.merge(total)))    
#time complexity : O(NlogN)
#space complexity : O(N)

import heapq
#optimal approach
class Nnode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Optmergelist:
    def buildlist(array):
        dummynode = Nnode(0,None)
        current = dummynode
        for data in array:
            current.next=Nnode(data,None)
            current=current.next
        return dummynode.next
    def optmergeklist(array):  #this array is the array consisting of multiple list or array having their own values
        dummynode=Nnode(0,None)
        current=dummynode
        heap = []  
        for i,node in enumerate(array):
            if node: #here node means the list
                heapq.heappush(heap,(node.val,i,node))  #and the heap will sort the nodes internally based on the value first, but if the values are same , then it will sort based on the index
        #here we are storing value of the node as well as the index and node as well
        while heap:
            val,i,node = heapq.heappop(heap)  #as this code returns the smallest value with node as well as index,
            #thats why the next of the dummy will be this first smallest value , which will be the head of the linked list
            current.next=node
            current=current.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next)) #here i means the position of the node not the index of values
        final = []
        itr=dummynode.next
        while itr:
            final.append(itr.val)
            itr=itr.next
        return final

list1=Optmergelist.buildlist([ -5 , -4 , -1])
list2=Optmergelist.buildlist([10 , 11 , 12]) 
total=[list1,list2]
print(Optmergelist.optmergeklist(total))
#time complexity : O(NlogK)   
#space complexity : O(K)  length of the total list as we are using heap

    

#Replace elements by its rank in the array
#Given an array of N integers, the task is to replace each element of the array by its rank in the array.v
def replaceleem(array):
    heap = []
    n=len(array)
    for i in range(n):
        heapq.heappush(heap,(array[i],i))   #this will store and sort the data as well as index of a given array based on the value 
    ans = [0] * n
    index = 1
    while heap:
        val,i = heapq.heappop(heap)
        ans[i] = index  #here index denotes the rank
        index+=1
    return ans
print(replaceleem([20, 15, 26, 2, 98, 6]))
#time complexity : O(NlogN)  logN is for the insertion of datas and their index in heap
#space complexity : O(N)


#sorting method
def replacenum(array):
    m={}
    n=len(array)
    
    ans = [0] * n
    a=sorted(array)
    index = 1
    for i in range(n):  #first of all we are looping through the sorted array to store the data and its rank as key-value pair
        if a[i] not in m:
            m[a[i]] = index
            index+=1
    for i in range(n):  #then we loop using the original array value to get the corresponding rank to store in the respective index based on the original array
        ans[i] = m[array[i]]
    return ans
print(replacenum([20, 15, 26, 2, 98, 6]))     
#time complexity : O(nlogn)
#space complexity : O(n)
    


#task scheduler
#You are given a list of tasks represented by uppercase English letters ('A' to 'Z'), and an integer n representing a cooldown interval between two same tasks.
#Each task takes exactly 1 CPU interval to complete.
#Tasks can be executed in any order, but identical tasks must be separated by at least n intervals, during which the CPU may remain idle or execute other tasks.
#Return the minimum number of CPU intervals required to complete all the tasks.


def taskscheduler(array,n):
    total= 0  #this is the total intervals needed to take to complete the tasks
    heap = []
    freqarray = [0] * 26
    for num in array:
        freqarray[ord(num)-ord('A')]+=1   #here we are storing the frequency of the num from given array in our freqarray
    for i in range(26):
        if freqarray[i] > 0:
            heapq.heappush(heap,-freqarray[i])  #here we are storing the negative value of the frequency of the num cause the default heapq method in python pops the negative value
   
    while heap:
         temp=[]
         for i in range(n+1):
           if heap: 
            count = heapq.heappop(heap)
            count+=1
            temp.append(count)
         for val in temp:
             if val<0:
                 heapq.heappush(heap,val)   
         if not heap:    #if the heap becomes empty in the iteration , then
             total+=len(temp)
         else:
             total+=n+1  #as in each iteration we are doing n+1 tasks
                     
           
    return total    
print(taskscheduler(["A","A","A","B","B","B"], 2))
#time complexity : O(N)
#space complexity : O(logN)  for the heap 



#task scheduler


