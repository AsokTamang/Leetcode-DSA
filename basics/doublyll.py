#doubly linked list
#in the doubly linked list we haw two linking points of a single node which is the prev that denotes the linkage to the previous node and other one
#is the next which denotes the linkage to the next node


class Node:
    def __init__(self,data,prev,next):
        self.data=data  #this denotes the data of the node
        self.prev=prev   #this denotes the previous node of the current node
        self.next=next   #this denotes the next node of the current node
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def appendData(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
            return
        itr=self.head  #here first of all we are declaring the iteration of the nodes
        while itr.next:  #then as long as the next value or next node exists then we keep on moving to the next node, until no more
            itr=itr.next
        new_node=Node(data,itr,None)    
          #then we make a new node whose previous will be the last node and it's next will be none            
        itr.next=new_node
    def prepend(self,data):
        if self.head is None:
            new_node=Node(data,None,None)
            self.head=new_node
            return
        itr=self.head
        new_node=Node(data,None,itr)   #the next of the newly created node will be the current head of the doubly linked list
        itr.prev=new_node
        self.head=new_node
   
    def countLength(self):
        itr=self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count    
    def delhead(self):
        itr=self.head.next
        self.head=itr
        itr.prev=None
        return self.head
    #so the trick for reversing the given linked list was swapping the prev and the next of the current node ,as like the two pointers and as all the nodes are calculated , the tempo will become the value None which is after the last node of the original linked list , so the previous of this node is obviously the head of our double linked list 
    def reverselist(self):
        itr=self.head
        tempo=None
        while itr:
            tempo=itr.prev
            itr.prev=itr.next
            itr.next=tempo
            itr=itr.prev  #as our itr.prev is made a itr.next 
            #so while looping the itr will be changed into itr.prev
        if tempo:
            self.head=tempo.prev   #as our temp was none initially , the final value of tempo will alos be none, so the self.head will be the prev of tempo    
    
    def deleteNode(self,index):
        if self.head is None:
            return
        elif index==0:
            itr=self.head.next
            self.head=itr
            itr.prev=None
        elif  index<0 and index>=self.countLength:
            raise ValueError
        else:
            itr=self.head
            count = 0
            
            while itr:
                if count == index-1:
                    a=itr.next.next
                    itr.next=a
                    a.prev=itr
                    return

                count+=1
                itr=itr.next
    def print(self):
        itr=self.head
        value =[]
        while itr:
            value.append(str(itr.data)) 
            itr=itr.next    
        return value            


dll=DoublyLinkedList()
dll.appendData('2')
dll.prepend('1')
dll.prepend('0')
print(dll.print())
dll.reverselist()
print(dll.print())
print(dll.countLength())



#Delete head of DLL
#Given the head of a doubly linked list, remove the node at the head of the linked list and return the head of the modified list.
#The head is the first node of the linked list.
#time complexity : O(1)
#space complexity : O(1)


        

        
        
        