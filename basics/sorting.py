#selection sort method
def sorting(array):
    for i in range(len(array)):   #here this loop runs upto the len of an array.
        min_index=i    #and we are setting the minimumIndex to i which is 0 right now at the beginning 
        for j in range(i,len(array)):
            if array[j]<array[min_index]:  #then we compare each and every elements in an array with the i indexed array element , and if its smaller then we change the minimum index to that value of j
                min_index=j   #then after completing the whole loop from i to len array we get the actual minimum index in each round
        array[i],array[min_index]=array[min_index],array[i]   #then we swap the i indexed with the minumin index element in an array.

   
    print(array)
sorting([9,2,16,13])

#bubble sort method

def bubbleSort(array):
    for i in range(len(array)):    #this is the outer loop which runs for 6 times
           
           for j in range(len(array)-1): 
       
            if array[j+1]<array[j]:
                array[j],array[j+1]=array[j+1],array[j]
    print(array)            


bubbleSort([9,27,11,5,7,1])



