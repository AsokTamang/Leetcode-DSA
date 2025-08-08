#in the binary search methods we will only use the binary search approach not the linear approach
#Given a sorted array of integers nums with 0-based indexing, find the index of a specified target integer. If the target is found in the array, return its index. If the target is not found, return -1.

def bs(array,k):
   low = 0
   high = len(array) - 1
   while low<=high:
      mid = (low+high) // 2 #for each iteration we calculate the mid 
      if array[mid] == k:
         return mid
      elif k>array[mid]:   #if the target number is way bigger than the mid then we just move the low pointer towars high and again repeat the process
         low+=1
      else:    #same here with the high pointer
         high-=1  
   return -1 #if the target element is not found      
print(bs([-1,0,3,5,9,12],2)) 
#time complexity : O(LogN) as we are using the approach of dividing an array into half and repeating the process till we find the target element 

#Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
#The lower bound algorithm finds the first and smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
#If no such index is found, return the size of the array.

#brute approach
def brutelowerbound(array,k):
   for i in range(len(array)):
      if array[i]>=k:
         return i
   return len(array)
print(brutelowerbound( [3,5,8,15,19],9))   
#time complexity : O(N)  which goes through each and every numbers in an array.
#space complexity : O(1)





#the down below is the better approach
def lowerbound(array,k):
   left = 0
   ans = 0
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2
      if array[mid] >= k :
         ans= mid
         right = mid - 1
      
      else:
         left=mid + 1
   if ans > 0 :
      return ans
   else:
      return len(array)
print('the lowerbound is ',lowerbound( [1,2,2,3],2))    
#time complexity : O(logN)
# space complexity : O(1) 


def upperbound(array,k):
   left = 0
   right = len(array) - 1
   ans = 0
   while left<=right:
      mid = (left + right) // 2
      if array[mid] > k :
         ans = mid
         right = mid - 1

         
      else:
        left = mid + 1
   if ans > 0 :
      return ans 
   else:
      return len(array)
print('The upperbound is : ',upperbound( [3,5,8,15,19],9))    
#time complexity : O(logN)
# space complexity : O(1) 





#Given a sorted array of nums consisting of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def insertposition(array,k):
   left = 0
   right = len(array) - 1
   while left <=right:
      mid = (left + right) // 2
      if array[mid] == k:
         return mid
      elif k>array[mid]:
         left=mid + 1   #if the target number is way greater than the mid value then ofcourse the number might be in the right half of an array
      else:
         right=mid -1   #same logic but opposite operation
   #if the whole loop ran , and we are still not able to find the target number then ofcourse the target number must be on the left index.
   return left         
   
print(insertposition([1, 3, 5, 6], 7))   
#time complexity : O(logN) 
# space complexity : O(1)


#Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.
def floorr(array,x):
   left = 0
   right = len(array) - 1 #last index
   ans = 0
   while left<=right:
      mid = (left + right) // 2
      if array[mid]<=x :
         ans =array[mid] #as the floor is the largest element in the array which is less than or equal to the target number. and
         #if the mid index number is lesser than or equal to x then we move the rane towars right half as we need to find the largest possible number lesser than or equal to the target number
         left = mid + 1
      else:
         right = mid - 1
   if ans > 0:
    return ans
   else:
      return -1
print('The floor is :', floorr([3, 4, 4, 7, 8, 10], 8))


def ceill(array,x):
   left = 0
   right = len(array) - 1 
   ans = 0  #here we are just declaring the variable ans
   while left<=right:
      mid = (left + right) // 2
      if array[mid]>=x:
         ans=array[mid]  
         right = mid - 1 #as we are trying to find the smallest number possible which is  greater than the x and if the mid indexed number is greater than or equal to the target number of course we are searching the required number in the left half for the smallest value possible
      else:
         #but if the mid indexed number is too small then 
         left = mid + 1
   if ans > 0:
    return ans
   else:
      return -1     
print('The ceil is :', ceill([3, 4, 4, 7, 8, 10], 8))
#time complexity : O(logN)  we are using the binary search method so it takes logN time complex
#space complexity : O(1)


#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].
def firstlast(array,x):
 def firstpos():
   left =first = 0 
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2
      if array[mid] == x :  #as we are trying to find the first position where the target number exists , if we find the index which maybe the later position then we move the right pointer towards left side
         first = mid 
         right-=1   #as the array is already sorted we are moving the right towards the left direction to get the initial index
      elif array[mid] < x :
         left = mid + 1
      else:
         right = mid - 1
   if first > 0 :
    return first
   else:
      return -1
       

 def endpos():
   left = 0
   right = len(array) - 1
   end = 0
   while left<=right:
      mid = (left + right) // 2
      if array[mid] == x:
         end = mid
         left+=1   #as the array is already sorted we are moving the left towards the right direction to get the later index
      elif array[mid] < x:
         left = mid  + 1
      else:
         right = mid - 1   
   if end > 0 :
    return end
   else:
      return -1
 firstt=firstpos()
 lastt=endpos()
 return [firstt,lastt]  
print(firstlast([5, 7, 7, 8, 8, 10],6))    










        
            

