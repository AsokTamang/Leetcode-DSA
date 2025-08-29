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
    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        iteration = self.head
        value = ''
        while iteration:
            value+=str(iteration.data) + '-'  #here as we are adding the value at the beginning of the data of every current node thats why the latest value will always be inserted at the beginning
            iteration=iteration.next
        print(value)
    def insert_at_end(self,data):  #to insert the data at the end first we need to check whether the self.head is null or not
        if self.head is None:
            self.head=Node(data,next=None)  #as we are inserting the data at the end , thats why our next will be none
            return
        itr = self.head  #here we are assuming itr as the self.head which is the head node of the linked list
        while itr:  #if the headnode of the linked list does exist then the current itr node will be the next itr node
            itr=itr.next
        #then after going through all the next nodes , we obviously come to the last or tail node
        itr=Node(data,next=None)       #then we insert the value or data at the last of the linked list whose next is None


if __name__=='__main__':
    ll=LinkedList()
    ll.insert_at_the_beginning(11)
    ll.insert_at_the_beginning(7)
    ll.print()        