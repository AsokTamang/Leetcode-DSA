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