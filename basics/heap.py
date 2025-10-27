#so the priority queue is a type of data structure where the data with the highest priority is given the first access compared to the datas with the lower priorities
import heapq
class Priorityqueue:
    def __init__(self):  
        self.elements = []   

    def isempty(self):
        return not self.elements #or we can codde return len(self.elements) == 0
    def put(self,priority,item):
         heapq.heappush(self.elements,(priority,item))  #while pushing the data with the priority , we must first pass the priority and then the item inside the tuple 
    def get(self):
        return heapq.heappop(self.elements)[1]  #we are returnign the items name only and this get function will also return the most prioritised element from the list
    def peek(self):
        return self.elements[0][1]  #peek means returning the first most element from our priority queue, which is the very first element from the list
    

if __name__=='__main__':
    p=Priorityqueue()
    print(p.isempty())  
    p.put(4,'dance')  
    p.put(1,'code')
    p.put(2,'eat')
    p.put(3,'sleep')
    print(p.elements)
    print(p.get())
    print(p.elements)
        
class Heapqueue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.elements = [0] * self.capacity
    def initializeheap(self):
        self.elements = []
        self.size = 0
    def parentind(self,i):
        return (i-1) // 2
    def leftind(self,i):
        return (2*i) + 1
    def rightind(self,i):
        return (2*i) + 2 
    def insert(self,x):
        if self.size ==self.capacity:    #if the self.size becomes equal to the self.capacity then we cannot insert the new element further , so return with the heapqueue overflow
            return 'heapqueue overflow'    
        self.elements[self.size] = x  #first of all we are inserting this new element at the last index of the array
        ind=self.size   #this is the index of this inserted new element 
        self.size+=1
        
        while ind!=0 and self.elements[self.parentind(ind)]>self.elements[ind]:  #we keep on swapping the current element with its parent element as long as its parent element is greater than it
            parentindex=self.parentind(ind)
            self.elements[parentindex],self.elements[ind]=self.elements[ind],self.elements[parentindex]
            ind = parentindex  #as we have swapped the current element with its parent element , the index of this element will be the index of the parent element
    def heapify(self,i):  #so the function heapify means , based on the left side and right side element we switch this current i indexed element with the smallest element
        leftindex=self.leftind(i)
        rightindex=self.rightind(i)
        smaller=i
        if leftindex<self.size and self.elements[self.leftind(i)]<self.elements[smaller]:
            smaller=leftindex
        if rightindex<self.size and self.elements[self.rightind(i)]<self.elements[smaller]:  #if the rigght index is within the range of our current size and right element is smaller than this i indexed element ,
            smaller=rightindex
        if smaller!=i:  #if the index consisting of the smaller number is not this current i index then we swap the elements
            self.elements[i],self.elements[smaller]=self.elements[smaller],self.elements[i]
            self.heapify(smaller)  #we heapify the index  recursively with the smaller index   
    def extractmin(self):
        if self.size == 0:
            return 'heap underflow'
        root = self.elements[0]
        self.elements[0] = self.elements[self.size-1]  #here we are replacing the first element with the last element
        self.elements.pop()  #removing the moved last element
        self.size-=1
        self.heapify(0)  #after replacing the first element with the last element , we use the heapify function to satisfy the minheap property
        return root
    def heapsize(self):
        return self.size    
    def changekey(self,i,val):    #this function is used to change the value of the element at the given index i
        prevvalue=self.elements[i]
        self.elements[i]=val

        if val<prevvalue:       
        #bubble up logic

            while i!=0 and self.elements[self.parentind(i)]>self.elements[i]:
                self.elements[self.parentind(i)],self.elements[i] = self.elements[i],self.elements[self.parentind(i)]
                i=self.parentind(i)  #as we have swapped the parent element with the current element , the current index is changed to the parent index
        else:
            self.heapify(i)  #if the new value is greater than the old value then we need to do bubble down
        return self.elements[i]   
    def deleteelem(self,i):
        self.changekey(i,float('-inf'))  #first of all we are changing the value at the given index to the most minimum infinity,which takes this element to the root with the help of our change key function
        #then we are using the extract min to remove this element
        self.extractmin()  
                
    
if __name__=='__main__':
    hh=Heapqueue(5)
    hh.insert(5)
    hh.insert(15)
    hh.insert(25)
    hh.insert(-5)
    hh.insert(2)
    print(hh.elements)
    print(hh.extractmin())
    print(hh.heapsize())
    print(hh.changekey(3,30))
    print(hh.elements)
    hh.deleteelem(2)
    print(hh.elements)
#time complexity:  
#insert : O(logN)
#heapify : O(logN)
#heapsize : O(1)
#deleteelem: O(logN)
#changekey: O(logN)


#implement min heap
#what is min heap?
# so the min heap is the binary tree where the root element is the smallest element in the  tree and the parent nodes are smaller than its  child nodes in the tree
#a leaf node is the node which is the leaf of the branch and the non leaf node is the node which has the child nodes or the leaf nodes in the tree.
class Lastheap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.elements = [0] * self.capacity
    def parentnode(self,i):
        return (i-1)//2
    def leftindex(self,i):
        return (2*i) + 1
    def rightindex(self,i):
        return (2*i) + 2
    def insert(self,x):   #here we are inserting the x which is the new value in the node
        if self.size==self.capacity:
            return 'heap overflow'
        self.elements[self.size] = x  #inserting at the last node
        i = self.size
        self.size+=1
        while i!=0 and self.elements[self.parentnode(i)] > self.elements[i]:
            self.elements[self.parentnode(i)],self.elements[i] = self.elements[i],self.elements[self.parentnode(i)]
            i=self.parentnode(i)    #as we have switched the parentnode and the i indexed element, the index of i will be the parent node
    def getmin(self):
        if self.size==0:
            return 'heap underflow'    
        return self.elements[0]  #returning the first most element from the list
    def heapify(self,i):
        n=len(self.elements)
        smaller = i
        leftind=self.leftindex(i)
        rightind=self.rightindex(i)
        if leftind<n and self.elements[leftind] < self.elements[i]:
            smaller=leftind
        if rightind < n and self.elements[rightind] < self.elements[i]:
            smaller=rightind
        if smaller!=i:
            self.elements[i],self.elements[smaller] = self.elements[smaller],self.elements[i]  
            self.heapify(smaller)       #recursively calling the heapify function

    def extractmin(self):
        root=self.elements[0]
        self.elements[0]=self.elements[self.size-1]
        self.size-=1
        self.elements.pop()  #removing the last element
        self.heapify(0)
        return root
    def heapsize(self):
        return self.size
    def isempty(self):
        return not self.elements   
    def changekey(self,i,val):
        prevval=self.elements[i]
        self.elements[i] = val  #new value
        if val>prevval:  #if the new value is greater than we need to bubble down
            self.heapify(i)
        else:  #if the new value is lesser than the previous value then we need to do the logic of bubble up because there might be the chance that its parent node value might be greater than the current node's value as we have inserted the lesser value
            while i!=0 and self.elements[self.parentnode(i)] > self.elements[i]:
                self.elements[self.parentnode(i)],self.elements[i]= self.elements[i],self.elements[self.parentnode(i)]
                i=self.parentnode(i)
        return self.elements[i]
lh=Lastheap(6)
lh.insert(1)
lh.insert(7)
lh.insert(11)
lh.insert(13)
lh.insert(23)
lh.insert(63)    
print(lh.elements)
print(lh.extractmin())
print(lh.elements)
#time complexity : 
#insert : O(logN)
#getmin: O(1)
#extractmin : O(logN)
#heapsize : O(1)
#isempty : O(1)
#changekeyvalue : O(logN)
#space complexity : O(N)

        

#revision
#check  if an array represents a min heap
def checkminheap(nums):
    n=len(nums)
    #inorder to check for the min heap property we must loop through the non-leaf nodes only as the leaf nodes doesnot has any child , so they already satisfy the min heap property
    for i in range(n//2):
        leftind = (2 * i) + 1
        rightind = (2 * i) + 2
        if leftind < n and nums[leftind] < nums[i]:
            return False
        if rightind < n and nums[rightind] < nums[i]:
            return False
    return True
print(checkminheap([10, 20, 30, 25, 15]))    
#time complexity : O(N)
#space complexity : O(1)


#conversion of min heap to max heap
def convertmintomax(nums):
    n=len(nums)
    def maxheapify(i):
        maximum=i   #initially lets assume that the current index i is the maximum
        leftind=(2* i) + 1
        rightind=(2*i) + 2
        if leftind<n and nums[leftind] > nums[maximum]:
            maximum=leftind
        if rightind<n and nums[rightind] >  nums[maximum]:
            maximum=rightind
        if maximum!=i:
            nums[i],nums[maximum]=nums[maximum],nums[i]
            maxheapify(maximum)        
    for i in range((n//2) - 1 , -1 , -1):
        maxheapify(i)
    return nums
print(convertmintomax( [-5, -4, -3, -2, -1]))    
#time complexity : O(N)
#space complexity : O(1)


#revision 
#sort k sorted array
def sortkarray(array,k):
    heap = []
    n=len(array)   
    index = 0
    for i in range(k+1):
        heapq.heappush(heap,array[i])    
    for i in range(k+1,n):
        array[index]=heapq.heappop(heap)  #appending the smallest element available in the heap in our array at the current index
        heapq.heappush(heap,array[i])
        index+=1
    while heap:   #if the heap still exists then we append the numbers from heap in the respective index for sorting the given array 
        array[index] = heapq.heappop(heap)
        index+=1        
    return array
print(sortkarray([2, 3, 1, 4], 2))    
#time complexity : O(NlogK)   
#space complexity : O(K)  for the heap size 


#kth largest and smallest element in an array
def kthlargestandsmallest(array,k):
    def kthlargest(array,k):  #inorder to find the largest element , first of all we need to design this tree in maxheap pattern using maxheapify
        array=array.copy()  #here we must make the copy of an array so that it won't change the result
        n=len(array)
        def maxheapify(ind,size):
            leftind = (2*ind) + 1 
            rightind = (2*ind) + 2
            maximum = ind
            if leftind< size and array[leftind] > array[maximum]:
                maximum=leftind
            if rightind< size and array[rightind] > array[maximum]:
                maximum=rightind 
            if maximum!=ind:
                array[maximum],array[ind] = array[ind],array[maximum]
                maxheapify(maximum,size)   #using recursion with the maximum index       

        for i in range((n//2) - 1 , - 1 ,-1):  #as the leaf nodes already satisfy the condition of min heap or maxheap , we start from the non-leaf
          maxheapify(i,n)
        size = n
        #if we need to find the kth largest or smallest element, then we need to remove the  root elment which is the maximum element at time k-1 times , then we can return the root element , which is the kth largest or kth smallest element
        for i in range(1,k):  
            array[0],array[size-1]=array[size-1],array[0]
            size-=1
            maxheapify(0,size)  #as we have replaced the root with the last element , we again need to heapify to maintain the max heapify pattern
        return array[0]      

        
    def kthsmallest(array,k):
        n=len(array)
        array=array.copy()
        def minheapify(ind,size):
            leftind = (2*ind) + 1 
            rightind = (2*ind) + 2
            minimum = ind
            if leftind< size and array[leftind] < array[minimum]:
                minimum=leftind
            if rightind< size and array[rightind] < array[minimum]:
                minimum=rightind 
            if minimum!=ind:
                array[minimum],array[ind] = array[ind],array[minimum]
                minheapify(minimum,size)   #using recursion with the minimum index       
        for i in range((n//2)-1,-1,-1):  #as the leaf nodes already satisfy the condition of min heap or minheap , we start from the non-leaf
          minheapify(i,n)
        size = n
        #if we need to find the kth largest or smallest element, then we need to remove the  root elment which is the minimum element at time k-1 times , then we can return the root element , which is the kth largest or kth smallest element
        for i in range(1,k):  
            array[0],array[size-1]=array[size-1],array[0]
            size-=1
            minheapify(0,size)
        return array[0]
    return f'kth smallest:{kthsmallest(array,k)} and kth largest:{kthlargest(array,k)}'
print(kthlargestandsmallest([1,2,6,4,5,3] , 3 )) 
#time complexity : O(N + KlogN)
#space complexity : O(1)

#merge k sorted lists
#Given heads of k sorted linked lists as an array called heads, merge them into one single sorted linked list and return the head of that list.
class Node1:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Mergeksortedlists:
    def mergethelist(self,array):  #here array is the parent list
        dummy=Node1(0,None)
        current = dummy
        heap = []  #this will store the node values as well as return the minimum node values for the final linked list in each iteration
        for i,node in enumerate(array):  #here i represents the index and node represents the head of each linked list
            if node:
                heapq.heappush(heap,(node.val,i,node))  #we are pushing the node inside the heap based on the value , index and node itself , cause if the values are same then the heap sort them according to the index
        while heap:
            val,i,node = heapq.heappop(heap)
            current.next = node
            current=current.next
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dummy.next
    def printlist(self,array):
        itr=self.mergethelist(array)
        ans = []
        while itr:
            ans.append(str(itr.val))
            itr=itr.next
        return ans    



      
        
    def buildlinkedlist(self,list):  #here list is just the normal array and from this normal array we have to make the linked list and return the head of the linked list
        dummy=Node1(0,None)
        current=dummy
        for data in list:
            current.next=Node1(data,None)
            current=current.next
        return dummy.next  #returning the head of the linked list
mg=Mergeksortedlists()
list1=mg.buildlinkedlist([1,2,3,4])
list2=mg.buildlinkedlist([-4,-3])
list3=mg.buildlinkedlist([-5 , -3 , 1 , 2 , 3 , 4])   
totallist=[list1,list2,list3] 
print(mg.printlist(totallist))
        


    
#task scheduler
#here the question has asked us to complete the given number of tasks in the minimum possible time intervals,
#and n is the time interval between the same task as no same task can be performed within the n value
def taskscheduler(array,n):
    totaltime = 0
    heap = []
    freqarray = [0] * 26
    for num in array:
        freqarray[ord(num)-ord('A')]+=1    #counting the frequency of each task from the given array
    for i in range(26):
        if freqarray[i] > 0:
         heapq.heappush(heap,-freqarray[i])     #here we are storing the negative value of the freq cause the heapq only operates for the smallest number or value at first
    while heap:
        temp = [ ]  #this is the temporary variable which is used for restoring the new value of popped value from the heap
        for i in range(n+1):
            if heap:
                count = heapq.heappop(heap)
                count+=1
                temp.append(count)
        for value in temp:
            if value<0:  #as we are storing the negative value in our heap , only if its negative we will push it back to the heap
                heapq.heappush(heap,value)
        if heap:
            totaltime+=n+1  #if the heap still exists then ofcourse the total time will be addition of  n+1
        else:
            totaltime+=len(temp)                     
    return totaltime
print(taskscheduler( ["A","A","A","B","B","B"],  2))
#time complexity : O(N)
#space complexity : O(1)
from collections import Counter
#brute handofstraights
def brutehandstraight(hand,groupsize):
    if len(hand) % groupsize!=0:
        return False
    hand.sort()  #sorting the given array
    m=Counter(hand)  #this makes the key-value pair of number and their count
    for num in hand:
        if m[num] == 0:  #if the very first value's count is 0 then we continue with another number
            continue
        for i in range(groupsize):
            card = num + i  #here for every number we must check if its next consecutive number exists or not
            if m[card]==0:  #if the freq of the needed number is 0 then it means we dont have the sufficient required number so we cannot form a group of length groupsize, so we return false
                return False
            else:
                m[card]-=1
        return True        
                 
print(brutehandstraight([1,2,3,4,5],  4))      
#time complexity : O(N)
#space complexity : O(1)  

#optimal solution
def optimalhandstraight(hand,groupsize):
    m=Counter(hand)   #here we are sorting the hands and then calculating the freq of these hands
    for hand in sorted(m.keys()):
        currentfreq=m[hand]
        for i in range(groupsize):
            card = hand + i
            if m[card] < currentfreq:
                return False
            m[card]-=currentfreq
    return True
print(optimalhandstraight( [1,2,3,4,5],   4))        


         

         
