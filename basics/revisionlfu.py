from collections import defaultdict
#LFU cache
class Node:
    def __init__(self,key,value,freq):
        self.key=key
        self.value=value
        self.freq=freq    #this is the number of count or frequency of the Node
        self.prev=None
        self.next=None
class Doublelinkedlist:
    def __init__(self):  #here the size denotes the initial size of the each frequency double linked list
        self.size = 0
        self.head= Node(-1,-1,0) #this is our dummy head and dummy node
        self.tail= Node(-1,-1,0)
        self.head.next= self.tail  
        self.tail.prev=self.head
    def addtohead(self,node):
        nxt=self.head.next
        node.prev=self.head
        node.next=nxt
        self.head.next=node
        nxt.prev=node

        self.size+=1   
    def removenode(self,node):
        if self.size==0:
            return
        prv=node.prev
        nxt=node.next
        prv.next=nxt
        nxt.prev=prv
        self.size-=1
    def removefromtail(self):
        if self.size == 0:
            return
        rmved = self.tail.prev
        self.removenode(rmved)  #as the size is already decreased in the removenode function,
        return rmved
class LFU:
    def __init__(self,capacity):
        self.capacity=capacity   #this is the fixed length of the LFU cache
        self.keynode_pair={}  #this stores the node with key as key and node as value
        self.freqnode_pair=defaultdict(Doublelinkedlist)  #this stores the list of node or node as value and freq as the key
        self.minfreq = 0  #the minimum freq will be 0 initially,
    def put(self,data):
        k = data[0]   #this is the key from the passed data 
        v=data[1]    #Value of new passed data
        newnode=Node(k,v,1)
        if k in self.keynode_pair:  #if the new passed node already exists in the node then we just need to update the node with the new value in self.key dict and update node with helper function
            node = self.keynode_pair[k]
            node.value=v
            self.update(node)
            return
        self.keynode_pair[k] =newnode
        self.freqnode_pair[1].addtohead(newnode)  #adding this new node in the head of the freq of 1 , cause this is new node which will have one freq
        self.minfreq=1
        if len(self.keynode_pair)>self.capacity:
            rmved = self.freqnode_pair[self.minfreq].removefromtail() #removing tailnode from the minimum freq list
            del self.keynode_pair[rmved.key]  #also we need to delete this node from our keynode pair
            return
    def get(self,key):
        if key not in self.keynode_pair:
            return -1
        else:
            self.update(self.keynode_pair[key])  #passing the node
            return self.keynode_pair[key].value 
    def update(self,node):
        currfreq=node.freq
        self.freqnode_pair[currfreq].removenode(node)   #removing the current node from the its curretn freq node pair list
        newfreq=currfreq+1
        node.freq=newfreq
        if currfreq == self.minfreq and self.freqnode_pair[currfreq] == 0:  #if the freq of this current passed node is the minimum freq of LFU cache and if its inital freq list  pair becomese empty  currently then we must update the minimum freq of this LFU cache 
            self.minfreq=currfreq+1
        self.freqnode_pair[newfreq].addtohead(node)  #adding this node to the new freq node pair
    def printdatas(self):
        a=[]
        for freq in self.freqnode_pair:
            itr=self.freqnode_pair[freq].head.next
            while itr!=self.freqnode_pair[freq].tail:
                a.append(str(itr.value))
                itr=itr.next
        return ''.join(a)        

    
lfu=LFU(3)
lfu.put([1,1])
lfu.put([3,3])
lfu.put([3,3])    
print(lfu.printdatas())
lfu.put([3,4])
print(lfu.get(3))
print(lfu.printdatas())
#time complexity : O(1)
#space complexity : O(1)           



   
