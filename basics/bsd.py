import math
import heapq


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


#Kth Missing Positive Number
#Given a sorted array of unique positive integers arr, your task is to return the kᵗʰ missing positive number that is not present in arr.
#The array is guaranteed to be strictly increasing, and the missing numbers are those positive integers that do not appear in arr but would appear in a full sequence starting from 1.


#so what we need to do is 
#first find the number missing numbers which arenot in the arrays starting from 1 to the max value of an array
#then we need to find the number of the given index k from the array consisting of missing numbers
def bruteposnum(array,k):   
    for i in range(len(array)):
        if array[i]<=k:
            k+=1
        else:
            break    
    return k
print(bruteposnum([3, 5, 7, 10],6)) 
#time complexity : O(N)
# space complexity : O(1)


#optimal approach
def optimalposnum(array,k):
    left = 0
    right = len(array)-1
    while left<=right:
        mid = (left + right) // 2
        missing=array[mid] - (mid + 1)  #here what we are calculating is the missing number of pieces at the index mid
        if missing<k:
            left = mid +1
        else:
            right = mid -1               
    return k + right + 1 
    #or we can also code return k + left     
print(optimalposnum([1, 4, 6, 8, 9],3))     
#time complexity : O(log(N))
# space complexity : O(1)       


#Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible. Find the maximum possible minimum distance.
#so what the question is asking us to put the given number of cows in such a way that the distance between two adjacent cows is minimum,but is the maximum among all the conditions of placement of cows in the stalls
def brutecows(array,k):
    array=sorted(array)  #first of all we need to sort the array
    ans = 0
    for i in range(1,max(array)):  #this outer loop is for assuming the minimum distance between two adjacent cows
        lastcowpos=array[0]
        cows = 1  #as have already placed the first cow in the first stall, we are coding the number of cows 1 here
        for j in range(1,len(array)):
            if i <=array[j] - lastcowpos:  #if the taken distance can be fit inbetween the stalls then we can place the cows
                cows+=1  #then we can increase the number of cows 
                lastcowpos=array[j]   #then we change the place of the last cow to the current i indexed stall
        if cows>=k:
            ans=max(ans,i)  #as we need to find the maximum possible minimum distance , we are using max between ans and i.
    return ans
print(brutecows([4, 2, 1, 3, 6],2))        
#time complexity : O(max(array) * O(N))
#space complexity : O(1)

#optimal approach
def optimalcows(array,k):
    array=sorted(array)
    left = 1
    right = max(array)
    ans = 0
    while left<=right:
        mid =(left + right) // 2 
        cows = 1  #here we are assuming the number of cows 1 cause we already placed it in the first stall
        last=array[0]
        for i in range(1,len(array)):
            if mid<=array[i] - last:
                cows+=1
                last=array[i]
        if cows>=k:  #if the obtained number of cows is greater than or equal to the given number of cows then we move our left pointer to right half,so that we can get the maximum possible minimum distance
            ans=max(ans,mid)
            left = mid + 1
        else:  #if the obtained number of cows is lesser then we just move our right pointer towards left half so that the mid value can be fitted majority of times so that the number of cows can be increased
            right= mid - 1 
    return ans
print(optimalcows( [0, 3, 4, 7, 10, 9],4))                   



#Book Allocation Problem
#Given an array nums of n integers, where nums[i] represents the number of pages in the i-th book, and an integer m representing the number of students, allocate all the books to the students so that each student gets at least one book, each book is allocated to only one student, and the allocation is contiguous.
#Allocate the books to m students in such a way that the maximum number of pages assigned to a student is minimized. If the allocation of books is not possible, return -1.


#what the question has asked?
#the question has asked us to give the minimum possible maximum number of pages given to each student from the given collection of books
#and if the number of books is lesser than the number of students then we just return -1
def brutebooks(array,m): #here m represents the number of students
    if len(array)<m:  #if the number of books is lesser than the number of students then we just return -1
        return -1
    for i in range(max(array),sum(array)+1):
        totalpages=0
        count= 1
        for pages in array:
            if totalpages+pages<=i:   #here we are checking if the taken maximum number of pages is greater than or equal to the sum of current value of totalpages and the current pages
                totalpages+=pages  #then we add the current pages to totalpages also which is given to the count student which is 1st student right now 
            else:
                count+=1   #if the totalsum exceeds the taken value of i then we just give the next total pages to the tha value greater than one of the count
                totalpages=pages     #and the totalpages will be the current pages 
        if count == m:  #as we need to find the most minimum possible value of maximum number of pages , we return the i as soon as the condition is matched.
            return i         
print(brutebooks( [25, 46, 28, 49, 24],4))   
#time complexity : O(sum(array)-max(array) * O(N))
# space complexity : O(1)      


#optimal approach
def optimalbooks(array,m):
    if len(array) < m:   #if the length of an array is lesser than the number of receivers then of course we cannot allocate the books to all the students.
        return -1
    ans = float('inf')  #assumed greatest positive infinity integer
    left = max(array)   #we must always begin our loop with the maximum pages in an array cause if we take the pagevalue lesser than the max page of an array then we cannot give the book to the book consisting of maximum pages to the student
    right=sum(array)
    while left<=right:
        mid = (left + right) // 2
        count = 1  #here count denotes the number of student who received the books
        currentpages=0     #countpages denotes the totalnumber of pages at the current time
        for pages in array:
         if mid>=currentpages+pages:   #if the taken or assumed maximum number of pages is greater than or equal to the sum of current pages then we just keep on adding those pages
             currentpages+=pages
         else:   #otherwise we just give the current book to another student and assume the currentpages to the current pages in an array
             count+=1
             currentpages = pages
        if count <= m:   #if the number of students who received the books lie within the range of m, then it means we can move the right pointer towards left half
            #as to find the minimum maximum pages possible
            ans=min(ans,mid)    
            right = mid - 1  
        else:   #if the obtained count is greater than the given number of students then we must increase the mid value so that the count value can be decreased
            left = mid + 1
    return ans
print(optimalbooks([12, 34, 67, 90],2))  
#time complexity : O(log(sum(array)-max(array)) * O(N))
#space complexity : O(1) 




#Split array - largest sum
#Given an integer array a of size n and an integer k. Split the array a into k non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.
#so what the question is asking us is to return the minimum possible of the largest sum among the consecutive subarrays splitted into given number of times

#brute approach
def splitarray(array,k):
    for i in range(max(array),sum(array)+1):
        count =1 #count denotes the nnumber of subarray then we start with the making the first subarray
        s = 0   #sum denotes the sum of the subarray
        for num in array:    #then we go through each numbers in an array , whether the taken i or taken sum matches the condition or not
            if i>=s+num:
                s+=num
            else:
                count+=1
                s= num
        if count<=k:
            return i
        else:
            continue     #if the count or obtained number of subarrays exceed the given number limit then we just break out of the loop.
print(splitarray([3,5,1],3))        
#time complexity : O(sum(array)-max(array)) * O(N)
#space complexity : O(1)


#optimal approach
def optimalarray(array,k):
    ans=float('inf')
    left = max(array)
    right = sum(array)
    while left<=right:
        count = 1  #count denotes the number of splitted subarray
        s = 0
        mid = (left + right) // 2
        for num in array:
         if mid>=s+num:
             s+=num
         else:
             count+=1   #if the current sum exceeds our mid value then we start a new subarray and the sum becomes the current num
             s = num
        if count<=k:  #if the obtained count is lesser than or equal to k then the mid might be an answer 
            ans=min(ans,mid) #but as the question is asking us for the most minimum value of largest sum , we are using minimum here.
            right = mid-1
        else:
            left = mid + 1    #here we are moving the left pointer towards the right half cause if the count is way too greater than k then we need to increase the taken sum which is makes the count or the number of splitted subarrays lesser              
    return ans
print(optimalarray( [1, 2, 3, 4, 5],3))
#time complexity : O(log(sum(array)-max(array))*O(N))
#space complexity : O(1)

                 
#Painter's Partition
#You are given A painters and an array C of N integers where C[i] denotes the length of the ith board. Each painter takes B units of time to paint 1 unit of board. You must assign boards to painters such that:
#Each painter paints only contiguous segments of boards.
#No board can be split between painters.
#The goal is to minimize the time to paint all boards.Return the minimum time required to paint all boards modulo 10000003.

#so what the question has given us is 
#the number of painters A
#C is the collection of boards showing their length
#B denotes the time taken to print 1 unit of board

#what the question is asking us :
#is to return the minimum time required to paint all boards

def brutepainter(c,a,b):  #here c is the collection of boards reprenting the length of boards , a is the number of painters and b is the unit of time
    for i in range(max(c),sum(c)+1):
        s = 0
        count = 1   #count denotes the number of painters
        for num in c:
            if i >=num:
                s+=num
            else:
                count+=1
        if count<=a:  #if the obtained number of painters is lesser than or equal to a then we return i
            return i * b   #b is the unit of time to paint 1 unit of board
        #as we need to return the minimum time required to print all the boards we return i as soon as the condition is met which is count<=a, which is the number of painters
print(brutepainter( [1, 10],2,5)) 
#time complexity : O(sum(c)-max(C) * O(N))
# space complexity : O(1)           



#optimal solution
def optimalpainter(c,a,b)  :#here c is the collection of painting boards denoting the length of boards , a is the number of painters and b is the unit of time 
    ans = float('inf')
    left = max(c)
    right = sum(c)
    while left<=right:
        mid = (left + right) // 2  
        count = 1
        s = 0
        for num in c:
            if mid>=s+num:
                s+=num
            else:
                count+=1
        if count<=a:
            ans = min(mid,ans)
            left = mid + 1
        else:
            right = mid -1     
    return ans * b
print(optimalpainter( [1, 10],2,5))                   
                


#Minimize Max Distance to Gas Station
#Given a sorted array arr of size n, containing integer positions of n gas stations on the X-axis, and an integer k, place k new gas stations on the X-axis.
#The new gas stations can be placed anywhere on the non-negative side of the X-axis, including non-integer positions.
#Let dist be the maximum distance between adjacent gas stations after adding the k new gas stations.
#Find the minimum value of dist.

def brutegas(array,k):   #here array is the given number of gas stations and k is the number of new gas stations that we must place them in betweeen the gasstations of the given array
    howmany=[0] * (len(array)-1)   #here howmany represents the number of gas stations that we have placed inbetween the gasstations from the given array
    for i in range(1,k+1):  #this outer loop represents the loop of placing the new gas station inbetween the gasstations from the given array
        maxsection = -1
        maxindex = -1
        for j in range(len(array)-1):  #here we are only running the loop until len(array) - 1 cause we need to find the difference between the two consecutive gas station so if we take the last gasstation then we cannot calculate the differenc of it with its next gasststion cause we go out of the loop
         diff = array[j+1] - array[j]
         distance = diff / (howmany[j] + 1)   #here the distance means the length or distance between the two consecutive gasstation at j index
         if distance > maxsection:       #if the current obtained distance is the maximum then the last maxsection then we change our maxsection to current distance and the maxindex to the current i index
             maxsection=distance
             maxindex=j 
        #so from this loop we get the maximum distance between the two consecutive gas stations at the specific index which is a gap at which we place the new gas station to reduce the distance
        howmany[maxindex]+=1     #then we start placing the new gas station at the index or the gap where the maximum distance between the consecutive gasstation has been found.
    maxans = -1
    #this loop is for finding the maximum distance between two consecitive gas station after reducing the distance between the gasstations in every gap by placing all the new gas station
    for i in range(len(array)-1):
        diff = array[i+1] - array[i]
        distance = diff / (howmany[i] + 1)
        maxans=max(maxans,distance)
    return maxans   
print(brutegas( [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10],9)) 
#time complexity : O(K * O(N))  #here K is the number of new gas stations to be placed and N is the number of gasstations in the given array
#space compelxity : O(1)


#better solution 
def bettergas(array,k):
    howmany=[0]*(len(array)-1)  #this howmany represents the number of gaps index in the original gasstation
    pq = []
    for i in range(len(array)-1):   #this loop is used for storing the sectionlength or distance and their respective indices in the pq using heap loop
        heapq.heappush(pq,(-1*array[i+1]-array[i],i))  #here we are storing the distance between the adjacent gasstations with their corresponding indices using heapq.heappush in pq
    for i in range(1,k+1):
        removed = heapq.heappop(pq)  #this removes the most smallest value from pq , which is the most largest distance between the adjacent gas stations
        placedindex=removed[1]   #as we got the index at which the  most maximum distance is , then we can add the new gasstation at this index
        howmany[placedindex]+=1    #here what we are doing is that we just found out about the gap which is the maximum then we just remove it from heap collection and we place the new gasstation at its respective index.
        diff = array[placedindex+1]-array[placedindex]
        #then we put the new obtained spacelength at that index after placing the new gasstation
        heapq.heappush(pq,(-1 * diff//(howmany[placedindex]+1),placedindex))  #then we add the obtained distance after placing the new gas station 
    #then the space lenghth remaining at the top of the heap will be our most minimum maximum distance between the adjacent gas stations
    return pq[0][0] * -1  #then we return the first tuple's first value which is the distance and multiply it by -1 as we placed the distances as the negative value
print(bettergas([1,13,17,23],5))

#optimal solution
#in this optimal approach what we are doing is first we are getting the value of mid which will act as our answer or the required most minimum maximum distacnce ,
#by taking this distance or value , we check how many new gasstations are required, if the number of required new gasstations exceeds the given number k then we just move the left to mid to increase the value of gap ,
# otherwise we move the right to mid to decrease the gap distance, as the question is asking us to get the minimum maximum distance

def countgasstations(distance,array):
    count = 0
    for i in range(len(array)-1):
        requirednumber=(array[i+1]-array[i]) / distance  #here we are calculating the number of required gas stations at the current gap
        if (array[i+1] - array[i]) == (distance * requirednumber):
            requirednumber -= 1
               #if the gap is exactly divisible by the taken distance then we only need gasstations just one value lesser than the requirednumber
        count+=requirednumber  #then in each gaps we calculate the number of gas stations required. 
    return count


def optimalgas(array,k):
    low=0
    high = 0
    for i in range(len(array)-1):
        high=max(high,array[i+1]-array[i])   #here we are calculating the maximum gap which is present in the original gas station
    while high - low > 1e-6:      #here we are running the loop as long as the most maximum distance is greater than the value of 1e-6 or 0.000001
        mid = (low + high) / 2.0     #this is our assumed maximum distance right now
        count = countgasstations(mid,array)
        if count>k:  #if the number of gas staions required for the current max distance is way greater than the given k value , then we just increase the value of low , to make the gap much bigger so that the number of gas stations required will be within the k range
            low = mid   
        else:  #if the number of required gas stations lie with in the k range then we try to decrease the gap or distance by moving the high to mid
            high =mid    
    return high
print(optimalgas([1, 2, 3, 4, 5, 6 ,7, 8, 9, 10],9))
#time complexity : O(N * log(len))   #len is the length of the answer and N is the length of an array
#space complexity : O(1)

#Median of 2 sorted arrays
#Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.
#The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.


#brute approach
def brutemedian(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    total=sorted(arr1+arr2)  #here we are first summing the array1 and array2 then we are summing up the array
    if len(total) % 2 !=0:
        index = len(total) // 2 
        ans=total[index] #this gives us the median element of the odd length array
    else:
        second = (len(total)) // 2 
        ans = (total[second] + total[second-1]) / 2
    return ans
print(brutemedian( [2, 4, 6], [1, 3,5]))
#time complexity : O(M+Nlog(M+N))
#space complexity : O(M+N)


#better approach
#in the better approach what we do is we dont use the third array for storing the numbers or for displaying the numbers what we do is we just catch the index
def bettermedian(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    n=n1 + n2   #this is our total length
    mainindex = (n1 + n2) // 2   #this is the main index which gives us the median if the length of the total array is odd but
    #if the length of the total arrays is even then we need to find the average between the numbers at the main index and mainindex-1
    secondaryindex = mainindex - 1  #this is required only when the total length is even cause we need to calculate the average
    i = 0 
    j = 0
    count = 0
    mainelem=0
    secelem=0
    while i<n1 and j<n2:   #here we are running the loop from i to length of arr1 and j to length of arr2
        if arr1[i]<arr2[j]:   #then we check if the i indexed array element is lesser than the j indexed array element ,
            #if yes then we check the index count with the required count 
            if count == mainindex:
                mainelem=arr1[i]
            if count == secondaryindex:
                secelem=arr1[i]    

            count+=1
            i+=1
        else:
            if count == mainindex:
                mainelem=arr2[j]
            if count == secondaryindex:
                secelem=arr2[j]
            count+=1
            j+=1     
    while i<n1:
        if count == mainindex:
            mainelem=arr1[i]
        if count == secondaryindex:
            secelem=arr1[i]
        count+=1
        i+=1
    while j<n2:
        if count == mainindex:
            mainelem=arr2[j]
        if count == secondaryindex:
            secelem=arr2[j]
        count+=1
        j+=1    
    if n % 2 != 0:
        return mainelem
    else:
        return (mainelem + secelem) / 2    
bettermedian([2, 4, 6],[1,3]) 
#time complexity : O(N + M)
#space complexity : O(1)   
                           













