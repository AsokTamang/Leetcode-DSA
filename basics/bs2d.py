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
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2
      if array[mid] >= k :
         return mid
      elif k>array[mid]:
         left+=1
      else:
         right-=1
   return len(array)
print(lowerbound( [3,5,8,15,19],9))    
#time complexity : O(logN)
# space complexity : O(1) 


def upperbound(array,k):
   left = 0
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2
      if array[mid] > k :
         return mid
      elif k>array[mid]:
         left+=1
      else:
         right-=1
   return len(array)
print(upperbound( [3,5,8,15,19],9))    
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
   
   


        
            

