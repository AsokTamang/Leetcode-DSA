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
        return heapq.heappop(self.elements)[1]  #we are returnign the items name only
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
        
