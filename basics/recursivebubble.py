def recursiveBubble(array,n): #n is the length of an array
    if (n==1): 
        print(array)
        return  #as the smallest element is already at the first position when n is 1 so we return the function
    for i in range(n-1):
        if array[i]>array[i+1]:
            array[i],array[i+1]=array[i+1],array[i]  #by doing this the largest element will be at the last so we must neglect this while doing recursion
    recursiveBubble(array,n-1)
         
recursiveBubble([1,0,3,7,7,8,1,6],8)