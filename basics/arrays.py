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
    largest=1  #here we are just assigning the positive inf float value to the largest variable
    seclarge=-1  #same with the seclarge variable
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
    largest=1
    seclargests=-1
    for i in range(len(array)):
        if array[i]>seclargests and array[i]>largest:   #here when the i index array value is greater than seclargest and also greater than the largest 
            seclargests=largest   #then ofcourse the largest will be the seclargest and the  array[i] will be the largest
            largest=array[i]
             
        elif array[i]>seclargests and (array[i]!=largest or array[i]<largest):      #and if the value is greater than the seclargest and is not equal to the largest or lesser than the largesst then 
            seclargests=array[i]      #the sec largest will be the array[i] value
    print(largest)
    print(seclargests) 
seclrgest([10,11,4,2,1,11,9])            