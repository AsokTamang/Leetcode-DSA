# Assign Cookies
def assigncookes(student, cookie):
    n = len(student)
    m = len(cookie)

    def helperfunction(studentindex, cookieindex):
        if (
            studentindex >= n or cookieindex >= m
        ):  # this is the base case where all the students or the cookies are passed
            return 0
        if cookie[cookieindex] >= student[studentindex]:
            return 1 + helperfunction(
                studentindex + 1, cookieindex + 1
            )  # here if the current indexed cookie satisfies the student then we add one to the satisfied number of student and recursivley move to next index of studnet as well as cookie
        else:
            return helperfunction(
                studentindex, cookieindex + 1
            )  # if the current cookie cannot satisfy this current student then we move to the next cookie for the same student

    return helperfunction(0, 0)


print(assigncookes([1, 2, 3], [1, 1]))
# time complexity : O(max(n,m))  due to recursion as we are going into only one way of recursion depth,either through cookies or through both students and cookies
# space complexity : O(max(n,m))  due to the recursion


# optimal approach
def optimalassigncookies(student, cookie):
    student.sort()
    cookie.sort()
    n = len(student)
    m = len(cookie)
    i = 0
    j = 0
    while i < n and j < m:
        if cookie[j] >= student[i]:
            i += 1  # we only move to the next index of student when the current student is satisfied
        j += 1  # here we move to the next index of cookie whether the current cookie satisfies the current student or not
    return i


print(optimalassigncookies([1, 2], [1, 2, 3]))
# time complexity : O(logN+logM+max(N,M)) here we are writing max(N,M) at last cause we are using the while loop until the max value between N and M
# space complexity : O(1)


# fractional Knapsack
# as the question is asking us to return the maximum value possible that can be places in a knackpack
# so we gonna reverse the value per unit for each weight from given arrays of value and weight
def fracknapsack(val, wt, k):  # k is the capacity
    array = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)
    totalvalue = 0
    totalwt = 0
    for val, wt in array:
        if (
            totalwt + wt <= k
        ):  # if the total weight after including the current weight is within the weight range then
            # we add this weigth and its value to
            totalwt += wt
            totalvalue += val
        else:
            remainingwt = k - totalwt
            totalvalue += remainingwt * (
                val / wt
            )  # here we are multipolying the value of one unit of current wt with the remaining wt inorder to add the remianing value
    return f"{totalvalue:.6f}"


print(fracknapsack([60, 100, 120], [10, 20, 30], 50))
# time complexity : O(NlogN)
# space complexity : O(N)


# minimum coins
# so the logic behind this solution is that as we are finding the most minimum possible number of coins, we must iterate from the last index of coins and as long as the current index satisfies to make the amount  ,we use this current indexed coin
# only if the current indexed coin fails to satisfy we move to the next coin
def minimumcoins(coins, amount):
    n = len(coins)
    count = 0
    for i in range(n - 1, -1, -1):
        while amount >= coins[i]:
            count += 1
            amount -= coins[i]
    return count


print(minimumcoins([1, 2, 5], 11))
# time complexity : O(amount)
# space complexity : O(1) M is the number of coins that are used to make the total amount given


# lemonade change
# brute approach
def lemonadechange(bills):
    n = len(bills)
    m = {}
    for i in range(n):
        m[bills[i]] = (
            m.get(bills[i], 0) + 1
        )  # here we are storing the freq of money that we are getting from a customer
        if (
            bills[i] > 5
        ):  # if the customer gave us more than 5 dollar then we must given them change
            changereq = bills[i] - 5  # this is the change we must give to the customers
            for num in sorted(
                m.keys(), reverse=True
            ):  # here we are sorting in ascending order so that the change can be found soon
                while changereq >= num and m[num] > 0:
                    changereq -= (
                        num  # reducing the change by the money we have in our store m
                    )
                    m[
                        num
                    ] -= 1  # also we must reduce the freq of cash that we used from our store
            if changereq > 0:
                # even after this while loop , if we still have change to give then it means we dont have enough money or req exact money for the change so we return false
                return False
    return True


print(lemonadechange([5, 5, 10, 10, 20]))
# time complexity : O(N**2+logN)
# space complexity : O(N)  number of cash we have in store approx N


# optimal  approach or lets say for the problem where the customers only pay in maximum 20 dollar cash
def optimallemonadechange(bills):
    five = ten = 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            ten += 1
            if not five:
                return False
            five -= 1
        else:  # if the customer gave us 20 bucks cash then
            if not ten or not five:
                return False
            elif ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True


print(optimallemonadechange([5, 5, 10, 5, 20]))
# time complexity : O(N)
# space complexity : O(1)


# Valid Paranthesis Checker
# brute approach
def validparenthesischecker(s):
    n = len(s)

    def recursiveparenthesischecker(index, count, s):
        if count < 0:
            return False
        if (
            index == n
        ):  # when our index reaches the limit then we check whether the string is valid or not by checking if count ==0
            return count == 0
        char = s[index]
        if char == "(":
            return recursiveparenthesischecker(index + 1, count + 1, s)
        elif char == ")":
            return recursiveparenthesischecker(index + 1, count - 1, s)
        else:
            return (
                recursiveparenthesischecker(index + 1, count, s)
                or recursiveparenthesischecker(index + 1, count + 1, s)
                or recursiveparenthesischecker(index + 1, count - 1, s)
            )

    return recursiveparenthesischecker(0, 0, s)
print(validparenthesischecker("(*))"))
# time complexity: O(3**N)
# space complexity : O(N)


#optimal approach
def optimalparenthesischecker(s):
    minopen=0  
    maxopen=0
    for char in s:
        if char =='(':
            minopen+=1
            maxopen+=1
        elif char ==')':
            minopen=max(minopen-1,0)
            maxopen-=1
        else:
            minopen=max(minopen-1,0)  #assuming * as )
            maxopen+=1  #assuming * as (
        if maxopen<0:  #here if the maxopen becomes negative then it means there is more closing brackets than the opening brackets
            return False    
    return minopen==0  
print(optimalparenthesischecker('*(()'))   
#time complexity : O(N)
#space complexity : O(1)  
         

#N meetings in one room
#so the logic behind the solution of this problem is that , inorder for the meeting to be included in a room,its starting time must be after the ending time of last meeting,
#and the question is asking us to return the maximum number of meetings that can be held , so for this we must sort the meetings based on their end time, 
#so that we can include the meetings with less ending time or quick ending time as soon as possible
#which results in the increase number of meetings
def Nmeetings(start,end):
    meetings = list(zip(start,end))
    meetings=sorted(meetings,key=lambda x:x[1])  #based on the meeting time
    lastendtime = meetings[0][1]  #here the first ending time of last meeting will be the ending time of first meeting
    n=len(start)
    count = 1  #as we can always include the first count
    for i in range(1,n):
        if meetings[i][0]>lastendtime:  #if the start time comes after the ending time of last meeting,then this current meeting can be held so we increase the count as well as change the ending time of last meeting
            count+=1
            lastendtime=meetings[i][1]

    return count
print(Nmeetings( [10, 12, 20] ,  [20, 25, 30]))
#time complexity : O(NlogN)
#space complexity : O(N)
      





#jump game -I
def jumpgame(input):
    n=len(input)
    maxindex = 0  #here maxindex stores the index or a position in a given array which can be reached by the maximum jump
    for i in range(n):
        if i > maxindex:   #if the current index is greater than the maxindex then it means this current index cannot be reached so we return false
            return False
        maxindex = max(maxindex,i+input[i])  
    return True   
print(jumpgame( [3, 2, 1, 0, 4]))
#time complexity : O(N)
#space complexity : O(1)


#jump game -II
#for the minimum number of jumps,we must use the maximum number of steps from each index
def jumpgameii(nums):
    maxindex = 0
    n=len(nums)
    currentend = 0  #this current end means the position which can be reached from the given indices using the farthest distance 
    count = 0
    for i in range(n):
        maxindex=max(maxindex,i+nums[i])
        if i == currentend:  #if we reach the current end position , which is found after jumping to the farthest position  then it means we must make jump to this current index
         count+=1
         currentend=maxindex   #then we also update the currentend position
    return count
print(jumpgameii( [5,9,3,2,1,0,2,3,3,1,0,0]))    


#minimum number of platforms
#brute approach
def bruteminplaotform(arr,dep): #here arr represents array and dep represents departure
    n=len(arr)
    ans =1  #the initial number of platform required is ofcourse 1
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if arr[i]>=arr[j] and arr[i]<=dep[j] or arr[j]>=arr[i] and arr[j]<=dep[i]:  #if the arrival and departure of the aeroplanes mismatch then we increase the number of platform
                count+=1
        ans=max(ans,count)
    return ans
print(bruteminplaotform( [900, 940, 950, 1100, 1500, 1800] , [910, 1200, 1120, 1130, 1900, 2000]))   
#time complexity : O(N**2)
#space complexity : O(1) 

#optimal approach
def optimalminplatform(arr,dep):
    arr.sort()
    dep.sort()
    i,j=0,0
    n=len(arr)
    count=0  #initially the number of platform required is ofcourse one as for the first plane to land and depart
    maxcount = 0
    while i<n and j<n:
        if arr[i]<=dep[j]:  #if the arrival of the next plane is within the departure of the previously arrived plane then we increase the count of platforms and also the index of arrival for comparison
            i+=1
            count+=1
        else:  #if the arrival of next plane is outside the departure of the previously arrived plane then we dont need another platform and we increase the index of departure
            j+=1
            count-=1   
        maxcount=max(maxcount,count)    
    return maxcount
print(optimalminplatform( [900, 1100, 1235] , [1000, 1200, 1240]))    
#time complexity : O(NlogN)
#space complexity : O(1)     


#Job sequencing Problem
#so the question is asking us to return the maximum profit which can be obtained by scheduling the jobs in the right way
def jobsequence(jobs):
    jobs=sorted(jobs,key=lambda x:x[2],reverse=True)  #here we are sorting the jobs based on the profits in the descending order, so that the job with high profit will be scheduled as soon as possible
    maxday=1
    n=len(jobs)
    for i in range(n):
        maxday=max(maxday,jobs[i][1])  #as the second index or index 1 in the jobs represent the days when this current job can be scheduled
    scheduled = [0] * maxday  #here we are maintaining the days upto the highest maxday or slot available in the jobs list
    totalprofit=0
    for job in jobs:
        id,deadline,profit=job
        #only if the slot is available , we are adding the profit of the current job
        for d in range(deadline,0,-1):  #as the earlier days from the current slot are also available so we run this loop
            if scheduled[d-1]==0:  #as the index of the list is 0-based we are subtracting 1 from job[1]
                #checking if the slot or the particular day is available or not,if its -1 then it means this particular slot or day is available
                scheduled[d-1]=deadline  #and inserting the slot of the current job as scheduled
                totalprofit+=profit  #adding the profit
                break  #after inserting this job , we break out of the loop
    return totalprofit        

    
print(jobsequence( [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]))
#time complexity: O(N+logN)
#space complexity : O(M)  max slot available in the job lists


#candy
def brutecandy(ratings):
    n=len(ratings)
    total = [1] * n #as atleast one candy must be assinged to each and every children
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            total[i]=total[i-1]+1
    for i in range(n-2,-1,-1):  #traversing from right to left
        if ratings[i]>ratings[i+1]:
            total[i] = max(total[i],total[i+1]+1)          #this addition of 1 to total[i+1] is cause we have already assigned the appropriate candies to the students having higher ranks compared to the preceding one
    return sum(total)        
print(brutecandy([1, 2, 2]))  
#time complexity : O(N)
#space complexity : O(N)

#shortest job first
import math
def shortestjob(bt):
    bt=sorted(bt)   #inorder to complete the shortest bursting job first
    n=len(bt)
    total = 0
    for i in range(1,n):
        total+=sum(bt[0:i])   #inorder for the current job to be started, all of the preceding jobs must be executed at first which has their own waiting time.
    return math.floor(total / n) 
print(shortestjob([9, 3, 1, 8, 2]))  
#time complexity : O(NlogN)
#space complexity : O(1)







     


