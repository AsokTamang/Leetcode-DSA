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


