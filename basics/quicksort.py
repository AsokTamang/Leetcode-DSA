def quicksort(array):
    if(len(array)<=1):
        return array
    pivot=array[0]   #here in each recursion we are taking the first element of an array as the pivot
    left=[num for num in array[1:] if num < pivot]   #then we are making the list of numbers smaller than the pivot inside a left array
    right=[num for num in array[1:] if num >= pivot] # and in the right the numbers greater than the pivot are taken
    return quicksort(left) + [pivot] + quicksort(right)
sorted=(quicksort([9,7,8,1,2,7,8,2,8]))
print('the second largest is :', sorted[len(sorted)-2])