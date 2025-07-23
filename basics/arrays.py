#Given an array of integers nums, return the value of the largest element in the array
def maxelem(array):
    max=array[0]
    for i in range(len(array)):
        if max<array[i]:
            max=array[i]
     
    print(max)
maxelem([5,4,10,2,1])    

#Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.
  
#better approach  
#its time complexity will be O(N) and space complexity will also be O(2) which is constant
def secondLargest(array):
    largest=float('-inf')  #here we are just assigning the positive inf float value to the largest variable
    seclarge=float('-inf') #same with the seclarge variable
    for i in range(len(array)):
        if(array[i]> largest):
            largest=array[i]
    for i in range(len(array)):
        if(array[i]>seclarge and (array[i]!=largest or array[i]<largest)):
            seclarge=array[i]
        elif (array[i]>seclarge and array[i]>largest):
            largest=array[i]
            seclarge=largest           
    print(largest)
    print(seclarge)
secondLargest([10,11,4,2,1,11,9])    

#optimal approach

def seclrgest(array):
    largest=float('-inf')
    seclargests=float('-inf')
    for i in range(len(array)):
        if array[i]>seclargests and array[i]>largest:   #here when the i index array value is greater than seclargest and also greater than the largest 
            seclargests=largest   #then ofcourse the largest will be the seclargest and the  array[i] will be the largest
            largest=array[i]
             
        elif array[i]>seclargests and (array[i]!=largest or array[i]<largest):      #and if the value is greater than the seclargest and is not equal to the largest or lesser than the largesst then 
            seclargests=array[i]      #the sec largest will be the array[i] value
    print(largest)
    print(seclargests) 
seclrgest([10,11,4,2,1,11,9])            

def secondsmallest(array):
    smallest=float('inf')
    secsmallest=float('inf')
    for i in range(len(array)):
        if(array[i]< smallest and array[i]<secsmallest ):  #here if the indexed i array elem is lesser than both smallest and the secsmallest then of course the smallest will be array[i] and the second smallest will be the smallest
            secsmallest=smallest
            smallest=array[i]
        elif (array[i] > smallest or array[i]!=smallest) and array[i]<secsmallest:
            secsmallest=array[i]   #then if the array[i] element is greater than the smallest and smaller than the second smallest then ofcourse the second elem will change to the index array elem
    print(smallest)
    print(secsmallest)
secondsmallest([10,11,4,2,1,11,9])            


#Given an array nums of n integers, return true if the array nums is sorted in non-decreasing order or else false.

def sorting(array,n):
   
    for i in range(n):
        if (array[i]>array[i+1]):
            return False
        else:
            return True

      
                
print(sorting([9,1,6,11,7,8],6))

#Given an integer array nums sorted in non-decreasing order, remove all duplicates in-place so that each unique element appears only once. Return the number of unique elements in the array.

#If the number of unique elements be k, then,#Change the array nums such that the first k elements of nums contain the unique values in the order that they were present originally.
#The remaining elements, as well as the size of the array does not matter in terms of correctness.
def sorting2(array):
    storage=list(set(array))
    tempo=[0] * len(array)
    for i in range(len(tempo)):
        if i < len(storage):
            tempo[i]=storage[i]
        else:
            tempo[i]='_'    
    print(tempo[0:])
sorting2([0, 0, 3, 3, 5, 6])    
    





            
            
  