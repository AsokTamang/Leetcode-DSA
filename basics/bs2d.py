# Binary search on 2D arrays
# Find row with maximum 1's
# Given a non-empty grid mat consisting of only 0s and 1s, where all the rows are sorted in ascending order, find the index of the row with the maximum number of ones.
# If two rows have the same number of ones, consider the one with a smaller index. If no 1 exists in the matrix, return -1.


def bruterow(array):
    number = 0
    ans = -1
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i][j] == 1:
                count += 1
        if count > number:
            number = count
            ans = i
        elif count == number and ans != -1:
            ans = min(ans, i)
    if ans > -1:
        return ans
    else:
        return -1


print(bruterow([[0, 0], [0, 0]]))
#time complexity : O(N*M)  where N is the length of the parent array and M is the length of the child array
#space complexity : O(1)

#optimal approach
def optimalrow(array):
    n = len(array)   #this is the length of the parent array
    m = len(array[0])   #This is the number of columns
    ans = -1
    row = 0
    col = m-1
    while row<n and col>=0:   #here what we are doing is 
        #we are checking from the first row and from this first row we are checking from the last index if this last index number is 1 then the answer might be this row  ,
        #and the reason that we are checking from the last index is that our child arrays are already sorted,
        if array[row][col] == 1:
            ans = row
            col-=1
        else:
            row+=1
    return ans  



#Search in a 2D matrix
#Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and the first element of a row is greater than the last element of the previous row (if it exists), and an integer target, determine if the target exists in the given mat or not.

def search2d(array,k):  #here k is the target which we need to check if this exists or not
    for i in range(len(array)):
     for j in range(len(array[0])):
         if array[i][j] == k:
             return True
    return False     
print(search2d(  [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ],78))   
#time complexity : O(N*M)
# space complexity : O(1)   


def findk(array,k):  #this function is the main function of checking whether the k lies in the array or not
    low = 0
    high = len(array)-1
    while low <=high:
        mid = (low + high) // 2
        if array[mid] == k:
            return True      
        elif array[mid] < k:
            low = mid + 1 
        elif array[mid] > k:
            high = mid - 1
    return False 
       




#so for the better approach what we do is we check in every rows whether the target k lies within the row or not.
def bettersearch2d(array,k):
    m=len(array[0])  #this is the length of the child array   
    for i in range(len(array)):
        #what this loop is doing is that first of it goes through every rows of the matrix ,and as the child rows are sorted in ascending order , if the target k lies within the child array, then we pass that specific array to the function which do the particular check of target k element or number
        if array[i][0] <=k <=array[i][m-1]:    #this check whether k lies in original array or not by checking in each and every rows
            #if it does then we pass this particular array where we found the target 
             return findk(array[i],k)
print(bettersearch2d( [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ], 8))  
#time complexity : O(N+log(M)) here N is the length of parent array and M is the length of child array 
# space complexity : O(1)  


#so for the row , we should calculate mid // m and for the column we should calculate mid % m , where m is the length if the child array
#in the optimal approach, what we do is we flatten the array imaginarily  
def optimalsearch2d(array,k):
  n = len(array)
  m=len(array[0])
  low = 0  #this is at the 0 index
  high = (n * m) - 1 #this is at the last index of the flatten array
  while low<=high:
      mid = (low + high) // 2     #this gives us the index value to check for target number k
      if array[mid//m][mid%m] == k:
          return True
      elif array[mid//m][mid%m] > k:
          high=mid-1
      else:
          low=mid+1
  return False
#time complexity : O(logN*M)
#space complexity : O(1)               


#Search in 2D matrix - II
#Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.

#brute appoach
#in the brute approach what we do is we go through each and every numbers in the given 2D matrix to check whehter the target k exists or not
def brute2dmatrix(array,k):
    for i in range(len(array)):  #this loop goes through the each rows
        for j in range(len(array[0])):   #this loop goes through each columns
            if array[i][j]==k:
                return True
    return False
print(brute2dmatrix( [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ],75))
#time complexity : O(N * M)
#space complexity : O(1)



   
      


           