#so the last element in the linked list is called the tail of the linked list and the starting element is called the head of the linked list
#and the main property of the linked list is that we can insert any number of datas or any random datas but we must know the preceding position or the preciding element of the position at which we are going to insert this new element
#cause this preceding position or preceding number gives us the next position at which we are going to insert the new element or new data.

class Node: 
    def __init__(self,data=None,next=None):  #here data represents the data or any value to be inserted in the node and next represents the pointer which connect us to the next data or value   
        self.data=data 
        self.next=next  #here next means the pointer pointing towards the next node
class LinkedList:
    def __init__(self):   #first of all we are creating an empty headed linked list which has no any connecting pointer.
        self.head=None
    def insert_at_the_beginning(self,data):
        node = Node(data,self.head)      #here we are creating a node having a data  
        self.head = node   #then we are creating a head based on the node we just created 
        #which means now the self.head which is the header of the linked list will be the recently created node
   
    def insert_at_end(self,data):  #to insert the data at the end first we need to check whether the self.head is null or not
        if self.head is None:
            self.head=Node(data,next=None)  #as we are inserting the data at the end , thats why our next will be none
            return
        itr = self.head  #here we are assuming itr as the self.head which is the head node of the linked list
        while itr:  #if the headnode of the linked list does exist then the current itr node will be the next itr node
            itr=itr.next
        #then after going through all the next nodes , we obviously come to the last or tail node
        itr.next=Node(data)      
          #then after going through each and every itr value or node we are inserting the new node at the end
           #then we insert the value or data at the last of the linked list whose next is None
    def insert_datalist(self,datalist):
        self.head=None  #as we are creating a completely new linked list , so we can use either one of the insert at the end or insert at the beginning function to insert these datas
        for data in  datalist:
            self.insert_at_the_beginning(data)
        itr= self.head
        c=0   
        while itr:   #this loop is for counting the number of nodes in the linked list
            c+=1
            itr=itr.next
        return c    
    
    def remove_at(self,pos):
        itr=self.head   #here head will always be the head of the node
        c = 0
        if pos==0:  #here if we want to remove the first element then the self.head will be the self.head.next
            self.head=self.head.next 
        if pos<0 or pos>=self.countlength():  #here the index must lie with in the range of our linked list length
            raise Exception('Invalid index')     #if the target index lies below 0 or is greater than or equal to the length of the linked list then we just raise an invalid index

        while itr:
            if c==pos - 1: #suppose we need to remove the element at index 1 then of course at first the count will be 0
                itr.next=itr.next.next  #here to remove the element at index 1 , the count must be 0 which is only possible when the current itr will be the first number 
                #so itr.next which is the 1 indexed number that we want to remove = itr.next.next will automatically remove the current itr.
                break
            c+=1
            itr=itr.next
        value = ''
        while itr:
            value+=itr.data
        return value    



    def countlength(self):
        itr=self.head
        c=0
        while itr:
            c+=1
            itr=itr.next   #as long as the itr or the node exists then we just keep on counting and going over the next node only after increasing the count by 1
        return(c)



    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        iteration = self.head
        value = ''
        while iteration:   #as long as the head or the node exists then we just keep on printing the values in the linked list
            value+=str(iteration.data)+ ', '  #here as we are adding the value at the beginning of the data of every current node thats why the latest value will always be inserted at the beginning
            iteration=iteration.next
        print(value)

if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_the_beginning(11)
    ll.insert_at_the_beginning(7)
    ll.insert_datalist(['apple','banana','orange'])
    ll.countlength()
    ll.print()
    print(ll.remove_at(1))  
