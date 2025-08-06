#counting the reverse pair of an array which means a[i] > 2 * a[j]
def finalmerge(array,low,mid,high):   #this function is for merging the splitted arrays and converting them into ascending order
    tempo = []
    left = low
    right = mid + 1 
    while left <=mid and right<=high:
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
    array[low:high+1] = tempo   #then we are making the change in the array at that specific index                



def countpairs(array,low,mid,high):
    right = mid + 1 
    count = 0
    for i in range(low,mid+1):
        while right<=high and array[i] > 2 * array[right]:
            right+=1
        count+=right - (mid+1)
    return count        




def mergesort(array,low,high):   #here low will be the first index of an array and high will be the last index of an array
    if low>=high:
        return 0 
    mid = (low + high) // 2
    #here we are splitting the array into half
    cl=mergesort(array,low,mid)  
    cr=mergesort(array,mid+1,high)
    #and for these each splitted arrays,before merging them we are counting the matched reverse pairs where a[i] > 2 *a[j] for which we need separate function
    cc =countpairs(array,low,mid,high)
    finalmerge(array,low,mid,high)
    return cl + cr + cc
array = [6, 4, 1, 2, 7]
print(mergesort(array[:],0,len(array)-1))