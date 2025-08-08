#Given an integer array nums. Return the number of reverse pairs in the array.
#An index pair (i, j) is called a reverse pair if:
#0 <= i < j < nums.length
#nums[i] > 2 * nums[j]

def merge(array,low,mid,high):
    left = low 
    right = mid + 1
    tempo=[]
    while left<=mid and right<=high:
        if array[left]<=array[right]:
            tempo.append(array[left])
            left+=1
        else:
            tempo.append(array[right])
            right+=1
    while left<=mid:
        tempo.append(array[left])
        left+=1
    while right<=high:
        tempo.append(array[right])
        right+=1
    array[low:high+1]=tempo    





def countreverse(array,low,mid,high):   #and for each splitted halves , we calculate the reverse pairs
    count = 0
    right = mid + 1
    for i in range(low,mid+1):
        while right<=high and array[i] > 2 * array[right]:
            right += 1
        count+=right - (mid + 1)   #then we calculate the number of numbers of left array which satisfy the condition    
    return count        

        



def mergemethod(array,low,high):   #so this function is used for splitting the array into two halves using merge sort algorithm,
    mid = (low + high) // 2 
    if low>=high:
        return 0
    cl=mergemethod(array,low,mid)
    cr=mergemethod(array,mid+1,high)
    cf=countreverse(array,low,mid,high)   #then before merging the arrays we just count the reverse pairs
    merge(array,low,mid,high)
    return cl + cr + cf
a = [6, 4, 1, 2, 7]
print(mergemethod(a[:],0,len(a)-1))

#time complexity : O(NlogN)  as we are usign the divide and conquer method for every array possible so it takes N * logN time complexity
#space complexity : O(N)     and as we are using tempo array which stores the sorted array so the space complexity is O(N)



     