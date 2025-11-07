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


#N meetings in one room
def nmeetings(start,end):
    array=sorted(zip(start,end),key=lambda x:x[1])  #here we are sorting the pair of starting and ending of a room based on their ending time , so that as long as the meetings are finished earlier we can increase the number of meetings that can be held in a room
    lastmeeting = array[0]  #here it the last meeting which was held in a room
    count=1  #as the very first meeting is already held
    for meeting in array[1:]:
        if meeting[0]>lastmeeting[1]:  #if the starting of the current meeting is greater than the ending of last meeting then this meeting can be held
         count+=1
         lastmeeting=meeting  #then as this current meeting is held , we change the lastmeeting to current meeting
    return count     
print(nmeetings( [1, 3, 0, 5, 8, 5] ,  [2, 4, 6, 7, 9, 9]))      
#time complexity : O(NlogN)
#space complexity : O(N)       

#jump game I
#the given array represents the maximum jump of positions that can be done from given number of indices
def jumpgamei(array):
    n=len(array)
    maxjumptill=0
    for i in range(n):
        if i > maxjumptill:  #if the index or the current position i is greater than the maxjump till then it means we cannot reach this current position i anyhow, so ofcourse we cannot reach the last index without the maxjumptill 
            return False
        maxjumptill=max(maxjumptill,i+array[i])
    return True
print(jumpgamei(  [5, 3, 2, 1, 0]))    
#time complexity : O(N)
#space complexity : O(1)

#jump game II
def jumpgameii(nums):
    maxjummpindex = 0 #this represents the position that can be reached by using the maximum jump capacity found till the current loop
    n=len(nums)
    number=0
    endofrange=0
    for i in range(n-1): 
        maxjummpindex=max(maxjummpindex,i+nums[i])
        if i == endofrange:  #if the current position is the end of the range produced from the maxjumpindex till now then it means we need one more jump to go beyound this position and we also change the endofrange with the new or current maxjumpindex depending upon the current indexed value
            number+=1
            endofrange=maxjummpindex
        
    return number
print(jumpgameii( [2,3,0,1,4]))    
#time complexity : O(N)
#space complexity : O(1)

#minimum number of platforms
#brute approach
def minimumplatform(arrival,dep):
    n=len(arrival)
    ans = 0
    for i in range(n):
        count =1  #we need one platfrom initially
        for j in range(i+1,n):  
            if arrival[j]<=dep[i]:  #if the arrival of the next plane is withint the departure of the last plane , then ofcourse we need extra railway platform
                count+=1
        ans=max(ans,count)
    return ans
print(minimumplatform( [900, 1100, 1235] ,  [1000, 1200, 1240]))            
#time complexity : O(N**2)
#space complexity : O(1)


#optimal approach
def optminimumplatform(arrival,dep):
    n=len(arrival)
    i=j=0
    count = 0
    ans = 0
    while i<n and j<n:
        if arrival[i]<dep[j]:
            count+=1
            i+=1
        else:
            j+=1
            count-=1
        ans=max(ans,count)
    return ans        
print(optminiplatoform([900, 1100, 1235] ,  [1000, 1200, 1240]))
#time complexity : O(N)
#space complexity : O(1)

#job sequencing problem
def jobsequence(jobs):
    jobs=sorted(jobs , key=lambda x:x[2],reverse=True)  #here are sorting the jobs based on the profit but in descending order
    maxdeadlinelimit = 0
    for job in jobs:
        maxdeadlinelimit=max(maxdeadlinelimit,job[1])  #using the max function we are calculating the maximum deadline limit given in a jobs array
    availabledays = [0] * maxdeadlinelimit   #this stores the days available for the particular jobs to be scheduled
    totalprofit = 0  
    count =0  #number of scheduled jobs 
    for job in jobs:
        id,d,profit = job  #d represents the deadline of this particular job
        for i in range(d,0,-1):  
            if availabledays[i-1] == 0:  #here we are checking if the days from this deadline are available or not for this job to be scheduled
                count +=1 
                availabledays[i-1] = id  #if yes then we schedule this job in this particular day
                totalprofit+=profit      #and we also add the profit of this job to the total
                break 
    return count,totalprofit
print(jobsequence([[1, 2, 100] , [2, 1, 19] , [3, 2, 27] , [4, 1, 25] , [5, 1, 15]]))        
#time complexity : O(N*M)  M represents the maximum deadline given in a array
#space complexity : O(M)


#candy
def candy(ratings):
    n=len(ratings)
    total = [1] * n  #as atleast one candy is to be given to every children
    for i in range(1,n):  #comparing the ratings of the children on the preceding manner
        if ratings[i]>ratings[i-1]:
            total[i]=total[i-1] + 1
    for i in range(n-2,-1,-1):  #comparing the ratings of the children but with the next children
        if ratings[i]>ratings[i+1]:
            total[i] = max(total[i],total[i+1]+1)
    return sum(total)                
print(candy([1, 2, 1, 4, 5]))
#time complexity : O(N)
#space complexity : O(N)

#shortest job first
import math
def sjf(bt):
    bt=sorted(bt)
    total = 0
    waitingtime = 0
    n=len(bt)
    for i in range(n-1):  #here we are looping only until the second last cause for the last jop , its waiting time is sum of all previous jobs and there's no point to calculate the last job's waiting time,as there are no jobs beyound this job
        waitingtime+=bt[i]
        total+=waitingtime
    return math.floor(total / n)    
print(sjf( [1, 2, 3, 4]))
#time complexity : O(NlogN)
#space complexity : O(1)

#LRU cache
#LRU cache algorithm follows the logic of having a head and tail node and the least recently node or data will at the tail and the most recently used node or data will be at the head
#and whenever any node or data is accessed , we put this node in the head
class LRU:
    def __init__(self,capacity):
        self.capacity = capacity
        self.m={}  #this is our data storage which stores key of the node and the node as key-value pair
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
    class Node:
        def __init__(self,key,value,next=None,prev=None):
            self.key=key
            self.value=value
            self.next=next
            self.prev=prev
    def add(self,node):
        nxt = self.head.next
        self.head.next=node
        node.next=nxt
        node.prev=self.head
        nxt.prev=node
    def delete(self,node):
        prv=node.prev
        nxt=node.next
        prv.next=nxt
        nxt.prev=prv
    def put(self,k,v):
        if k in self.m:
            delnode = self.m[k]
            del self.m[k]
            self.delete(delnode)  
        newnode=self.Node(k,v)
        self.m[k]=newnode  
        self.add(newnode)
        if len(self.m)>self.capacity:
            delnode = self.tail.prev
            del self.m[delnode.key]
            self.delete(delnode)
        return self.m[k].value

    def get(self,k):
        if k in self.m:
            nnode=self.m[k]
            self.delete(nnode)  #we are deleting the node from its original position 
            self.add(nnode)  #then we are adding this node in the head of the linked list
            return nnode.value  #and we return the value
        return -1    
    def printdatas(self):
        ans=[]
        itr=self.head.next
        while itr!=self.tail:
            ans.append(str(itr.value))
            itr=itr.next
        return ans
lru=LRU(5)
lru.put(1,1)
lru.put(2,2)
lru.put(3,3)
lru.put(4,4)
lru.put(5,5)
lru.put(6,6)
print(lru.put(6,7))
print(lru.get(2))
print(lru.printdatas())
#time complexity : O(1) for both get and put
#space complexity : O(N)

#insert interval
def insertinterval(intervals,newinterval):
    i = 0
    n=len(intervals)
    ans = []
    while i<n and intervals[i][1]<newinterval[0]:  #if the current interval's ending is smaller than the starting of the new interval then it means they dont overlap with eachother
     ans.append(intervals[i])
     i+=1
     #as we have already checked for the ending of the intervals smaller than the starting of newinterval
    while i<n and intervals[i][1]>=newinterval[0] and  intervals[i][0]<=newinterval[1]:  #if the ending of current interval is greater than or equal the starting of newinterval  and the starting of the current interval is samller or equal to the ending of the new interval then it means they overlap with eachother
        current=intervals[i]
        newinterval[0]=min(current[0],newinterval[0])  #then based on the values of starting and ending , we change the value of new interval
        newinterval[1]=max(current[1],newinterval[1])
        i+=1
    ans.append(newinterval)
    while i<n:
        ans.append(intervals[i])
        i+=1
    return ans
print(insertinterval( [ [1, 3] , [6, 9] ] ,  [2, 5]))        
#time complexity : O(N)
#space complexity : O(N) in worst case