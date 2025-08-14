import math


# Given a positive integer n. Find and return its square root. If n is not a perfect square, then return the floor value of sqrt(n).
# brute approach
def brutesqr(num):
    ans = 0
    for i in range(1, num + 1):
        if (i * i) <= num:
            ans = i
        else:
            break  # if the product becomes greater than the integer itself then there is no point in calculating the product , we are just breaknig or getting out of the loop.
    return ans


print(brutesqr(28))
# time complexity : O(N)
# space complexity : O(1)


def optimalsqr(num):
    ans = 0
    left = 1
    right = num
    while left <= right:
        mid = (left + right) // 2
        if (
            mid * mid <= num
        ):  # if the product of the mid is lesser than or equal to num then the mid might be an answer so
            ans = mid
            left = (
                mid + 1
            )  # as the product of mid * mid is lesser we move the left pointer in the right half
        else:  # if the product is way too greater then we just move the right pointer in the left half
            right = mid - 1
    return ans


print(optimalsqr(28))
# time complexity : O(logN)
# space complexity : O(1)


# Find Nth root of a number
# Given two numbers N and M, find the Nth root of M. The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. If the Nth root is not an integer, return -1.
# brute approach
def nthroot(N, M):
    ans = 0
    for i in range(1, M + 1):
        if i**N <= M:
            ans = i
        else:
            break
    if isinstance(i**N, int):
        return ans
    else:
        return -1


print(nthroot(3, 27))
# time complexity :O(N)
# space complexity : O(1)


# better approach
def betternth(N, M):
    ans = -1
    left, right = 1, M
    while left <= right:
        mid = (left + right) // 2
        if (mid**N) == M:
            ans = mid
            return ans
        elif (mid**N) < M:
            left = mid + 1
        else:
            right = mid - 1
    return ans


print(betternth(4, 69))
# time complexity : O(logM)
# space complexity : O(1)


# KOKO EATING BANANAS
# A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas. An integer h represents the total time in hours to eat all the bananas.
# Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.
# Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.


# brute approach
# so the question is literally asking us to find the minimum number of bananas that a monkey must eat per hour to finish all the bananas in the given piles so that the total time taken will be exactly the given time h hrs
# and to calculate the time for each pile we devide the pile by the number of hours and the number of hours lie between 1 and the maximum number of bananas in the given array of piles
def brutekoko(array, h):
    for i in range(
        1, max(array) + 1
    ):  # as the required minimum number of bananas lie between 1 and maximum number of banana in an array, we are using this for loop here
        totaltime = 0
        for num in array:
            totaltime += math.ceil(
                num / i
            )  # here we are using math.ceil cause we are calculating the number of hours taken for koko to finish eating the bananas from the given pile ,
        if totaltime == h:
            ans = i
    return ans


print(brutekoko([25, 12, 8, 14, 19], 5))
# time complexity : O(max(array) * N)   where N is the number of piles in an array
# space complexity : 0


# better or optimal approach
# in the optimal approach what we do is , we just use the binary search method between 1 and the maximum number in an array,
# and calculate the total time taken by adding for each piles based on its number of bananas, and if the total time is equal to the given time while the number of bananas to be eaten is minimum , then we get our answer.
def betterkoko(array, h):
    left = 1
    right = max(
        array
    )  # as our answer lies between 1 and the maximum number in an array
    # and the fact that the answer lies between 1 and the maximum number in an array is,as 0 cannot be used for the number of banana to be eaten per hr, and for maximum case whichever number higher than the maximum number of array , the dividor will be the same for every left value
    while left <= right:
        mid = (left + right) // 2
        totaltime = 0
        for num in array:  # this loop runs for N times
            totaltime += math.ceil(
                num / mid
            )  # we are using the math.ceil cause we also need to find the extra hours taken for each pile
        if totaltime <= h:
            ans = mid
            right = (
                mid - 1
            )  # as our answer must be the minimum number of bananas per hours for the total time to be exactly h , we decrease our range inorder to make our mid lesser or smaller which is the divider of the number of bananas in the pile  , to increase the totaltime value
            # so that we will have a higher chance of getting the matched total time.
        elif totaltime > h:
            left = mid + 1
    return ans


print(betterkoko([25, 12, 8, 14, 19], 5))
# time complexity : O(log(max(array) * N))
# space complexity : O(1)


# Given n roses and an array nums where nums[i] denotes that the 'ith' rose will bloom on the nums[i]th day, only adjacent bloomed roses can be picked to make a bouquet. Exactly k adjacent bloomed roses are required to make a single bouquet. Find the minimum number of days required to make at least m bouquets, each containing k roses. Return -1 if it is not possible.
# what we need to do in this algorithm is that, we need to find the minimum number of days or minimum value of day when the adjacent number of roses to make one bouquet is 3 and we need to make 2 such bouquet using this minimum value of day\
# as given in question , the array is [7, 7, 7, 7, 13, 11, 12, 7]  so the range of our answer lies between 7 and 13 cause below day 7 no flowers are bloomed
def brutebloom(
    array, m, k
):  # here m is the number of bouquet and k is the number of adjacent roses
    if (
        len(array) < m * k
    ):  # if there is no enough number of roses in an array then of course we return -1
        return -1
    for i in range(min(array), max(array) + 1):
        # for each day we check the number of days in the given array
        roses = 0
        bouquets = 0
        for num in array:
            if i >= num:
                roses += 1
                if roses == k:
                    bouquets += 1
                    roses = 0  # after making one complete bouquets from 3 roses or k roses we reset the count or the number of roses to 0 again
            else:  # as soon as the  taken day is smaller than the given day in an array we reset the count or number of roses to 0 cause we need the adjacent roses
                roses = 0
        if bouquets >= m:
            return i
    return (
        -1
    )  # we return -1 when there arenot 2 '3 adjacent roses'   as  roses bloomed on 3 adjacent days are required to make the bouquet


print(brutebloom([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
# time complexity : O((max(array)-min(array) +1 )*N)  #as our outer loop is running between the range of maximum value in the given array and the minimum value so we add 1 to include the minimum value too
# space complexity : O(1)


def optimalbloom(
    array, m, k
):  # m is the number of bouquets and k is the number of adjacent roses
    left = min(array)
    right = max(array)
    ans = 0
    while left <= right:
        bouquets = 0
        roses = 0
        mid = (left + right) // 2
        for num in array:
            if mid >= num:
                roses += 1
                if (
                    roses == k
                ):  # as soon as the adjacent roses count becomes k then we can make one complete bouquet ,and after making one complete bouquet we reset the roses to 0
                    bouquets += 1
                    roses = 0
            else:  # as soon as the mid is lesser than the number in an array then we reset the count of roses to 0
                roses = 0

        if bouquets >= m:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    if ans > 0:
        return ans
    else:
        return -1


print(optimalbloom([1, 10, 3, 10, 2], 3, 2))
# time complexity : O((max(array)-min(array)+1) * log(N))
# space compplexity : O(1)



#Find the smallest divisor
#Given an array of integers nums and an integer limit as the threshold value, find the smallest positive integer divisor such that upon dividing all the elements of the array by this divisor, the sum of the division results is less than or equal to the threshold value.
#Each result of the division is rounded up to the nearest integer greater than or equal to that element.

def brutedivisor(array,l):    #here l is the limit threshold as the sum of the value obtained after dividing the numbers in an array by that specific number must be less than or equal to this
    for i in range(1,max(array)+1):
        s= 0 
        for num in array:
            s+=math.ceil(num/i)
        if s<=l:
            return i 
    return -1
print(brutedivisor( [1, 2, 3, 4, 5],8))        
#time complexity : O(N * (max(array)-min(array)+1))


#optimal approach
def optimaldivisor(array,l):
    left = 1
    right = max(array)
    ans=-1
    while left<=right:
        mid = (left + right) // 2
        s=0
        for num in array:
            s+=math.ceil(num/mid)
        if s>l:   #if the sum is greater than the threshold then we just move the left pointer towards the right half to decrease the value of s
            left = mid + 1
        elif s<=l:
            ans= mid
            right = mid - 1
    return ans        
print(optimaldivisor([1, 2, 3, 4, 5],8))
#time complexity : O(N * (max(array) - min(array)+1))
#space complexity : O(1)


#Capacity to Ship Packages Within D Days

#You are given an array weights where weights[i] represents the weight of the i-th package on a conveyor belt. All the packages must be shipped in the order given from one port to another within days days.
#Each day, the ship can carry a contiguous sequence of packages, as long as the total weight does not exceed its maximum capacity.
#Your task is to find the minimum possible capacity of the ship so that all packages can be shipped within the given number of days.

#what the question has given us 
#the question has given us the packages , each one having their own weights which can be shipped in one day
#what we need to find
# 1. the minimum weight capacity that is greater than the weight capacity of each given packages so that the shipping can be done in given number of days


#brute approach
def brutepackage(array,n):  #here n is the number of days
    summ =sum(array)  #here we are getting the total sum of an array
    #our loop ranges between the maximum number in an array and the sum of an array cause we need to find the minimum capacity which can hold all the given packages to be shipped with in given numebr of days
    #so the ranges belowe the maximum of array cannot include the packages like the max in an array and the number ranging after the summation of an array remains the same
    for i in range(max(array),summ+1): 
        days = 1
        totalweights=0
        for j in range(0,len(array)):
            if totalweights+array[j]<=i:   #we keep on shipping the packages where the total weights of those packages is lesser than or equal to the taken weight capacity to be shipped per days

                totalweights+=array[j]
            else:   #if the weights to be shipped are exceeded then we just move to next days
                days+=1
                totalweights=array[j]
        if days<=n:
            return i  
print(brutepackage( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],5))     



#optimal approach
def optimalpackage(array,n):
    left = max(array)
    right=sum(array)
    ans=0
    while left<=right:
        mid = (left + right) // 2 
        weights = 0
        days = 1
        for num in array:   
            if weights + num <=mid:
                weights+=num
            else:
                days+=1
                weights=num
        if days<=n:
            ans=mid
            right=mid - 1 #to find the required minimum capacity    
        else:   #but if the obtained days are more than the given days limit , then we just move into higher range so that the number of days will be reduced , which will probably take us within the given number of days' range
            left = mid + 1             
    return ans
print(optimalpackage( [3, 2, 2, 4, 1, 4],3))
#time complexity :O(N * log(summ(array) - max(array) + 1))
#space complexity : O(1)


