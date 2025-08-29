class Node:  #here we are making a class of node ,
    #this class is responsible for creating a node
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    #this class is mainly responsible for creating the linked list and the linked list always has the head. so , we must create a head of this linked list
    def __init__(self):  
        self.head=None
    def insert_at_beginning(self,data):  #here to insert the new data at the beginning of the linked list , we first need to create a node having its next as the self.head which is the previous head of the linked list
        value = Node(data,self.head)
        self.head=value        #here self.head means we are creating a new head which is this newly created node
    def insert_at_end(self,data):
        itr=self.head  #here we are storing the head of the linked list in a var called itr
        while itr.next:  #then as long as this itr.next exists which we try to avoid or move
            itr=itr.next     #by making it's value the next node from it
        #Then at last we come to the node where the itr.next does not exists then this itr's next will be the newly created node that we have.    
        new_value=Node(data,None)  #as at the last node the next will be none   
        itr.next=new_value    #in this way, we insert the value at the last of the linked list
    def print(self):
        itr = self.head  
        value=''
        while itr:
            value+=str(itr.data)+','
            itr=itr.next
        return value
    def countlength(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr=itr.next
        return count
    def searchelem(self,pos):
        itr = self.head
        count = 0
        value = ''
        if pos==0:
            value+=self.head.data
            return value
        if pos<0 or pos>=self.countlength():
            raise Exception('Invalid index')
        while itr:
            if count==pos-1:
                value+=itr.next.data  #here the count must be pos-1 , then it's next node data will be the required data that is needed to search
                return value


           
            itr=itr.next
            count+=1

        

    def removethenode(self,pos):
        count = 0
        itr = self.head
        if pos == 0:  #if we want to remove the first or the head of the linked list then the self.head will be changed into self.head.next
            self.head=self.head.next
            return
        if pos<0 or pos>=self.countlength():
            raise Exception('Invalid index')  #if the targeted index is lesser than 0 and greater than or equal to the length of the linked list then we raise an exceptional error.
        while itr:
            if count == pos - 1:   #here this is like a trick or you can say a formulae ,if the current count is same as that of the index-1 then we come to the targeted itr or head whose next is the head we want to remove
                itr.next=itr.next.next
                break
            count+=1
            itr=itr.next
    def insertdatas(self,datalist):
        for data in datalist:
            self.insert_at_beginning(data)        
            


        




if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_beginning('77')
    ll.insert_at_end('11')
    ll.insert_at_end('22')
    print(ll.countlength())
    print(ll.print())
    ll.insertdatas(['apple','orange','banana'])
    print(ll.print())
    print(ll.searchelem(1))
    
