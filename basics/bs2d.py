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
#time complexity : O(logN)
#space complexity : O(1)

#You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.
#Return the count of occurrences of target in the array.


def countoccurence(array,x):
   left = 0
   right = len(array) - 1
   count = 0
   a=[]
   while left<=right:
      mid = (left + right) // 2
      if array[mid] == x:
         a.append(mid)
         if mid not in a:
          count+=1
          left+=1
         else:
            left+=1 
      elif array[mid]<x:   #if the mid indexed number is lesser than x then we just increase the left to mid + 1
         left = mid + 1
      else:
         right = mid - 1
   return count
print(countoccurence( [0, 0, 1, 1, 1, 2, 3],1))      
   

#You are given a sorted array of integers arr and an integer target. Your task is to determine how many times target appears in arr.
#Return the count of occurrences of target in the array.

def countoccurance(array,x):
   def firstoccurance():
      left = 0
      first=-1
      right = len(array) - 1 
      while left<=right:
         mid = (left + right) // 2
         if array[mid] == x:
            first=mid
            right=mid - 1  #As we are trying to find the first index for the target number we are moving the right pointer towards the left path
         elif array[mid]>x:
            right = mid - 1
         else:
            left=mid + 1
      return first
   def lastoccurance():
      left = 0
      last=-1
      right = len(array) - 1 
      while left<=right:
         mid = (left + right) // 2
         if array[mid] == x:
            last=mid
            left=mid + 1  #As we are trying to find the first index for the target number we are moving the right pointer towards the left path
         elif array[mid]>x:
            right = mid - 1
         else:
            left=mid + 1
      return last
   first=firstoccurance()
   last=lastoccurance()
   count = last-first+1  #as our array is already sorted so thats why we are using this formula to calculate the number of occurences of a number.
   return count
print('The number of occurences of a number is :',countoccurance([0, 0, 1, 1, 1, 2, 3],1))


#Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.
#in this problem what we do is we check the previous or the after array either they are sorted or not , if th
def searchtarget(array,k):
   left = 0
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2 
      if array[mid] == k:
         return mid
      else:
        if array[left]< array[mid]:  #here first of all we are checking whether the preceding array before the midindex is sorted or not
           if array[left]<=k and k<=array[mid]:     
             right = mid - 1
           else:
              left=mid + 1
        else:
           if array[mid]<=k and k<=array[right]:    #if the preceding array is not sorted then ofcourse the later array is sorted , then we check whether the target number exists between mid and right
              left = mid + 1   #thats why we cancel the left part
           else:
              right = mid - 1           
   return -1
print(searchtarget([4, 5, 6, 7, 0, 1, 2],0))  
#time complexity : O(logN)   
# space complexity : O(1)    


#Problem Statement: Given an integer array arr of size N, sorted in ascending order (may contain duplicate values) and a target value k. Now the array is rotated at some pivot point unknown to you. Return True if k is present and otherwise, return False. 
#as the question is stating that the array may consists of the duplicate values
#so our edge case is what if the first number and mid and last indexed numbers are same 
#in that edge case what we will do is we just decrease the range of an array by 1 , if the midindexd number is not equal to the target number , then of course the first index and the last index number will also wont be equal to the target number.
def searchrotated2(array,x):
   left = 0
   right = len(array) - 1
   while left<=right:
      mid = (left + right) // 2 
      if array[mid] == x:
         return True
      elif array[mid] == array[left] ==array[right]:   #if all of these are equal but arenot equal to the target number as the question states that the array may consists the duplicate number
         left+=1
         right-=1
      elif array[left]<=array[mid]:   #if the left subarray before the mid index is sorted
         if array[left]<=x<=array[mid]:   #if the target number lies in this  left subarray which is sorted then we just destroy the right half.
            right=mid - 1
         else:
            left=mid + 1 
      else:
         if array[mid]<=x<=array[right]:   #if the target number lies in this right subarray which is sorted then we just destroy the left half.
            left=mid + 1
         else:
            right=mid - 1 
   return False
print(searchrotated2([7, 8, 1, 2, 3, 3, 3, 4, 5, 6],1))


#Given an integer array nums of size N, sorted in ascending order with distinct values, and then rotated an unknown number of times (between 1 and N), find the minimum element in the array.

def minimumrotated(array):
   left = 0
   right = len(array) - 1
   ans=float('inf')   #the highest positive number in python
   while left<=right:
      mid=(left+right) // 2
      #but in the edge case if the whole given array is sorted then we just dont need to do the bs as the left index number will be the most minimum
      if array[left]<array[right]:
         ans=min(ans,array[left])
         break
      elif array[left]<array[mid]:     #first of all we are checking whether the left subarray is sorted or not,if yes then ofcourse the most minimum till now will be the first number in the left subarray
          ans=min(ans,array[left])
          #As we find out the most minimum number from the left sorted subarray till the index mid we destroy this subarray and move the left to mid+1
          left=mid + 1
      elif array[mid]<array[right]:  #but if the right subarray is sorted then of course the mid indexed number will be the most minimum
          ans=min(ans,array[mid])
          right=mid-1
   return ans
print(minimumrotated( [4, 5, 6, 7, 0, 1, 2, 3]))     
#time compelxity : O(logN)
#space complexity : O(1)
     
#Given an integer array nums of size n, sorted in ascending order with distinct values. The array has been right rotated an unknown number of times, between 0 and n-1 (including). Determine the number of rotations performed on the array.
#to calculate the number of rotations we must find the index of the smallest number in an array
def numberrotation(array):
   left = 0
   right = len(array) - 1
   mini=float('inf')
   index = 0
   while left<=right:
      mid = (left + right) // 2 
      if array[left]<array[mid]:  #if the left arrays is sorted then of course the first number in the left subarray will be the smallest
         if array[left]<mini: 
          index = left
          mini=array[left]
         left=mid+1
         
      elif array[mid]<array[right]:
         if array[mid]<mini: 
          index = mid
          mini=array[mid]
         right=mid-1
        
   return index
print(numberrotation([4, 5, 6, 7, 0, 1, 2, 3]))

         
#Given an array nums sorted in non-decreasing order. Every number in the array except one appears twice. Find the single number in the array.
#brute approach
def findsingle(array):
   ans = 0
   for i in range(len(array)):
      if i == 0 :
         if array[i]!=array[i+1]:
            ans = array[i]
      elif i ==len(array) - 1:  #if the i is at the last index
         if array[i]!=array[i-1]:
            ans = array[i] 
      else:  #if the i is not at the first index as well as not at the last index then
         if array[i]!=array[i+1] and array[i]!=array[i-1]:
            ans=array[i]
   return ans
print(findsingle([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))         
#time complexity : O(N)
#space complexity : O(1)
#optimal approach
def optimalsingle(array):
   ans = 0
   left = 1
   right = len(array) - 2
   if array[0]!=array[1]: 
       ans=array[0] 
       return ans
   elif array[len(array)-1]!=array[len(array)-2]:
      ans = array[len(array)-1]   #then our answer will the last indexed number
      return ans
   while left<=right:
      mid = (left + right) // 2
      if array[mid]!=array[mid-1] and array[mid]!=array[mid+1]:
         ans=array[mid]
         return ans
      else:
         if mid % 2 == 0 and array[mid] == array[mid+1] or array[mid]==array[mid-1]:  #here we are declaring the condition that if the mid index is at even index and mid indexed number is equal to the later index number then, 
            #our answer lies on the right half , so we must destroy the left half
            left = mid +1 
         elif mid%2 != 0 and array[mid] == array[mid+1] or array[mid]==array[mid-1]:  #but if the mid index is at odd position and if this indexed number is equal to the previous one or the later one then, of course our 
            #answer lies in the preceding half so we must destroy the right half
            right=mid-1 
   return ans
print(optimalsingle( [1, 1, 3, 5, 5]))              
   
