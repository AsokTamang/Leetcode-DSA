def quicksort(array):
    if (len(array)<=1):   #if due to the recustion only one element is left in an array either left or right then we return the total array
        return(array)
         
    pivot=array[0]  #here we are taking the first element of an array as the pivot
    left = [num for num in array[1:] if num <pivot]
    right=[num for num in array[1:] if num>=pivot]
    return(quicksort(left) + [pivot] + quicksort(right))
print(quicksort([7,2,1,9,11,6,8]))   