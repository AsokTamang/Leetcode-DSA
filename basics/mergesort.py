# so the thing i learned from watching strivers vid was that inorder for the merge sort to happen, we need to divide an array into two with the range of starting point
# to the middle point and then middle point +1 to the end point and then we call the same merge sort function on these two arrays. till the base case when the starting point is equal to or greater than the ending point.
# and inside this main merge sort function there is separate merging function where we merge the arrays returned from the dividing merge function and the sorting will happen based on the order asked by the question either ascending or descending.

import math


# this is the function for merging
def merge(array, low, mid_index, high):
    tempo = []  # this is a temporary array for storing the sorted array
    left = low
    right = mid_index + 1
    while left <= mid_index and right <= high:
        if array[left] <= array[right]:
            tempo.append(array[left])
            left += 1
        else:
            tempo.append(array[right])
            right += 1
    # then after the while loop if still there is an array on both left and right side then we append those array into the tempo array
    while left <= mid_index:
        tempo.append(array[left])
    while right <= high:
        tempo.append(array[right])
    for i in range(len(tempo)):
        array[i] = tempo[i]
    print(array)


# down below is the main function
def mergesort(array, low, high):

    mid_index = (low + high) // 2  # here we are finding the min-index of an array
    if low == high:
        return
    mergesort(
        array, low, mid_index
    )  # here for the first half of array we are passing low as the low and mid_index as the high
    mergesort(
        array, mid_index + 1, high
    )  # then for the second half of array, we are passing mid_index +1 as low and high as the high
    merge(array, low, mid_index, high)


def ms(array, low, n):
    mergesort(array, low, n - 1)


ms(
    [0, 2, 4, 1, 6, 6, 7, 1], 0, 8
)  # here we are passing the array and the low which is 0 and the n-1 which is the lenght of an array-1
