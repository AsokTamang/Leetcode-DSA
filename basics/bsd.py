import math
#Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).
#brute approach
def brutesqr(num):
    ans = 0
    for i in range(1,num+1):
        if (i * i) <=num:
            ans = i
        else:
            break    #if the product becomes greater than the integer itself then there is no point in calculating the product , we are just breaknig or getting out of the loop.
    return ans
print(brutesqr(28))    
#time complexity : O(N)
# space complexity : O(1)  

def optimalsqr(num):
    ans = 0
    left = 1 
    right = num
    while left<=right:
        mid = (left + right) // 2
        if mid * mid <=num:   #if the product of the mid is lesser than or equal to num then the mid might be an answer so 
            ans=mid
            left=mid+1   #as the product of mid * mid is lesser we move the left pointer in the right half
        else:  #if the product is way too greater then we just move the right pointer in the left half
            right=mid - 1
    return(ans)
print(optimalsqr(28))            
#time complexity : O(logN)
#space complexity : O(1)


#Find Nth root of a number
#Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
#brute approach
def nthroot(N,M):
    ans=0
    for i in range(1,M+1):
        if i ** N <=M:
            ans=i
        else:
            break
    if isinstance(i ** N,int):    
     return ans
    else:
        return -1
print(nthroot(3,27)) 
#time complexity :O(N)
# space complexity : O(1)

#better approach
def betternth(N, M):
    ans = -1
    left, right = 1, M
    while left <= right:
        mid = (left + right) // 2
        if (mid**N)==M:
            ans=mid
            return ans
        elif (mid ** N) < M:
            left = mid + 1
        else:
            right = mid - 1
    return ans

print(betternth(4, 69))
#time complexity : O(logM)
#space complexity : O(1)
      

#KOKO EATING BANANAS
#A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.
#Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.
#Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.

#brute approach
#so the question is literally asking us to find the minimum number of bananas that a monkey must eat per hour to finish all the bananas in the given piles so that the total time taken will be exactly the given time h hrs
#and to calculate the time for each pile we devide the pile by the number of hours and the number of hours lie between 1 and the maximum number of bananas in the given array of piles
def brutekoko(array,h):
    for i in range(1,max(array)+1):  # as the required minimum number of bananas lie between 1 and maximum number of banana in an array, we are using this for loop here
        totaltime=0
        for num in array:
            totaltime+=math.ceil(num/i)   #here we are using math.ceil cause we are calculating the number of hours taken for koko to finish eating the bananas from the given pile ,
        if totaltime==h:
            ans=i
    return ans
print(brutekoko([25, 12, 8, 14, 19],5))            
#time complexity : O(max(array) * N)   where N is the number of piles in an array
# space complexity : 0            



#better or optimal approach
#in the optimal approach what we do is , we just use the binary search method between 1 and the maximum number in an array,
#and calculate the total time taken by adding for each piles based on its number of bananas, and if the total time is equal to the given time while the number of bananas to be eaten is minimum , then we get our answer.
def betterkoko(array,h):
    left = 1
    right = max(array)   #as our answer lies between 1 and the maximum number in an array
    #and the fact that the answer lies between 1 and the maximum number in an array is,as 0 cannot be used for the number of banana to be eaten per hr, and for maximum case whichever number higher than the maximum number of array , the dividor will be the same for every left value
    while left<=right:
        mid = (left + right) //2
        totaltime=0
        for num in array:    #this loop runs for N times
            totaltime+=math.ceil(num/mid)    #we are using the math.ceil cause we also need to find the extra hours taken for each pile
        if totaltime<=h:
            ans=mid         
            right=mid-1 #as our answer must be the minimum number of bananas per hours for the total time to be exactly h , we decrease our range inorder to make our mid lesser or smaller which is the divider of the number of bananas in the pile  , to increase the totaltime value 
            #so that we will have a higher chance of getting the matched total time.
        elif totaltime>h:
           left=mid+1
    return ans        
print(betterkoko( [25, 12, 8, 14, 19], 5))
#time complexity : O(log(max(array) * N))   
#space complexity : O(1)


