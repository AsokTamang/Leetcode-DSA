#Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.
#A subarray is a contiguous non-empty sequence of elements within an array.

def maxprod(array):
    maxi=float('-inf')
    p = 1
    for i in range(len(array)):
        if p == 0:  #if in anycase the counting product becomes 0 then we remake it to 1 to start a new subarray again. 
            p=1
        p*=array[i]
        maxi=max(maxi,p)   #then for each product we evaluate the maximum product
        
    print(maxi)
maxprod([-5, 0, -2])            