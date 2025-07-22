#Given an array of integers nums, return the value of the largest element in the array
def maxelem(array):
    max=array[0]
    for i in range(len(array)):
        if max<array[i]:
            max=array[i]
     
    print(max)
maxelem([5,4,10,2,1])    