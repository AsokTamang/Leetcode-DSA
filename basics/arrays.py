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

#Given an integer array nums, rotate the array to the left by one.
def rotatearray(array,n):
    first=array[0]
    for i in range(n):
        if i == n-1:
         array[i]=first
        else:
            array[i]=array[i+1] 
    print(array)
rotatearray([10, 0, 3, 3, 5, 6],6)        

def rotatentimes(array,n):
    for i in range(n):
        first=array[0]
        for j in range(len(array)):
            if j == len(array)-1:
             array[j]=first
            else:
             array[j]=array[j+1] 
        print(array)
rotatentimes([10, 0, 3, 3, 5, 6],2)


#Given an integer array nums, move all the 0's to the end of the array. The relative order of the other elements must remain the same. This must be done in place, without making a copy of the array.
def movezeros(array):
   j=0
   for i in range(len(array)):    
       if (array[i]!=0):
           array[i],array[j]=array[j],array[i]
           j+=1
   print(array)       
movezeros([10, 0, 3, 3, 5, 6])     


#Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array. If the target is not found in the array, return -1
                 
def findnum(nums,target):
    for i in range(len(nums)) :
        if nums[i]==target:
            return i
     
    return -1 
        
print(findnum([10, 0, 3, 3, 5, 6],3))



#Given two sorted arrays nums1 and nums2, return an array that contains the union of these two arrays. The elements in the union must be in ascending order.

def sum(array):
    if (len(array)<=1):
        return array

    pivot=array[0]
    left=[num for num in array[1:] if num<pivot]
    right=[num for num in array[1:] if num>=pivot]
    return sum(left) + [pivot] + sum(right)



def union(array1,array2):
    tempo=list(set(array1+array2))
    print(sum(tempo))

(union( [1, 2, 3, 4, 5],[1, 2, 7]))
            
#next solution of union of two sorted arrays
def union2(array1,array2):
    i=0
    j=0
    l1=len(array1)-1
    l2=len(array2)-1
    tempo=[]
    while i<=l1 and  j<=l2:   #here we are using the two pointers method to append the smaller value in the tempo var by comparing the value between the two arrays
        if (array1[i]<array2[j]):
            if( len(tempo)==0 or  tempo[-1]!=array1[i])  :
                tempo.append(array1[i])
            i+=1
        else:
            if( len(tempo)==0 or tempo[-1]!=array2[j] ):
                tempo.append(array2[j])
            j+=1
    while i<=l1:
       
            if(len(tempo)==0 or tempo[-1]!=array1[i]):
                tempo.append(array1[i])
            i+=1
    while j<=l2:
       
            if(len(tempo)==0  or tempo[-1]!=array2[j] ):
                tempo.append(array2[j])
            j+=1
    print(tempo)
union2([1, 2, 3, 4, 5],[1, 2, 7])            


#Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

def findmiss(array,n):
    for i in range(n+1):
        if i not in array:
            print(i)
findmiss( [0, 5, 3, 1, 4],5)

#Given a binary array nums, return the maximum number of consecutive 1s in the array.

def findconsecutive(array):
    count = 0
    maximum=0
    for i in range(len(array)):
        if array[i] == 1:   
            count+=1   #for every found of element 1 , we increase the count by 1
        else:
            count=0
        maximum=max(count,maximum)     #then for every loop we calculate the maximum even if the count is 0 or greater than 0
    print('The maximum consecutives of 1 is:', maximum)           
findconsecutive([1, 1, 0, 0, 1, 1, 1, 0])

#Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.  
def findonce(array,n):  #here n is the length of an array
    tempo=[0] * (max(array)+1)     #as for the hass map the length of an array must be greater than 1 value of the maximum digit in an array
    for i in range(n):
        tempo[array[i]]+=1
    for j in range(len(tempo)):
        if tempo[j]==1:
            print(j)
findonce([1, 2, 3, 4, 3, 1, 4],7)      


#but the most optimal method to find the number which appears only one time in an array can be found using xor cause xor means the a ^ a is 0 but 0 ^ a is a so if we use xor for every numbers in an array only the number left will be the number which appears only one time in an array
def optimalonce(array):
    x=0
    for num in array:
        x^=num      #this code will run xor or ^ for every numbers in an array
    print('The number in an array which appears only one time in an array is:', x)
optimalonce([1, 2, 3, 4, 3, 1, 4]) 

#Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
def summing(array,n,k):    #here n is the length of an array and k is the target element
    s= 0
    sub_Array=[] 
    for i in range(n):
        if array[i]<=k/2 and s<k:     #here to find the longest subarrays we need to have more nums inside a subarray so for that the numbers inside this subarray must be certainly very low compared with the target value
         s+=array[i]
         sub_Array.append(array[i])
    if s == k:
     print(sub_Array)
     print(len(sub_Array))
    else:
        print(0) 
summing( [10, 5, 2, 7, 1, 9],6,15)    

#sliding window approach
def slider(array,k):
    left = 0
    subarray=[]
    max_len=0
    s= 0
    for right in range(len(array)):   #this right goes through every elements in an array.
       
        s+=array[right]
           
        if s > k :   #but if the sum is too big then we subtract the sum with the arrays left most element and we move the left pointer towards right
            s-=array[left]   
            left+=1
            max_len=right-left+1     #here we are calculating the length of a subarray as suppose when the window's length is decreased
        elif s == k:
            if right - left +1 > max_len:   #and if the sum is equal to the target element and the valeu of current lenght which is right - left +1 is greater than the previous max lenght then we assign the current one to the max length 
                subarray=array[left:right+1]   #so that the new sub array becomes the array from array[left:right+1]
                max_len=right-left+1
    
              
    
    if max_len>0:   #and ofcourse if the final max_length is greater than 0 we print the maximum length as well as the subarray otherwise we print 0
     print(max_len)
     print(subarray)
    else:
        print(0)                 

slider([10, 5, 2, 7, 1, 9],15)






          
    



            
            
  