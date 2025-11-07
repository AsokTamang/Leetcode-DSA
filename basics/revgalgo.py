#assign cookies
def assigncookies(student,cookie):
    student.sort()  #here we are sorting both student and cookie so that the least greedy stident can be satisfied easily by the smallest amount of cookie
    cookie.sort()
    i=0  #for student
    j=0  #for cookie
    n=len(student)
    number = 0
    while i<n:
        if cookie[j]>=student[i]:
            number+=1  
            i+=1          
        j+=1  
        
    return number          
print(assigncookies([4, 5, 1] , [6, 4, 2]))
#time complexity : O(NlogN+MlogM)
#space complexity : O(1)


#Fractional Knapsack
def fractionalknapsack(val,wt,k):
    totalwt =0 
    array = sorted(zip(val,wt),key=lambda x:x[0]/x[1],reverse=True )  #here we are sorting reversely based on the fraction of value and weight
    maxvalue =0
    for val,wt in array:
        if totalwt+wt<=k:
            totalwt+=wt
            maxvalue+=val
        else:
            remainingwt = k-totalwt
            additionalval = (val/wt) * remainingwt
            maxvalue+=additionalval
    return f'{maxvalue:.6f}'
print(fractionalknapsack([60,100,120],  [10,20,30],  50)) 
#time complexity : O(NlogN)
#space complexity : O(N)  


#minimum coins
def minimumcoins(coins,amount):
    n=len(coins)
    coins.sort()
    count = 0
    s=0
    for i in range(n-1,-1,-1):
        while coins[i]<=amount:
            s+=coins[i]  #10
            amount-=coins[i] #1
            count+=1
       
    if amount==0:  #here amount = 0 means we have the required quantity of coins in a given list of coins inorder to make the given quantity of amount
     return count
    return -1
print(minimumcoins( [2, 5],  3))    
#time complexity : O(NlogN)
#space complexity : O(1)    

#lemonade change
#brute approach which means the bills consists of only 5,10, and 20
def lemonadechange(bills):
    n=len(bills)
    fives,tens = 0,0
    for num in bills:
        if num == 5:
            fives+=1
        elif num == 10:
            tens+=1
            if fives:
                fives-=1
            else:
                return False        
        else:  #if the number is 20
            if tens and fives:
                tens-=1
                fives-=1
            elif fives>=3:
                fives-=3
            else: #which means we have no change
                return False
    return True
print(lemonadechange([5, 5, 10, 20]))      
#time complexity : O(N)
#space complexity : O(1)       
                

#for the bills containing more than 20 
def optimallemonadechange(bills):
    m={}
    for num in bills:
        m[num]=m.get(num,0) + 1  
        if num > 5:
            changerequired = num - 5
            for bill in sorted(m.keys(),reverse=True):  #this loop is for checking the cash we have in our box, and here we are reversing the keys so that we can find the cash for change as soon as possible
                if  bill<=changerequired and m[bill]>0:
                    changerequired=changerequired-bill
                    m[bill]-=1
            if changerequired>0:  #if we still have change to given even after that for bill loop, then it means we dont have the required cash to give as a change for a customer
                return False      
    return True
print(optimallemonadechange([5, 5, 10, 5, 20]))          
#time complexity : O(N**2+logN)
#space complexity : O(N)


#valid parenthesis
def brutevalidparenthesis(s):
    n=len(s)
    def recursivevalidparenthesis(index,count):  #index indicates the index of a given string s and count indicates the measure based on which we determine whether the given string is valid or not
     if count<0:
         return False
     if index==n:   #if we already went through all the characters from a given string, we check the value of count
         return count==0
     char = s[index]
     if char=='(':
        return recursivevalidparenthesis(index+1,count+1)
     elif char == ')':
        return recursivevalidparenthesis(index+1,count-1)
     else:  #if the char is * then we can assume this * as ( or ) or empty character
         return recursivevalidparenthesis(index+1,count) or recursivevalidparenthesis(index+1,count+1) or recursivevalidparenthesis(index+1,count-1)         
        
    return recursivevalidparenthesis(0,0)
print(brutevalidparenthesis('*(()'))
#time complexity : O(3**N)
#space complexity : O(N)
 

#optimal approach
def optimalvalidparenthesis(s):
    minopen=0   #here minopen means we are assuming * as ) so the number of openings will be minimum
    maxopen=0   #here maxopen means we are assuming * as ( so the number of openings will be maximum
    for char in s:
        if char == '(':
            minopen+=1
            maxopen+=1
        elif char ==')':
            minopen=max(minopen-1,0) 
            maxopen-=1
        else:
            minopen=max(minopen-1,0)  #here we are using max between 0 and minopen-1 cause the minopen mustnot be 0 , as we use this value to return the answer and minopen-1 reduces the count as we are assuming * as )
            maxopen+=1  #here we are assuming * as (
        if maxopen<0:
            return False
    return minopen==0
print(optimalvalidparenthesis('(*))'))
#time complexity : O(N)
#space complexity : O(1)

        

#jump game - I
def jumpgamei(input):
    n=len(input)
    maxindex = 0  #this maxindex stores the position or the index which can be reached by the maximum jump that is available in the index
    for i in range(n):
        if i > maxindex:  #here i > maxindex means this i cannot be reached even with the maxindex until this index , which means we are unable to reach this index which proves that we can never reach the last index or final end
            return False  
        maxindex=max(maxindex,input[i]+i)
    return True
print(jumpgamei( [3, 2, 1, 0, 4]))    
#time complexity : O(N)
#space complexity : O(1)


#jump game II
#brute approach using recursion
def brutejumpgameii(nums):
    n=len(nums)
    def recurjump(index, jump):
        if index>=n:
            return jump
        minjump=float('inf')
        for i in range(1,nums[index]+1):   #we are exeperimenting every possible jumps that can be done from the current index 
            minjump=min(minjump,recurjump(index+i,jump+1))  #with this loop , we go through every possible indices that can reached by jumping from the current passed 'index'
        return minjump     
    return recurjump(0,0)  #initially we start from the root index and ofcourse 0 jump
print(brutejumpgameii([2,3,1,1,4]))
#time complexity : O(N**N)
#space complexity : O(N)


#optimal approach
#as the question is asking us to return the minimum number of jumps to reach the last index , what we do is take a currentend ,which is the end that can be reached by obtaining the maximum reach found till the current index
def optjumpgameii(nums):
    maxreach = 0
    n=len(nums)
    currentend = 0
    jumps=0 
    for i in range(n):
        maxreach=max(maxreach,nums[i]+i)
        if i == currentend:  #if the current index is the last currentend which was obtained with the help of maxreach then to move to the next we index , we must jump ,
            jumps+=1
            currentend=maxreach
    return jumps  
print(optjumpgameii([2,3,1,1,4]))      
#time complexity : O(n)
#space complexity : O(1)


#minimum number of  platforms required for a railway
#brute approach
def bruteminimumplatform(arr,dep):  #here arr represents the arrival of the aeroplane and dep represents the departure of the plane
    n=len(arr)
    minim = 0
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if arr[i]<=dep[j] and dep[i]>=arr[j]:  #if the arrival of one plane is smaller than the  departure of another plane and the departure of that plane also must be smaller than the arrival of that second plane , for these two planes to be overlapped
                 count+=1
        minim=max(minim,count)
    return minim
print(bruteminimumplatform( [900, 940, 950, 1100, 1500, 1800] ,  [910, 1200, 1120, 1130, 1900, 2000]))            
#time complexity : O(N**2)
#space complexity : O(1)


#optimal approach
def optminiplatoform(arr,dep):
    n=len(arr)
    i=j=0
    minim = 0
    count = 0
    while i<n and j<n:
        if arr[i]<=dep[j]:  #only if the arrival of the plane is smaller than the departure of the another plane , we inrease the count of trainstation
            i+=1
            count+=1
        else:
            j+=1
            count-=1
        minim=max(minim,count)
    return minim     
print(optminiplatoform( [900, 1100, 1235] , [1000, 1200, 1240]))   
#time complexity : O(N)
#space complexity : O(1)


#job sequencing problem
def jobsequence(jobs):
    jobs=sorted(jobs,key=lambda x:x[2],reverse=True)
    maxim = 0
    for job in jobs:
        maxim=max(maxim,job[1])
    availabledeadline=[0] * maxim
    totalprofit = 0
    for job in jobs:
        id,deadlinelimit,profit = job
        for i in range(deadlinelimit,0,-1):  #we must check the whole preceding days from the given deadline day of the current job
            if availabledeadline[i-1]==0:  #only if the day is available or anyother job is not used in this current day , we place this job in this day
                availabledeadline[i-1]=i
                totalprofit+=profit
                break  #and we must break after inserting this job as we can only take this job only one time per day
    return totalprofit
print(jobsequence( [ [1, 4, 20] , [2, 1, 10] , [3, 1, 40] , [4, 1, 30] ]))
#time complexity : O(NlogN)
#space complexity : O(M) max available deadline 

#candy
def candychild(ratings):
    n=len(ratings)
    total = [1] * n  #atleast one candy must be served to every children
    for i in range(1,n):
        if ratings[i]>ratings[i-1]:
            total[i]=total[i-1] + 1  #as the higher rated child must have greater number of candy than the one with the lower candy
    for i in range(n-2,-1,-1):
        if ratings[i]>ratings[i+1]:
            total[i] = max(total[i+1]+1,total[i])  #here we are using max cause we have already assigned the required number of candies to students by comparing with the ranking of previous students,
            #so for the comparison of next students, we must use the max
    return sum(total)                 
print(candychild([1, 2, 2]))
#time complexity : O(N)
#space complexity : O(N)


#merge intervals
def mergeintervals(intervals):
    ans = [intervals[0]]  #storing the first array of the intervals initially
    for array in intervals[1:]:
        last = ans[-1]
        if last[1]>=array[0]:  #if the ending of the last array in our ans is greater than or equal to the starting of current array then
         last[1] = max(last[1],array[1])
        else:
            ans.append(array)
    return ans
print(mergeintervals( [[1,4],[4,5]]))    
#time complexity : O(N)
#space complexity : O(N) in the worst case        


