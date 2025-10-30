#so the logic for LFU is whenever we do put method or get method , we increase the frequency of that specific node , and when the frequency is increased this node will be
#assigned in the higher frequency double linked list 
#but in the process of putting the new node , when the capacity of cache is exceeded we remove the node with least frequency,
#but there also might be a case where the multiple nodes has the least frequency, in this case we remove the least used node from that frequency,
#so whenever the action of put , get happens on a specific node , we increase its frequency.

from collections import defaultdict

class Node:
    def __init__(self,key,value,freq):  #here freq denotes the number of counts that this node currently has
        self.key=key
        self.value=value
        self.freq=freq
        self.prev=None
        self.next=None
class Doublelinkedlist:
    def __init__(self):   #here size means the number of nodes in this list 
        self.head=Node(-1,-1,None)
        self.tail=Node(-1,-1,None)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0  #initially the size is always zero
    def addtohead(self,node):
        nxt=self.head.next
        node.prev=self.head
        node.next=nxt
        self.head.next=node
        self.size+=1
    def deletenode(self,node):
        prv=node.prev
        nxt=node.next
        prv.next=nxt
        nxt.prev=prv
        self.size-=1
    def removefromtail(self):
        if self.size==0: #we cannot delete the node from an empty list
            return
        rem=self.tail.prev
        self.deletenode(rem)
        return rem
#so our design of node as well as the double linked list is done,
# now its time to design the actual LFU

class LFU:
    def __init__(self,capacity):  #capacity means the number of nodes that our LFU must consists of
        self.capacity=capacity
        self.keynode_pair={}  #this stores the key and the node in key-value pair
        self.minfreq=0     #initially as we dont have any nodes so the self.min freq is 0
        self.freqnode =defaultdict(Doublelinkedlist)
    def put(self,data):
        if data[0] in self.keynode_pair:  #here data[0] means the key of the node
            self.update(self.keynode_pair[data[0]])
            return
        newnode=Node(data[0],data[0],1) #here 1 denotes the freq of this newnode
        self.freqnode[1].addtohead(newnode)
        self.keynode_pair[data[0]]=newnode
        self.minfreq=1  #also the minimum freq will be one

        if len(self.keynode_pair)>self.capacity:  #if the length of key-node pair exceeds the capacity after adding this new node then we have to remove the tail node from the minimum freq list if multiple nodes exist in this minimum freq list
            lfulist = self.freqnode[self.minfreq]  #this is the list of minimum freq
            rmvd=lfulist.removefromtail()
            del self.keynode_pair[rmvd.key]  #also deleting from the key-node list



    def get(self,k):
        if k in self.keynode_pair:
            self.update(self.keynode_pair[k])  #passing the node in our helper function
            return self.keynode_pair[k].value  #returning the value of this passed node
        else:
            return -1     
    def update(self,node):  #this is our helper function which updates the node
        currentfreq=node.freq  #this is the current frequency of the passed node
        self.freqnode[currentfreq].deletenode(node)  #deleting this passed node from its current freq list
        if currentfreq == self.minfreq and self.freqnode[currentfreq] == 0:  #if the  frequency of this passed node is the current minimm=um freq of our LFU then we must update the minimum freq of LFU cache
            self.minfreq=currentfreq+1 
        node.freq=currentfreq+1      
        self.freqnode[currentfreq+1].addtohead(node)   
    def printcache(self):
        a=[]
        for f in self.freqnode:
            itr=self.freqnode[f].head.next
            while itr!=self.freqnode[f].tail:
                a.append(str(itr.value))
                itr=itr.next  
        return ''.join(a)         

ll=LFU(4)
ll.put([1,1])
ll.put([2,2])
ll.put([3,3])
ll.put([4,4])
print(ll.get(3))
print(ll.printcache())


#kth largest element in an array
def kthlargest(nums,k):  #here the quesion is asking us to return the kth largest element in an array
    def heapifymax(size,i):
        maximum = i  #lets assume the current index is the maximum
        leftind = (2* i) +1
        rightind = (2*i) + 2  
        if leftind<size and nums[leftind] > nums[maximum]:
            maximum=leftind
        if rightind<size and nums[rightind] > nums[maximum]:
            maximum=rightind
        if maximum!=i:
            nums[maximum],nums[i]=nums[i],nums[maximum]
            heapifymax(size,maximum) 
    n=len(nums)

    for i in range((n//2)-1,-1,-1):  #here we must heapifymax from the non-leaf node which is not the leaf but the parent node itself
        heapifymax(n,i)   
    size = n         
    for i in range(1,k):
        nums[0]=nums[size-1]   #removing the very first elmeent which is the first maximum element then decreasing the size and heapifying for max tree
        size-=1  #and repeating this process from 1 to k-1 times
        heapifymax(size,0)    
    return nums[0]   #then the very first element or the root element after the loop is the kth largest element
print(kthlargest( [-5, 4, 1, 2, -3], k = 5))
#time complexity : O(klogN)  k is the value given and n is the length of a given array
#space complexity : O(1)


        

def kthsmallest(nums,k):  #here the quesion is asking us to return the kth largest element in an array
    def heapifymin(size,i):
        minimum = i  #lets assume the current index is the minimum
        leftind = (2* i) +1
        rightind = (2*i) + 2  
        if leftind<size and nums[leftind] <nums[minimum]:
            minimum=leftind
        if rightind<size and nums[rightind] < nums[minimum]:
            minimum=rightind
        if minimum!=i:
            nums[minimum],nums[i]=nums[i],nums[minimum]
            heapifymin(size,minimum) 
    n=len(nums)

    for i in range(n//2):  #here we must heapifymax from the non-leaf node which is not the leaf but the parent node itself
        heapifymin(n,i)   
    size = n         
    for i in range(1,k):
        nums[0]=nums[size-1]   #removing the very first elmeent which is the first maximum element then decreasing the size and heapifying for max tree
        size-=1  #and repeating this process from 1 to k-1 times
        heapifymin(size,0)    
    return nums[0]   #then the very first element or the root element after the loop is the kth largest element
print(kthsmallest([7, 10, 4, 3, 20, 15], k = 3))
#time complexity : O(klogN)  k is the value given and n is the length of a given array
#space complexity : O(1)

import heapq
#sort k sorted array
def ksortedarray(array,k):
    heap = []
    index = 0
    n=len(array)
    for i in range(k+1):
        heapq.heappush(heap,array[i])
    for i in range(k+1,n):
        array[index] = heapq.heappop(heap)
        heapq.heappush(heap,array[i])
        index+=1      
    while heap and  index<n:
        array[index] = heapq.heappop(heap)
        index+=1
    return array      
print(ksortedarray([2, 3, 1, 4],  k = 2 ))
#time complexity : O(nlogK)
#space complexity : O(K)  for the heap 


#merge k sorted lists
#Given heads of k sorted linked lists as an array called heads, merge them into one single sorted linked list and return the head of that list.
class Nnode:
    def __init__(self,val,next=None): #here val represents the value of the node
        self.next =next
        self.val = val 
class MergeKlist:     
    def buildlinkedlist(array):  #this functions is used for building the linked list and this function returns the head of the linked list
        dummy=Nnode(0,None)
        current = dummy
        for num in array:
            current.next=Nnode(num,None)
            current=current.next
        return dummy.next         
    def mergelinkedlist(array):  #here array represents the  linked list inside a parent list
        dummy=Nnode(0,None)
        current = dummy
        heap = []
        for i,node in enumerate(array):
            if node:
             heapq.heappush(heap,(node.val,i,node))  #here we are pushing the nodes based on the node value first then the index
        while heap:
                val,i,node=heapq.heappop(heap)
                current.next = node
                current=current.next
                if node.next:
                    heapq.heappush(heap,(node.next.val,i,node.next))
        a=[]
        itr=dummy.next
        while itr:
            a.append(str(itr.val))
            itr=itr.next

        return '->'.join(a)     
          
list1=MergeKlist.buildlinkedlist([1,2,3,4])
list2=MergeKlist.buildlinkedlist([-4,-3])
list3=MergeKlist.buildlinkedlist([ -5 , -3 , 1 , 2 , 3 , 4])    
totallist=[list1,list2,list3]
print(MergeKlist.mergelinkedlist(totallist))
#time complexity : O(NlogK)  N is the total number of nodes in all the child lists and K is the number of such list in parent list
#space complexity : O(K)  due to heap


#Replace elements by its rank in the array
#Given an array of N integers, the task is to replace each element of the array by its rank in the array.
def replaceelements(array):
    n=len(array)
    ans = [0] * n
    heap = []
    for i in range(n):
        heapq.heappush(heap,(array[i],i))
    index = 1
    while heap:
        val,i = heapq.heappop(heap)  #here i represents the original index of the number in a given original array
        ans[i] = index  #as the very first element's index must be 1 so we start by 1 
        #and this loop goes on
        index+=1  
    return ans
print(replaceelements([4, 2, 4]))        
#time complexity : O(NlogN)
#space complexity : O(N)


#task scheduler
#the question is asking us to return the most possible total minimum time interval ,as two different task can be done just next to each other but for the identical tasks the,they must be separated by n intervals
def taskscheduler(array,n):
    freqarray = [0] * 26
    for i in range(len(array)):
        freqarray[ord(array[i])-ord('A')]+=1   #counting the frequency of task from a given array
    heap = []
    for i in range(26):
        if freqarray[i] > 0:
         heapq.heappush(heap,-freqarray[i])  #here we must store in the negative form cause python heapq returns the minimum value or smallest value while popping
    totaltime = 0
    while heap:
        temp = []  #this stores the number of task left for each iteration 
        for i in range(n+1):
            if heap:
                count = heapq.heappop(heap)
                count+=1  #reducing the value which means we are using the task
                temp.append(count)
        for num in temp:
            if num < 0:
                heapq.heappush(heap,num)
        if heap:  #if the heap still exists then it means we have successfully completed n+1 task in the current cycle maintaining n interval between identical tasks if there is sufficient number of task else remained idle if needed
            totaltime+=n+1
        else:
            totaltime+=len(temp)
    return totaltime     
print(taskscheduler( ["A","A","A","B","B","B"], 2))          
#time complexity : O(N)
#space complexity : O(K)  number of distinct elements in a given array     


#hand of straights
from collections import Counter
def handofstraights(hand,n):  #here n is the size of a group consisting of consecutive cards
    m=Counter(hand)
    for num in sorted(m.keys()):
        count = m[num]  
        if count>0:
            for i in range(n):
                if m[num + i] < count:
                    return False  #we return false as soon as the frequency of the next coming number of the current card number is less than the count or freq of the current card number, cause if the condition is like this then
                m[num + i]-=count
                #we cannot form a group of size n with the consecutive numbers
    return True
print(handofstraights( [1,2,3,4,5],  4))        
#time complexity : O(N)
#space complexity : O(M) number of distinct elements from a given array
from collections import defaultdict
#design a twitter
class Twitter:
    def __init__(self):
        self.time = 1 #here self.time represents the time during which the tweet was posted as the question has asked us to return the 10 most recent tweets based on the user
        self.followinglist = defaultdict(set)  #here the default dict represents the set of the users followed by the specific users example userid->[user1,user2,user3]
        self.tweet=defaultdict(list)    #here defaultdict represents the list of the tweets posted by the specific user example: userid->[t1,t2,t3]
    def posttweet(self,userid,tweetid):
        self.tweet[userid].append((self.time,tweetid))  #here we are appending the tweet with given id in the list of the user represented by userid
        self.time+=1
    def follow(self,followerid,followeeid):
        self.followinglist[followerid].add(followeeid)
    def unfollow(self,followerid,followeeid):
        self.followinglist[followerid].discard(followeeid)
    def getnewsfeed(self,userid):  #as the most recent tweets have the higher time , so we must use heapq method to remove the old tweets as they have the lesser time
        heap = []
        ans = []
        for t in self.tweet[userid]:
            heapq.heappush(heap,t)
            if len(heap) > 10:
                heapq.heappop(heap)  #here the pop is based on the time
        for followee in self.followinglist[userid]:
            for t in self.tweet[followee]:
                heapq.heappush(heap,t)
                if len(heap)>10:
                    heapq.heappop(heap)
        while heap:
            ans.append(heapq.heappop(heap)[1])
        return ans[::-1]  #as the most recent must come before , we are reversing the heap as the tweet goes from most recent to least recent
tw=Twitter()
tw.posttweet(1,2)
tw.posttweet(2,6)
print(tw.getnewsfeed(1))
tw.follow(1,2)
print(tw.getnewsfeed(1))
tw.unfollow(1, 2)
tw.posttweet(1,7)
print(tw.getnewsfeed(1))
#time complexity: O(N)  N is the total  number of tweets
#space complexity : O(N) 


#Minimum Cost to Connect Sticks
def minimumcost(sticks):
    heap=[]
    totalcost = 0
    for num in sticks:
        heapq.heappush(heap,num)
    while len(heap)>1:
        firstsmall = heapq.heappop(heap)
        secondsmall = heapq.heappop(heap)
        pair = firstsmall + secondsmall
        totalcost+=pair
        heapq.heappush(heap,pair)
    return totalcost
print(minimumcost( [1, 8, 3, 5]))    
#time complexity : O(N)
#space complexity : O(N)


        
#maximum sum combination
#brute approach
def brutemaximumsum(nums1,nums2,k):
    ans=[]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            ans.append(nums1[i]+nums2[j])
    ans.sort(reverse=True)
    return ans[:k]
print(brutemaximumsum([7, 3],  [1, 6],  2))
#time complexity : O(N**2logN)
#space complexity : O(N)
                        

#optimal solution
def optsumcombination(nums1,nums2,k):
    n=len(nums1)
    nums1.sort()
    nums2.sort()
    heap = []
    ans = []
    seen=set()
    heapq.heappush(heap,(-(nums1[n-1]+nums2[n-1]),n-1,n-1))
    seen.add((n-1,n-1))
    c=0
    while heap and c<k:
        s,i,j = heapq.heappop(heap)
        ans.append(-s)
        c+=1
        if (i-1,j) not in seen:
            heapq.heappush(heap,(-(nums1[i-1]+nums2[j]),i-1,j))
            seen.add((i-1,j))
        if (i,j-1) not in seen:
            heapq.heappush(heap,(-(nums1[i]+nums2[j-1]),i,j-1))
            seen.add((i,j-1))
    return ans
print(optsumcombination( [3, 4, 5],  [2, 6, 3], 2))    
#time complexity : O(NlogN + klogK) here NlogN is for sorting the given array and KlogK is for the heaping as well as appending the sum 
#space complexity : O(k+N)  K denotes the heap and N denotes the total number of values in both of these lists      






#Find Median from Data Stream
class MedianFInder:
    def __init__(self):
      self.small = []  #this array stores the smaller half of the array and it uses maxheap property 
      self.large = []  #this array stores the larger half of the array and it uses minheap property
    def addnum(self,val):
        heapq.heappush(self.small,-val)
        if self.small and self.large and -self.small[0] > self.large[0]:  #the elements in the smaller half must be smaller than or equal to the elements in the larger half
            v=heapq.heappop(self.small)
            heapq.heappush(self.large,-v)
        if len(self.small) > len(self.large) + 1:
            v=heapq.heappop(self.small)   
            heapq.heappush(self.large,-v)
        if len(self.large) > len(self.small)+1:
            v=heapq.heappop(self.large)
            heapq.heappush(self.small,-v)     



    def findmedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2   #as in the smaller half array or heap , we have stored the number in a negative form
mf=MedianFInder()
mf.addnum(1)
mf.addnum(2)
mf.addnum(3)
print(mf.findmedian())
#time complexity : 
#addnum- O(logN)
#findmedian - O(1)
#space complexity : O(N)



#Kth largest element in a stream of running integers   
#so in this question we have to find the kth ranked larger element from our given array
#for this we can use the min-heap , and inorder to find the kth largest element, we can pop elment if the length of our array becomes greater than k
#so the root element in our array is the kth ranked larger element      
class Kthlargest:
    def __init__(self,array,k):  #here we have to return the kth largest element from the given array
        self.array =array
        self.k=k   
        heapq.heapify(self.array)   
    
    def add(self,val):
        heapq.heappush(self.array,val)
        if len(self.array)>self.k:
            heapq.heappop(self.array)
    def findkthlargest(self): 
        return self.array[0]
    
kl=Kthlargest([1, 2, 3, 4],3)
(kl.add(5))
(kl.add(2))
(kl.add(7))
print(kl.findkthlargest())
#time complexity :
# add: O(logk)
#findkthalargest : O(1) 


#minimum cost to connect sticks
def minimumcost(sticks):
    heap = []
    for num in sticks:
        heapq.heappush(heap,num)
    total=0
    while len(heap)>1:  #as long as we are not forming one total stick , we continue this loop
        stick1=heapq.heappop(heap)
        stick2=heapq.heappop(heap)
        formedstick = stick1+stick2  #this is the stick formed from the minimum length possible from every sticks
        heapq.heappush(heap,formedstick)
        total+=formedstick
    return total
print(minimumcost([1, 8, 3, 5]))
#time complexity :  O(NlogN)
#space complexity : O(N)







                 





