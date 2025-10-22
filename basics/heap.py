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
            self.heapify(smaller)  #we heapify the index      
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
    
if __name__=='__main__':
    hh=Heapqueue(5)
    hh.insert(5)
    hh.insert(15)
    hh.insert(25)
    hh.insert(-5)
    hh.insert(2)
    print(hh.elements)
    print(hh.extractmin())
    print(hh.elements)
    print(hh.heapsize())
    print(hh.changekey(3,30))
    print(hh.elements)
#time complexity:  
#insert : O(logN)
#heapify : O(logN)
#heapsize : O(1)