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
# time complexity : O(N*M)  where N is the length of the parent array and M is the length of the child array
# space complexity : O(1)


# optimal approach
def optimalrow(array):
    n = len(array)  # this is the length of the parent array
    m = len(array[0])  # This is the number of columns
    ans = -1
    row = 0
    col = m - 1
    while row < n and col >= 0:  # here what we are doing is
        # we are checking from the first row and from this first row we are checking from the last index if this last index number is 1 then the answer might be this row  ,
        # and the reason that we are checking from the last index is that our child arrays are already sorted,
        if array[row][col] == 1:
            ans = row
            col -= 1
        else:
            row += 1
    return ans


# Search in a 2D matrix
# Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, and the first element of a row is greater than the last element of the previous row (if it exists), and an integer target, determine if the target exists in the given mat or not.


def search2d(
    array, k
):  # here k is the target which we need to check if this exists or not
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == k:
                return True
    return False


print(search2d([[1, 2, 4], [6, 7, 8], [9, 10, 34]], 78))
# time complexity : O(N*M)
# space complexity : O(1)


def findk(
    array, k
):  # this function is the main function of checking whether the k lies in the array or not
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == k:
            return True
        elif array[mid] < k:
            low = mid + 1
        elif array[mid] > k:
            high = mid - 1
    return False


# so for the better approach what we do is we check in every rows whether the target k lies within the row or not.
def bettersearch2d(array, k):
    m = len(array[0])  # this is the length of the child array
    for i in range(len(array)):
        # what this loop is doing is that first of it goes through every rows of the matrix ,and as the child rows are sorted in ascending order , if the target k lies within the child array, then we pass that specific array to the function which do the particular check of target k element or number
        if (
            array[i][0] <= k <= array[i][m - 1]
        ):  # this check whether k lies in original array or not by checking in each and every rows
            # if it does then we pass this particular array where we found the target
            return findk(array[i], k)


print(bettersearch2d([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
# time complexity : O(N+log(M)) here N is the length of parent array and M is the length of child array
# space complexity : O(1)


# so for the row , we should calculate mid // m and for the column we should calculate mid % m , where m is the length if the child array
# in the optimal approach, what we do is we flatten the array imaginarily
def optimalsearch2d(array, k):
    n = len(array)
    m = len(array[0])
    low = 0  # this is at the 0 index
    high = (n * m) - 1  # this is at the last index of the flatten array
    while low <= high:
        mid = (
            low + high
        ) // 2  # this gives us the index value to check for target number k
        if array[mid // m][mid % m] == k:
            return True
        elif array[mid // m][mid % m] > k:
            high = mid - 1
        else:
            low = mid + 1
    return False


# time complexity : O(logN*M)
# space complexity : O(1)


# Search in 2D matrix - II
# Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, write an efficient algorithm to search for a specific integer target in the matrix.


# brute appoach
# in the brute approach what we do is we go through each and every numbers in the given 2D matrix to check whehter the target k exists or not
def brute2dmatrix(array, k):
    for i in range(len(array)):  # this loop goes through the each rows
        for j in range(len(array[0])):  # this loop goes through each columns
            if array[i][j] == k:
                return True
    return False


print(
    brute2dmatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        75,
    )
)
# time complexity : O(N * M)
# space complexity : O(1)


# better approach
# in the better approach what we will do is we go through each and every rows and check  by using the binary search method
def checkrow(array, k):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == k:
            return True
        elif array[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
    return False


def better2dmatrix(array, k):
    for i in range(len(array)):  # going through each and every rows
        check = checkrow(
            array[i], k
        )  # then we pass i indexed row or lets say each and every rows to check the target k using the function checkrow
        if check:
            return True  # if we found k then we return true
        else:
            continue  # otherwise we just continue with another iteration of i.
    return False


print(
    better2dmatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        5,
    )
)
# time complexity : O(N*logM)  for every rows we check k using binary search so the time complexity is O(N*logM)
# space complexity : O(1)


# optimal approach
# in the optimal approach what we gonna do is we first check with the last indexed number of the first row , as our numbers are sorted row wise as well as column wise
# lets say in the opposite L shape
def optimal2dmatrix(array, k):
    row = 0
    column = len(array[0]) - 1
    while (
        row <= len(array) - 1 and column >= 0
    ):  # the row can go as much as until number of rows - 1 and the columns can only go until 0 otherwise it will be out of the range
        if array[row][column] == k:
            return (row, column)
        elif array[row][column] > k:
            column -= 1
        elif array[row][column] < k:
            row += 1
    return False


print(
    optimal2dmatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        30,
    )
)
# time complexity : O(N + M)   here time complexity is O(N + M) because what we are doing is we are only going through every rows and columns but alternately.
# space complexity : O(1)


# Find peak element
# Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.
# Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].
# Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.
# Note:
# As there can be many peak values, 1 is given as output if the returned index is a peak number, otherwise 0.


def brutepeak(array):
    n = len(array)
    if len(array) == 1 or array[0] > array[1]:
        return 0  # if there is only one element in an array or the first number is greater than the second number then of course the peak number or element will be 0
    elif array[n - 1] > array[n - 2]:
        return (
            n - 1
        )  # if the last indexed number is greater than the second last than ofcourse this last index will be our answer cause after this index there are no numbers in an array.
    else:
        for i in range(
            1, n - 1
        ):  # then we are running the loop from 1 index to n-1 index as we already did the checking for the first as well as the last indexed number
            if array[i - 1] < array[i] and array[i] > array[i + 1]:
                return i
    return -1  # we are returning -1 if there are no peak elements


print(brutepeak([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
# time complexity : O(N)
# space complexity : O(1)


# better approach
def betterpeak(array):
    n = len(array)
    if len(array) == 1 or array[0] > array[1]:
        return 0  # if there is only one element in an array or the first number is greater than the second number then of course the peak number or element will be 0
    elif array[n - 1] > array[n - 2]:
        return (
            n - 1
        )  # if the last indexed number is greater than the second last than ofcourse this last index will be our answer cause after this index there are no numbers in an array.
    else:
        left = 1
        right = n - 2
        while left <= right:
            mid = (left + right) // 2
            if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
                return mid
            elif (
                array[mid] > array[mid - 1]
            ):  # if the current mid indexed number is greater than the previous one then the peak number must be in the right half
                left = mid + 1
            elif (
                array[mid] > array[mid + 1]
            ):  # otherwise if the current midindexed number is greater than it's later number then the peak number must be in the left half
                right = mid - 1
            else:  # if the mid is at that point where going either side will help us to reach the peak number then we can either go to the left half or the right half
                left = mid + 1
        return -1


print(betterpeak([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
# time complexity : O(logN)
# space complexity : O(1)


# peak element in 2d matrix
# brute approach


# practicing of peak element in 2d matrix
# so the naive brute approach will be going through each and every elements or numbers in an array and checking if the left and the right indexed number is greater than the mid indexed number
# in this brute approach what we can do is we can go through each and every numbers in the array and check whether that specific number is greater than its previous number as well as the later number
def brutepeak2d(array):
    for i in range(len(array)):  # first of all looping through each and every rows
        for j in range(len(array[0])):  # looping through each and every columns
            left = array[i][j - 1] if j - 1 >= 0 else -1
            right = array[i][j + 1] if j + 1 < len(array[0]) else -1
            top = (
                array[i - 1][j] if i - 1 >= 0 else -1
            )  # the top must be greater than or equal to 0 otherwise its value will be -1
            bottom = (
                array[i + 1][j] if i + 1 < len(array) else -1
            )  # the bottom must be within the number of rows , if it exceeds then the value of bottom will be -1
            if (
                array[i][j] > left
                and array[i][j] > right
                and array[i][j] > top
                and array[i][j] > bottom
            ):
                return (i, j)
    return -1


print(
    brutepeak2d(
        [
            [3, 8, 12, 15, 20],
            [5, 10, 14, 18, 25],
            [7, 13, 17, 22, 28],
            [9, 16, 21, 26, 30],
            [11, 19, 40, 27, 35],
        ]
    )
)
#time complexity : O(N*M)
#space complexity : O(1)

def findmax(array, mid):
    m = -1
    ans = 0
    for i in range(len(array)):  # we go through each rows
        if (
            array[i][mid] > m
        ):  # here what we are doing is finding the maximum number in the given column mid from each rows
            m = array[i][mid]
            ans = i
    return ans


def optimalpeak2d(array):
    # in the optimal approach what we are doing is we are checking the mid index based on the column wise or vertically then we find out the maximum element or number in that specific column where the mid lies
    low = 0  # we make the low as 0 caus
    high = len(array[0]) - 1  # high will be the last index of our column
    while low <= high:
        mid = (low + high) // 2
        # as we get the mid value now what we try to do is we find out the maximum value from that specific column where this mid lies
        row = findmax(
            array, mid
        )  # now as we find out the row which has the maximum value in this specific column mid
        left = (
           array[row][mid - 1] if mid - 1 >= 0 else -1
        )  # here the left or mid - 1 must be with in the range of array[0]
        right = (
            array[row][mid + 1] if mid + 1 < len(array[0]) else -1
        )  # here the right or mid + 1 also must be with in the range of array[0] which is lesser than the length of child array
        if left <= array[row][mid] and right <= array[row][mid]:
            return (row, mid)
        elif (
            left != -1 and left > array[row][mid]
        ):  # if the left indexed number at the obtained row is greater than the mid indexed number then our answer or peak number lies in the left half
            high = mid - 1
        elif (
            right != -1 and right > array[row][mid]
        ):  # if the right indexed number at the obtained row is greater than the mid indexed number then our answer lies in the right half
            low = mid + 1
    return -1


print(
    optimalpeak2d(
        [
            [3, 8, 12, 15, 20],
            [5, 10, 14, 18, 25],
            [7, 13, 17, 22, 28],
            [9, 16, 21, 26, 30],
            [11, 19, 40, 27, 35],
        ]
    )
)
# time complexity : O(logM * N)  here M is the number of columns and N is the number of rows
# space complexity : O(1)


#Matrix Median
#brute approach
#so the naive brute approach can be sorting the given 2d matrix in 1 array in ascending order then finding the median
def brutemedian2d(array):
    test = []
    for i in range(len(array)):
        for j in range(len(array[0])):
            test.append(array[i][j])
    #now as we are done appending all the numbers from 2d matrix in an array called test , we need to sort them
    test=sorted(test)
    medianindex=len(test) // 2
    if len(test) % 2 !=0:
        return test[medianindex]
    else:
        return (test[medianindex] + test[medianindex-1]) / 2  
print(brutemedian2d([ [1, 3, 8], [2, 3, 4], [1, 2, 5] ]  ))           
#time complexity : O(N*M * logN*M) logN*M is for sorting the array
#space complexity : O(N*M)


def upperbound(array,mid):  #this is the main function for counting the number of elements which are lesser than or equal to the given mid value , 
    #in this function what we do is 
    low = 0
    high = len(array)-1
    ans = len(array)   #all of the numbers in the row might be lesser than or equal to the midvalue
    while low<=high: 
        midvalue = (low + high) // 2
        if array[midvalue]>mid:   #if the current midvalue indexed number is greatr than the given mid then this midvalue index might be our answer which gives the number of elements which are lesser than or equal to given mid
            ans = midvalue   #as the midvalue gives us the index of the numebr which is greater than the given mid and as our array is sorted row wise, the numbers before this index is always smaller than or equal to the given mid and instead of moving to right half , we just destroy the right half and move into the left half
            high=midvalue-1  #to check whether there might exist a number that can be greater than the given mid
        else:
            low=midvalue + 1    
    return ans        






def smallequal(array,mid):  #this is just a pathway function which passes the mid value to check the numbers smaller or equal to the this mid value in the given matrix by going through each and every rows
    count = 0
    for i in range(len(array)):
        count+=upperbound(array[i],mid)
    return count    



#optimal approach
def optimalmedian2d(array):
    low =float('inf')
    high = float('-inf')
    n=len(array)  #n is the length of an array or number of rows
    m=len(array[0])  #m is the length of a child array or number of columns
    #as our arrays are sorted row wise
    #we can just go through the first column to get the smallest number in the matrix and we can just go through the last column to get the largest number in the matrix
    for i in range(len(array)):  #going through each and every rows
        low = min(low,array[i][0])   #going through every first columns
        high = max(high,array[i][m-1])   #through every last columns
    median = (n * m) // 2  
    while low<=high:
        mid = (low + high) // 2 
        #now as we get the mid value which might be our median
        #but first we need to check how many numbers are lesser than or equal to this mid value   
        smallerequal = smallequal(array,mid)
        if smallerequal<=median:  #if the number of elements which are lesser than the  mid value is way lesser than the median index then our answer might lie in the right half
            low=mid+1
        else:   #if the number of elements which are lesser than the mid value is greater than the median index then our answer lies in the left half
            high = mid-1
    return low   
print(optimalmedian2d([ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] ))       

#so the main concept behind this optimal solution is we need to find the number of elements smaller than  or equal to the obtained mid and this number which 
#is the number of elements smaller than or equal to the obtained mid must be just greater than the median position or index which is (n*m) // 2, not too great and not too small
#time complexity : O(log(max-min) * O(N*logM))  #here N is the number of rows and M is the number of columns
#space complexity : O(1)