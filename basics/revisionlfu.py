#so in the LFU cache what we need to do is , we have to maintain a node of key,value,freq where freq is the frequency of a node,and of course prev,next
#and we need to make a doublelinked list which has the size , means the number of nodes in the double linked list , then make the dummyhead and tail
#then finally we need to make the LFU cache which contains the default dict of this double linked list , that stores the double list of nodes and their freq in the form of key-value pair
from collections import defaultdict
class Node:
    def __init__(self,key,value,freq):
        self.key = key
        self.value= value
        self.freq = freq
        self.prev = None
        self.next=None
class Doublelinkedlist:
    def __init__(self):
        self.size = 0  #the initial size of the double linked list
        self.head=Node(-1,-1,0)
        self.tail=Node(-1,-1,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def addtohead(self,node):
        nxt=self.head.next
        node.prev=self.head
        node.next=nxt
        self.head.next=node
        nxt.prev=node
        self.size+=1
    def deletenode(self,node):
        if self.size == 0:
            return
        prv=node.prev
        nxt=node.next
        prv.next=nxt
        nxt.prev=prv
        self.size-=1
    def deletefromtail(self):  #as we need to remove the least frequently used node which lies at the tail of the double linked list
           if self.size == 0:
               return 
           rmved = self.tail.prev 
           self.deletenode(rmved)
           return rmved
    #our double linked list is also designed
class LFU:
    def __init__(self,capacity):  #capacity means the total number of nodes that will be in the LFU cache
        self.keynode_pair = { }  #this dict storest the key of nodes and nodes in the form of key-value pair
        self.freqnode_pair=defaultdict(Doublelinkedlist)  #this dictionary stores the freq of nodes and the doublelinked list in  the key-value pair
        self.capacity = capacity
        self.minfreq = 0
    def put(self,data):
        k = data[0]  #key of the node
        v=data[1]    #value of the node
        if k in self.keynode_pair:  #first we update in the freqnode pair  cause the current or previous freq of node matters
            self.keynode_pair[k].value = v
            self.update(self.keynode_pair[k])
            return 
        
        if len(self.keynode_pair) == self.capacity:  #if the current size is same as that of the given capacity then we must remove the tail node from the minimum freq freqnode pair list
            lst=self.freqnode_pair[self.minfreq]
            remved=lst.deletefromtail()
            del self.keynode_pair[remved.key]
        newnode = Node(k,v,1)
        self.keynode_pair[k] = newnode
        self.freqnode_pair[1].addtohead(newnode)  #adding this new node in the head of the double linked list of freq pair 1
        self.minfreq = 1
       
            

            
    def update(self,node): #this is our helper function
        currfreq=node.freq  #current freq of node
        self.freqnode_pair[currfreq].deletenode(node)
        if currfreq == self.minfreq and self.freqnode_pair[currfreq].size == 0:
            self.minfreq = currfreq + 1
        self.freqnode_pair[currfreq+1].addtohead(node)   #updating the freq of node and inserting this passed node in one value greater than its prev freq in freq node pair
        
        node.freq=currfreq+1  #here we are also updating the freq of this passed node
    def get(self,k): #here k is the key
        if k not in self.keynode_pair:
            return -1
        node = self.keynode_pair[k]
        v= node.value

        self.update(node)
        return v
    def printdatas(self):
        a=[]
        for freq in self.freqnode_pair:  
            itr=self.freqnode_pair[freq].head.next  #in each frequency there is a list of nodes with head as well as tail
            while itr!=self.freqnode_pair[freq].tail:
                a.append(str(itr.value))
                itr=itr.next
        return ''.join(a)        

lfuu=LFU(4)
lfuu.put([1,1])
lfuu.put([2,2])
lfuu.put([3,3])
lfuu.put([4,4])
print(lfuu.get(4))
print(lfuu.printdatas())
print(lfuu.get(1))
print(lfuu.printdatas())



