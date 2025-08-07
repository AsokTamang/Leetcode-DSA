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