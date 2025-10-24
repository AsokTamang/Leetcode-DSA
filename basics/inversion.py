#Given an integer array nums. Return the number of inversions in the array.
#Two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
#It indicates how close an array is to being sorted.
#A sorted array has an inversion count of 0.
#An array sorted in descending order has maximum inversion.
#to find the inversion method the optimal solution will be the merge sort method


def mergesort(array,low,mid,high):
    count = 0
    left = low 
    right = mid + 1 
    tempo = []    #here we are making a temporary storage or variable which will store the sorted array
    while left<=mid and right<=high:    #and the left array will be from the index low until the mid and the right array will be from the index mid+1 until high
         if array[left]<=array[right]:
             tempo.append(array[left])
             left+=1
         else:
             tempo.append(array[right])    #if the left side number is greater then we append the smaller which is right side array first and this is the condition which was asked by the question , so we calculate the count of inversion     
             count+= mid-left+1    #here if the certain number at the index left is greater than the certain number at the certain index right then the remaining numbers in the left arrray will also be greater than this right indexed number so the count will be the length of the remaining array from index left 
             right+=1
    while left<=mid:
        tempo.append(array[left])
        left+=1
    while right<=high:
        tempo.append(array[right])
        right+=1
    array[low:high+1]=tempo   #then we make change in the array
    return count                 


def splitt(array,low,high):
    mid = (low + high) //2
    if low >=high:   #if the low value is greater than or equal to the high then we just return and start merging
        return 0 
    #otherwise we just keep on splitting the array
    cl=splitt(array,low,mid)    #our mid will be the new high
    cr=splitt(array,mid+1,high)   #our mid+1 will be the new low and high will be the high 
    cm=mergesort(array,low,mid,high)
    return cl+cr+cm   #here cl is the counting left array numbers , cr is the counting right array numbers and cm is the counting merging numbers
a=[2, 3, 7, 1, 3, 5]
print(splitt(a[:],0,len(a)-1))

