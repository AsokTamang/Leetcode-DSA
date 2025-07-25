#Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
#bruteforce approach
def subarray(array,k):
  
    length=0
    for i in range(len(array)):  #this loop is the outer loop which means it runs for every elements
        s= 0
        for j in range(i,len(array)):
            s+=array[j]
            if s == k:
                length=max(length,j-i+1)   #j-i+1 gives us the length of a subarray
    print(length)
subarray([5,3,2,1,7,1,2,3],11)                


#better approach      
#here in this better approach what we are doing this we are making a subarray from the first index until last and in
#of this subarrays we are  calcuakting whether the sum is equal to or greater than the value of k , if equals then we calculate the maximum kenght 
#but if sum is greater than k , then we just remove the most left part from a sum  and decrease the length of a ssubarrays by subtracting the value of 1 from left
def bettersubarray(array,k):
    s = 0
    length=0
    left = 0
    for i in range(len(array)):
        s+=array[i]
        if s == k:
            if i-left + 1 > length:
                length=max(length,i-left+1) 
        elif s > k :   #but if the sum is greater than the value of k then we remove the extreme left number from our sum
            s-=array[left]
            left+=1     #which means the size of subarray is decreased by 1 from the left side as we keep going on adding the value at the right side           
            length=i-left + 1
    if length > 0:
        print(length)
    else:
        print(0)
bettersubarray([5,3,2,1,7,1,2,3],11)   


#optimal approach
#in the optimal approach what we can do is we can store all the values or nums in an array inside a dict where sum and index acts as a key-value pair
def optimalsubarray(array,k):
    s = 0
    length=0
    d={}
    for i in range(len(array)):
        s+=array[i]
        if s not in d:
            d[s]=i    #then we store the sum at that particular index as a key and the index as a value
        if s == k:
            length=max(length,i+1)      #here as our loop is running from 0 index,so the length is ofcourse i-0+1 so i+1
        elif s-k in d:    #if the current value of s - k exists in our dict then we are trying to find the index of thtat particular s in our dic
            length=max(length,(i-d[s-k]) )  #which is the subtraction of current value of i and index of that particular number and we
            #we are not adding the 1 to measure the lenght of a subarray cause the index at which we find the match or value of s - k is not needed , as we only need the subarrays which starts after this particluar index
    if (length > 0):
        print(length)
    else:
        print(0)
optimalsubarray([5,3,2,1,7,1,2,3],11)            

